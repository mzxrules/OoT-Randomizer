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
    WF = make_dungeon('Woodfall Temple', ['Woodfall Temple Beginning', 'Woodfall Temple Central Pillar'], ItemFactory('Boss Key (Woodfall Temple)'), ItemFactory(['Small Key (Woodfall Temple)'] * 1), ItemFactory(['Map (Woodfall Temple)', 'Compass (Woodfall Temple)']))
    SH = make_dungeon('Snowhead Temple', ['Snowhead Temple Beginning'], ItemFactory('Boss Key (Snowhead Temple)'), ItemFactory(['Small Key (Snowhead Temple)'] * 3), ItemFactory(['Map (Snowhead Temple)', 'Compass (Snowhead Temple)']))
    GB = make_dungeon('Great Bay Temple', ['Great Bay Temple Beginning'], ItemFactory('Boss Key (Great Bay Temple)'), ItemFactory(['Small Key (Great Bay Temple)'] * 1), ItemFactory(['Map (Great Bay Temple)', 'Compass (Great Bay Temple)']))
    ST = make_dungeon('Stone Tower Temple', ['Stone Tower Temple Beginning'], ItemFactory('Boss Key (Stone Tower Temple)'), ItemFactory(['Small Key (Stone Tower Temple)'] * 2), ItemFactory(['Map (Stone Tower Temple)', 'Compass (Stone Tower Temple)']))

    if world.dungeon_mq['DT']:
        DT = make_dungeon(
            'Deku Tree', 
            ['Deku Tree Lobby', 'Deku Tree Compass Room', 'Deku Tree Boss Room'], 
            None, [],
            ItemFactory(['Map (Deku Tree)', 'Compass (Deku Tree)']))
    else:
        DT = make_dungeon(
            'Deku Tree', 
            ['Deku Tree Lobby', 'Deku Tree Slingshot Room', 'Deku Tree Boss Room'], 
            None, [],
            ItemFactory(['Map (Deku Tree)', 'Compass (Deku Tree)']))
    world.dungeons = [WF, SH, GB, ST]



    if world.dungeon_mq['BW']:
        BW = make_dungeon(
            'Bottom of the Well', 
            ['Bottom of the Well'], 
            None, 
            ItemFactory(['Small Key (Bottom of the Well)'] * 2), 
            ItemFactory(['Map (Bottom of the Well)', 'Compass (Bottom of the Well)']))
    else:
        BW = make_dungeon(
            'Bottom of the Well', 
            ['Bottom of the Well'], 
            None, 
            ItemFactory(['Small Key (Bottom of the Well)'] * 3), 
            ItemFactory(['Map (Bottom of the Well)', 'Compass (Bottom of the Well)']))

    if world.dungeon_mq['FiT']:
        FiT = make_dungeon(
            'Fire Temple', 
            ['Fire Temple Lower', 'Fire Lower Locked Door', 'Fire Big Lava Room', 'Fire Lower Maze', 'Fire Upper Maze', 
             'Fire Temple Upper', 'Fire Boss Room'], 
            ItemFactory('Boss Key (Fire Temple)'), 
            ItemFactory(['Small Key (Fire Temple)'] * 5), 
            ItemFactory(['Map (Fire Temple)', 'Compass (Fire Temple)']))
    else:
        FiT = make_dungeon(
            'Fire Temple', 
            ['Fire Temple Lower', 'Fire Temple Middle', 'Fire Temple Upper'], 
            ItemFactory('Boss Key (Fire Temple)'), 
            ItemFactory(['Small Key (Fire Temple)'] * 8), 
            ItemFactory(['Map (Fire Temple)', 'Compass (Fire Temple)']))

    # Ice Cavern is built identically in vanilla and MQ
    IC = make_dungeon(
        'Ice Cavern', 
        ['Ice Cavern'], 
        None, [], 
        ItemFactory(['Map (Ice Cavern)', 'Compass (Ice Cavern)']))

    if world.dungeon_mq['WT']:
        WT = make_dungeon(
            'Water Temple', 
            ['Water Temple Lobby', 'Water Temple Lowered Water Levels', 'Water Temple Dark Link Region', 
             'Water Temple Basement Gated Areas'], 
            ItemFactory('Boss Key (Water Temple)'), 
            ItemFactory(['Small Key (Water Temple)'] * 2), 
            ItemFactory(['Map (Water Temple)', 'Compass (Water Temple)']))
    else:
        WT = make_dungeon(
            'Water Temple', 
            ['Water Temple Lobby', 'Water Temple Middle Water Level', 'Water Temple Dark Link Region'], 
            ItemFactory('Boss Key (Water Temple)'), 
            ItemFactory(['Small Key (Water Temple)'] * 6), 
            ItemFactory(['Map (Water Temple)', 'Compass (Water Temple)']))

