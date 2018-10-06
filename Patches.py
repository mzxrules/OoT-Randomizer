import io
import logging
import os
import platform
import struct
import subprocess
import random

from Hints import buildGossipHints, buildBossRewardHints
from Utils import local_path, output_path
from Items import ItemFactory, item_data

TunicColors = {
    "Custom Color": [0, 0, 0],
    "Kokiri Green": [0x1E, 0x69, 0x1B],
    "Goron Red": [0x64, 0x14, 0x00],
    "Zora Blue": [0x00, 0x3C, 0x64],
    "Black": [0x30, 0x30, 0x30],
    "White": [0xF0, 0xF0, 0xFF],
    "Azure Blue": [0x13, 0x9E, 0xD8],
    "Vivid Cyan": [0x13, 0xE9, 0xD8],
    "Light Red": [0xF8, 0x7C, 0x6D],
    "Fuchsia":[0xFF, 0x00, 0xFF],
    "Purple": [0x95, 0x30, 0x80],
    "MM Purple": [0x50, 0x52, 0x9A],
    "Twitch Purple": [0x64, 0x41, 0xA5],
    "Purple Heart": [0x8A, 0x2B, 0xE2],
    "Persian Rose": [0xFF, 0x14, 0x93],
    "Dirty Yellow": [0xE0, 0xD8, 0x60],
    "Blush Pink": [0xF8, 0x6C, 0xF8],
    "Hot Pink": [0xFF, 0x69, 0xB4],
    "Rose Pink": [0xFF, 0x90, 0xB3],
    "Orange": [0xE0, 0x79, 0x40],
    "Gray": [0xA0, 0xA0, 0xB0],
    "Gold": [0xD8, 0xB0, 0x60],
    "Silver": [0xD0, 0xF0, 0xFF],
    "Beige": [0xC0, 0xA0, 0xA0],
    "Teal": [0x30, 0xD0, 0xB0],
    "Blood Red": [0x83, 0x03, 0x03],
    "Blood Orange": [0xFE, 0x4B, 0x03],
    "Royal Blue": [0x40, 0x00, 0x90],
    "Sonic Blue": [0x50, 0x90, 0xE0],
    "NES Green": [0x00, 0xD0, 0x00],
    "Dark Green": [0x00, 0x25, 0x18],
    "Lumen": [80, 140, 240],
}

NaviColors = {
    "Custom Color": [0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x00, 0x00],
    "Gold": [0xFE, 0xCC, 0x3C, 0xFF, 0xFE, 0xC0, 0x07, 0x00],
    "White": [0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0xFF, 0x00],
    "Green": [0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0x00],
    "Light Blue": [0x96, 0x96, 0xFF, 0xFF, 0x96, 0x96, 0xFF, 0x00],
    "Yellow": [0xFF, 0xFF, 0x00, 0xFF, 0xC8, 0x9B, 0x00, 0x00],
    "Red": [0xFF, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0x00, 0x00],
    "Magenta": [0xFF, 0x00, 0xFF, 0xFF, 0xC8, 0x00, 0x9B, 0x00],
    "Black": [0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x00, 0x00],
    "Tatl": [0xFF, 0xFF, 0xFF, 0xFF, 0xC8, 0x98, 0x00, 0x00],
    "Tael": [0x49, 0x14, 0x6C, 0xFF, 0xFF, 0x00, 0x00, 0x00],
    "Fi": [0x2C, 0x9E, 0xC4, 0xFF, 0x2C, 0x19, 0x83, 0x00],
    "Ciela": [0xE6, 0xDE, 0x83, 0xFF, 0xC6, 0xBE, 0x5B, 0x00],
    "Epona": [0xD1, 0x49, 0x02, 0xFF, 0x55, 0x1F, 0x08, 0x00],
    "Ezlo": [0x62, 0x9C, 0x5F, 0xFF, 0x3F, 0x5D, 0x37, 0x00],
    "King of Red Lions": [0xA8, 0x33, 0x17, 0xFF, 0xDE, 0xD7, 0xC5, 0x00],
    "Linebeck": [0x03, 0x26, 0x60, 0xFF, 0xEF, 0xFF, 0xFF, 0x00],
    "Loftwing": [0xD6, 0x2E, 0x31, 0xFF, 0xFD, 0xE6, 0xCC, 0x00],
    "Midna": [0x19, 0x24, 0x26, 0xFF, 0xD2, 0x83, 0x30, 0x00],
    "Phantom Zelda": [0x97, 0x7A, 0x6C, 0xFF, 0x6F, 0x46, 0x67, 0x00],
}

def get_tunic_colors():
    return list(TunicColors.keys())

def get_tunic_color_options():
    return ["Random Choice", "Completely Random"] + get_tunic_colors()

def get_navi_colors():
    return list(NaviColors.keys())

def get_navi_color_options():
    return ["Random Choice", "Completely Random"] + get_navi_colors()

