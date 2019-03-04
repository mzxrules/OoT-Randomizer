import ast
import os
import io
import json
from inspect import cleandoc
from DungeonList import dungeon_table
from Utils import data_path
from RuleCAST import RuleCAST



def to_c_sym(item:str):
    return item.replace("(","").replace(")","").replace(" ","_").replace("'", "").replace("-","_").upper()

class DummyWorld(object):
    def __init__(self):
        l =['shuffle', 'dungeons', 'regions', 'itempool', 'state', '_cached_locations', '_entrance_cache', '_region_cache', '_location_cache', 'required_locations', 'shop_prices', 'scrub_prices', 'light_arrow_location', 'settings', 'check_version', 'checked_version', 'rom', 'output_dir', 'output_file', 'seed', 'patch_file', 'cosmetics_only', 'count', 'world_count', 'player_num', 'create_spoiler', 'create_cosmetics_log', 'compress_rom', 'open_forest', 'open_kakariko', 'open_door_of_time', 'open_fountain', 'gerudo_fortress', 'bridge', 'logic_rules', 'all_reachable', 'bombchus_in_logic', 'one_item_per_dungeon', 'trials_random', 'trials', 'no_escape_sequence', 'no_guard_stealth', 'no_epona_race', 'fast_chests', 'logic_no_night_tokens_without_suns_song', 'free_scarecrow', 'start_with_fast_travel', 'start_with_rupees', 'start_with_wallet', 'start_with_deku_equipment', 'big_poe_count_random', 'big_poe_count', 'shuffle_kokiri_sword', 'shuffle_ocarinas', 'shuffle_weird_egg', 'shuffle_gerudo_card', 'shuffle_song_items', 'shuffle_scrubs', 'shopsanity', 'tokensanity', 'shuffle_mapcompass', 'shuffle_smallkeys', 'shuffle_bosskeys', 'enhance_map_compass', 'unlocked_ganondorf', 'mq_dungeons_random', 'mq_dungeons', 'disabled_locations', 'allowed_tricks', 'logic_earliest_adult_trade', 'logic_latest_adult_trade', 'logic_lens', 'ocarina_songs', 'correct_chest_sizes', 'clearer_hints', 'hints', 'hint_dist', 'text_shuffle', 'junk_ice_traps', 'item_pool_value', 'damage_multiplier', 'starting_tod', 'default_targeting', 'background_music', 'display_dpad', 'kokiri_color', 'goron_color', 'zora_color', 'navi_color_default', 'navi_color_enemy', 'navi_color_npc', 'navi_color_prop', 'sword_trail_duration', 'sword_trail_color_inner', 'sword_trail_color_outer', 'sfx_low_hp', 'sfx_navi_overworld', 'sfx_navi_enemy', 'sfx_menu_cursor', 'sfx_menu_select', 'sfx_horse_neigh', 'sfx_nightfall', 'sfx_hover_boots', 'sfx_ocarina', 'settings_string', 'numeric_seed', 'logic_morpha_with_scale', 'logic_fewer_tunic_requirements', 'logic_child_deadhand', 'logic_man_on_roof', 'logic_dc_staircase', 'logic_dc_jump', 'logic_gerudo_kitchen', 'logic_deku_basement_gs', 'logic_rusted_switches', 'logic_botw_basement', 'logic_forest_mq_block_puzzle', 'logic_spirit_child_bombchu', 'logic_windmill_poh', 'logic_crater_bean_poh_with_hovers', 'logic_gtg_mq_with_hookshot', 'logic_forest_vines', 'logic_forest_well_swim', 'logic_dmt_bombable', 'logic_water_bk_chest', 'logic_adult_kokiri_gs', 'logic_spirit_mq_frozen_eye', 'logic_fire_mq_bk_chest', 'logic_zora_with_cucco', 'logic_zora_with_hovers', 'keysanity', 'check_beatable_only', 'skipped_trials', 'dungeon_mq', 'can_take_damage', 'id']

        for i in l:
            self.__dict__[i] = None

