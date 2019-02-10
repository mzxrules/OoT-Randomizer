# TODO: This file was completely removed from the OoT fork
# I'm keeping it in for legacy purposes.
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

    ('Mountain Snowball Block', 'Path To Mountain Village North'),
    ('Mountain Snowball Block Backwards', 'Path To Mountain Village South'),
    ('Frozen MV Lower To Top', 'Mountain Village Top (Frozen)'),
    ('Frozen MV Top To Lower', 'Mountain Village Lower (Frozen)'),
    ('Frozen Lake To Grotto Platform', 'Mountain Lake Grotto Platform (Frozen)'),
    ('Frozen Lake Grotto Platform To Goron Race Platform', 'Mountain Lake Goron Race Platform (Frozen)'),
    ('Frozen Lake Grotto Platform To Main', 'Mountain Lake Main (Frozen)'),
    ('Frozen Lake Goron Race Platform To Grotto Platform', 'Mountain Lake Grotto Platform (Frozen)'),
    ('Frozen Goron Village Outer To Lens Cave Region', 'Goron Village Outer Lens Cave Region (Frozen)'),
    ('Frozen Lens Cave Region To Goron Village', 'Goron Village Outer Main (Frozen)'),

    ('Snowhead Path MV Side To Mid', 'Snowhead Path Mid Region'),
    ('Snowhead Path Mid To MV Side', 'Snowhead Path MV Side'),
    ('Snowhead Path Mid To SH Side', 'Snowhead Path Snowhead Side'),
    ('Snowhead Path SH Side To Mid', 'Snowhead Path Mid Region'),
    ('Outside SH Owl To Central', 'Outside Snowhead Central Region'),
    ('Outside SH Central To Owl', 'Outside Snowhead Owl Region'),
    ('Outside SH Central To Entrance', 'Outside Snowhead Entrance Region'),
    ('Outside SH To Central', 'Outside Snowhead Central Region'),

    ('TF Great Bay Gate', 'Beyond Great Bay Gate'),
    ('TF Great Bay Gate Backwards', 'Termina Field'),
    # ('', ''),
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

    ('TF To Observatory Over Fence', 'Astral Observatory Deck'),

    ('TF To Swamp', 'Swamp Path'),
    ('Fountain Platform To Fountain', 'Woodfall Fairy Shrine'),

    ('TF To Mountain', 'Path To Mountain Village South'),
    ('TF From Mountain', 'Beyond The Icicles'),
    ('Mountain Path North Exit', 'Mountain Village Lower (Frozen)'),
    ('Frozen MV To MV Path North', 'Path To Mountain Village North'),
    ('Frozen MV To Smithy', 'Smithy'),
    ('Frozen MV Lower To Lake', 'Goron Village Outer Main (Frozen)'),
    ('Frozen MV Lower To Snowhead Path', 'Snowhead Path MV Side'),
    ('Frozen MV Top To Goron Grave', 'Goron Grave'),
    ('Frozen Lake To MV', 'Mountain Village Lower (Frozen)'),
    ('Frozen Lake To Goron Village Outside', 'Goron Village Outer Main (Frozen)'),
    ('Frozen Lake To Hot Spring', 'Mountain Lake Hot Spring Grotto'),
    ('Frozen Lake Grotto Platform To Grotto', 'Mountain Lake Grotto'),
    ('Frozen Lake Goron Race Platform To Goron Race', 'Goron Racetrack'),
    ('Frozen Goron Village Outer To Lake', 'Mountain Lake Main (Frozen)'),
    ('Frozen Goron Village Outer To Inner', 'Goron Village Inner'),
    ('Frozen Lens Cave Region To Lens Cave', 'Lens of Truth Cave'),

    ('Smithy Frozen Exit', 'Mountain Village Lower (Frozen)'),
    # ('Smithy Thawed Exit', ''),
    ('Mountain Lake Grotto Frozen Exit', 'Mountain Lake Grotto Platform (Frozen)'),
    # ('Mountain Lake Grotto Thawed Exit', ''),
    ('Frozen Goron Race Exit', 'Mountain Lake Goron Race Platform (Frozen)'),
    # ('Thawed Goron Race Exit', ''),
    ('Lens of Truth Cave Frozen Exit', 'Goron Village Outer Main (Frozen)'),
    # ('Lens of Truth Cave Thawed Exit', ''),
    ('Goron Village Inner Frozen Exit', 'Goron Village Outer Main (Frozen)'),
    # ('Goron Village Inner Thawed Exit', ''),
    ('Goron Village Inner To Shop', 'Goron Village Shop'),
    ('Snowhead Path To MV', 'Mountain Village Lower (Frozen)'),
    ('Snowhead Path SH Side To SH', 'Snowhead Path MV Side'),
    ('Outside SH Owl To SH Path', 'Snowhead Path Snowhead Side'),
    ('Outside SH Central To Fairy Shrine', 'Snowhead Fairy Shrine'),
    ('Snowhead Fairy Shrine Exit', 'Outside Snowhead Entrance Region'),

    # ('', ''),
    ('TF From Great Bay Coast', 'Beyond Great Bay Gate'),
    ('TF To Great Bay Coast', 'Great Bay Coast'),
    ('GF Great Bay', 'Great Bay Fairy Shrine'),

    ('TF To Ikana', 'Path To Ikana'),
    ('GF Stone Tower', 'Stone Tower Fairy Shrine'),
    ]

# dungeon entrance links
default_dungeon_connections = [
    # ('Woodfall Temple Entrance', 'Woodfall Temple Lobby'),
    ('Outside SH To SH', 'SH Lobby'),
    ]