def patch_rom(world, rom):
    with open(local_path('data/rom_patch.txt'), 'r') as stream:
        for line in stream:
            address, value = [int(x, 16) for x in line.split(',')]
            rom.write_byte(address, value)

    # Write Randomizer title screen logo
    with open(local_path('data/title.bin'), 'rb') as stream:
        titleBytes = stream.read()
        rom.write_bytes(0x01795300, titleBytes)

    # will be populated with data to be written to initial save
    # see initial_save.asm and config.asm for more details on specifics
    # or just use the following functions to add an entry to the table
    initial_save_table = []

    # will set the bits of value to the offset in the save (or'ing them with what is already there)
    def write_bits_to_save(offset, value, filter=None):
        nonlocal initial_save_table

        if filter and not filter(value):
            return

        initial_save_table += [(offset & 0xFF00) >> 8, offset & 0xFF, 0x00, value]



    # will overwrite the byte at offset with the given value
    def write_byte_to_save(offset, value, filter=None):
        nonlocal initial_save_table

        if filter and not filter(value):
            return

        initial_save_table += [(offset & 0xFF00) >> 8, offset & 0xFF, 0x01, value]

    # will overwrite the byte at offset with the given value
    def write_bytes_to_save(offset, bytes, filter=None):
        for i, value in enumerate(bytes):
            write_byte_to_save(offset + i, value, filter)

    # will overwrite the byte at offset with the given value
    def write_save_table(rom):
        nonlocal initial_save_table

        table_len = len(initial_save_table)
        if table_len > 0x400:
            raise Exception("The Initial Save Table has exceeded it's maximum capacity: 0x%03X/0x400" % table_len)
        rom.write_bytes(0x3481800, initial_save_table)


    # Initial Save Data
    patch_files(rom, mq_scenes)

    # Load Message and Shop Data
    messages = read_messages(rom)
    shop_items = read_shop_items(rom, shop_item_file.start + 0x1DEC)
    remove_unused_messages(messages)

    # Sets hooks for gossip stone changes
    if world.hints != 'none':
        writeGossipStoneHintsHints(world, messages)

    # TODO: change to Majora text? if there's a reason to do that
    # build silly ganon lines
    buildGanonText(world, messages)

    # TODO: Update for MM
    # Write item overrides
    override_table = get_override_table(world)
    rom.write_bytes(0x3481000, sum(override_table, []))
    rom.write_byte(0x03481C00, world.id + 1) # Write player ID

    # TODO: figure out and find these overrides for MM
    # Revert Song Get Override Injection
    if not world.shuffle_song_items:
        # general get song
        rom.write_int32(0xAE5DF8, 0x240200FF)
        rom.write_int32(0xAE5E04, 0xAD0F00A4)
        # requiem of spirit
        rom.write_int32s(0xAC9ABC, [0x3C010001, 0x00300821])
        # sun song
        rom.write_int32(0xE09F68, 0x8C6F00A4)
        rom.write_int32(0xE09F74, 0x01CFC024)
        rom.write_int32(0xE09FB0, 0x240F0001)
        # epona
        rom.write_int32(0xD7E77C, 0x8C4900A4)
        rom.write_int32(0xD7E784, 0x8D088C24)
        rom.write_int32s(0xD7E8D4, [0x8DCE8C24, 0x8C4F00A4])
        rom.write_int32s(0xD7E140, [0x8DCE8C24, 0x8C6F00A4])
        rom.write_int32(0xD7EBBC, 0x14410008)
        rom.write_int32(0xD7EC1C, 0x17010010)
        # song of time
        rom.write_int32(0xDB532C, 0x24050003)

    # TODO: Find appropriate address to do this in MM
    # Set default targeting option to Hold
    if world.default_targeting == 'hold':
        rom.write_byte(0xB71E6D, 0x01)

    # Set OHKO mode
    if world.difficulty == 'ohko':
        rom.write_int32(0xAE80A8, 0xA4A00030) # sh  zero,48(a1)
        rom.write_int32(0xAE80B4, 0x06000003) # bltz s0, +0003

    # Patch songs and boss rewards
    for location in world.get_locations():
        item = location.item
        itemid = copy.copy(item.code)
        locationaddress = location.address
        secondaryaddress = location.address2

        if itemid is None or location.address is None:
            continue

        if location.type == 'Song' and not world.shuffle_song_items:
            rom.write_byte(locationaddress, itemid[0])
            itemid[0] = itemid[0] + 0x0D
            rom.write_byte(secondaryaddress, itemid[0])
            if location.name == 'Impa at Castle':
                impa_fix = 0x65 - itemid[1]
                rom.write_byte(0xD12ECB, impa_fix)
                rom.write_byte(0x2E8E931, item_data[item.name]) #Fix text box
            elif location.name == 'Song from Malon':
                if item.name == 'Suns Song':
                    rom.write_byte(locationaddress, itemid[0])
                malon_fix = 0x8C34 - (itemid[1] * 4)
                malon_fix_high = malon_fix >> 8
                malon_fix_low = malon_fix & 0x00FF
                rom.write_bytes(0xD7E142, [malon_fix_high, malon_fix_low])
                rom.write_bytes(0xD7E8D6, [malon_fix_high, malon_fix_low]) # I really don't like hardcoding these addresses, but for now.....
                rom.write_bytes(0xD7E786, [malon_fix_high, malon_fix_low])
                rom.write_byte(0x29BECB9, item_data[item.name]) #Fix text box
            elif location.name == 'Song from Composer Grave':
                sun_fix = 0x8C34 - (itemid[1] * 4)
                sun_fix_high = sun_fix >> 8
                sun_fix_low = sun_fix & 0x00FF
                rom.write_bytes(0xE09F66, [sun_fix_high, sun_fix_low])
                rom.write_byte(0x332A87D, item_data[item.name]) #Fix text box
            elif location.name == 'Song from Saria':
                saria_fix = 0x65 - itemid[1]
                rom.write_byte(0xE2A02B, saria_fix)
                rom.write_byte(0x20B1DBD, item_data[item.name]) #Fix text box
            elif location.name == 'Song from Ocarina of Time':
                rom.write_byte(0x252FC95, item_data[item.name]) #Fix text box
            elif location.name == 'Song at Windmill':
                windmill_fix = 0x65 - itemid[1]
                rom.write_byte(0xE42ABF, windmill_fix)
                rom.write_byte(0x3041091, item_data[item.name]) #Fix text box
            elif location.name == 'Sheik Forest Song':
                minuet_fix = 0x65 - itemid[1]
                rom.write_byte(0xC7BAA3, minuet_fix)
                rom.write_byte(0x20B0815, item_data[item.name]) #Fix text box
            elif location.name == 'Sheik at Temple':
                prelude_fix = 0x65 - itemid[1]
                rom.write_byte(0xC805EF, prelude_fix)
                rom.write_byte(0x2531335, item_data[item.name]) #Fix text box
            elif location.name == 'Sheik in Crater':
                bolero_fix = 0x65 - itemid[1]
                rom.write_byte(0xC7BC57, bolero_fix)
                rom.write_byte(0x224D7FD, item_data[item.name]) #Fix text box
            elif location.name == 'Sheik in Ice Cavern':
                serenade_fix = 0x65 - itemid[1]
                rom.write_byte(0xC7BD77, serenade_fix)
                rom.write_byte(0x2BEC895, item_data[item.name]) #Fix text box
            elif location.name == 'Sheik in Kakariko':
                nocturne_fix = 0x65 - itemid[1]
                rom.write_byte(0xAC9A5B, nocturne_fix)
                rom.write_byte(0x2000FED, item_data[item.name]) #Fix text box
            elif location.name == 'Sheik at Colossus':
                rom.write_byte(0x218C589, item_data[item.name]) #Fix text box
        elif location.type == 'Boss':
            else:
                rom.write_byte(locationaddress, itemid)
                rom.write_byte(secondaryaddress, item_data[item.name][2])

    # add a cheaper bombchu pack to the bombchu shop
    # describe
    update_message_by_id(messages, 0x80FE, '\x08\x05\x41Bombchu   (5 pieces)   60 Rupees\x01\x05\x40This looks like a toy mouse, but\x01it\'s actually a self-propelled time\x01bomb!\x09\x0A', 0x03)
    # purchase
    update_message_by_id(messages, 0x80FF, '\x08Bombchu    5 Pieces    60 Rupees\x01\x01\x1B\x05\x42Buy\x01Don\'t buy\x05\x40\x09', 0x03)
    rbl_bombchu = shop_items[0x0018]
    rbl_bombchu.price = 60
    rbl_bombchu.pieces = 5
    rbl_bombchu.get_item_id = 0x006A
    rbl_bombchu.description_message = 0x80FE
    rbl_bombchu.purchase_message = 0x80FF

    # TODO: Find these for MM Shops
    '''
    shop_objs = place_shop_items(rom, world, shop_items, messages,
        world.get_region('Kokiri Shop').locations, True)
    shop_objs |= {0x00FC, 0x00B2, 0x0101, 0x0102, 0x00FD, 0x00C5} # Shop objects
    rom.write_byte(0x2587029, len(shop_objs))
    rom.write_int32(0x258702C, 0x0300F600)
    rom.write_int16s(0x2596600, list(shop_objs))
    '''

    # Update grotto id data
    set_grotto_id_data(rom)

    if world.shuffle_smallkeys == 'remove' or world.shuffle_bosskeys == 'remove':
        locked_doors = get_locked_doors(rom, world)
        for _,[door_byte, door_bits] in locked_doors.items():
            write_bits_to_save(door_byte, door_bits)

    # Update chest type sizes
    if world.correct_chest_sizes:
        update_chest_sizes(rom, override_table)

    '''
    # TODO: Update these messages to reflect MM
    # give dungeon items the correct messages
    message_patch_for_dungeon_items(messages, shop_items, world)
    if world.shuffle_mapcompass == 'keysanity' and world.enhance_map_compass:
        reward_list = {'Kokiri Emerald':   "\x05\x42Kokiri Emerald\x05\x40",
                       'Goron Ruby':       "\x05\x41Goron Ruby\x05\x40",
                       'Zora Sapphire':    "\x05\x43Zora Sapphire\x05\x40",
                       'Forest Medallion': "\x05\x42Forest Medallion\x05\x40",
                       'Fire Medallion':   "\x05\x41Fire Medallion\x05\x40",
                       'Water Medallion':  "\x05\x43Water Medallion\x05\x40",
                       'Spirit Medallion': "\x05\x46Spirit Medallion\x05\x40",
                       'Shadow Medallion': "\x05\x45Shadow Medallion\x05\x40",
                       'Light Medallion':  "\x05\x44Light Medallion\x05\x40"
        }
        dungeon_list = {'DT':   ("the \x05\x42Deku Tree", 'Queen Gohma', 0x62, 0x88),
                        'DC':   ("\x05\x41Dodongo\'s Cavern", 'King Dodongo', 0x63, 0x89),
                        'JB':   ("\x05\x43Jabu Jabu\'s Belly", 'Barinade', 0x64, 0x8a),
                        'FoT':  ("the \x05\x42Forest Temple", 'Phantom Ganon', 0x65, 0x8b),
                        'FiT':  ("the \x05\x41Fire Temple", 'Volvagia', 0x7c, 0x8c),
                        'WT':   ("the \x05\x43Water Temple", 'Morpha', 0x7d, 0x8e),
                        'SpT':  ("the \x05\x46Spirit Temple", 'Twinrova', 0x7e, 0x8f),
                        'IC':   ("the \x05\x44Ice Cavern", None, 0x87, 0x92),
                        'BW':   ("the \x05\x45Bottom of the Well", None, 0xa2, 0xa5),
                        'ShT':   ("the \x05\x45Shadow Temple", 'Bongo Bongo', 0x7f, 0xa3),
        }
        for dungeon in world.dungeon_mq:
            if dungeon in ['GTG', 'GC']:
                pass
            elif dungeon in ['BW', 'IC']:
                dungeon_name, boss_name, compass_id, map_id = dungeon_list[dungeon]
                if world.world_count > 1:
                    map_message = "\x13\x76\x08\x05\x42\x0F\x05\x40 found the \x05\x41Dungeon Map\x05\x40\x01for %s\x05\x40!\x09" % (dungeon_name)
                else:
                    map_message = "\x13\x76\x08You found the \x05\x41Dungeon Map\x05\x40\x01for %s\x05\x40!\x01It\'s %s!\x09" % (dungeon_name, "masterful" if world.dungeon_mq[dungeon] else "ordinary")

                if world.quest == 'mixed':
                    update_message_by_id(messages, map_id, map_message)
            else:
                dungeon_name, boss_name, compass_id, map_id = dungeon_list[dungeon]
                dungeon_reward = reward_list[world.get_location(boss_name).item.name]
                if world.world_count > 1:
                    compass_message = "\x13\x75\x08\x05\x42\x0F\x05\x40 found the \x05\x41Compass\x05\x40\x01for %s\x05\x40!\x09" % (dungeon_name)
                else:
                    compass_message = "\x13\x75\x08You found the \x05\x41Compass\x05\x40\x01for %s\x05\x40!\x01It holds the %s!\x09" % (dungeon_name, dungeon_reward)
                update_message_by_id(messages, compass_id, compass_message)
                if world.quest == 'mixed':
                    if world.world_count > 1:
                        map_message = "\x13\x76\x08\x05\x42\x0F\x05\x40 found the \x05\x41Dungeon Map\x05\x40\x01for %s\x05\x40!\x09" % (dungeon_name)
                    else:
                        map_message = "\x13\x76\x08You found the \x05\x41Dungeon Map\x05\x40\x01for %s\x05\x40!\x01It\'s %s!\x09" % (dungeon_name, "masterful" if world.dungeon_mq[dungeon] else "ordinary")
                    update_message_by_id(messages, map_id, map_message)
        '''
    else:
        # Set hints for boss reward shuffle # TODO: Find correct thing in MM
        # rom.write_bytes(0xE2ADB2, [0x70, 0x7A])
        # rom.write_bytes(0xE2ADB6, [0x70, 0x57])
        buildBossRewardHints(world, messages)

    # add song messages
    add_song_messages(messages, world)

    # reduce item message lengths
    update_item_messages(messages, world)

    # TODO: create a third wallet for MM
    # Add 3rd Wallet Upgrade
    # rom.write_int16(0xB6D57E, 0x0003)
    # rom.write_int16(0xB6EC52, 999)
    # tycoon_message = "\x08\x13\x57You got a \x05\x43Tycoon's Wallet\x05\x40!\x01Now you can hold\x01up to \x05\x46999\x05\x40 \x05\x46Rupees\x05\x40."
    if world.world_count > 1:
       # tycoon_message = make_player_message(tycoon_message)
    update_message_by_id(messages, 0x00F8, tycoon_message, 0x23)

    repack_messages(rom, messages)
    write_shop_items(rom, shop_item_file.start + 0x1DEC, shop_items)

    # text shuffle
    if world.text_shuffle == 'except_hints':
        shuffle_messages(rom, except_hints=True)
    elif world.text_shuffle == 'complete':
        shuffle_messages(rom, except_hints=False)

    # output a text dump, for testing...
    #with open('keysanity_' + str(world.seed) + '_dump.txt', 'w', encoding='utf-16') as f:
    #     messages = read_messages(rom)
    #     f.write('item_message_strings = {\n')
    #     for m in messages:
    #        f.write("\t0x%04X: \"%s\",\n" % (m.id, m.get_python_string()))
    #     f.write('}\n')

    if world.ocarina_songs:
        replace_songs(rom, scarecrow_song)

    # actually write the save table to rom
    write_save_table(rom)

    # patch music
    if world.background_music == 'random':
        randomize_music(rom)
    elif world.background_music == 'off':
        disable_music(rom)

    # re-seed for aesthetic effects. They shouldn't be affected by the generation seed
    random.seed()

    # patch tunic colors
    # Custom color tunic stuff
    Tunics = []
    Tunics.append(0x00B6DA38) # Kokiri Tunic
    Tunics.append(0x00B6DA3B) # Goron Tunic
    Tunics.append(0x00B6DA3E) # Zora Tunic
    colorList = get_tunic_colors()
    randomColors = random_choices(colorList, k=3)

    for i in range(len(Tunics)):
        # get the color option
        thisColor = world.tunic_colors[i]
        # handle true random
        randColor = [random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)]
        if thisColor == 'Completely Random':
            color = randColor
        else:
            # handle random
            if world.tunic_colors[i] == 'Random Choice':
                color = TunicColors[randomColors[i]]
            # grab the color from the list
            elif thisColor in TunicColors:
                color = TunicColors[thisColor]
            # build color from hex code
            else:
                color = list(int(thisColor[i:i+2], 16) for i in (0, 2 ,4))
        rom.write_bytes(Tunics[i], color)

    # patch navi colors
    Navi = []
    Navi.append([0x00B5E184]) # Default
    Navi.append([0x00B5E19C, 0x00B5E1BC]) # Enemy, Boss
    Navi.append([0x00B5E194]) # NPC
    Navi.append([0x00B5E174, 0x00B5E17C, 0x00B5E18C, 0x00B5E1A4, 0x00B5E1AC, 0x00B5E1B4, 0x00B5E1C4, 0x00B5E1CC, 0x00B5E1D4]) # Everything else
    naviList = get_navi_colors()
    randomColors = random_choices(naviList, k=4)

    for i in range(len(Navi)):
        # do everything in the inner loop so that "true random" changes even for subcategories
        for j in range(len(Navi[i])):
            # get the color option
            thisColor = world.navi_colors[i]
            # handle true random
            randColor = [random.getrandbits(8), random.getrandbits(8), random.getrandbits(8), 0xFF,
                         random.getrandbits(8), random.getrandbits(8), random.getrandbits(8), 0x00]
            if thisColor == 'Completely Random':
                color = randColor
            else:
                # handle random
                if world.navi_colors[i] == 'Random Choice':
                    color = NaviColors[randomColors[i]]
                # grab the color from the list
                elif thisColor in NaviColors:
                    color = NaviColors[thisColor]
                # build color from hex code
                else:
                    color = list(int(thisColor[i:i+2], 16) for i in (0, 2 ,4))
                    color = color + [0xFF] + color + [0x00]
            rom.write_bytes(Navi[i][j], color)

    #Navi hints
    NaviHint = []
    NaviHint.append([0xAE7EF2, 0xC26C7E]) #Overworld Hint
    NaviHint.append([0xAE7EC6]) #Enemy Target Hint
    naviHintSFXList = ['Default', 'Notification', 'Rupee', 'Timer', 'Tamborine', 'Recovery Heart', 'Carrot Refill', 'Navi - Hey!', 'Navi - Random', 'Zelda - Gasp', 'Cluck', 'Mweep!', 'None']
    randomNaviHintSFX = random_choices(naviHintSFXList, k=2)

    for i in range(len(NaviHint)):
        for j in range(len(NaviHint[i])):
            thisNaviHintSFX = world.navi_hint_sounds[i]
            if thisNaviHintSFX == 'Random Choice':
                thisNaviHintSFX = randomNaviHintSFX[i]
            if thisNaviHintSFX == 'Notification':
                naviHintSFX = [0x48, 0x20]
            elif thisNaviHintSFX == 'Rupee':
                naviHintSFX = [0x48, 0x03]
            elif thisNaviHintSFX == 'Timer':
                naviHintSFX = [0x48, 0x1A]
            elif thisNaviHintSFX == 'Tamborine':
                naviHintSFX = [0x48, 0x42]
            elif thisNaviHintSFX == 'Recovery Heart':
                naviHintSFX = [0x48, 0x0B]
            elif thisNaviHintSFX == 'Carrot Refill':
                naviHintSFX = [0x48, 0x45]
            elif thisNaviHintSFX == 'Navi - Hey!':
                naviHintSFX = [0x68, 0x5F]
            elif thisNaviHintSFX == 'Navi - Random':
                naviHintSFX = [0x68, 0x43]
            elif thisNaviHintSFX == 'Zelda - Gasp':
                naviHintSFX = [0x68, 0x79]
            elif thisNaviHintSFX == 'Cluck':
                naviHintSFX = [0x28, 0x12]
            elif thisNaviHintSFX == 'Mweep!':
                naviHintSFX = [0x68, 0x7A]
            elif thisNaviHintSFX == 'None':
                naviHintSFX = [0x00, 0x00]
            if thisNaviHintSFX != 'Default':
                rom.write_bytes(NaviHint[i][j], naviHintSFX)

    #Low health beep
    healthSFXList = ['Default', 'Softer Beep', 'Rupee', 'Timer', 'Tamborine', 'Recovery Heart', 'Carrot Refill', 'Navi - Hey!', 'Zelda - Gasp', 'Cluck', 'Mweep!', 'None']
    randomSFX = random.choice(healthSFXList)
    address = 0xADBA1A

    if world.healthSFX == 'Random Choice':
        thisHealthSFX = randomSFX
    else:
        thisHealthSFX = world.healthSFX
    if thisHealthSFX == 'Default':
        healthSFX = [0x48, 0x1B]
    elif thisHealthSFX == 'Softer Beep':
        healthSFX = [0x48, 0x04]
    elif thisHealthSFX == 'Rupee':
        healthSFX = [0x48, 0x03]
    elif thisHealthSFX == 'Timer':
        healthSFX = [0x48, 0x1A]
    elif thisHealthSFX == 'Tamborine':
        healthSFX = [0x48, 0x42]
    elif thisHealthSFX == 'Recovery Heart':
        healthSFX = [0x48, 0x0B]
    elif thisHealthSFX == 'Carrot Refill':
        healthSFX = [0x48, 0x45]
    elif thisHealthSFX == 'Navi - Hey!':
        healthSFX = [0x68, 0x5F]
    elif thisHealthSFX == 'Zelda - Gasp':
        healthSFX = [0x68, 0x79]
    elif thisHealthSFX == 'Cluck':
        healthSFX = [0x28, 0x12]
    elif thisHealthSFX == 'Mweep!':
        healthSFX = [0x68, 0x7A]
    elif thisHealthSFX == 'None':
        healthSFX = [0x00, 0x00, 0x00, 0x00]
        address = 0xADBA14
    rom.write_bytes(address, healthSFX)

    return rom

