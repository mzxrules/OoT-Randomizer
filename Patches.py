import io
import json
import logging
import os
import platform
import struct
import subprocess
import random
import copy

from Hints import writeGossipStoneHintsHints, buildBossRewardHints, buildGanonText, getSimpleHintNoPrefix
from Utils import local_path, default_output_path, random_choices
from Items import ItemFactory, item_data
from Messages import *
from OcarinaSongs import Song, str_to_song, replace_songs
from MQ import patch_files, File, update_dmadata, insert_space, add_relocations

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

    # Load Message and Shop Data
    # messages = read_messages(rom)
     # remove_unused_messages(messages)

    # Sets hooks for gossip stone changes
    if world.hints != 'none':
        pass # writeGossipStoneHintsHints(world, messages)

    # DOOT: Update for MM
    # Write item overrides
    override_table = get_override_table(world)
    # rom.write_bytes(0x3481000, sum(override_table, []))
    # rom.write_byte(0x03481C00, world.id + 1) # Write player ID

    # DOOT: Find appropriate address to do this in MM
    # Set default targeting option to Hold
    if world.default_targeting == 'hold':
        pass # rom.write_byte(0xB71E6D, 0x01)

    # Patch songs and boss rewards
    for location in world.get_locations():
        item = location.item
        itemid = copy.copy(item.code)
        locationaddress = location.address
        secondaryaddress = location.address2

        if itemid is None or location.address is None:
            pass

        if location.type == 'Song' and not world.shuffle_song_items:
            # DOOT: find out what things we need to patch for this to work
            pass
        elif location.type == 'Boss':
            rom.write_byte(locationaddress, itemid)
            rom.write_byte(secondaryaddress, item_data[item.name][2])

    if world.shuffle_smallkeys == 'remove' or world.shuffle_bosskeys == 'remove':
        locked_doors = get_locked_doors(rom, world)
        for _,[door_byte, door_bits] in locked_doors.items():
            write_bits_to_save(door_byte, door_bits)

    # Update chest type sizes
    if world.correct_chest_sizes:
        update_chest_sizes(rom, override_table)

    # DOOT: Update these messages to reflect MM
    # give dungeon items the correct messages
    # message_patch_for_dungeon_items(messages, shop_items, world)
    if world.shuffle_mapcompass == 'keysanity' and world.enhance_map_compass:
        reward_list = {'Odolwa\'s Remains': "\x05\x42Odolwa\'s Remains\x05\x40",
                       'Goht\'s Remains':   "\x05\x41Goht\'s Remains\x05\x40",
                       'Gyorg\'s Remains':  "\x05\x43Gyorg\'s Remains\x05\x40",
                       'Twinmold\'s Remains': "\x05\x45Twinmold\'s Remains\x05\x40",
        }
        dungeon_list = {'WFT':  ("the \x05\x42Woodfall Temple", 'Odolwa', 0x65, 0x8b),
                        'SHT':  ("the \x05\x41Snowhead Temple", 'Goht', 0x7c, 0x8c),
                        'GBT':   ("the \x05\x43Great Bay Temple", 'Gyorg', 0x7d, 0x8e),
                        'STT':   ("the \x05\x45Stone Tower Temple", 'Twinmold', 0x7f, 0xa3),
        }

    # Set hints for boss reward shuffle # DOOT: Find correct thing in MM
    # rom.write_bytes(0xE2ADB2, [0x70, 0x7A])
    # rom.write_bytes(0xE2ADB6, [0x70, 0x57])
    # buildBossRewardHints(world, messages)

    # add song messages
    # add_song_messages(messages, world)

    # reduce item message lengths
    # update_item_messages(messages, world)

    # DOOT: create a third wallet for MM
    # repack_messages(rom, messages)
    # write_shop_items(rom, shop_item_file.start + 0x1DEC, shop_items)

    # text shuffle
    if world.text_shuffle == 'except_hints':
        pass # shuffle_messages(rom, except_hints=True)
    elif world.text_shuffle == 'complete':
        pass # shuffle_messages(rom, except_hints=False)

    # output a text dump, for testing...
    #with open('keysanity_' + str(world.seed) + '_dump.txt', 'w', encoding='utf-16') as f:
    #     messages = read_messages(rom)
    #     f.write('item_message_strings = {\n')
    #     for m in messages:
    #        f.write("\t0x%04X: \"%s\",\n" % (m.id, m.get_python_string()))
    #     f.write('}\n')

    if world.ocarina_songs:
        pass # replace_songs(rom, scarecrow_song)

    # actually write the save table to rom
    # write_save_table(rom)

    # patch music
    if world.background_music == 'random':
        randomize_music(rom)
    elif world.background_music == 'off':
        disable_music(rom)

    # re-seed for aesthetic effects. They shouldn't be affected by the generation seed
    random.seed()
    # Human Link Colors
    # set_color(world, rom, [0x0116639C, 0x011668C4, 0x01166DCC, 0x01166FA4, 0x01167064, 0x0116766C, 0x01167AE4, 0x01167D1C, 0x011681EC], world.tunic_colors[0])
    set_color(world, rom, [0x0116639C, 0x011668C4, 0x01166DCC], world.tunic_colors[1])
    set_color(world, rom, [0x01166FA4, 0x01167064, 0x0116766C, 0x01167AE4], world.tunic_colors[0])
    set_color(world, rom, [0x01167D1C, 0x011681EC], world.tunic_colors[2])
    # Deku Link Colors
    # set_color(world, rom, [0x011A8EB2], world.tunic_palettes[0], 256, True)
    # set_color(world, rom, [0x011A8F32], world.tunic_palettes[1], 32, True)
    set_color(world, rom, [0x011A90B0], world.tunic_palettes[2], 1, True)
    # Goron Link Colors
    set_color(world, rom, [0x0117C780, 0x01186EB8, 0x01186F38], world.tunic_palettes[3], 64, True)
    set_color(world, rom, [0x0117C800], world.tunic_palettes[4], 64, True)
    set_color(world, rom, [0x01197000], world.tunic_palettes[5], 256, True)
    set_color(world, rom, [0x0119E578], world.tunic_palettes[6], 256, True)
    set_color(world, rom, [0x01197140], world.tunic_palettes[7], 32, True)
    set_color(world, rom, [0x01197100], world.tunic_palettes[8], 32, True)
    set_color(world, rom, [0x010FB0B0, 0x011A2228], world.tunic_palettes[9], 512, True)
    # patch navi colors

    #Navi hints

    #Low health beep

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
        if actor_id == 0x0006: #Chest Actor
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

