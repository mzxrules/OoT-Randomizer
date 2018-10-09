import random

from BaseClasses import Dungeon
from Items import ItemFactory


def create_dungeons(world):
    def make_dungeon(name, dungeon_regions_names, boss_key, small_keys, dungeon_items):
        dungeon_regions = [world.get_region(region) for region in dungeon_regions_names]

        dungeon = Dungeon(name, dungeon_regions, boss_key, small_keys, dungeon_items)
        for region in dungeon.regions:
            region.dungeon = dungeon
        return dungeon

    WF = make_dungeon(
        'Woodfall Temple',
       ['Woodfall Temple Beginning', 'Woodfall Temple Central Pillar'], 
       ItemFactory('Boss Key (Woodfall Temple)'), 
       ItemFactory(['Small Key (Woodfall Temple)'] * 1),
       ItemFactory(['Map (Woodfall Temple)', 'Compass (Woodfall Temple)']))

    SH = make_dungeon(
        'Snowhead Temple', 
        ['Snowhead Temple Beginning'], 
        ItemFactory('Boss Key (Snowhead Temple)'), 
        ItemFactory(['Small Key (Snowhead Temple)'] * 3), 
        ItemFactory(['Map (Snowhead Temple)', 'Compass (Snowhead Temple)']))

    GB = make_dungeon(
        'Great Bay Temple', 
        ['Great Bay Temple Beginning'], 
        ItemFactory('Boss Key (Great Bay Temple)'), 
        ItemFactory(['Small Key (Great Bay Temple)'] * 1), 
        ItemFactory(['Map (Great Bay Temple)', 'Compass (Great Bay Temple)']))

    ST = make_dungeon(
        'Stone Tower Temple', 
        ['Stone Tower Temple Beginning'], 
        ItemFactory('Boss Key (Stone Tower Temple)'), 
        ItemFactory(['Small Key (Stone Tower Temple)'] * 2), 
        ItemFactory(['Map (Stone Tower Temple)', 'Compass (Stone Tower Temple)']))

    world.dungeons = [WF, SH, GB, ST]