def get_override_table(world):
    override_entries = []
    for location in world.get_locations():
        override_entries.append(get_override_entry(location))
    override_entries.sort()
    return override_entries

def get_override_entry(location):
    scene = location.scene
    default = location.default
    item_id = location.item.index
    if None in [scene, default, item_id]:
        return []

    player_id = (location.item.world.id + 1) << 3

    if location.type in ['NPC', 'BossHeart', 'Song']:
        return [scene, player_id | 0x00, default, item_id]
    elif location.type == 'Chest':
        flag = default & 0x1F
        return [scene, player_id | 0x01, flag, item_id]
    elif location.type == 'Collectable':
        return [scene, player_id | 0x02, default, item_id]
    elif location.type == 'GS Token':
        return [scene, player_id | 0x03, default, item_id]
    elif location.type == 'Shop' and location.item.type != 'Shop':
        return [scene, player_id | 0x00, default, item_id]
    elif location.type == 'GrottoNPC' and location.item.type != 'Shop':
        return [scene, player_id | 0x04, default, item_id]
    else:
        return []


chestTypeMap = {
        #    small   big     boss
    0x0000: [0x5000, 0x0000, 0x2000], #Large
    0x1000: [0x7000, 0x1000, 0x1000], #Large, Appears, Clear Flag
    0x2000: [0x5000, 0x0000, 0x2000], #Boss Key’s Chest
    0x3000: [0x8000, 0x3000, 0x3000], #Large, Falling, Switch Flag
    0x4000: [0x6000, 0x4000, 0x4000], #Large, Invisible
    0x5000: [0x5000, 0x0000, 0x2000], #Small
    0x6000: [0x6000, 0x4000, 0x4000], #Small, Invisible
    0x7000: [0x7000, 0x1000, 0x1000], #Small, Appears, Clear Flag
    0x8000: [0x8000, 0x3000, 0x3000], #Small, Falling, Switch Flag
    0x9000: [0x9000, 0x9000, 0x9000], #Large, Appears, Zelda's Lullaby
    0xA000: [0xA000, 0xA000, 0xA000], #Large, Appears, Sun's Song Triggered
    0xB000: [0xB000, 0xB000, 0xB000], #Large, Appears, Switch Flag
    0xC000: [0x5000, 0x0000, 0x2000], #Large
    0xD000: [0x5000, 0x0000, 0x2000], #Large
    0xE000: [0x5000, 0x0000, 0x2000], #Large
    0xF000: [0x5000, 0x0000, 0x2000], #Large
}