# Woops
# Format: (Title, Sequence ID)
bgm_sequence_ids = [
    (0x02, 'Termina Field'),
    (0x03, 'Forest Chase'),
    (0x04, 'Majora\'s Theme'),
    (0x05, 'Clock Tower'),
    (0x06, 'Stone Tower Temple'),
    (0x07, 'Inverted Stone Tower Temple'),
    (0x09, 'Title'),
    (0x0A, 'Mask Salesman'),
    (0x0B, 'Song of Healing'),
    (0x0C, 'Southern Swamp'),
    (0x0D, 'Aliens'),
    (0x0E, 'Mini Game'),
    (0x0F, 'Sharp\'s Curse'),
    (0x10, 'Great Bay Coast'),
    (0x11, 'Ikana Valley'),
    (0x12, 'Deku Palace Royal Chamber'),
    (0x13, 'Mountain Village'),
    (0x14, 'Pirates Fortress'),
    (0x15, 'Clock Town Day 1'),
    (0x16, 'Clock Town Day 2'),
    (0x17, 'Clock Town Day 3'),
    # (0x18, '[File Select]'),
    (0x1A, 'Battle'),
    (0x1B, 'Boss Battle'),
    (0x1C, 'Woodfall Temple'),
    (0x1D, 'Clock Town Day 1 Duplicate'),
    (0x1E, 'Forest Ambush'),
    (0x1F, 'House'),
    (0x23, 'Clock Town Day 2 Duplicate'),
    (0x25, 'Mini Game 2'),
    (0x26, 'Goron Race'),
    (0x27, 'Music Box House'),
    (0x28, 'Fairy Fountain'),
    (0x29, 'Zelda\'s Lullaby'),
    (0x2A, 'Rosa Sisters Dance'),
    (0x2C, 'Marine Research Lab'),
    (0x2D, 'The Four Giants'),
    (0x2E, 'Windmill Guy'),
    (0x2F, 'Romani Ranch'),
    (0x30, 'Goron Village'),
    (0x31, 'Mayor Dotour'),
    (0x36, 'Zora Hall'),
    (0x38, 'Mini Boss'),
    (0x3A, 'Astral Observatory'),
    (0x3B, 'Clock Town Cavern'),
    (0x3C, 'Milk Bar'),
    (0x3E, 'Woods of Mystery'),
    (0x40, 'Gorman Race'),
    (0x43, 'Potion Shop'),
    (0x44, 'Store'),
    (0x45, 'Gaebora'),
    (0x46, 'Target Practice'),
    (0x50, 'Sword Training'),
    (0x53, 'Bremen March'),
    (0x54, 'Ballad of the Wind Fish'),
    (0x55, 'Song of Soaring'),
    (0x56, 'Milk Bar Duplicate'),
    (0x57, 'Final Hours'),
    (0x58, 'Mikau\'s Tale'),
    (0x5A, 'Don Gero\'s Song'),
    (0x60, 'Moon?'),
    (0x65, 'Snowhead Temple'),
    (0x66, 'Great Bay Temple'),
    # (0x67, 'Demo Tide Sax'),
    # (0x68, 'Demo Tide Vocal'),
    (0x69, 'Majora\'s Wrath'),
    (0x6A, 'Majora\'s Incarnation'),
    (0x6B, 'Majora\'s Mask Battle'),
    (0x6C, 'Bass Practice'),
    (0x6D, 'Drums Practice'),
    (0x6E, 'Piano Practice'),
    (0x6F, 'Ikana Castle'),
    (0x70, 'Calling the Four Giants'),
    (0x71, 'Kamaro\'s Dance'),
    (0x72, 'Cremia\'s Wagon'),
    (0x73, 'Keaton'),
    (0x74, 'End Credits'),
    (0x75, 'Forest Ambush Duplicate'),
    (0x76, 'Title Screen'),
    (0x7B, 'To The Moon'),
    (0x7C, 'Bye Giants'),
    (0x7D, 'Tatl and Tael'),
    (0x7E, 'Moon Destruction'),
    (0x7F, 'End Credits 2')
]
short_bgm_sequence_ids = [
    (0x08, 'Event Failed'),
    (0x19, 'Event Clear'),
    (0x20, 'Game Over'),
    (0x21, 'Boss Clear'),
    (0x22, 'Item Catch'),
    (0x24, 'Heart Piece Get'),
    (0x2B, 'Open Chest'),
    (0x32, 'Ocarina Epona\'s Song'),
    (0x33, 'Ocarina Sun\'s Song'),
    (0x34, 'Ocarina Song of Time'),
    (0x35, 'Ocarina Song of Storms'),
    (0x37, 'A New Mask'),
    (0x39, 'Small Item Catch'),
    (0x3D, 'Appear'),
    (0x3F, 'Goron Race Finish'),
    (0x41, 'Race Finish'),
    (0x42, 'Gorman Bros.'),
    (0x47, 'Ocarina Song of Soaring'),
    (0x48, 'Ocarina Song of Healing'),
    (0x49, 'Inverted Song Time'),
    (0x4A, 'Song of Double Time'),
    (0x4B, 'Sonata of Awakening'),
    (0x4C, 'Goron Lullaby'),
    (0x4D, 'New Wave Bossa Nova'),
    (0x4E, 'Elegy of Emptiness'),
    (0x4F, 'Oath to Order'),
    (0x51, 'Ocarina Goron Lullaby Intro'),
    (0x52, 'New Song'),
    (0x59, 'Single Guitar Chord'),
    (0x5B, 'Ocarina Sonata of Awakening'),
    (0x5C, 'Ocarina Goron Lullaby'),
    (0x5D, 'Ocarina New Wave Bossa Nova'),
    (0x5E, 'Ocarina Elegy of Emptiness'),
    (0x5F, 'Ocarina Oath to Order'),
    (0x61, 'Ocarina Goron Lullaby Intro'),
    (0x62, 'Bass Guitar Session'),
    (0x63, 'Piano Solo'),
    (0x64, 'Indigogo Rehearsal'),
    (0x77, 'Surfacing Woodfall'),
    (0x78, 'Woodfall Clear'),
    (0x79, 'Snowhead Clear'),
]

