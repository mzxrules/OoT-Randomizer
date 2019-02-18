import os

from Dungeon import Dungeon
from Item import ItemFactory
from Utils import data_path


dungeon_table = [
    {
        'name': 'Woodfall Temple',
        'boss_key':     1,
        'small_key':    1,
        'dungeon_item': 1,
    },
    {
        'name': 'Snowhead Temple',
        'boss_key':     1,
        'small_key':    3,
        'dungeon_item': 1,
    },
    {
        'name': 'Great Bay Temple',
        'boss_key':     1,
        'small_key':    1,
        'dungeon_item': 1,
    },
    {
        'name': 'Stone Tower Temple',
        'boss_key':     1,
        'small_key':    4,
        'dungeon_item': 1,
    }
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
