import collections
from BaseClasses import Region, Location, Entrance, RegionType


def create_regions(world):

    world.regions = [
        create_ow_region('Beginning',[], ['Cursed Underground']),
        create_interior_region('Deku Flower Tutorial Area', [], ['Clock Tower Twisted Hallway']),
        create_interior_region('Clock Tower',
            ['Remove the Cursed Mask', 'Song from HMS',
            'Dropped Ocarina', 'Song from Skull Kid'],
            ['Clock Tower Exit', 'Clock Tower Twisted Hallway Backwards']),

        # TODO: Suffix Entrance to all of these
        create_ow_region('South Clock Town',
            ['SCT 20 Rupee Chest', 'Festival Tower Rupee Chest',
            'Clock Town Owl Statue', 'Love on the Balcony'],
            ['Clock Tower Entrance', 'Clock Tower Carnival Door', 'South Mailbox',
            'SCT Top Exit to WCT', 'SCT Bottom Exit to WCT', 'SCT Exit to NCT',
            'SCT Exit to NCT', 'SCT Bottom Exit to ECT', 'SCT Top Exit to ECT',
            'Clock Town South Gate', 'SCT Exit to Laundry Pool']),
        create_interior_region('Clock Tower Rooftop', [], ['Moon Portal']),

        create_ow_region('East Clock Town',
            ['Free The Postman', 'ECT 100 Rupee Chest', 'Delivery to Mama Kafei'],
            ['Honey and Darling', 'Treasure Chest Shop', 'Town Shooting Gallery', 'East Mailbox',
            'Milk Bar', 'Stock Pot Inn', 'Stock Pot Inn Secret Entrance', 'Mayors Office',
            'Bomber Bouncer', 'ECT Top Exit to SCT', 'ECT Bottom Exit to SCT',
            'ECT Exit to NCT', 'Clock Town East Gate']),
        create_interior_region('Honey and Darling',
            ['Honey and Darling Bombchu Bowling Prize', 'Honey and Darling Archery Prize',
            'Honey and Darling Basket Bomb Throw Prize', 'Honey and Darling Grand Champion'],
            ['Honey and Darling Exit']),
        create_interior_region('Treasure Chest Shop', ['Treasure Chest Game Piece of Heart Prize'], ['Treasure Chest Shop Exit']),
        create_interior_region('Town Shooting Gallery', ['Town Shooting Beat the Record', 'Town Shooting Perfect Score'], ['Town Shooting Gallery Exit']),
        create_interior_region('Milk Bar', ['Bar Performance'], ['Milk Bar Exit']),
        create_interior_region('Stock Pot Inn',
            ['Do You Have a Reservation?', 'Have you seen this man?',
            'What is the Carnival of Time?', 'Who are the Four Giants?',
            'Love in the Toilet?', 'Stock Pot Reservation Chest', 'Anjus Chest',
            'We Shall Greet The Morning Together'],
            ['Stock Pot Inn Roof Exit', 'Stock Pot Inn Front Door']),
        create_interior_region('Mayors Office', ['Expert Person Solver Takes the Case', 'Love is the True Mayor'], ['Mayors Office Exit']),
        create_interior_region('Bomber Tunnel', ['Bomber Tunnel Chest'], ['Bomber Tunnel Exit', 'Tunnel Balloon From ECT']),
        create_interior_region('Astral Observatory', ['Moon Cry'], ['Tunnel Balloon From Observatory', 'Astral Observatory Exit']),
        create_ow_region('Astral Observatory Deck', ['Moons Sad Crater'], ['Bomber Tunnel', 'Astral Observatory Fence']),

        create_ow_region('West Clock Town',
            ['200 Rupee Prize', '5000 Rupee Prize', 'Spread the Dance of Kamaro',
            'Hidden Owl Statue'],
            ['Curiosity Shop', 'Trading Post', 'Bomb Shop',
            'Post Office', 'Lottery Shop', 'Swordsmans School',
             'Clock Town West Gate', 'WCT Top Exit to SCT', 'WCT Bottom Exit to SCT']),
        create_ow_region('Mailbox', ['Deliver Letter to Kafei', 'Mailbox HP']),
        create_interior_region('Curiosity Shop', ['Buying The Overpriced Mask'], ['Curiosity Shop Exit']),
        create_interior_region('Trading Post', [], ['Trading Post Exit']),
        create_interior_region('Bomb Shop', ['Buy Bomb Bag', 'Buy Bigger Bomb Bag'], ['Bomb Shop Exit']),
        create_interior_region('Post Office', ['The Highest Priority of Mails', 'Counting Is Hard'], ['Post Office Exit']),
        create_interior_region('Lottery Shop', [], ['Lottery Shop Exit']),
        create_interior_region('Swordsmans School', ['Expert Jump Slash Execution'], ['Swordsmans School Exit']),

        create_ow_region('North Clock Town',
            [ 'Bombers Tag Reward', 'Love on a Tree', 'Tingle Town Map',
            'Tingle Woodfall Map', 'Foil Sakon'],
            ['GF Clock Town', 'Deku Playground', 'Clock Town North Gate',
            'NCT Exit to SCT', 'NCT Exit to ECT', 'North Mailbox']),
        # TODO: Don't know how to handle the clock town stray fairy right now
        # I think for now, we could just place checks on the fairy herself
        # But later we'll have Stray Fairy Pickups in the pool
        create_interior_region('Clock Town Fairy Shrine', ['Clock Town GF Reward'], ['Clock Town Fairy Shrine Exit']),
        create_interior_region('Deku Playground', ['Deku Challenge Day 1', 'Deku Challenge Day 2', 'Deku Challenge Day 3', 'Master of the Deku Playground'], ['Clock Town']),

        create_ow_region('Laundry Pool',
            ['Speak To Town Frog', 'Listen To A Grownup Complain'],
            ['Curiosity Backroom Entrance', 'Laundry Pool Exit to SCT']),
        create_interior_region('Curiosity Shop Backroom', ['Deliver This To Anju', 'Kafei Left A Mask', 'Kafei Left A Letter'], ['Clock Town']),

        create_ow_region('Termina Field',
            ['Learn Kamaro\'s Dance', 'TF Chest In The Grass', 'TF Chest On A Stump'],
            ['Termina Field to Swamp', 'South Gate to Clock Town',
            'Mountain Icicles', 'North Gate to Clock Town',
            'Great Bay Gate', 'West Gate to Clock Town',
            'Termina Field to Ikana', 'East Gate to Clock Town',
            'Sleeping Peahat Grotto', 'Bees In A Pond Grotto',
            'Swamp Gossips', 'Mountain Gossips', 'Ocean Gossips',
            'Canyon Gossips', 'Dodongo Grotto', 'Milk Road']),

        create_ow_region('Path to Swamp', ['Bat Guarded Tree Treasure'], ['Termina Field', 'Swamp Shooting Gallery', 'Southern Swamp']),
        create_ow_region('Southern Swamp', ['Swamp Tourist Roof Love'], ['Lost Woods', 'Potion Shop', 'Swamp Big Octo', 'Tourist Centre Big Octo', 'Swamp Tourist Centre']),
        create_interior_region('Swamp Tourist Centre', ['Swamp Tourist Free Product', 'Pictograph Contest Winner'], ['Boat Ride', 'Southern Swamp']),
        create_ow_region('Boat Ride', None, ['Poison Swamp']),
        create_ow_region('Poison Swamp', [], ['Swamp Exit to Deku Palace', 'Swamp Spider House Entrance']),
        # TODO Give an exit
        create_interior_region('Swamp Spider House'),
        create_ow_region('Deku Palace', ['Deku Palace HP'], ['Deku Palace Back Entrance', 'Deku Palace Chamber Entrance']),
        create_interior_region('Deku Palace Royal Chamber'),
        create_interior_region('Deku Palace Shrine'),
        # TODO All of the Woodfall area
        create_interior_region('Woodfall',
            [],
            []),

        create_ow_region('Woodfall Owl Platform', [], ['Woodfall Temple Entrance', 'GF Woodfall', 'Woodfall']),

        create_dungeon_region('Woodfall Temple Lobby',
            [],
            ['Woodfall Temple Lobby Ledge', 'Woodfall Temple Front Exit']),
        create_dungeon_region('Woodfall Temple First Floor',
            [],
            ['Woodfall Temple Small Key Door', 'Woodfall Temple Wooden Flower']),
        create_dungeon_region('Woodfall Temple Push Block Bridge Room',
            [],
            ['Woodfall Temple Upstairs Spiderweb']),
        create_dungeon_region('Woodfall Temple Dark Puff Gauntlet',
            [],
            ['Woodfall Temple ']),
        create_interior_region('Woodfall Fairy Shrine', ['Woodfall GF Reward'], ['Woodfall']),

        create_ow_region('Mountain Icicles', [], ['Termina Field North Exit', 'Termina Field From Mountain']),
        create_ow_region('Mountain Village Path South', [], ['Mountain Snowball Block', 'Mountain Path South Exit']),
        create_ow_region('Path to Mountain Village North', [], ['Mountain Path North Exit', 'Mountain Snowball Block']),
        create_ow_region('Mountain Village',
            ['Frog Choir'],
            ['Mountain Smithy', 'Goron Shrine', 'MV Exit to Snowhead',
            'MV Exit to Goron Village', 'MV Exit to Termina Field']),
        create_ow_region('Path to Goron Village'),
        create_ow_region('Outside Goron Village'),
        create_interior_region('Lens of Truth Cave'),
        create_interior_region('Goron Village'),
        create_interior_region('Goron Shrine'),
        create_ow_region('Path to Snowhead'),
        create_ow_region('Snowhead'),
        create_interior_region('Snowhead Fairy Shrine', ['Snowhead GF Reward'], ['Snowhead Spire']),

        create_ow_region('Great Bay Coast'),
        create_interior_region('Fisherman Hut'),
        create_interior_region('Oceanside Spider House'),
        create_interior_region('Marine Research Lab'),
        create_ow_region('Pirate Fortress'),
        create_interior_region('Pinnacle Rock'),
        create_ow_region('Zora Cape'),
        create_interior_region('Zora Hall'),
        create_interior_region('Zora Shop'),
        create_interior_region('Zora Hall Drummer Room'),
        create_interior_region('Zora Hall Lulu Room'),
        create_interior_region('Zora Hall Bassist Room'),
        create_interior_region('Zora Hall Pianist Room'),
        create_interior_region('Waterfall Rapids', ['Beaver Bottle', 'Beaver HP']),
        create_interior_region('Great Bay Fairy Shrine', ['Great Bay GF Reward'], ['Great Bay Fairy Ledge']),

        create_ow_region('Path to Ikana'),
        create_ow_region('Ikana Graveyard', ['Captains Chest'],
            ['SoS Grave Grotto', 'HP Grave Grotto', 'Dampe Grave Grotto', 'Dampe Door']),
        create_interior_region('Dampe Grave'),
        create_grotto_region('Storms Grave'),
        create_grotto_region('Heart Piece Grave'),
        create_interior_region('Sakon Hideout'),
        create_interior_region('Secret Shrine'),
        create_interior_region('Poe Sister House'),
        create_interior_region('Spoop Cave'),
        create_interior_region('Music Box House'),
        create_interior_region('Bottom of the Well'),
        create_ow_region('Ikana Castle'),
        create_ow_region('Stone Tower'),
        create_interior_region('Stone Tower Fairy Shrine', ['Stone Tower GF Reward'], ['Ikana Canyon'])
    ]
    world.intialize_regions()