chestAnimationExtendedFast = [
    0x87, # Progressive Nut Capacity
    0x88, # Progressive Stick Capacity
    0x98, # Deku Tree Compass
    0x99, # Dodongo's Cavern Compass
    0x9A, # Jabu Jabu Compass
    0x9B, # Forest Temple Compass
    0x9C, # Fire Temple Compass
    0x9D, # Water Temple Compass
    0x9E, # Spirit Temple Compass
    0x9F, # Shadow Temple Compass
    0xA0, # Bottom of the Well Compass
    0xA1, # Ice Cavern Compass
    0xA2, # Deku Tree Map
    0xA3, # Dodongo's Cavern Map
    0xA4, # Jabu Jabu Map
    0xA5, # Forest Temple Map
    0xA6, # Fire Temple Map
    0xA7, # Water Temple Map
    0xA8, # Spirit Temple Map
    0xA9, # Shadow Temple Map
    0xAA, # Bottom of the Well Map
    0xAB, # Ice Cavern Map
    0xB6, # Recovery Heart
    0xB7, # Arrows (5)
    0xB8, # Arrows (10)
    0xB9, # Arrows (30)
    0xBA, # Bombs (5)
    0xBB, # Bombs (10)
    0xBC, # Bombs (20)
    0xBD, # Deku Nuts (5)
    0xBE, # Deku Nuts (10)
    0xD0, # Deku Stick (1)
    0xD1, # Deky Seeds (30)
]