def randomize_music_sequence_ids(rom, sequence_ids):
    # Read in all the Music data
    bgm_data = []
    for bgm in sequence_ids:
        bgm_sequence = rom.read_bytes(0xC77B80 + (bgm[0] * 0x10), 0x10)
        bgm_instrument = rom.read_int16(0xC77A62 + (bgm[0] * 2))
        bgm_data.append((bgm_sequence, bgm_instrument))

    # shuffle data
    random.shuffle(bgm_data)

    # Write Music data back in random ordering
    for bgm in sequence_ids:
        bgm_sequence, bgm_instrument = bgm_data.pop()
        rom.write_bytes(0xC77B80+ (bgm[0] * 0x10), bgm_sequence)
        rom.write_int16(0xC77A62 + (bgm[0] * 2), bgm_instrument)


def randomize_music(rom):
    randomize_music_sequence_ids( rom, bgm_sequence_ids )
    randomize_music_sequence_ids( rom, short_bgm_sequence_ids )

   # Write Fairy Fountain instrument to File Select (uses same track but different instrument set pointer for some reason)
    rom.write_int16(0xC77A62 + (0x18 * 2), rom.read_int16(0xC77A62 + (0x28 * 2)))

def disable_music(rom):
    # First track is no music
    blank_track = rom.read_bytes(0xC77B80 + (0 * 0x10), 0x10)
    for bgm in bgm_sequence_ids:
        rom.write_bytes(0xC77B80 + (bgm[0] * 0x10), blank_track)

def boss_reward_index(world, boss_name):
    code = world.get_location(boss_name).item.code
    if code >= 0x6C:
        return code - 0x6C
    else:
        return 3 + code - 0x66

def set_color(world, rom, offsets, thisColor, length=1, pack=False):
    colorList = get_tunic_colors()
    randomColors = random_choices(colorList, k=3)
    randColor = [random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)]
    if thisColor == 'Completely Random':
        color = randColor
    else:
        # handle random
        if thisColor == 'Random Choice':
            color = TunicColors[randomColors[i]]
        # grab the color from the list
        elif thisColor in TunicColors:
            color = TunicColors[thisColor]
        # build color from hex code
        else:
            color = list(int(thisColor[i:i+2], 16) for i in (0, 2 ,4))
    for offset in offsets:
        if pack:
            red = int( color[0] / 8 )
            green = int( color[1] / 8 )
            blue = int( color[2] / 8 )
            packedColor = 0x1 | (blue << 1) | (green << 6) | (red<< 11)
            print( color, '->', hex(packedColor) )

            for short in range(length):
                rom.write_int16(offset+(short*2), packedColor)
        else:
            for word in range(length):
                rom.write_bytes(offset+(word*4), color)

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