class RuleCGen(ast.NodeVisitor):
    '''Converts RuleCAST's AST output into C code'''
    
    def generic_visit(self, node):
        id = ""
        if (hasattr(node, 'id')):
            id = node.id

        return "__NOTIMPL_{}__".format(type(node).__name__)

    def visit_Expression(self, node):
        return self.visit(node.body)

    def visit_BoolOp(self, node):
        code = "__BoolOp__"

        if type(node.op) is ast.And:
            code = "&&"
        if type(node.op) is ast.Or:
            code = "||"

        result = self.visit(node.values[0])

        for subnode in node.values[1:]:
            result += " " + code + " " + self.visit(subnode)

        return "(" + result + ")";
        
    def visit_Name(self, node):
        return node.id

    def visit_Str(self, node):
        return 'OPTION_{}'.format(to_c_sym(node.s))

    def visit_Call(self, node):
        call = self.visit(node.func)
        args = ", ".join([self.visit(arg) for arg in node.args])
        return "{}({})".format(call, args)

    def visit_Compare(self, node):
        left = self.visit(node.left)
        op = ""

        if len(node.ops) >= 2:
            return "__COMPARE_MULTI__"

        right = self.visit(node.comparators[0])

        optype = type(node.ops[0])

        if optype is ast.Eq:
            op = "=="
        elif optype is ast.NotEq:
            op = "!="
        elif optype is ast.Lt:
            op = "<"
        elif optype is ast.LtE:
            op = "<="
        elif optype is ast.Gt:
            op = ">"
        elif optype is ast.GtE:
            op = ">="
        elif optype is ast.IsNot:
            op = "!="
        else:
            op = "__COMPARE_OP_{}__".format(node.ops[0].__name__)

        return "{} {} {}".format(left, op, right)

    def visit_Num(self, node):
        return str(node.n)

    def visit_Attribute(self, node):
        return "{}.{}".format(self.visit(node.value), node.attr)

    def visit_NameConstant(self, node):
        return "{}".format(node.value).lower()

    def visit_UnaryOp(self, node):
        if type(node.op) is ast.Not:
            return "!{}".format(self.visit(node.operand))
        else:
            return "__UnaryOp__{}".format(self.visit(node.operand))

    def visit_Subscript(self, node):
        value = self.visit(node.value)
        return "{}[{}]".format(value, self.visit(node.slice))

    def visit_Index(self, node):
        return self.visit(node.value)


class RuleCGenFile(object):

    def __init__(self):
        self.world = DummyWorld()
        self.parser = RuleCGen()

    @staticmethod
    def get_rule_file_list():
        result = []
        result.append((os.path.join(data_path('World'), 'Overworld.json'), False))
        for item in dungeon_table:
            name = item['name']
            result.append((os.path.join(data_path('World'), name + '.json'), False))
            result.append((os.path.join(data_path('World'), name + ' MQ.json'), True))
        return result
    
    @staticmethod
    def load_rule_json(file_path):
        json_string = ""
        with io.open(file_path, 'r') as file:
            for line in file.readlines():
                json_string += line.split('#')[0].replace('\n', ' ')
        return json.loads(json_string)


    def Go(self):
        func_count = 0
        output = cleandoc('''
        /* Generated C Code */

        #include "state.h"
        #include "region.h"
        #include "regionlist.h"
        #include <stdbool.h>''') +'\n\n'


        region_names = {}

        gen_functions = ""


        for filename, ismq in RuleCGenFile.get_rule_file_list():
            rules = RuleCGenFile.load_rule_json(filename)
            mq_txt = "MQ_" if ismq else ""
            for region in rules:
                region_name = region['region_name']
                region_names[to_c_sym(region_name)] = (region_name, ismq)
                location_list = []
                exit_list = []
                if 'locations' in region:
                    for loc, rule in region['locations'].items():
                        loc_sym = to_c_sym(loc)
                        func = "rule_{}_loc_{}{}".format(func_count, mq_txt, loc_sym)
                        gen_functions += self.new_rule(func, rule)
                        func_count += 1
                if 'exits' in region:
                    for exit, rule in region['exits'].items():
                        reg_sym = to_c_sym(exit)
                        func = "rule_{}_exit_{}".format(func_count,reg_sym)
                        gen_functions += self.new_rule(func, rule)
                        func_count += 1

        regionlist_h = self.dump_region_list(region_names)
        output += gen_functions

        with open(os.path.join("ASM","world", "gen_rule.c"), 'w') as outfile:
            outfile.write(output)
        with open(os.path.join("ASM", "world", "regionlist.h"), 'w') as outfile:
            outfile.write(regionlist_h)

    def dump_region_list(self, regions):
        region_e = ""
        for k in regions:
            region_e += "    REGION_{},\n".format(to_c_sym(k))
            ## region_struct += "    {{ .k = {} .name = {} }},\n".format(k, v[0])
        region_e = cleandoc('''
        #ifndef REGIONLIST_H
        #define REGIONLIST_H
        typedef enum
        {
        ''') + '\n' + region_e + '\n' + cleandoc('''
        } region_e;
        #endif
        ''')

        return region_e

    def new_rule(self, name, rule):
        parser = self.parser
        output = "bool {}(state_t *state){}\n    return ".format(name, '{');

        if rule is None:
            rule = "True"
        else:
            rule = rule.strip()
        rule = rule.split('#')[0]

        ast_rule = ast.parse(rule, mode='eval')
        ast_rule = RuleCAST(self.world).visit(ast_rule)
        output += parser.visit(ast_rule)
        output += ";\n}\n\n"
        return output