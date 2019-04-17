import ast
import os
import io
import json
import textwrap
from inspect import cleandoc
from DungeonList import dungeon_table
from Utils import data_path
from RuleCAST import RuleCAST
from LocationList import location_table
from ItemList import item_table
import ItemPool

def to_c_sym(item:str):
    return item.replace("(","").replace(")","").replace("[","").replace("]","").replace(" ","_").replace("'", "").replace("-","_").upper()

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

class RuleModel(object):
    def __init__(self, world, parser, name, rule):

        proto = "bool {}(state_t *state)".format(name)

        if rule is None:
            rule = "True"
        else:
            rule = rule.strip()
        rule = rule.split('#')[0]

        ast_rule = ast.parse(rule, mode='eval')
        ast_rule = RuleCAST(world).visit(ast_rule)
        rule = parser.visit(ast_rule)

        self.name = name
        self.proto = proto
        self.rule = rule
        self.c = proto + '{\n    return ' + rule +  ";\n}\n\n"

class LocationModel(object):
    def __init__(self, name, ismq, scene_id = 255):
        self.name = name
        self.symbol = 'LOCATION_' + to_c_sym(name)
        self.scene = scene_id
        self.rule = None
        self.mq = ismq
        self.region = "NULL"

            
class ExitModel(object):
    def __init__(self, start, dest):
        self.name = start + ' -> ' + dest
        self.start = 'REGION_' + to_c_sym(start)
        self.dest = 'REGION_' + to_c_sym(dest)
        self.rule = None

class RegionModel(object):
    def __init__(self, name, is_mq, scene_id):
        self.name = name
        self.mq = is_mq
        self.scene = scene_id
        self.symbol = 'REGION_' + to_c_sym(name)
        self.locations = []
        self.exits = []
        self.core_region = None


    def get_core_symbol(self):
        if self.core_region is not None:
            return self.core_region.symbol
        return self.symbol


    def set_world(self, world):
        self.world = world


    def add_location(self, location):
        location.world = self.world
        self.locations.append(location)


    def add_exit(self, exit):
        exit.world = self.world
        self.exits.append(exit)



class WorldModel(object):
    def __init__(self):
        self.regions = {}
        self.dungeon_regions = []
        self.rules = {}
        self.locations = {}
        self.location_conflicts = []


    def add_region(self, region, is_overworld):
        if is_overworld:
            self.regions[region.symbol] = region
        else:
            if region.symbol not in self.regions:
                self.regions[region.symbol] = RegionModel(region.name, False, region.scene)

            core_region = self.regions[region.symbol]
            region.core_region = core_region

            region_ver = "VA_" if region.mq else "MQ_"

            region.symbol = region_ver + region.symbol
            self.dungeon_regions.append(region)

    def bind_rule(self, entity, rule:RuleModel):
        if rule.rule in self.rules:
            rule = self.rules[rule.rule]
        else:
            self.rules[rule.rule] = rule

        if entity is not None:
            entity.rule = rule


    def bind_location(self, region:RegionModel, location:LocationModel):
        if location.symbol in self.locations:
            loc = self.locations[location.symbol]
            if loc.rule.rule != location.rule.rule:
                self.location_conflicts.append((loc, location))
        else:
            self.locations[location.symbol] = location
        region.locations.append(location)
        location.region = region.get_core_symbol()

