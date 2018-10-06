import random

def link_entrances(world):

    # setup mandatory connections
    for exitname, regionname in mandatory_connections:
        connect_simple(world, exitname, regionname)
    if world.dungeon_mq['DT']:
        for exitname, regionname in DT_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in DT_vanilla_connections:
            connect_simple(world, exitname, regionname)
    if world.dungeon_mq['DC']:
        for exitname, regionname in DC_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in DC_vanilla_connections:
            connect_simple(world, exitname, regionname)
    if world.dungeon_mq['JB']:
        for exitname, regionname in JB_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in JB_vanilla_connections:
            connect_simple(world, exitname, regionname)
    if world.dungeon_mq['FoT']:
        for exitname, regionname in FoT_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in FoT_vanilla_connections:
            connect_simple(world, exitname, regionname)
    if world.dungeon_mq['FiT']:
        for exitname, regionname in FiT_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in FiT_vanilla_connections:
            connect_simple(world, exitname, regionname)
    if world.dungeon_mq['WT']:
        for exitname, regionname in WT_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in WT_vanilla_connections:
            connect_simple(world, exitname, regionname)
    if world.dungeon_mq['GTG']:
        for exitname, regionname in GTG_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in GTG_vanilla_connections:
            connect_simple(world, exitname, regionname)
    if world.dungeon_mq['SpT']:
        for exitname, regionname in SpT_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in SpT_vanilla_connections:
            connect_simple(world, exitname, regionname)
    if world.dungeon_mq['ShT']:
        for exitname, regionname in ShT_MQ_connections:
            connect_simple(world, exitname, regionname)
    else:
        for exitname, regionname in ShT_vanilla_connections:
            connect_simple(world, exitname, regionname)
    # if we do not shuffle, set default connections
    if world.shuffle == 'vanilla':
        for exitname, regionname in default_connections:
            connect_simple(world, exitname, regionname)
        for exitname, regionname in default_dungeon_connections:
            connect_simple(world, exitname, regionname)
    else:
        raise NotImplementedError('Shuffling not supported yet')


def connect_simple(world, exitname, regionname):
    world.get_entrance(exitname).connect(world.get_region(regionname))

def connect_entrance(world, entrancename, exitname):
    entrance = world.get_entrance(entrancename)
    # check if we got an entrance or a region to connect to
    try:
        region = world.get_region(exitname)
        exit = None
    except RuntimeError:
        exit = world.get_entrance(exitname)
        region = exit.parent_region

    # if this was already connected somewhere, remove the backreference
    if entrance.connected_region is not None:
        entrance.connected_region.entrances.remove(entrance)

    target = exit_ids[exit.name][0] if exit is not None else exit_ids.get(region.name, None)
    addresses = door_addresses[entrance.name][0]

    entrance.connect(region, addresses, target)
    world.spoiler.set_entrance(entrance.name, exit.name if exit is not None else region.name, 'entrance')


def connect_exit(world, exitname, entrancename):
    entrance = world.get_entrance(entrancename)
    exit = world.get_entrance(exitname)

    # if this was already connected somewhere, remove the backreference
    if exit.connected_region is not None:
        exit.connected_region.entrances.remove(exit)

    exit.connect(entrance.parent_region, door_addresses[entrance.name][1], exit_ids[exit.name][1])
    world.spoiler.set_entrance(entrance.name, exit.name, 'exit')


def connect_random(world, exitlist, targetlist, two_way=False):
    targetlist = list(targetlist)
    random.shuffle(targetlist)

    for exit, target in zip(exitlist, targetlist):
        if two_way:
            connect_two_way(world, exit, target)
        else:
            connect_entrance(world, exit, target)


def connect_doors(world, doors, targets):
    """This works inplace"""
    random.shuffle(doors)
    random.shuffle(targets)
    while doors:
        door = doors.pop()
        target = targets.pop()
        connect_entrance(world, door, target)


def connect_fairy(world, entrancename, exitname):
    entrance = world.get_entrance(entrancename)
    exit = world.get_region(exitname)

    entrance.connect(exit, Fairy_addresses[entrance.name], Fairy_IDs[exit.name])
    world.spoiler.set_entrance(entrance.name, exit.name, 'both')

# these are connections that cannot be shuffled and always exist.
# They logically separate areas that do not cross loading zones
mandatory_connections = [ ('Cursed Underground', 'Clock Tower'),
                                                ('South Mailbox', 'Mailbox'),
                                                ('East Mailbox', 'Mailbox'),
                                                ('North Mailbox', 'Mailbox'),
                                                ('Tunnel Balloon From Observatory', 'Bomber Tunnel'),
                                                ('Tunnel Balloon From ECT', 'Astral Observatory'),
                                                ('Termina Field North Exit', 'Path to Mountain Village South'),
                                                ('Termina Field From Mountain', 'Termina Field'),
                                                ('Mountain Snowball Block', 'Path to Mountain Village North'),
                                                ('Mountain Snowball Block Backwards', 'Path to Mountain Village South'),
                                                ('Great Bay Gate', 'Great Bay Coast'),
                        ]

