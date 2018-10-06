import argparse
import textwrap
import string
import re
import random
import hashlib

from Patches import get_tunic_color_options, get_navi_color_options
from version import __version__
from Utils import random_choices

class ArgumentDefaultsHelpFormatter(argparse.RawTextHelpFormatter):

    def _get_help_string(self, action):
        return textwrap.dedent(action.help)


# 32 characters
letters = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
index_to_letter = { i: letters[i] for i in range(32) }
letter_to_index = { v: k for k, v in index_to_letter.items() }

def bit_string_to_text(bits):
    # pad the bits array to be multiple of 5
    if len(bits) % 5 > 0:
        bits += [0] * (5 - len(bits) % 5)
    # convert to characters
    result = ""
    for i in range(0, len(bits), 5):
        chunk = bits[i:i + 5]
        value = 0
        for b in range(5):
            value |= chunk[b] << b
        result += index_to_letter[value]
    return result

def text_to_bit_string(text):
    bits = []
    for c in text:
        index = letter_to_index[c]
        for b in range(5):
            bits += [ (index >> b) & 1 ]
    return bits

# holds the info for a single setting
class Setting_Info():

    def __init__(self, name, type, bitwidth=0, shared=False, args_params={}, gui_params=None):
        self.name = name # name of the setting, used as a key to retrieve the setting's value everywhere
        self.type = type # type of the setting's value, used to properly convert types in GUI code
        self.bitwidth = bitwidth # number of bits needed to store the setting, used in converting settings to a string
        self.shared = shared # whether or not the setting is one that should be shared, used in converting settings to a string
        self.args_params = args_params # parameters that should be pased to the command line argument parser's add_argument() function
        self.gui_params = gui_params # parameters that the gui uses to build the widget components

# holds the particular choices for a run's settings
class Settings():

    def get_settings_display(self):
        padding = 0
        for setting in filter(lambda s: s.shared, setting_infos):
            padding = max( len(setting.name), padding )
        padding += 2
        output = ''
        for setting in filter(lambda s: s.shared, setting_infos):
            name = setting.name + ': ' + ' ' * (padding - len(setting.name))
            val = str(self.__dict__[setting.name])
            output += name + val + '\n'
        return output

    def get_settings_string(self):
        bits = []
        for setting in filter(lambda s: s.shared and s.bitwidth > 0, setting_infos):
            value = self.__dict__[setting.name]
            i_bits = []
            if setting.type == bool:
                i_bits = [ 1 if value else 0 ]
            if setting.type == str:
                index = setting.args_params['choices'].index(value)
                # https://stackoverflow.com/questions/10321978/integer-to-bitfield-as-a-list
                i_bits = [1 if digit=='1' else 0 for digit in bin(index)[2:]]
                i_bits.reverse()
            if setting.type == int:
                value = value - ('min' in setting.gui_params and setting.gui_params['min'] or 0)
                value = int(value / ('step' in setting.gui_params and setting.gui_params['step'] or 1))
                value = min(value, ('max' in setting.gui_params and setting.gui_params['max'] or value))
                # https://stackoverflow.com/questions/10321978/integer-to-bitfield-as-a-list
                i_bits = [1 if digit=='1' else 0 for digit in bin(value)[2:]]
                i_bits.reverse()
            # pad it
            i_bits += [0] * ( setting.bitwidth - len(i_bits) )
            bits += i_bits
        return bit_string_to_text(bits)

    def update_with_settings_string(self, text):
        bits = text_to_bit_string(text)

        for setting in filter(lambda s: s.shared and s.bitwidth > 0, setting_infos):
            cur_bits = bits[:setting.bitwidth]
            bits = bits[setting.bitwidth:]
            value = None
            if setting.type == bool:
                value = True if cur_bits[0] == 1 else False
            if setting.type == str:
                index = 0
                for b in range(setting.bitwidth):
                    index |= cur_bits[b] << b
                value = setting.args_params['choices'][index]
            if setting.type == int:
                value = 0
                for b in range(setting.bitwidth):
                    value |= cur_bits[b] << b
                value = value * ('step' in setting.gui_params and setting.gui_params['step'] or 1)
                value = value + ('min' in setting.gui_params and setting.gui_params['min'] or 0)
            self.__dict__[setting.name] = value

        self.settings_string = self.get_settings_string()
        self.numeric_seed = self.get_numeric_seed()

    def get_numeric_seed(self):
        # salt seed with the settings, and hash to get a numeric seed
        full_string = self.settings_string + __version__ + self.seed
        return int(hashlib.sha256(full_string.encode('utf-8')).hexdigest(), 16)

    def sanatize_seed(self):
        # leave only alphanumeric and some punctuation
        self.seed = re.sub(r'[^a-zA-Z0-9_-]', '', self.seed, re.UNICODE)

    def update_seed(self, seed):
        self.seed = seed
        self.sanatize_seed()
        self.numeric_seed = self.get_numeric_seed()

    def update(self):
        self.settings_string = self.get_settings_string()
        self.numeric_seed = self.get_numeric_seed()

    # add the settings as fields, and calculate information based on them
    def __init__(self, settings_dict):
        self.__dict__.update(settings_dict)
        for info in setting_infos:
            if info.name not in self.__dict__:
                if info.type == bool:
                    self.__dict__[info.name] = True if info.gui_params['default'] == 'checked' else False
                if info.type == str:
                    if 'default' in info.args_params:
                        self.__dict__[info.name] = info.gui_params['default'] or info.args_params['default']
                    else:
                        self.__dict__[info.name] = ""
                if info.type == int:
                    self.__dict__[info.name] = info.gui_params['default'] or 1
        self.settings_string = self.get_settings_string()
        if(self.seed is None):
            # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
            self.seed = ''.join(random_choices(string.ascii_uppercase + string.digits, k=10))
        self.sanatize_seed()
        self.numeric_seed = self.get_numeric_seed()