def room_get_actors(rom, actor_func, room_data, scene, alternate=None):
    actors = {}
    room_start = alternate if alternate else room_data
    command = 0
    while command != 0x14: # 0x14 = end header
        command = rom.read_byte(room_data)
        if command == 0x01: # actor list
            actor_count = rom.read_byte(room_data + 1)
            actor_list = room_start + (rom.read_int32(room_data + 4) & 0x00FFFFFF)
            for _ in range(0, actor_count):
                actor_id = rom.read_int16(actor_list)
                entry = actor_func(rom, actor_id, actor_list, scene)
                if entry:
                    actors[actor_list] = entry
                actor_list = actor_list + 16
        if command == 0x18: # Alternate header list
            header_list = room_start + (rom.read_int32(room_data + 4) & 0x00FFFFFF)
            for alt_id in range(0,3):
                header_data = room_start + (rom.read_int32(header_list) & 0x00FFFFFF)
                if header_data != 0 and not alternate:
                    actors.update(room_get_actors(rom, actor_func, header_data, scene, room_start))
                header_list = header_list + 4
        room_data = room_data + 8
    return actors


def scene_get_actors(rom, actor_func, scene_data, scene, alternate=None, processed_rooms=None):
    if processed_rooms == None:
        processed_rooms = []
    actors = {}
    scene_start = alternate if alternate else scene_data
    command = 0
    while command != 0x14: # 0x14 = end header
        command = rom.read_byte(scene_data)
        if command == 0x04: #room list
            room_count = rom.read_byte(scene_data + 1)
            room_list = scene_start + (rom.read_int32(scene_data + 4) & 0x00FFFFFF)
            for _ in range(0, room_count):
                room_data = rom.read_int32(room_list);

                if not room_data in processed_rooms:
                    actors.update(room_get_actors(rom, actor_func, room_data, scene))
                    processed_rooms.append(room_data)
                room_list = room_list + 8
        if command == 0x0E: #transition actor list
            actor_count = rom.read_byte(scene_data + 1)
            actor_list = scene_start + (rom.read_int32(scene_data + 4) & 0x00FFFFFF)
            for _ in range(0, actor_count):
                actor_id = rom.read_int16(actor_list + 4)
                entry = actor_func(rom, actor_id, actor_list, scene)
                if entry:
                    actors[actor_list] = entry
                actor_list = actor_list + 16
        if command == 0x18: # Alternate header list
            header_list = scene_start + (rom.read_int32(scene_data + 4) & 0x00FFFFFF)
            for alt_id in range(0,3):
                header_data = scene_start + (rom.read_int32(header_list) & 0x00FFFFFF)
                if header_data != 0 and not alternate:
                    actors.update(scene_get_actors(rom, actor_func, header_data, scene, scene_start, processed_rooms))
                header_list = header_list + 4

        scene_data = scene_data + 8
    return actors