# these connections are the pairs of owl statues that may be shuffled

# entrances that cross a loading zone and may be shuffled
default_connections = [('Clock Tower Exit', 'South Clock Town'),
                                        ('Clock Tower Twisted Hallway', 'Clock Tower'),
                                        ('Clock Tower Twisted Hallway Backwards', 'Deku Flower Tutorial Area'),
                                        ('Clock Tower Entrance', 'Clock Tower'),
                                        ('Clock Tower Carnival Door', 'Clock Tower Rooftop'),
                                        ('SCT Top Exit to WCT', 'West Clock Town'),
                                        ('SCT Bottom Exit to WCT', 'West Clock Town'),
                                        ('SCT Exit to NCT', 'SCT Exit to NCT', 'North Clock Town'),
                                        ('SCT Bottom Exit to ECT', 'East Clock Town'),
                                        ('SCT Top Exit to ECT', 'East Clock Town'),
                                        ('Clock Town South Gate', 'Termina Field'),
                                        ('SCT Exit to Laundry Pool', 'Laundry Pool'),
                                        ('Honey and Darling', 'Honey and Darling'),
                                        ('Treasure Chest Shop', 'Treasure Chest Shop'),
                                        ('Town Shooting Gallery', 'Town Shooting Gallery'),
                                        ('Milk Bar', 'Milk Bar'),
                                        ('Stock Pot Inn', 'Stock Pot Inn'),
                                        ('Stock Pot Inn Secret Entrance', 'Stock Pot Inn'),
                                        ('Mayors Office', 'Mayors Office'),
                                        ('Bomber Bouncer', 'Bomber Tunnel'),
                                        ('Honey and Darling Exit', 'East Clock Town'),
                                        ('Treasure Chest Shop Exit', 'East Clock Town'),
                                        ('Town Shooting Gallery Exit', 'East Clock Town'),
                                        ('Milk Bar Exit', 'East Clock Town'),
                                        ('Stock Pot Inn Roof', 'East Clock Town'),
                                        ('Stock Pot Inn Front Door', 'East Clock Town'),
                                        ('Mayors Office Exit', 'East Clock Town'),
                                        ('Bomber Tunnel Exit', 'East Clock Town'),
                                        ('ECT Top Exit to SCT', 'South Clock Town'),
                                        ('ECT Bottom Exit to SCT', 'South Clock Town'),
                                        ('ECT Exit to NCT', 'North Clock Town'),
                                        ('Clock Town East Gate', 'Termina Field'),
                                        ('Curiosity Shop', 'Curiosity Shop'),
                                        ('Trading Post', 'Trading Post'),
                                        ('Bomb Shop', 'Bomb Shop'),
                                        ('Post Office', 'Post Office'),
                                        ('Lottery Shop', 'Lottery Shop'),
                                        ('Swordsmans School', 'Swordsmans School'),
                                        ('Curiosity Shop Exit', 'West Clock Town'),
                                        ('Trading Post Exit', 'West Clock Town'),
                                        ('Bomb Shop Exit', 'West Clock Town'),
                                        ('Post Office Exit', 'West Clock Town'),
                                        ('Lottery Shop Exit', 'WestClock Town'),
                                        ('Swordsmans School Exit', 'West Clock Town'),
                                        ('Clock Town West Gate', 'Termina Field'),
                                        ('WCT Top Exit to SCT', 'South Clock Town'),
                                        ('WCT Bottom Exit to SCT', 'South Clock Town'),
                                        ('Deku Playground', 'Deku Playground'),
                                        ('Deku Playground Exit', 'North Clock Town'),
                                        ('GF Clock Town', 'Clock Town Fairy Shrine'),
                                        ('South Gate to Clock Town', 'South Clock Town'),
                                        ('North Gate to Clock Town', 'North Clock Town'),
                                        ('West Gate to Clock Town', 'West Clock Town'),
                                        ('East Gate to Clock Town', 'East Clock Town'),
                                        ('Termina Field to Swamp', 'Path to Swamp'),
                                        ('Termina Field to Ikana', 'Path to Ikana'),

                                        ('GF Woodfall', 'Woodfall Fairy Shrine'),

                                        ('Mountain Icicles', 'Path to Mountain Village South'),
                                        ('Mountain Icicles Backwards', 'Path to Mountain Village South'),
                                        ('Mountain Village Entrance', 'Mountain Village'),
                                        (''),
                                        ('GF Snowhead', 'Snowhead Fairy Shrine'),

                                        ('GF Great Bay', 'Great Bay Fairy Shrine'),

                                        ('GF Stone Tower', 'Stone Tower Fairy Shrine'),
                                        ]

# dungeon entrance links
default_dungeon_connections = [('Woodfall Temple Entrance', 'Woodfall Temple Lobby'),
                              ]
