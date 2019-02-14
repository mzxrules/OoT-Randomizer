import random
import os

from Dungeon import Dungeon
from Item import ItemFactory
from Utils import data_path


dungeon_table = [
    {
        'name': 'Deku Tree',
        'boss_key':     0,
        'small_key':    0,
        'dungeon_item': 1,
    },
    {
        'name': 'Dodongos Cavern',
        'boss_key':     0,
        'small_key':    0,
        'dungeon_item': 1,
    },
    {
        'name': 'Jabu Jabus Belly',
        'boss_key':     0,
        'small_key':    0,
        'dungeon_item': 1,
    },
    {
        'name': 'Forest Temple',
        'boss_key':     1,
        'small_key':    5,
        'dungeon_item': 1,
    },
    {
        'name': 'Bottom of the Well',
        'boss_key':     0,
        'small_key':    3,
        'dungeon_item': 1,
    },
    {
        'name': 'Fire Temple',
        'boss_key':     1,
        'small_key':    8,
        'dungeon_item': 1,
    },
    {
        'name': 'Ice Cavern',
        'boss_key':     0,
        'small_key':    0,
        'dungeon_item': 1,
    },
    {
        'name': 'Water Temple',
        'boss_key':     1,
        'small_key':    6,
        'dungeon_item': 1,
    },
    {
        'name': 'Shadow Temple',
        'boss_key':     1,
        'small_key':    5,
        'dungeon_item': 1,
    },
    {
        'name': 'Gerudo Training Grounds',
        'boss_key':     0,
        'small_key':    9,
        'dungeon_item': 0,
    },
    {
        'name': 'Spirit Temple',
        'boss_key':     1,
        'small_key':    5,
        'dungeon_item': 1,
    },
    {
        'name': 'Ganons Castle',
        'boss_key':     1,
        'small_key':    2,
        'dungeon_item': 0,
    },
]


def create_dungeons(world):
    for dungeon_info in dungeon_table:
        name = dungeon_info['name']
        dungeon_json = os.path.join(data_path('World'), name + '.json')
        world.load_regions_from_json(dungeon_json)

        boss_keys = ItemFactory(['Boss Key (%s)' % name] * dungeon_info['boss_key'])
        small_keys = ItemFactory(['Small Key (%s)' % name] * dungeon_info['small_key'])
        dungeon_items = ItemFactory(['Map (%s)' % name,
                                     'Compass (%s)' % name] * dungeon_info['dungeon_item'])

        world.dungeons.append(Dungeon(world, name, boss_keys, small_keys, dungeon_items))