def get_actor_list(rom, actor_func):
    actors = {}
    scene_table = 0x00B71440
    for scene in range(0x00, 0x65):
        scene_data = rom.read_int32(scene_table + (scene * 0x14));
        actors.update(scene_get_actors(rom, actor_func, scene_data, scene))
    return actors

def get_override_itemid(override_table, scene, type, flags):
    for entry in override_table:
        if len(entry) == 4 and entry[0] == scene and (entry[1] & 0x07) == type and entry[2] == flags:
            return entry[3]
    return None

def update_chest_sizes(rom, override_table):
    def get_chest(rom, actor_id, actor, scene):
        if actor_id == 0x000A: #Chest Actor
            actor_var = rom.read_int16(actor + 14)
            return [scene, actor_var & 0x001F]

    chest_list = get_actor_list(rom, get_chest)
    for actor, [scene, flags] in chest_list.items():
        item_id = get_override_itemid(override_table, scene, 1, flags)

        if None in [actor, scene, flags, item_id]:
            continue
        # Do not change the size of the chest under the grave in Dodongo's Cavern MQ.
        if scene == 1 and flags == 1:
            continue

        itemType = 0  # Item animation

        if item_id >= 0x80: # if extended item, always big except from exception list
            itemType = 0 if item_id in chestAnimationExtendedFast else 1
        elif rom.read_byte(0xBEEE8E + (item_id * 6) + 2) & 0x80: # get animation from rom, ice trap is big
            itemType = 0 # No animation, small chest
        else:
            itemType = 1 # Long animation, big chest
        # Don't use boss chests

        default = rom.read_int16(actor + 14)
        chestType = default & 0xF000
        newChestType = chestTypeMap[chestType][itemType]
        default = (default & 0x0FFF) | newChestType
        rom.write_int16(actor + 14, default)

