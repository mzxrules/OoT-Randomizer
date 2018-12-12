import random

def link_entrances(world):

    # setup mandatory connections
    for exitname, regionname in mandatory_connections:
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
mandatory_connections = [
    ('Cursed Underground', 'Clock Tower Basement'),
    ('South Mailbox', 'Mailbox'),
    ('East Mailbox', 'Mailbox'),
    ('North Mailbox', 'Mailbox'),
    ('Tunnel Balloon From Observatory', 'Bomber Tunnel'),
    ('Tunnel Balloon From ECT', 'Astral Observatory'),
    ('TF Mountain Icicles', 'Beyond The Icicles'),
    ('TF Mountain Icicles Backwards', 'Termina Field'),
    ('Mountain Snowball Block', 'Path to Mountain Village North'),
    ('Mountain Snowball Block Backwards', 'Path to Mountain Village South'),
    ('TF Great Bay Gate', 'Beyond Great Bay Gate'),
    ('TF Great Bay Gate Backwards', 'Termina Field'),
    ]

# these connections are the pairs of owl statues that may be shuffled

# entrances that cross a loading zone and may be shuffled
default_connections = [
    ('Clock Tower Exit', 'South Clock Town'),
    ('Clock Tower Twisted Hallway', 'Clock Tower Basement'),
    ('Clock Tower Twisted Hallway Backwards', 'Deku Flower Tutorial Area'),
    ('To Clock Tower Basement', 'Clock Tower Basement'),
    ('To Clock Tower Rooftop', 'Clock Tower Rooftop'),
    ('SCT Top Exit to WCT', 'West Clock Town'),
    ('SCT Bottom Exit to WCT', 'West Clock Town'),
    ('SCT Exit to NCT', 'North Clock Town'),
    ('SCT Bottom Exit to ECT', 'East Clock Town'),
    ('SCT Top Exit to ECT', 'East Clock Town'),
    ('Clock Town South Gate', 'Termina Field'),
    ('SCT Exit to Laundry Pool', 'Laundry Pool'),
    ('To Honey and Darling', 'Honey and Darling'),
    ('To Treasure Chest Shop', 'Treasure Chest Shop'),
    ('To Town Shooting Gallery', 'Town Shooting Gallery'),
    ('To Milk Bar', 'Milk Bar'),
    ('To Stock Pot Inn', 'Stock Pot Inn'),
    ('To Stock Pot Inn Secret Entrance', 'Stock Pot Inn'),
    ('To Mayors Office', 'Mayors Office'),
    ('Bomber Bouncer', 'Bomber Tunnel'),
    ('Honey and Darling Exit', 'East Clock Town'),
    ('Treasure Chest Shop Exit', 'East Clock Town'),
    ('Town Shooting Gallery Exit', 'East Clock Town'),
    ('Milk Bar Exit', 'East Clock Town'),
    ('Stock Pot Inn Roof Exit', 'East Clock Town'),
    ('Stock Pot Inn Front Door', 'East Clock Town'),
    ('Mayors Office Exit', 'East Clock Town'),
    ('Bomber Tunnel Exit', 'East Clock Town'),
    ('ECT Top Exit to SCT', 'South Clock Town'),
    ('ECT Bottom Exit to SCT', 'South Clock Town'),
    ('ECT Exit to NCT', 'North Clock Town'),
    ('Clock Town East Gate', 'Termina Field'),
    ('To Curiosity Shop', 'Curiosity Shop'),
    ('To Trading Post', 'Trading Post'),
    ('To Bomb Shop', 'Bomb Shop'),
    ('To Post Office', 'Post Office'),
    ('To Lottery Shop', 'Lottery Shop'),
    ('To Swordsmans School', 'Swordsmans School'),
    ('Curiosity Shop Exit', 'West Clock Town'),
    ('Trading Post Exit', 'West Clock Town'),
    ('Bomb Shop Exit', 'West Clock Town'),
    ('Post Office Exit', 'West Clock Town'),
    ('Lottery Shop Exit', 'West Clock Town'),
    ('Swordsmans School Exit', 'West Clock Town'),
    ('Clock Town West Gate', 'Termina Field'),
    ('WCT Top Exit to SCT', 'South Clock Town'),
    ('WCT Bottom Exit to SCT', 'South Clock Town'),
    ('To Deku Playground', 'Deku Playground'),
    ('Deku Playground Exit', 'North Clock Town'),
    ('To GF Clock Town', 'Clock Town Fairy Shrine'),
    ('South Gate To Clock Town', 'South Clock Town'),
    ('North Gate To Clock Town', 'North Clock Town'),
    ('West Gate To Clock Town', 'West Clock Town'),
    ('East Gate To Clock Town', 'East Clock Town'),
    ('TF To Swamp', 'Swamp Path'),
    ('TF To Mountain', 'Path to Mountain Village South'),
    ('TF From Mountain', 'Beyond The Icicles'),
    ('TF To Ikana', 'Path to Ikana'),
    ('Cleaned Fountain Platform To Fountain', 'Woodfall Fairy Shrine'),
    ('Poisoned Fountain Platform To Fountain', 'Woodfall Fairy Shrine'),
    ('Mountain Path North Exit', 'Mountain Village'),
    ('Goron Blizzard', 'Snowhead Spire'),
    ('GF Snowhead', 'Snowhead Fairy Shrine'),
    ('TF From Great Bay Coast', 'Beyond Great Bay Gate'),
    ('TF To Great Bay Coast', 'Great Bay Coast'),
    ('GF Great Bay', 'Great Bay Fairy Shrine'),
    ('GF Stone Tower', 'Stone Tower Fairy Shrine'),
    ]

# dungeon entrance links
default_dungeon_connections = [
    # ('Woodfall Temple Entrance', 'Woodfall Temple Lobby'),
    ('Snowhead Temple Entrance', 'SH Lobby'),
    ]