class CGen(object):


    def __init__(self):
        self.world = DummyWorld()
        self.parser = RuleCGen()


    @staticmethod
    def get_rule_file_list():
        result = []
        dungeons = {
            'Deku Tree' : 0,
            'Dodongos Cavern' : 1,
            'Jabu Jabus Belly' : 2,
            'Forest Temple' : 3,
            'Fire Temple' : 4,
            'Water Temple' : 5,
            'Spirit Temple' : 6,
            'Shadow Temple' : 7,
            'Bottom of the Well' : 8,
            'Ice Cavern' : 9,
            'Gerudo Training Grounds' : 11,
            'Ganons Castle' : 13
            }
        result.append((os.path.join(data_path('World'), 'Overworld.json'), 255, False, True))
        for item in dungeon_table:
            name = item['name']
            result.append((os.path.join(data_path('World'), name + '.json'), dungeons[name], False, False))
            result.append((os.path.join(data_path('World'), name + ' MQ.json'), dungeons[name], True, False))
        return result
    
    @staticmethod
    def load_rule_json(file_path):
        json_string = ""
        with io.open(file_path, 'r') as file:
            for line in file.readlines():
                json_string += line.split('#')[0].replace('\n', ' ')
        return json.loads(json_string)




    def Go(self):
        world_model = WorldModel()
        world_model.bind_rule(None, RuleModel(self.world, self.parser, "rule_true", "True"))
        world_model.bind_rule(None, RuleModel(self.world, self.parser, "rule_false", "False"))
        func_count = 0

        for filename, scene_id, ismq, is_overworld in CGen.get_rule_file_list():

            rules = CGen.load_rule_json(filename)
            mq_txt = "MQ_" if ismq else ""
            for region in rules:
                
                region_name = region['region_name']
                region_model = RegionModel(region_name, ismq, scene_id)
                world_model.add_region(region_model, is_overworld)

                if 'locations' in region:
                    for loc, rule in region['locations'].items():
                        location_model = LocationModel(loc, ismq, scene_id)
                        func = "rule_{}_{}".format(func_count, location_model.symbol)
                        rule = RuleModel(self.world, self.parser, func, rule)

                        world_model.bind_rule(location_model, rule)
                        world_model.bind_location(region_model, location_model)
                        func_count += 1

                if 'exits' in region:
                    for exit, rule in region['exits'].items():
                        exit_model = ExitModel(region_name, exit)
                        func = "rule_{}_{}_to_{}".format(func_count, exit_model.start, exit_model.dest)
                        rule = RuleModel(self.world, self.parser, func, rule)
                        world_model.bind_rule(exit_model, rule)
                        region_model.exits.append(exit_model)
                        func_count += 1


        self.create_regionlist_files(world_model)
        self.create_locationlist_files(world_model)
        self.create_rule_files(world_model)
        self.create_itempool_files(world_model)
        self.create_itemlist_file()

    def create_itemlist_file(self):
        
        itemlist_c = cleandoc('''
        /* Generated C code */

        #include <stdbool.h>
        #include "item.h"

        item_info_t item_table[] = {''')

        for item in item_table:
            v = item_table[item]
            gi = v[2]
            if gi is None:
                gi = 0
            g = v[1]
            if g is None:
                g = "ITEM_FILL_NORMAL"
            elif g == True:
                g = "ITEM_FILL_ADVANCEMENT"
            elif g == False:
                g = "ITEM_FILL_PRIORITY"

            item_sym = to_c_sym(item)
            item_type_sym = "ITEM_TYPE_" + to_c_sym(v[0])
            if item_type_sym == 'ITEM_TYPE_FORTRESSSMALLKEY':
                item_type_sym = 'ITEM_TYPE_FORTRESS_SMALLKEY'
            element = cleandoc('''
            [{}] = {{
                .k = {},
                .name = "{}",
                .type = {},
                .fill = {},
                .gi = 0x{:02X}
            }},
            ''').format(item_sym, item_sym, item, item_type_sym, g, gi)
            element = textwrap.indent(element, '    ')
            itemlist_c += '\n' + element
        itemlist_c += '\n};\n\n'


        for t in ['Song', 'Event', 'Shop']:
            itemlist_c += "item_{}_t {}_items[] = {{".format(t.lower(), t.lower())
            for item in item_table:
                v = item_table[item]
                if v[0] == t and v[3] is not None:
                    element = cleandoc('''
                    {{
                        .k = {},
                    ''').format(to_c_sym(item))
                    s = v[3]
                    for k in s:
                        f = '0x{:02X}' 
                        if k == 'bit_mask':
                            f = '0x{:08X}' 
                        elif k == 'object':
                            f = '0x{:04X}' 
                        elif k == 'price':
                            f = '{}'
                        line = "\n    .{{}} = {},".format(f)
                        element += line.format(k,s[k])
                    element +="\n},"
                    element = textwrap.indent(element, '    ')
                    itemlist_c += '\n' + element
            itemlist_c += "\n};\n\n"

        with open(os.path.join("ASM", "world", "itemlist.c"), 'w') as outfile:
            outfile.write(itemlist_c)


    def create_itempool_files(self, world_model):
        pool = \
            ItemPool.alwaysitems + \
            ItemPool.normal_items + \
            ItemPool.songlist + \
            ItemPool.rewardlist + \
            ['Bottle'] * 3 + \
            ['Bottle with Letter'] + \
            ['Ocarina'] * 2 + \
            ['Weird Egg'] + \
            ['POCKET_EGG']
            #shuffle_ocarinas = true 
            #shuffle_weird_egg = true


        for dungeon_info in dungeon_table:
            name = dungeon_info['name']
            pool += ['Boss Key (%s)' % name] * dungeon_info['boss_key']
            pool += ['Small Key (%s)' % name] * dungeon_info['small_key']
        
        itempool_h = cleandoc('''
        /* Generated C Code */

        #ifndef ITEMPOOL_H
        #define ITEMPOOL_H
        #include "item.h"
        
        item_e itempool_test [] = { 
        ''') +'\n'

        for item in pool:
            item = to_c_sym(item)
            itempool_h += "    {},\n".format(item)

        itempool_h += '};\n#endif'

        
        with open(os.path.join("ASM", "world", "itempool.h"), 'w') as outfile:
            outfile.write(itempool_h)


    def create_rule_files(self, world_model):
        
        rules_c = cleandoc('''
        /* Generated C Code */

        #include "state.h"
        #include "region.h"
        #include "regionlist.h"
        #include <stdbool.h>''') +'\n\n'

        rules_h = cleandoc('''
        /* Generated C Code */

        #ifndef RULES_H
        #define RULES_H

        #include "state.h"


        typedef bool (*rule_f)(state_t*);
        ''') +'\n\n'

        for k, rule in world_model.rules.items():
            rules_c += rule.c
            rules_h += 'extern ' + rule.proto + ';\n'

        rules_h += "#endif // !RULES_H"

        with open(os.path.join("ASM","world", "rules.c"), 'w') as outfile:
            outfile.write(rules_c)

        with open(os.path.join("ASM","world", "rules.h"), 'w') as outfile:
            outfile.write(rules_h)


    def create_regionlist_files(self, world_model:WorldModel):
        base_regions = list(world_model.regions.values())
        dungeon_regions = world_model.dungeon_regions
        regions = base_regions + dungeon_regions

        regionlist_h = cleandoc('''
        /* Generated C Code */

        #ifndef REGIONLIST_H
        #define REGIONLIST_H
        ''') + '\n' + self.create_named_enum("region_e", [region.symbol for region in regions]) + cleandoc('''
        #endif
        ''')
        
        regionlist_c = cleandoc('''
        /* Generated C Code */

        #include <stddef.h>
        #include "region.h"

        region_t world_regions[] = ''')

        regionlist_c += self.generate_region_array(base_regions, '', lambda r: r.symbol) + ';'

        for var_name, is_mq in [('va_only_regions', False), ('mq_only_regions', True)]:
            
            regionlist_c += '\n\n' + cleandoc('''
            region_list_t {}[] = {{
            ''').format(var_name)
            for scene in range(0, 14):
                scene_regions = [r for r in dungeon_regions if r.scene == scene and r.mq == is_mq]
                count = len(scene_regions)

                _c = '\n[{}] = {{\n'.format(scene)
                
                _c_scene_regions = ""
                if count == 0:
                    _c_scene_regions = "NULL";
                else:
                    _c_scene_regions = self.generate_region_array(scene_regions, '    ', None)
                    _c_scene_regions = "(region_t[]) " + _c_scene_regions
                _c += cleandoc('''
                    .count = {},
                    .values = {}
                }},\n''').format(count, _c_scene_regions)
                regionlist_c += textwrap.indent(_c, '    ')
            regionlist_c += "\n};"

        with open(os.path.join("ASM", "world", "regionlist.h"), 'w') as outfile:
            outfile.write(regionlist_h)
            
        with open(os.path.join("ASM", "world", "regionlist.c"), 'w') as outfile:
            outfile.write(regionlist_c)
    

    def generate_region_array(self, regions, indent, key_lambda):
        regionlist_c = ""
        for region in regions:
            _c = ""
            if key_lambda is None:
                _c = '{\n'
            else:
                _c = '[{}] = {{\n'.format(key_lambda(region))
            _c_loc = textwrap.indent(",\n".join([x.symbol for x in region.locations]), '        ').rstrip()
            loc_count = len(region.locations)
            if loc_count > 0:
                _c_loc = '\n' + _c_loc
                _c_loc = '(location_e[]) {' + _c_loc + '\n    }'
            else:
                _c_loc = 'NULL'
            _c_exits = ""
            
            exit_count = len(region.exits)
            if exit_count == 0:
                _c_exits = "NULL"
            else:
                for exit in region.exits:
                    _c_exit = '\n' + cleandoc('''
                    {{
                        .start = {},
                        .dest = {},
                        .rule = {}
                    }},
                    ''').format(exit.start, exit.dest, exit.rule.name)
                    _c_exits += _c_exit
                
                _c_exits = textwrap.indent(_c_exits, '        ') + '\n    }'
                _c_exits = '(exit_rule_t[]) {' + _c_exits
            _c += cleandoc('''
                .k = {},
                .name = "{}",
                .loc_count = {},
                .locations = {},
                .exit_count = {},
                .exits = {},
            }},
            ''').format(region.get_core_symbol(), region.name, loc_count, _c_loc, exit_count, _c_exits)
            _c = textwrap.indent(_c, '    ')
            regionlist_c += _c + '\n'

        return "{\n" + textwrap.indent(regionlist_c + "}", indent)


    def create_named_enum(self, typedef_name, items, prefix = ""):
        c = "typedef enum{\n"
        for item in items:
            c += "    {}{},\n".format(prefix, item)
        return c + "}} {};\n\n".format(typedef_name)

    def create_locationlist_files(self, world_model:WorldModel):
        location_e = []
        location_type_e = set()
        location_hint_e = set()

        
        _c = cleandoc('''
            /* Generated C Code */

            #include <stdbool.h>
            #include <stddef.h>
            #include "region.h"

            location_t location_table [] = {''') +'\n'


        for k, v in location_table.items():
            loc_k = "LOCATION_" + to_c_sym(k)
            loc_name = k
            loc_type = "LOCATION_TYPE_" + to_c_sym(v[0])
            location_type_e.add(loc_type)
            loc_hint = v[3]
            if loc_hint is not None:
                loc_hint = "LOCATION_HINT_" + to_c_sym(loc_hint)
                location_hint_e.add(loc_hint)
            else:
                loc_hint = "LOCATION_HINT_NONE"

            loc_scene = v[1]
            loc_default = v[2]

            if loc_scene is None:
                loc_scene = 255

            if loc_default is None:
                loc_default = 0

            location_e.append(loc_k)
            loc_ = world_model.locations[loc_k]

            line ="""\
                [{}] = {{
                    .k = {},
                    .name = "{}",
                    .type = {},
                    .scene = 0x{:02X},
                    .var = 0x{:02X},
                    .hint = {},
                    .region = {},
                    .rule = {},
                    .item = ITEM_E_NONE,
                    .active = true
                }},\n""".format(loc_k, loc_k, loc_name, loc_type, loc_scene, loc_default, loc_hint, loc_.region, loc_.rule.name)
            line = textwrap.dedent(line)
            line = textwrap.indent(line, '    ')
            _c += line

        _c += "};\n\n"
        _c += "location_conflict_list_t location_conflicts [] = {\n"

        conflicts = [[] for i in range(14)]

        for locA, locB in world_model.location_conflicts:
            mq_rule = locA.rule.name if locA.mq else locB.rule.name
            va_rule = locB.rule.name if locA.mq else locA.rule.name

            conflicts[locA.scene].append((locA.symbol, va_rule, mq_rule))

        for scene_id in range(14):
            scene_conflicts = conflicts[scene_id]
            count = len(scene_conflicts)
            _c_values = ""
            if count == 0:
                _c_values = "NULL"
            else:
                for k, va_rule, mq_rule in scene_conflicts:
                    _c_values += cleandoc('''
                        {{
                            .k = {},
                            .va_rule = {},
                            .mq_rule = {}
                        }},''').format(k, va_rule, mq_rule) +'\n'
                _c_values = "(location_conflict_t[]) {\n" + textwrap.indent(_c_values, '        ') \
                    + "    }"
            line = cleandoc('''
            [{}] = {{
                .count = {},
                .values = {}
            }},''').format(scene_id, count, _c_values)+'\n'
            _c += textwrap.indent(line, '    ')
        _c += "};\n"


        _h = cleandoc('''
        /* Generated C Code */

        #ifndef LOCATIONLIST_H
        #define LOCATIONLIST_H

        ''')+"\n\n"
        temp = list(location_type_e)
        temp.sort()
        _h += self.create_named_enum("location_type_e", ["LOCATION_TYPE_INVALID"] + temp)
        temp = list(location_hint_e)
        temp.sort()
        _h += self.create_named_enum("location_hint_e", ["LOCATION_HINT_NONE"] + temp)
        _h += self.create_named_enum("location_e", location_e + ["LOCATION_MAX"] + ["LOCATION_NONE"])
        _h += "#endif // !LOCATIONLIST_H"

        
        with open(os.path.join("ASM","world", "locationlist.h"), 'w') as outfile:
            outfile.write(_h)

        with open(os.path.join("ASM","world", "locationlist.c"), 'w') as outfile:
            outfile.write(_c)


test = CGen()
test.Go()