def set_grotto_id_data(rom):
    def set_grotto_id(rom, actor_id, actor, scene):
        if actor_id == 0x009B: #Grotto
            actor_zrot = rom.read_int16(actor + 12)
            actor_var = rom.read_int16(actor + 14);
            grotto_scene = actor_var >> 12
            grotto_entrance = actor_zrot & 0x000F
            grotto_id = actor_var & 0x00FF

            if grotto_scene == 0 and grotto_entrance in [2, 4, 7, 10]:
                grotto_scenes.add(scene)
                rom.write_byte(actor + 15, len(grotto_scenes))

    grotto_scenes = set()

    get_actor_list(rom, set_grotto_id)

def set_deku_salesman_data(rom):
    def set_deku_salesman(rom, actor_id, actor, scene):
        if actor_id == 0x0195: #Salesman
            actor_var = rom.read_int16(actor + 14)
            if actor_var == 6:
                rom.write_int16(actor + 14, 0x0003)

    get_actor_list(rom, set_deku_salesman)

def get_locked_doors(rom, world):
    def locked_door(rom, actor_id, actor, scene):
        actor_var = rom.read_int16(actor + 14)
        actor_type = actor_var >> 6
        actor_flag = actor_var & 0x003F

        flag_id = (1 << actor_flag)
        flag_byte = 3 - (actor_flag >> 3)
        flag_bits = 1 << (actor_flag & 0x07)

        # If locked door, set the door's unlock flag
        if world.shuffle_smallkeys == 'remove':
            if actor_id == 0x0009 and actor_type == 0x02:
                return [0x00D4 + scene * 0x1C + 0x04 + flag_byte, flag_bits]
            if actor_id == 0x002E and actor_type == 0x0B:
                return [0x00D4 + scene * 0x1C + 0x04 + flag_byte, flag_bits]

        # If boss door, set the door's unlock flag
        if world.shuffle_bosskeys == 'remove':
            if actor_id == 0x002E and actor_type == 0x05:
                return [0x00D4 + scene * 0x1C + 0x04 + flag_byte, flag_bits]

    return get_actor_list(rom, locked_door)

def place_shop_items(rom, world, shop_items, messages, locations, init_shop_id=False):
    if init_shop_id:
        place_shop_items.shop_id = 0x32

    shop_objs = { 0x0148 } # Sold Out
    messages
    for location in locations:
        shop_objs.add(location.item.object)
        if location.item.type == 'Shop':
            rom.write_int16(location.address, location.item.index)
        else:
            shop_id = place_shop_items.shop_id
            rom.write_int16(location.address, shop_id)
            shop_item = shop_items[shop_id]

            shop_item.object = location.item.object
            shop_item.model = location.item.model - 1
            shop_item.price = location.price
            shop_item.pieces = 1
            shop_item.get_item_id = location.default
            shop_item.func1 = 0x808648CC
            shop_item.func2 = 0x808636B8
            shop_item.func3 = 0x00000000
            shop_item.func4 = 0x80863FB4

            message_id = (shop_id - 0x32) * 2
            shop_item.description_message = 0x8100 + message_id
            shop_item.purchase_message = 0x8100 + message_id + 1

            shuffle_messages.shop_item_messages.extend(
                [shop_item.description_message, shop_item.purchase_message])

            if location.item.dungeonitem:
                split_item_name = location.item.name.split('(')
                split_item_name[1] = '(' + split_item_name[1]
                if world.world_count > 1:
                    description_text = '\x08\x05\x41%s  %d Rupees\x01%s\x01\x05\x42Player %d\x05\x40\x01Special deal! ONE LEFT!\x09\x0A\x02' % (split_item_name[0], location.price, split_item_name[1], location.item.world.id + 1)
                else:
                    description_text = '\x08\x05\x41%s  %d Rupees\x01%s\x01\x05\x40Special deal! ONE LEFT!\x01Get it while it lasts!\x09\x0A\x02' % (split_item_name[0], location.price, split_item_name[1])
                purchase_text = '\x08%s  %d Rupees\x09\x01%s\x01\x1B\x05\x42Buy\x01Don\'t buy\x05\x40\x02' % (split_item_name[0], location.price, split_item_name[1])
            else:
                shop_item_name = getSimpleHintNoPrefix(location.item)

                if world.world_count > 1:
                    description_text = '\x08\x05\x41%s  %d Rupees\x01\x05\x42Player %d\x05\x40\x01Special deal! ONE LEFT!\x09\x0A\x02' % (shop_item_name, location.price, location.item.world.id + 1)
                else:
                    description_text = '\x08\x05\x41%s  %d Rupees\x01\x05\x40Special deal! ONE LEFT!\x01Get it while it lasts!\x09\x0A\x02' % (shop_item_name, location.price)
                purchase_text = '\x08%s  %d Rupees\x09\x01\x01\x1B\x05\x42Buy\x01Don\'t buy\x05\x40\x02' % (shop_item_name, location.price)

            update_message_by_id(messages, shop_item.description_message, description_text, 0x03)
            update_message_by_id(messages, shop_item.purchase_message, purchase_text, 0x03)

            place_shop_items.shop_id += 1

    return shop_objs