def parse_custom_tunic_color(s):
    if s == 'Custom Color':
        raise argparse.ArgumentTypeError('Specify custom color by using \'Custom (#xxxxxx)\'')
    elif re.match(r'^Custom \(#[A-Fa-f0-9]{6}\)$', s):
        return re.findall(r'[A-Fa-f0-9]{6}', s)[0]
    elif s in get_tunic_color_options():
        return s
    else:
        raise argparse.ArgumentTypeError('Invalid color specified')

def parse_custom_navi_color(s):
    if s == 'Custom Color':
        raise argparse.ArgumentTypeError('Specify custom color by using \'Custom (#xxxxxx)\'')
    elif re.match(r'^Custom \(#[A-Fa-f0-9]{6}\)$', s):
        return re.findall(r'[A-Fa-f0-9]{6}', s)[0]
    elif s in get_navi_color_options():
        return s
    else:
        raise argparse.ArgumentTypeError('Invalid color specified')

# a list of the possible settings
setting_infos = [
    Setting_Info('check_version', bool, 0, False,
    {
        'help': '''\
                Checks if you are on the latest version
                ''',
        'action': 'store_true'
    }),
    Setting_Info('checked_version', str, 0, False, {
            'default': '',
            'help': 'Supress version warnings if checked_version is less than __version__.'}),
    Setting_Info('rom', str, 0, False, {
            'default': 'ZOOTDEC.z64',
            'help': 'Path to an OoT 1.0 rom to use as a base.'}),
    Setting_Info('output_dir', str, 0, False, {
            'default': '',
            'help': 'Path to output directory for rom generation.'}),
    Setting_Info('seed', str, 0, False, {
            'help': 'Define seed number to generate.'}),
    Setting_Info('count', int, 0, False, {
            'help': '''\
                    Use to batch generate multiple seeds with same settings.
                    If --seed is provided, it will be used for the first seed, then
                    used to derive the next seed (i.e. generating 10 seeds with
                    --seed given will produce the same 10 (different) roms each
                    time).
                    ''',
            'type': int}),
    Setting_Info('world_count', int, 0, False, {
            'default': 1,
            'help': '''\
                    Use to create a multi-world generation for co-op seeds.
                    World count is the number of players. Warning: Increasing
                    the world count will drastically increase generation time.
                    ''',
            'type': int}),
    Setting_Info('player_num', int, 0, False, {
            'default': 1,
            'help': '''\
                    Use to select world to generate when there are multiple worlds.
                    ''',
            'type': int}),
    Setting_Info('create_spoiler', bool, 1, True,
        {
            'help': 'Output a Spoiler File',
            'action': 'store_true'
        },
        {
            'text': 'Create Spoiler Log',
            'group': 'rom_tab',
            'widget': 'Checkbutton',
            'default': 'checked',
            'dependency': lambda guivar: guivar['compress_rom'].get() != 'No ROM Output',
            'tooltip':'''\
                      Enabling this will change the seed.
                      '''
        }),
    Setting_Info('compress_rom', str, 2, False,
        {
            'default': 'True',
            'const': 'True',
            'nargs': '?',
            'choices': ['True', 'False', 'None'],
            'help': '''\
                    Create a compressed version of the output rom file.
                    True: Compresses. Improves stability. Will take longer to generate
                    False: Uncompressed. Unstable. Faster generation
                    None: No ROM Output. Creates spoiler log only
                    ''',
        },
        {
            'text': 'Compress Rom',
            'group': 'rom_tab',
            'widget': 'Radiobutton',
            'default': 'Compressed [Stable]',
            'horizontal': True,
            'options': {
                'Compressed [Stable]': 'True',
                'Uncompressed [Crashes]': 'False',
                'No ROM Output': 'None',
            },
            'tooltip':'''\
                      The first time compressed generation will take a while
                      but subsequent generations will be quick. It is highly
                      recommended to compress or the game will crash
                      frequently except on real N64 hardware.
                      '''
        }),
    Setting_Info('open_moon', bool, 1, True,
        {
            'help': '''\
                    A gate no longer blocks the way back through the
                    twisted hallway in the Clock Tower. Going back
                    through here takes you to the moon. Talking to Majora
                    warps you back into the Clock Tower.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Open Moon',
            'group': 'open',
            'widget': 'Checkbutton',
            'default': 'checked',
            'tooltip':'''\
                    A gate no longer blocks the way back through the
                    twisted hallway in the Clock Tower. Going back
                    through here takes you to the moon. Talking to Majora
                    warps you back into the Clock Tower. The cutscene
                    leading the moon warps you straight to Majora
                      '''
        }),
    Setting_Info('skip_first_cycle', bool, 1, True,
        {
            'help': '''\
                    Start the game in clock tower with the Ocarina in hand
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Skip First Cycle',
            'group': 'open',
            'widget': 'Checkbutton',
            'default': 'checked',
            'tooltip':'''\
                    Ocarina starts placed in your inventory
                      '''
        }),
    Setting_Info('oath', str, 2, True,
        {
            'default': 'remains',
            'const': 'remains',
            'nargs': '?',
            'choices': ['remains', 'masks', 'rewards', 'dungeons', 'hundo', 'open'],
            'help': '''\
                    Select requirement to be taught the Oath to Order. (default: %(default)s)
                    Remains:    Collect all four boss remains.
                    Masks:  Collect all 24 masks.
                    Rewards:    Collect all Stray Fairy rewards.
                    Dungeons:   Collect all boss remains and Stray Fairy rewards.
                    Hundo:  Collect all boss remains, masks, and fairy rewards.
                    Open:   The song will be known upon starting the game.
                    '''
        },
        {
            'text': '',
            'group': 'open',
            'widget': 'Combobox',
            'default': 'Remains',
            'options': {
                'Remains' : 'remains',
                'All Masks' : 'masks',
                'Stray Fairy Rewards' : 'rewards',
                'Complete Dungeons' : 'dungeons',
                '100%' : 'hundo',
                'Open' : 'open'
            },
            'tooltip':'''\
                    Remains: All boss remains.
                    All Masks:  All masks.
                    Stray Fairy Rewards: All Stray Fairy rewards.
                    Complete Dungeons: All boss remains and Stray Fairy rewards.
                    100%: All boss remains, masks, and fairy rewards.
                    Open:   The song will be known upon starting the game.
                      '''
        }),
    Setting_Info('all_reachable', bool, 1, True,
        {
            'help': '''\
                    When disabled, only check if the game is beatable with
                    placement. Do not ensure all locations are reachable.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'All Locations Reachable',
            'group': 'world',
            'widget': 'Checkbutton',
            'default': 'checked',
            'tooltip':'''\
                      When this option is enabled, the randomizer will
                      guarantee that every item is obtainable, and every
                      location is reachable.

                      When disabled, only required items and locations
                      to beat the game will be guaranteed reachable.

                      Even when enabled, some locations may still be able
                      to hold the keys needed to reach them.
                      '''
        }),
    Setting_Info('bombchus_in_logic', bool, 1, True,
        {
            'help': '''\
                    Bombchus will be considered in logic. This has a few effects:
                    -Back alley shop will open once you've found Bombchus
                    -It will sell an affordable pack (5 for 60), and never sell out
                    -Bombchus refills cannot be bought until Bomchus have been obtained.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Bombchus are considered in logic',
            'group': 'world',
            'widget': 'Checkbutton',
            'default': 'checked',
            'tooltip':'''\
                      Bombchus are properly considered in logic.

                      The first Bombchu pack will always be 20.
                      Subsequent packs will be 5 or 10 based on
                      how many you have.

                      Bombchus can be purchased for 60/99/180
                      rupees once they are been found.

                      Bombchu Bowling opens with Bombchus.
                      Bombchus are available at Kokiri Shop
                      and the Bazaar. Bombchu refills cannot
                      be bought until Bombchus have been
                      obtained.
                      ''',
        }),
    Setting_Info('one_item_per_dungeon', bool, 1, True,
        {
            'help': '''\
                    Each dungeon will have exactly one major item.
                    Does not include dungeon items or GS Tokens.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Dungeons have one major item',
            'group': 'world',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Dungeons have exactly one major
                      item. This naturally makes each
                      dungeon similar in value instaed
                      of valued based on chest count.

                      Dungeon items and GS Tokens do
                      not count as major items.
                      ''',
        }),
    Setting_Info('no_escape_sequence', bool, 1, True,
        {
            'help': '''\
                    The tower collapse escape sequence between Ganondorf and Ganon will be skipped.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Skip Moon Stopping Cutscene',
            'group': 'convenience',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      The moon stopping cutscene that follows the playing of the
                      Oath to Order will be skipped.
                      '''
        }),
    Setting_Info('no_pirate_bees', bool, 1, True,
        {
            'help': '''\
                    The crawlspace into Hyrule Castle will take you straight to Zelda.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Skip Pirate Clearing Sequence',
            'group': 'convenience',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      The pirates are cleared from the Hookshot room.
                      '''
        }),
    Setting_Info('no_epona_race', bool, 1, True,
        {
            'help': '''\
                    Having Epona's Song will allow you to summon
                    Epona without accessing Romani Ranch.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Skip Epona Race',
            'group': 'convenience',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Epona can be summoned with Epona's Song
                      without accessing Romani Ranch.
                      '''
        }),
    Setting_Info('fast_chests', bool, 1, True,
        {
            'help': '''\
                    Makes all chests open without the large chest opening cutscene
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Fast Chest Cutscenes',
            'group': 'convenience',
            'widget': 'Checkbutton',
            'default': 'checked',
            'tooltip':'''\
                      All chest animations are fast. If disabled,
                      the animation time is slow for major items.
                      '''
        }),
    Setting_Info('zora_egg_count_random', bool, 1, True,
        {
            'help': '''\
                    Sets a random number of Zora Eggs to receive an item from the buyer.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Random Zora Egg Count',
            'group': 'convenience',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Some Zora Eggs will already be spawned into the Marine Research Lab
                      '''
        }),
    Setting_Info('zora_egg_count', int, 4, True,
        {
            'default': 7,
            'const': 7,
            'nargs': '?',
            'choices': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
            'help': '''\
                    Select the number of Zora Eggs to receive the New Wave Bossa Nova.
                    ''',
            'type': int,
        },
        {
            'group': 'convenience',
            'widget': 'Scale',
            'default': 7,
            'min': 1,
            'max': 18,
            'tooltip':'''\
                      The Baby Zoras will sing for turning
                      in the chosen number of Zora Eggs.
                      ''',
            'dependency': lambda guivar: not guivar['zora_egg_count_random'].get(),
        }),
    Setting_Info('free_scarecrow', bool, 1, True,
        {
            'help': '''\
                    Start with the scarecrow song. You do not need
                    to play it as child or adult at the scarecrow
                    patch to be able to summon Pierre.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Start with Scarecrow Song',
            'group': 'convenience',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Skips needing to show the scarecrow
                      your ocarina to learn Scarecrow Song.
                      '''
        }),
    Setting_Info('scarecrow_song', str, 0, False,
        {
            'default': 'DAAAAAAA',
            'const': 'DAAAAAAA',
            'nargs': '?',
            'help': '''\
                    The song started with if 'free_scarecrow' is True
                    Valid notes: A, U, L, R, D
                    ''',
        },
        {
            'group': 'convenience',
            'widget': 'Entry',
            'default': 'DAAAAAAA',
            'dependency': lambda guivar: guivar['free_scarecrow'].get(),
            'tooltip':'''\
                      Song must be 8 notes long and have at least
                      two different notes.
                      Valid notes are:
                      'A': A Button
                      'D': C-Down
                      'U': C-Up
                      'L': C-Left
                      'R': C-Right
                      '''
        }),
    Setting_Info('shuffle_ocarina', bool, 1, True,
        {
            'help': '''\
                    Shuffles the Ocarina of Time into the pool.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Shuffle Ocarina of Time',
            'group': 'logic',
            'widget': 'Checkbutton',
            'default': 'checked',
            'tooltip':'''\
                      Disabling this will make the Ocarina of Time
                      always available at the start.
                      '''
        }),
    Setting_Info('shuffle_song_items', bool, 1, True,
        {
            'help': '''\
                    Shuffles the songs with with rest of the item pool so that
                    song can appear at other locations, and items can appear at
                    the song locations.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Shuffle Songs with Items',
            'group': 'logic',
            'widget': 'Checkbutton',
            'default': 'checked',
            'tooltip':'''\
                      Songs can appear anywhere as normal items,
                      not just at vanilla song locations.
                      ''',
        }),
    Setting_Info('shuffle_scrubs', bool, 1, True,
        {
            'help': '''\
                    All Deku Scrub Salesmen will give a random item.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Shuffle Deku Salescrubs',
            'group': 'logic',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Each Deku Scrub Salesman will give
                      a random item. Vanilla OoT has 36
                      Deku Scrub Salesmen. The prices
                      are all reduced to 10 Rupees.
                      '''
        }),
    Setting_Info('shopsanity', str, 3, True,
        {
            'default': 'off',
            'const': 'off',
            'nargs': '?',
            'choices': ['off', '0', '1', '2', '3', '4', 'random'],
            'help': '''\
                    Shop contents are randomized. Non-shop items
                    are one time purchases. This setting also
                    changes the item pool to introduce a new Wallet
                    upgrade and more money.
                    off:        Normal Shops*
                    0-4:        Shop contents are shuffled and N non-shop
                                items are added to every shop. So more
                                possible item locations.
                    random:     Shop contents are shuffles and each shop
                                will have a random number of non-shop items
                    '''
        },
        {
            'text': 'Shopsanity',
            'group': 'logic',
            'widget': 'Combobox',
            'default': 'Off',
            'options': {
                'Off': 'off',
                'Shuffled Shops (0 Items)': '0',
                'Shuffled Shops (1 Items)': '1',
                'Shuffled Shops (2 Items)': '2',
                'Shuffled Shops (3 Items)': '3',
                'Shuffled Shops (4 Items)': '4',
                'Shuffled Shops (Random)': 'random',
            },
            'tooltip':'''\
                      Shop contents are randomized.
                      (X Items): Shops have X random non-shop (Special
                      Deal!) items. They will always be on the left
                      side. This means that every shop will have more
                      possible item locations. So +2 means 2 items
                      per shop.

                      (Random): Each shop will have a random number
                      of non-shop items, up to a maximum of 4.

                      The non-shop items have no requirements except
                      money, while the normal shop items (such as
                      200/300 rupee tunics) have normal vanilla
                      requirements. This means that, for example,
                      as a child you cannot buy 200/300 rupee
                      tunics, but you can buy non-shop tunics.

                      Non-shop bombchus will unlock the chu slot
                      in your inventory, which, if bombchus are in
                      logic, is needed to buy chu refills. If not in
                      logic, the bomb bag is required.
                      '''
        }),
    Setting_Info('shuffle_mapcompass', str, 2, True,
        {
        'default': 'dungeon',
        'const': 'dungeon',
        'nargs': '?',
        'choices': ['remove', 'dungeon', 'keysanity'],
        'help': '''\
                    Sets the Map and Compass placement rules
                    remove:      Maps and Compasses are removed from the world
                    dungeon:     Maps and Compasses are put in their dungeon
                    keysanity:   Maps and Compasses can appear anywhere
                    '''
        },
        {
            'text': 'Shuffle Dungeon Items',
            'group': 'logic',
            'widget': 'Combobox',
            'default': 'Maps/Compasses: Dungeon Only',
            'options': {
                'Maps/Compasses: Remove': 'remove',
                'Maps/Compasses: Dungeon Only': 'dungeon',
                'Maps/Compasses: Anywhere': 'keysanity'
            },
            'tooltip':'''\
                      'Remove': Maps and Compasses are removed.
                      This will add a small amount of money and
                      refill items to the pool.

                      'Dungeon': Maps and Compasses can only appear
                      in their respective dungeon.

                      'Anywhere': Maps and Compasses can appear
                      anywhere in the world.

                      Setting 'Remove' or 'Anywhere' will add 2
                      more possible locations to each Dungeons.
                      This makes dungeons more profitable, especially
                      Ice Cavern, Water Temple, and Jabu Jabu's Belly.
                      '''
        }),
    Setting_Info('shuffle_smallkeys', str, 2, True,
        {
        'default': 'dungeon',
        'const': 'dungeon',
        'nargs': '?',
        'choices': ['remove', 'dungeon', 'keysanity'],
        'help': '''\
                    Sets the Small Keys placement rules
                    remove:      Small Keys are removed from the world
                    dungeon:     Small Keys are put in their Dungeon
                    keysanity:   Small Keys can appear anywhere
                    '''
        },
        {
            'group': 'logic',
            'widget': 'Combobox',
            'default': 'Small Keys: Dungeon Only',
            'options': {
                'Small Keys: Remove (Keysy)': 'remove',
                'Small Keys: Dungeon Only': 'dungeon',
                'Small Keys: Anywhere (Keysanity)': 'keysanity'
            },
            'tooltip':'''\
                      'Remove': Small Keys are removed. All locked
                      doors in dungeons will be unlocked. An easier
                      mode.

                      'Dungeon': Small Keys can only appear in their
                      respective dungeon. If Fire Temple is not a
                      Master Quest dungeon, the door to the Boss Key
                      chest will be unlocked

                      'Anywhere': Small Keys can appear
                      anywhere in the world. A difficult mode since
                      it is more likely to need to enter a dungeon
                      multiple times.

                      Try different combination out, such as:
                      'Small Keys: Dungeon' + 'Boss Keys: Anywhere'
                      for a milder Keysanity experience.
                      '''
        }),
    Setting_Info('shuffle_bosskeys', str, 2, True,
        {
        'default': 'dungeon',
        'const': 'dungeon',
        'nargs': '?',
        'choices': ['remove', 'dungeon', 'keysanity'],
        'help': '''\
                    Sets the Boss Keys placement rules
                    remove:      Boss Keys are removed from the world
                    dungeon:     Boss Keys are put in their Dungeon
                    keysanity:   Boss Keys can appear anywhere
                    '''
        },
        {
            'group': 'logic',
            'widget': 'Combobox',
            'default': 'Boss Keys: Dungeon Only',
            'options': {
                'Boss Keys: Remove (Keysy)': 'remove',
                'Boss Keys: Dungeon Only': 'dungeon',
                'Boss Keys: Anywhere (Keysanity)': 'keysanity'
            },
            'tooltip':'''\
                      'Remove': Boss Keys are removed. All locked
                      doors in dungeons will be unlocked. An easier
                      mode.

                      'Dungeon': Boss Keys can only appear in their
                      respective dungeon.

                      'Anywhere': Boss Keys can appear
                      anywhere in the world. A difficult mode since
                      it is more likely to need to enter a dungeon
                      multiple times.

                      Try different combination out, such as:
                      'Small Keys: Dungeon' + 'Boss Keys: Anywhere'
                      for a milder Keysanity experience.
                      '''
        }),
    Setting_Info('enhance_map_compass', bool, 1, True,
        {
            'help': '''\
                    Gives the Map and Compass extra functionality.
                    Map will tell if a dungeon is vanilla or Master Quest.
                    Compass will tell what medallion or stone is within.
                    This setting will only activate these functions if the
                    other settings would make this useful information.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Maps and Compasses give information',
            'group': 'logic',
            'widget': 'Checkbutton',
            'default': 'checked',
            'tooltip':'''\
                    Gives the Map and Compass extra functionality.
                    Map will tell if a dungeon is vanilla or Master Quest.
                    Compass will tell what medallion or stone is within.
                    This option is only available if shuffle 'Maps/Compasses'
                    is set to 'Anywhere'
                      ''',
            'dependency': lambda guivar: guivar['shuffle_mapcompass'].get() == 'Maps/Compasses: Anywhere',
        }),
    Setting_Info('tokensanity', str, 2, True,
        {
            'default': 'off',
            'const': 'off',
            'nargs': '?',
            'choices': ['off', 'dungeons', 'all'],
            'help': '''\
                    Gold Skulltula Tokens will be shuffled into the pool,
                    and Gold Skulltula locations can have any item.
                    off:        Don't use this feature
                    dungeons:   Only dungeon Skulltulas will be shuffled
                    all:        All Gold Skulltulas will be shuffled
                    '''
        },
        {
            'text': 'Tokensanity',
            'group': 'logic',
            'widget': 'Combobox',
            'default': 'Off',
            'options': {
                'Off': 'off',
                'Dungeons Only': 'dungeons',
                'All Tokens': 'all',
            },
            'tooltip':'''\
                      Token reward from Gold Skulltulas are
                      shuffled into the pool.

                      'Dungeon Only': This only shuffles
                      the GS locations that are within
                      dungeons, increasing the value of
                      most dungeons and making internal
                      dungeon exploration more diverse.

                      'All Tokens': Effectively adds 100
                      new locations for items to appear.
                      '''
        }),
    Setting_Info('quest', str, 2, True,
        {
            'default': 'vanilla',
            'const': 'vanilla',
            'nargs': '?',
            'choices': ['vanilla', 'master', 'mixed'],
            'help': '''\
                    Select requirement to spawn the Rainbow Bridge to reach Ganon's Castle. (default: %(default)s)
                    Vanilla:       Dungeons will be the original Ocarina of Time dungeons.
                    Master:        Dungeons will be in the form of the Master Quest.
                    Mixed:         Each dungeon will randomly be either standard or Master Quest.
                    '''
        },
        {
            'text': 'Dungeon Quest',
            'group': 'world',
            'widget': 'Combobox',
            'default': 'Vanilla',
            'options': {
                'Vanilla': 'vanilla',
                'Master Quest': 'master',
                'Mixed': 'mixed',
            },
            'tooltip':'''\
                      'Vanilla': Dungeons will be in their
                      default OoT form.

                      'Master Quest': Dungeons will be in the
                      form found in OoT: Master Quest.

                      'Mixed': Each dungeon will have a
                      random chance to be in either form.
                      ''',
        }),
    Setting_Info('logic_no_zora_eggs', bool, 1, True,
        {
            'help': '''\
                    You will not be expected to collect 7 zora eggs.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'No Zora Eggs',
            'group': 'rewards',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      The Baby Zoras will not have an important item
                      '''
        }),
    Setting_Info('logic_no_perfect_archery', bool, 1, True,
        {
            'help': '''\
                    You will not be expected to win the second prize for the shooting galleries.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'No Perfect Shooting Galleries',
            'group': 'rewards',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Beating the shooting galleries for a second
                      time will not yield a required item.
                      '''
        }),
    Setting_Info('logic_tricks', bool, 1, True,
        {
            'help': '''\
                    Enable various tricks.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Require minor tricks',
            'group': 'tricks',
            'widget': 'SpecialCheckbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Enables a large number of tricks.
                      Still does not require glitches.
                      '''
        }),
    Setting_Info('logic_goron_boost', bool, 1, True,
        {
            'help': '''\
                    Goron Boost could be required to get places
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Goron Boost',
            'group': 'tricks',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Take damage from a bomb while doing a
                      ground pound as Goron Link
                      '''
        }),
    Setting_Info('logic_lens', str, 2, True,
        {
            'default': 'all',
            'const': 'always',
            'nargs': '?',
            'choices': ['darmani', 'all'],
            'help': '''\
                    Choose what expects the Lens of Truth:
                    all:              All lens spots expect the lens (except those that did not in the original game)
                    darmani:            Only picking up Darmani's item requires the lens
                    '''
        },
        {
            'text': 'Lens of Truth',
            'group': 'tricks',
            'widget': 'Combobox',
            'default': 'Required everywhere',
            'options': {
                'Required everywhere': 'all',
                'Wasteland and Chest Minigame': 'chest-wasteland',
                'Only Chest Minigame': 'chest',
            },
            'tooltip':'''\
                      'Required everywhere': every invisible or
                      fake object will expect you to have the
                      Lens of Truth and Magic. The exception is
                      passing through the first wall in Bottom of
                      the Well, since that is required in vanilla.

                      'Wasteland': The lens is needed to follow
                      the ghost guide across the Haunted Wasteland.
                      '''
        }),
    Setting_Info('ocarina_songs', bool, 1, True,
        {
            'help': '''\
                    Randomizes the notes need to play for each ocarina song.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Randomize ocarina song notes',
            'group': 'other',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Will need to memorize a new set of songs.
                      Can be silly, but difficult. Songs are
                      generally sensible, and warp songs are
                      typically more difficult.
                      '''
        }),
    Setting_Info('correct_chest_sizes', bool, 1, True,
        {
            'help': '''\
                    Updates the chest sizes to match their contents.
                    Small Chest = Non-required Item
                    Big Chest = Progression Item
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Chest size matches contents',
            'group': 'other',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      Chests will be large if they contain a major
                      item, and small if they don't. Allows skipping
                      chests if they are small. However, skipping
                      small chests will mean having low health,
                      ammo, and rupees, so doing so is a risk.
                      '''
        }),
    Setting_Info('clearer_hints', bool, 1, True,
        {
            'help': '''\
                    The hints provided by Gossip Stones are
                    very direct.
                    ''',
            'action': 'store_true'
        },
        {
            'text': 'Clearer hints',
            'group': 'other',
            'widget': 'Checkbutton',
            'default': 'unchecked',
            'tooltip':'''\
                      The hints provided by Gossip Stones will
                      be very direct if this option is enabled.
                      '''
        }),
    Setting_Info('hints', str, 2, True,
        {
            'default': 'none',
            'const': 'agony',
            'nargs': '?',
            'choices': ['none', 'mask', 'agony', 'always'],
            'help': '''\
                    Choose how Gossip Stones behave
                    none:   Default behavior
                    mask:   Have useful hints that are read with the Mask of Truth
                    agony:  Have useful hints that are read with Stone of Agony
                    always: Have useful hints which can always be read
                    '''
        },
        {
            'text': 'Gossip Stones',
            'group': 'other',
            'widget': 'Combobox',
            'default': 'Hints; Need Stone of Agony',
            'options': {
                'No Hints': 'none',
                'Hints; Need Mask of Truth': 'mask',
                'Hints; Need Stone of Agony': 'agony',
                'Hints; Need Nothing': 'always',
            },
            'tooltip':'''\
                      Gossip Stones can be made to give hints
                      about where items can be found.

                      Different settings can be chosen to
                      decide which item is needed to
                      speak to Gossip Stones. Choosing to
                      stick with the Mask of Truth will
                      make the hints very difficult to
                      obtain.

                      Hints for 'on the way of the hero' are
                      locations that contain items that are
                      required to beat the game.
                      '''
        }),
    Setting_Info('text_shuffle', str, 2, True,
        {
            'default': 'none',
            'const': 'none',
            'nargs': '?',
            'choices': ['none', 'except_hints', 'complete'],
            'help': '''\
                    Choose how to shuffle the game's messages.
                    none:          Default behavior
                    except_hints:  All text except Gossip Stone hints and dungeon reward hints is shuffled.
                    complete:      All text is shuffled
                    '''
        },
        {
            'text': 'Text Shuffle',
            'group': 'other',
            'widget': 'Combobox',
            'default': 'No text shuffled',
            'options': {
                'No text shuffled': 'none',
                'Shuffled except Hints and Keys': 'except_hints',
                'All text shuffled': 'complete',
            },
            'tooltip':'''\
                      Will make things confusing for comedic value.

                      'Shuffled except Hints and Keys': Key texts
                      not shuffled because in keysanity it is
                      impossible to tell what dungeon it is for
                      without the correct text. Similarly, non-shop
                      items sold in shops will also not be shuffled
                      so that the price of the item can be known.
                      '''
        }),
    Setting_Info('difficulty', str, 2, True,
        {
            'default': 'normal',
            'const': 'normal',
            'nargs': '?',
            'choices': ['normal', 'hard', 'very_hard', 'ohko'],
            'help': '''\
                    Change the item pool for an added challenge.
                    normal:         Default items
                    hard:           Double defense, double magic, and all 8 heart containers are removed
                    very_hard:      Double defense, double magic, Nayru's Love, and all health upgrades are removed
                    ohko:           Same as very hard, and Link will die in one hit.
                    '''
        },
        {
            'text': 'Difficulty',
            'group': 'other',
            'widget': 'Combobox',
            'default': 'Normal',
            'options': {
                'Normal': 'normal',
                'Hard': 'hard',
                'Very Hard': 'very_hard',
                'OHKO': 'ohko'
            },
            'tooltip':'''\
                      Makes health less available

                      'Hard': Heart Containers, Double Magic,
                      and Double Defense are removed.

                      'Very Hard': Heart Containers, Heart,
                      Pieces, Double Magic, Double Defense,
                      and Nayru's Love are removed.

                      'OHKO': Link dies in one hit.
                      '''
        }),
    Setting_Info('default_targeting', str, 1, False,
        {
            'default': 'hold',
            'const': 'always',
            'nargs': '?',
            'choices': ['hold', 'switch'],
            'help': '''\
                    Choose what the default Z-targeting is.
                    '''
        },
        {
            'text': 'Default Targeting Option',
            'group': 'rom_tab',
            'widget': 'Combobox',
            'default': 'Hold',
            'options': {
                'Hold': 'hold',
                'Switch': 'switch',
            }
        }),
    Setting_Info('background_music', str, 2, False,
        {
            'default': 'normal',
            'const': 'normal',
            'nargs': '?',
            'choices': ['normal', 'off', 'random'],
            'help': '''\
                    Sets the background music behavior
                    normal:      Areas play their normal background music
                    off:         No background music
                    random:      Areas play random background music
                    '''
        },
        {
            'text': 'Background Music',
            'group': 'cosmetics',
            'widget': 'Combobox',
            'default': 'Normal',
            'options': {
                'Normal': 'normal',
                'No Music': 'off',
                'Random': 'random',
            },
            'tooltip': '''\
                       'No Music': No background music.
                       is played.

                       'Random': Area background music is
                       randomized.
                       '''
        }),

    Setting_Info('humancolor', str, 0, False,
        {
            'default': 'Kokiri Green',
            'const': 'Kokiri Green',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Kokiri Tunic. (default: %(default)s)
                    Color:              Make the Kokiri Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Kokiri Tunic Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Kokiri Green',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('dekucolor', str, 0, False,
        {
            'default': 'Goron Red',
            'const': 'Goron Red',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Goron Tunic. (default: %(default)s)
                    Color:              Make the Goron Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Deku Tunic Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Goron Red',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('goroncolor', str, 0, False,
        {
            'default': 'Goron Red',
            'const': 'Goron Red',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Goron Tunic. (default: %(default)s)
                    Color:              Make the Goron Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Goron Tunic Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Goron Red',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('zoracolor', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Zora Tunic Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('deitycolor', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Fierce Deity Tunic Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('kokiriswordcolor', str, 0, False,
        {
            'default': 'Kokiri Green',
            'const': 'Kokiri Green',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Kokiri Tunic. (default: %(default)s)
                    Color:              Make the Kokiri Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Sword Slash Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Kokiri Green',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('dekuspincolor', str, 0, False,
        {
            'default': 'Goron Red',
            'const': 'Goron Red',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Goron Tunic. (default: %(default)s)
                    Color:              Make the Goron Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Deku Spin Trail Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Goron Red',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('zorafincolor', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Zora Fin Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('boomerangcolor', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Zora Boomerang Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('deityswordcolor', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Fierce Deity Sword Slash Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('deitybeamcolor', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Fierce Deity Sword Beam Color',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('navicolordefault', str, 0, False,
        {
            'default': 'White',
            'const': 'White',
            'nargs': '?',
            'type': parse_custom_navi_color,
            'help': '''\
                    Choose the color for Navi when she is idle. (default: %(default)s)
                    Color:             Make the Navi this color.
                    Random Choice:     Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Navi Idle',
            'group': 'navicolor',
            'widget': 'Combobox',
            'default': 'White',
            'options': get_navi_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Comepletely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('navicolorenemy', str, 0, False,
        {
            'default': 'Yellow',
            'const': 'Yellow',
            'nargs': '?',
            'type': parse_custom_navi_color,
            'help': '''\
                    Choose the color for Navi when she is targeting an enemy. (default: %(default)s)
                    Color:             Make the Navi this color.
                    Random Choice:     Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Navi Targeting Enemy',
            'group': 'navicolor',
            'widget': 'Combobox',
            'default': 'Yellow',
            'options': get_navi_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Comepletely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('navicolornpc', str, 0, False,
        {
            'default': 'Light Blue',
            'const': 'Light Blue',
            'nargs': '?',
            'type': parse_custom_navi_color,
            'help': '''\
                    Choose the color for Navi when she is targeting an NPC. (default: %(default)s)
                    Color:             Make the Navi this color.
                    Random Choice:     Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Navi Targeting NPC',
            'group': 'navicolor',
            'widget': 'Combobox',
            'default': 'Light Blue',
            'options': get_navi_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Comepletely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('navicolorprop', str, 0, False,
        {
            'default': 'Green',
            'const': 'Green',
            'nargs': '?',
            'type': parse_custom_navi_color,
            'help': '''\
                    Choose the color for Navi when she is targeting a prop. (default: %(default)s)
                    Color:             Make the Navi this color.
                    Random Choice:     Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Navi Targeting Prop',
            'group': 'navicolor',
            'widget': 'Combobox',
            'default': 'Green',
            'options': get_navi_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Comepletely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('menuforecolour', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Menu Foreground Colour',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('menubackcolor', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Menu Colour Background',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('menucloudcolor', str, 0, False,
        {
            'default': 'Zora Blue',
            'const': 'Zora Blue',
            'nargs': '?',
            'type': parse_custom_tunic_color,
            'help': '''\
                    Choose the color for Link's Zora Tunic. (default: %(default)s)
                    Color:              Make the Zora Tunic this color.
                    Random Choice:      Choose a random color from this list of colors.
                    Completely Random: Choose a random color from any color the N64 can draw.
                    '''
        },
        {
            'text': 'Menu Colour Clouds',
            'group': 'tuniccolor',
            'widget': 'Combobox',
            'default': 'Zora Blue',
            'options': get_tunic_color_options(),
            'tooltip':'''\
                      'Random Choice': Choose a random
                      color from this list of colors.
                      'Completely Random': Choose a random
                      color from any color the N64 can draw.
                      '''
        }),
    Setting_Info('navisfxoverworld', str, 0, False,
        {
            'default': 'Default',
            'const': 'Default',
            'nargs': '?',
            'choices': ['Default', 'Notification', 'Rupee', 'Timer', 'Tamborine', 'Recovery Heart', 'Carrot Refill', 'Navi - Hey!', 'Navi - Random', 'Zelda - Gasp', 'Cluck', 'Mweep!', 'Random', 'None'],
            'help': '''\
                    Select the sound effect that plays when Navi has a hint. (default: %(default)s)
                    Sound:         Replace the sound effect with the chosen sound.
                    Random Choice: Replace the sound effect with a random sound from this list.
                    None:          Eliminate Navi hint sounds.
                    '''
        },
        {
            'text': 'Navi Hint',
            'group': 'navihint',
            'widget': 'Combobox',
            'default': 'Default',
            'options': [
                'Random Choice',
                'Default',
                'Notification',
                'Rupee',
                'Timer',
                'Tamborine',
                'Recovery Heart',
                'Carrot Refill',
                'Navi - Hey!',
                'Navi - Random',
                'Zelda - Gasp',
                'Cluck',
                'Mweep!',
                'None',
            ]
        }),
        Setting_Info('navisfxenemytarget', str, 0, False,
        {
            'default': 'Default',
            'const': 'Default',
            'nargs': '?',
            'choices': ['Default', 'Notification', 'Rupee', 'Timer', 'Tamborine', 'Recovery Heart', 'Carrot Refill', 'Navi - Hey!', 'Navi - Random', 'Zelda - Gasp', 'Cluck', 'Mweep!', 'Random', 'None'],
            'help': '''\
                    Select the sound effect that plays when targeting an enemy. (default: %(default)s)
                    Sound:         Replace the sound effect with the chosen sound.
                    Random Choice: Replace the sound effect with a random sound from this list.
                    None:          Eliminate Navi hint sounds.
                    '''
        },
        {
            'text': 'Navi Enemy Target',
            'group': 'navihint',
            'widget': 'Combobox',
            'default': 'Default',
            'options': [
                'Random Choice',
                'Default',
                'Notification',
                'Rupee',
                'Timer',
                'Tamborine',
                'Recovery Heart',
                'Carrot Refill',
                'Navi - Hey!',
                'Navi - Random',
                'Zelda - Gasp',
                'Cluck',
                'Mweep!',
                'None',
            ]
        }),
    Setting_Info('healthSFX', str, 0, False,
        {
            'default': 'Default',
            'const': 'Default',
            'nargs': '?',
            'choices': ['Default', 'Softer Beep', 'Rupee', 'Timer', 'Tamborine', 'Recovery Heart', 'Carrot Refill', 'Navi - Hey!', 'Zelda - Gasp', 'Cluck', 'Mweep!', 'Random', 'None'],
            'help': '''\
                    Select the sound effect that loops at low health. (default: %(default)s)
                    Sound:         Replace the sound effect with the chosen sound.
                    Random Choice: Replace the sound effect with a random sound from this list.
                    None:          Eliminate heart beeps.
                    '''
        },
        {
            'text': 'Low Health SFX',
            'group': 'lowhp',
            'widget': 'Combobox',
            'default': 'Default',
            'options': [
                'Random Choice',
                'Default',
                'Softer Beep',
                'Rupee',
                'Timer',
                'Tamborine',
                'Recovery Heart',
                'Carrot Refill',
                'Navi - Hey!',
                'Zelda - Gasp',
                'Cluck',
                'Mweep!',
                'None',
            ],
            'tooltip':'''\
                      'Random Choice': Choose a random
                      sound from this list.
                      'Default': Beep. Beep. Beep.
                      '''
        }),
]

# gets the randomizer settings, whether to open the gui, and the logger level from command line arguments
def get_settings_from_command_line_args():
    parser = argparse.ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    for info in setting_infos:
        parser.add_argument("--" + info.name, **info.args_params)

    parser.add_argument('--gui', help='Launch the GUI', action='store_true')
    parser.add_argument('--loglevel', default='info', const='info', nargs='?', choices=['error', 'info', 'warning', 'debug'], help='Select level of logging for output.')
    parser.add_argument('--settings_string', help='Provide sharable settings using a settings string. This will override all flags that it specifies.')

    args = parser.parse_args()

    result = {}
    for info in setting_infos:
        result[info.name] = vars(args)[info.name]
    settings = Settings(result)

    if args.settings_string is not None:
        settings.update_with_settings_string(args.settings_string)

    return settings, args.gui, args.loglevel