def create_ow_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Overworld, locations, exits)

def create_interior_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Interior, locations, exits)

def create_dungeon_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Dungeon, locations, exits)

def create_grotto_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Grotto, locations, exits)

def _create_region(name, type, locations=None, exits=None, scene_listing=0x0, scene_name='Grottos'):
    ret = Region(name, type)
    if locations is None:
        locations = []
    if exits is None:
        exits = []

    for exit in exits:
        ret.exits.append(Entrance(exit, ret))
    for location in locations:
        address, address2, default, type = location_table[location]
        ret.locations.append(Location(location, address, address2, default, type, ret))
    return ret

location_table = {'Hidden Owl Statue': (0x221224E, None, 0x0F, 'Statue'),
                    'Great Bay Coast Owl Statue': (0x26DE42E, None, 0x00, 'Statue'),
                    'Great Bay Coast Warp Opened': (None, None, None, 'Event'),
                    'Zora Cape Owl Statue': (0x27153BA, None, 0x01, 'Statue'),
                    'Zora Cape Coast Warp Opened': (None, None, None, 'Event'),
                    'Snowhead Owl Statue': (0x2C112EA, None, 0x02, 'Statue'),
                    'Snowhead Coast Warp Opened': (None, None, None, 'Event'),
                    'Moutain Village Owl Statue': (0x2AA62BE, None, 0x03, 'Statue'),
                    'Mountain Village Warp Opened': (None, None, None, 'Event'),
                    'Moutain Village Spring Owl Statue': (0x2BDD332, None, 0x03, 'Statue'),
                    'Mountain Village Spring Warp Opened': (None, None, None, 'Event'),
                    'Clock Town Owl Statue': (0x2E5C292, None, 0x04, 'Statue'),
                    'Clock Town Warp Opened': (None, None, None, 'Event'),
                    'Milk Road Owl Statue': (0x23640D6, None, 0x05, 'Statue'),
                    'Milk Road Warp Opened': (None, None, None, 'Event'),
                    'Woodfall Owl Statue': (0x28841E2, None, 0x06, 'Statue'),
                    'Woodfall Warp Opened': (None, None, None, 'Event'),
                    'Swamp Owl Statue': (0x28372EE, None, 0x07, 'Statue'),
                    'Swamp Warp Opened': (None, None, None, 'Event'),
                    'Ikana Canyon Owl Statue': (0x2055422, None, 0x08, 'Statue'),
                    'Ikana Canyon Warp Opened': (None, None, None, 'Event'),
                    'Stone Tower Owl Statue': (0x2BA92AE, None, 0x09, 'Statue'),
                    'Stone Tower Warp Opened': (None, None, None, 'Event'),

                    'Song from Skull Kid': (None, None, None, 'Song'),
                    'Song from HMS': (None, None, None, 'Song'),
                    'Song from Romani': (None, None, None, 'Song'),
                    'Song from Monkey': (None, None, None, 'Song'),
                    'Song on Owl Tablet': (None, None, None, 'Song'),
                    'Song from Baby Goron': (None, None, None, 'Song'),
                    'Song from Baby Zoras': (None, None, None, 'Song'),
                    'Song in Composer Grave': (None, None, None, 'Song'),
                    'Song from Igos': (None, None, None, 'Song'),
                    'Song from the Giants': (None, None, None, 'Song'),

                    'SCT 20 Rupee Chest': (None, None, 0x5080, 'Chest'),
                    'Festival Tower Rupee Chest': (None, None, None, 'Chest'),
                    'ECT 100 Rupee Chest': (None, None, None, 'Chest'),

                    'Termina Field Stump Chest': (0x25C5D44, None, 0x5080, 'Chest', 0x26, 'Termina Field'),
                    'Termina Field Meadow Chest': (0x25C5D54, None, 5081, 'Chest', 0x26, 'Termina Field'),
                    'Termina Field Underwater Chest': (0x25C5D64, None, 0x5082, 'Chest', 0x26, 'Termina Field'),

                    'Woodfall Owl Platform Chest': (),
                    'Woodfall Red Rupee Chest': (),
                    'Woodfall HP Chest': (),

                    'Lens Grotto Lens Chest': (),
                    'Lens Grotto Invisible Chest': (),
                    'Lens Grotto Chest Under Rock': (),



                    'WFT Map Chest': (None, None, None, 'Chest'),
                    'WFT Small Key Chest': (None, None, None, 'Chest'),
                    'WFT Compass Chest': (None, None, None, 'Chest'),
                    'WFT Bow Chest': (None, None, None, 'Chest'),
                    'WFT Boss Key Chest': (None, None, None, 'Chest'),
                    'WFT Lobby Fairy Chest': (None, None, None, 'Chest'),
                    'WFT Central Room Switch Chest': (None, None, None, 'Chest'),
                    'WFT Dark Puff Battle Arena Chest': (None, None, None, 'Chest'),

                    'Town Deku Salesman': (None, None, None, 'NPC'),
                    'Swamp Deku Salesman': (None, None, None, 'NPC'),
                    'Mountain Deku Salesman': (None, None, None, 'NPC'),
                    'Ocean Deku Salesman': (None, None, None, 'NPC'),
                    'Canyon Deku Salesman': (None, None, None, 'NPC'),
                    'Song from Goron Elder': (None, None, None, 'NPC'),

                    'Love on the Balcony': (None, None, None, 'Collectable'),
                    'Claim Odolwa\'s Remains': (None, None, None, 'Remains'),
                    'Claim Odolwa\'s Heart': (None, None, None, 'Collectable'),
                    'Claim Goht\'s Remains': (None, None, None, 'Remains'),
                    'Claim Goht\'s Heart': (None, None, None, 'Collectable'),
                    'Claim Gyorg\'s Remains': (None, None, None, 'Remains'),
                    'Claim Gyorg\'s Heart': (None, None, None, 'Collectable'),
                    'Claim Odolwa\'s Remains': (None, None, None, 'Remains'),
                    'Claim Odolwa\'s Heart': (None, None, None, 'Collectable'),
                    'Defeat Odolwa': (None, None, None, 'Event'),
                    'Defeat Goht': (None, None, None, 'Event'),
                    'Defeat Gyorg': (None, None, None, 'Event'),
                    'Defeat Twinmold': (None, None, None, 'Event'),
                    'Song from Giants': (None, None, None, 'Song'),

                    'WFT Lobby Floating Fairy': (None, None, None, 'Fairy'),
                    'WFT Central Flower Corner Pot': (None, None, None, 'Pot'),
                    'WFT Deku Flower Elevator Beehive': (None, None, None, 'Bees'),
                    'WFT Bridge Room Beehive': (None, None, None, 'Bees'),
                    'WFT Under Poison Bridge': (None, None, None, 'Bubble Fairy'),
                    'WFT Central Flower Bubble Fairy': (None, None, None, 'Bubble Fairy'),
                    'WFT Lower East Bubble Fairy': (None, None, None, 'Bubble Fairy'),
                    'WFT Upper East Bubble Fairy': (None, None, None, 'Bubble Fairy'),
                    'WFT West Bubble Fairy': (None, None, None, 'Bubble Fairy'),
                    'WFT Hot Bubble Fairy': (None, None, None, 'Bubble Fairy'),
                    'WFT Central Flower Deku Baba': (None, None, None, 'Enemy'),
                    'WFT Bridge Skulltula': (None, None, None, 'Enemy'),
                    'Open the Moon': (None, None, None, 'Event')}