# Format: (Title, Sequence ID)
bgm_sequence_ids = [
    ('Hyrule Field', 0x02),
    ('Dodongos Cavern', 0x18),
    ('Kakariko Adult', 0x19),
    ('Battle', 0x1A),
    ('Boss Battle', 0x1B),
    ('Inside Deku Tree', 0x1C),
    ('Market', 0x1D),
    ('Title Theme', 0x1E),
    ('House', 0x1F),
    ('Jabu Jabu', 0x26),
    ('Kakariko Child', 0x27),
    ('Fairy Fountain', 0x28),
    ('Zelda Theme', 0x29),
    ('Fire Temple', 0x2A),
    ('Forest Temple', 0x2C),
    ('Castle Courtyard', 0x2D),
    ('Ganondorf Theme', 0x2E),
    ('Lon Lon Ranch', 0x2F),
    ('Goron City', 0x30),
    ('Miniboss Battle', 0x38),
    ('Temple of Time', 0x3A),
    ('Kokiri Forest', 0x3C),
    ('Lost Woods', 0x3E),
    ('Spirit Temple', 0x3F),
    ('Horse Race', 0x40),
    ('Ingo Theme', 0x42),
    ('Fairy Flying', 0x4A),
    ('Deku Tree', 0x4B),
    ('Windmill Hut', 0x4C),
    ('Shooting Gallery', 0x4E),
    ('Sheik Theme', 0x4F),
    ('Zoras Domain', 0x50),
    ('Shop', 0x55),
    ('Chamber of the Sages', 0x56),
    ('Ice Cavern', 0x58),
    ('Kaepora Gaebora', 0x5A),
    ('Shadow Temple', 0x5B),
    ('Water Temple', 0x5C),
    ('Gerudo Valley', 0x5F),
    ('Potion Shop', 0x60),
    ('Kotake and Koume', 0x61),
    ('Castle Escape', 0x62),
    ('Castle Underground', 0x63),
    ('Ganondorf Battle', 0x64),
    ('Ganon Battle', 0x65),
    ('Fire Boss', 0x6B),
    ('Mini-game', 0x6C)
]

def randomize_music(rom):
    # Read in all the Music data
    bgm_data = []
    for bgm in bgm_sequence_ids:
        bgm_sequence = rom.read_bytes(0xB89AE0 + (bgm[1] * 0x10), 0x10)
        bgm_instrument = rom.read_int16(0xB89910 + 0xDD + (bgm[1] * 2))
        bgm_data.append((bgm_sequence, bgm_instrument))

    # shuffle data
    random.shuffle(bgm_data)

    # Write Music data back in random ordering
    for bgm in bgm_sequence_ids:
        bgm_sequence, bgm_instrument = bgm_data.pop()
        rom.write_bytes(0xB89AE0 + (bgm[1] * 0x10), bgm_sequence)
        rom.write_int16(0xB89910 + 0xDD + (bgm[1] * 2), bgm_instrument)

   # Write Fairy Fountain instrument to File Select (uses same track but different instrument set pointer for some reason)
    rom.write_int16(0xB89910 + 0xDD + (0x57 * 2), rom.read_int16(0xB89910 + 0xDD + (0x28 * 2)))

def disable_music(rom):
    # First track is no music
    blank_track = rom.read_bytes(0xB89AE0 + (0 * 0x10), 0x10)
    for bgm in bgm_sequence_ids:
        rom.write_bytes(0xB89AE0 + (bgm[1] * 0x10), blank_track)

def boss_reward_index(world, boss_name):
    code = world.get_location(boss_name).item.code
    if code >= 0x6C:
        return code - 0x6C
    else:
        return 3 + code - 0x66

def configure_dungeon_info(rom, world):
    mq_enable = world.quest == 'mixed'
    mapcompass_keysanity = world.settings.shuffle_mapcompass == 'keysanity' and world.settings.enhance_map_compass

    bosses = ['Queen Gohma', 'King Dodongo', 'Barinade', 'Phantom Ganon',
            'Volvagia', 'Morpha', 'Twinrova', 'Bongo Bongo']
    dungeon_rewards = [boss_reward_index(world, boss) for boss in bosses]

    codes = ['DT', 'DC', 'JB', 'FoT', 'FiT', 'WT', 'SpT', 'ShT',
            'BW', 'IC', 'Tower (N/A)', 'GTG', 'Hideout (N/A)', 'GC']
    dungeon_is_mq = [1 if world.dungeon_mq.get(c) else 0 for c in codes]

    rom.write_int32(rom.sym('cfg_dungeon_info_enable'), 1)
    rom.write_int32(rom.sym('cfg_dungeon_info_mq_enable'), int(mq_enable))
    rom.write_int32(rom.sym('cfg_dungeon_info_mq_need_map'), int(mapcompass_keysanity))
    rom.write_int32(rom.sym('cfg_dungeon_info_reward_need_compass'), int(mapcompass_keysanity))
    rom.write_int32(rom.sym('cfg_dungeon_info_reward_need_altar'), int(not mapcompass_keysanity))
    rom.write_bytes(rom.sym('cfg_dungeon_rewards'), dungeon_rewards)
    rom.write_bytes(rom.sym('cfg_dungeon_is_mq'), dungeon_is_mq)
