import collections
from BaseClasses import Region, Location, Entrance, RegionType

def shop_address(shop_id, shelf_id):
    return 0xC71ED0 + (0x40 * shop_id) + (0x08 * shelf_id)

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

    if world.dungeon_mq['DC']:
        world.regions.extend([
            create_dungeon_region(
                'Dodongos Cavern Beginning', 
                None, 
                ['Dodongos Cavern Exit', 'Dodongos Cavern Lobby']),
            create_dungeon_region(
                'Dodongos Cavern Lobby', 
                ['Dodongos Cavern MQ Map Chest', 'Dodongos Cavern MQ Compass Chest', 'Dodongos Cavern MQ Larva Room Chest', 
                 'Dodongos Cavern MQ Torch Puzzle Room Chest', 'Dodongos Cavern MQ Bomb Bag Chest', 
                 'GS Dodongo\'s Cavern MQ Song of Time Block Room', 'GS Dodongo\'s Cavern MQ Larva Room', 
                 'GS Dodongo\'s Cavern MQ Lizalfos Room', 'GS Dodongo\'s Cavern MQ Scrub Room',
                 'DC MQ Deku Scrub Deku Sticks', 'DC MQ Deku Scrub Deku Seeds',
                 'DC MQ Deku Scrub Deku Shield', 'DC MQ Deku Scrub Red Potion'], 
                ['Dodongos Cavern Bomb Drop']),
            create_dungeon_region(
                'Dodongos Cavern Boss Area', 
                ['Dodongos Cavern MQ Under Grave Chest', 'Chest Above King Dodongo', 'King Dodongo Heart', 
                 'King Dodongo', 'GS Dodongo\'s Cavern MQ Back Area']),
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Dodongos Cavern Beginning', 
                None, 
                ['Dodongos Cavern Exit', 'Dodongos Cavern Lobby']),
            create_dungeon_region(
                'Dodongos Cavern Lobby', 
                ['Dodongos Cavern Map Chest', 'Dodongos Cavern Compass Chest', 'GS Dodongo\'s Cavern East Side Room', 
                 'GS Dodongo\'s Cavern Scarecrow', 'DC Deku Scrub Deku Sticks', 'DC Deku Scrub Deku Shield'], 
                ['Dodongos Cavern Retreat', 'Dodongos Cavern Left Door']),
            create_dungeon_region(
                'Dodongos Cavern Climb', 
                ['Dodongos Cavern Bomb Flower Platform', 'GS Dodongo\'s Cavern Vines Above Stairs',
                 'DC Deku Scrub Deku Seeds', 'DC Deku Scrub Deku Nuts'], 
                ['Dodongos Cavern Bridge Fall', 'Dodongos Cavern Slingshot Target']),
            create_dungeon_region(
                'Dodongos Cavern Far Bridge', 
                ['Dodongos Cavern Bomb Bag Chest', 'Dodongos Cavern End of Bridge Chest', 
                 'GS Dodongo\'s Cavern Alcove Above Stairs'], 
                ['Dodongos Cavern Bomb Drop', 'Dodongos Cavern Bridge Fall 2']),
            create_dungeon_region(
                'Dodongos Cavern Boss Area', 
                ['Chest Above King Dodongo', 'King Dodongo Heart', 'King Dodongo', 'GS Dodongo\'s Cavern Back Room'], 
                ['Dodongos Cavern Exit Skull'])
        ])

    if world.dungeon_mq['JB']:
        world.regions.extend([
            create_dungeon_region(
                'Jabu Jabus Belly Beginning', 
                ['Jabu Jabus Belly MQ Map Chest', 'Jabu Jabus Belly MQ Entry Side Chest'], 
                ['Jabu Jabus Belly Exit', 'Jabu Jabus Belly Cow Switch']),
            create_dungeon_region(
                'Jabu Jabus Belly Main', 
                ['Jabu Jabus Belly MQ Second Room Lower Chest', 'Jabu Jabus Belly MQ Compass Chest', 
                 'Jabu Jabus Belly MQ Basement South Chest', 'Jabu Jabus Belly MQ Basement North Chest', 
                 'Jabu Jabus Belly MQ Boomerang Room Small Chest', 'MQ Boomerang Chest', 'GS Jabu Jabu MQ Boomerang Room'], 
                ['Jabu Jabus Belly Retreat', 'Jabu Jabus Belly Tentacle Access']),
            create_dungeon_region(
                'Jabu Jabus Belly Depths', 
                ['Jabu Jabus Belly MQ Falling Like Like Room Chest', 'GS Jabu Jabu MQ Tailpasaran Room', 
                 'GS Jabu Jabu MQ Invisible Enemies Room'], 
                ['Jabu Jabus Belly Elevator', 'Jabu Jabus Belly Octopus']),
            create_dungeon_region(
                'Jabu Jabus Belly Boss Area', 
                ['Jabu Jabus Belly MQ Second Room Upper Chest', 'Jabu Jabus Belly MQ Near Boss Chest', 
                 'Barinade Heart', 'Barinade', 'GS Jabu Jabu MQ Near Boss'], 
                ['Jabu Jabus Belly Final Backtrack'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Jabu Jabus Belly Beginning', 
                None, 
                ['Jabu Jabus Belly Exit', 'Jabu Jabus Belly Ceiling Switch']),
            create_dungeon_region(
                'Jabu Jabus Belly Main', 
                ['Boomerang Chest', 'GS Jabu Jabu Water Switch Room', 'Jabu Deku Scrub Deku Nuts'], 
                ['Jabu Jabus Belly Retreat', 'Jabu Jabus Belly Tentacles']),
            create_dungeon_region(
                'Jabu Jabus Belly Depths', 
                ['Jabu Jabus Belly Map Chest', 'Jabu Jabus Belly Compass Chest', 'GS Jabu Jabu Lobby Basement Lower', 
                 'GS Jabu Jabu Lobby Basement Upper'], 
                ['Jabu Jabus Belly Elevator', 'Jabu Jabus Belly Octopus']),
            create_dungeon_region(
                'Jabu Jabus Belly Boss Area', 
                ['Barinade Heart', 'Barinade', 'GS Jabu Jabu Near Boss'], 
                ['Jabu Jabus Belly Final Backtrack'])
        ])

    if world.dungeon_mq['FoT']:
        world.regions.extend([
            create_dungeon_region(
                'Forest Temple Lobby', 
                ['Forest Temple MQ First Chest', 'GS Forest Temple MQ First Hallway'], 
                ['Forest Temple Exit', 'Forest Temple Lobby Locked Door']),
            create_dungeon_region(
                'Forest Temple Central Area', 
                ['Forest Temple MQ Chest Behind Lobby', 'GS Forest Temple MQ Block Push Room'], 
                ['Forest Temple West Eye Switch', 'Forest Temple East Eye Switch', 
                 'Forest Temple Block Puzzle Solve', 'Forest Temple Crystal Switch Jump']),
            create_dungeon_region(
                'Forest Temple After Block Puzzle', 
                ['Forest Temple MQ Boss Key Chest'], 
                ['Forest Temple Twisted Hall']),
            create_dungeon_region(
                'Forest Temple Outdoor Ledge', 
                ['Forest Temple MQ Redead Chest'], 
                ['Forest Temple Drop to NW Outdoors']),
            create_dungeon_region(
                'Forest Temple NW Outdoors', 
                ['GS Forest Temple MQ Outdoor West'], 
                ['Forest Temple Well Connection', 'Forest Temple Webs']),
            create_dungeon_region(
                'Forest Temple NE Outdoors', 
                ['Forest Temple MQ Well Chest', 'GS Forest Temple MQ Outdoor East', 'GS Forest Temple MQ Well'], 
                ['Forest Temple Climb to Top Ledges', 'Forest Temple Longshot to NE Outdoors Ledge']),
            create_dungeon_region(
                'Forest Temple Outdoors Top Ledges', 
                ['Forest Temple MQ NE Outdoors Upper Chest'], 
                ['Forest Temple Top Drop to NE Outdoors']),
            create_dungeon_region(
                'Forest Temple NE Outdoors Ledge', 
                ['Forest Temple MQ NE Outdoors Lower Chest'], 
                ['Forest Temple Drop to NE Outdoors', 'Forest Temple Song of Time Block Climb']),
            create_dungeon_region(
                'Forest Temple Bow Region', 
                ['Forest Temple MQ Bow Chest', 'Forest Temple MQ Map Chest', 'Forest Temple MQ Compass Chest'], 
                ['Forest Temple Drop to Falling Room']),
            create_dungeon_region(
                'Forest Temple Falling Room', 
                ['Forest Temple MQ Falling Room Chest'], 
                ['Forest Temple Falling Room Exit', 'Forest Temple Elevator']),
            create_dungeon_region(
                'Forest Temple Boss Region', 
                ['Forest Temple MQ Near Boss Chest', 'Phantom Ganon Heart', 'Phantom Ganon'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Forest Temple Lobby', 
                ['Forest Temple First Chest', 'Forest Temple Chest Behind Lobby', 'GS Forest Temple First Room', 
                 'GS Forest Temple Lobby'], 
                ['Forest Temple Exit', 'Forest Temple Song of Time Block', 'Forest Temple Lobby Eyeball Switch', 
                 'Forest Temple Lobby Locked Door']),
            create_dungeon_region(
                'Forest Temple NW Outdoors', 
                ['Forest Temple Well Chest', 'Forest Temple Map Chest', 'GS Forest Temple Outdoor West'], 
                ['Forest Temple Through Map Room']),
            create_dungeon_region(
                'Forest Temple NE Outdoors', 
                ['Forest Temple Outside Hookshot Chest', 'GS Forest Temple Outdoor East'], 
                ['Forest Temple Well Connection', 'Forest Temple Outside to Lobby', 'Forest Temple Scarecrows Song']),
            create_dungeon_region(
                'Forest Temple Falling Room', 
                ['Forest Temple Falling Room Chest'], 
                ['Forest Temple Falling Room Exit', 'Forest Temple Elevator']),
            create_dungeon_region(
                'Forest Temple Block Push Room', 
                ['Forest Temple Block Push Chest'], 
                ['Forest Temple Outside Backdoor', 'Forest Temple Twisted Hall', 'Forest Temple Straightened Hall']),
            create_dungeon_region(
                'Forest Temple Straightened Hall', 
                ['Forest Temple Boss Key Chest'], 
                ['Forest Temple Boss Key Chest Drop']),
            create_dungeon_region(
                'Forest Temple Outside Upper Ledge', 
                ['Forest Temple Floormaster Chest'], 
                ['Forest Temple Outside Ledge Drop']),
            create_dungeon_region(
                'Forest Temple Bow Region', 
                ['Forest Temple Bow Chest', 'Forest Temple Red Poe Chest', 'Forest Temple Blue Poe Chest'], 
                ['Forest Temple Drop to Falling Room']),
            create_dungeon_region(
                'Forest Temple Boss Region', 
                ['Forest Temple Near Boss Chest', 'Phantom Ganon Heart', 'Phantom Ganon', 'GS Forest Temple Basement'])
        ])

    if world.dungeon_mq['FiT']:
        world.regions.extend([
            create_dungeon_region(
                'Fire Temple Lower', 
                ['Fire Temple MQ Entrance Hallway Small Chest', 'Fire Temple MQ Chest Near Boss'], 
                ['Fire Temple Exit', 'Fire Temple Boss Door', 'Fire Temple Lower Locked Door', 'Fire Temple Hammer Statue']),
            create_dungeon_region(
                'Fire Lower Locked Door', 
                ['Fire Temple MQ Megaton Hammer Chest', 'Fire Temple MQ Map Chest']),
            create_dungeon_region(
                'Fire Big Lava Room', 
                ['Fire Temple MQ Boss Key Chest', 'Fire Temple MQ Big Lava Room Bombable Chest', 'GS Fire Temple MQ Big Lava Room'], 
                ['Fire Temple Early Climb']),
            create_dungeon_region(
                'Fire Lower Maze', 
                ['Fire Temple MQ Maze Lower Chest'], 
                ['Fire Temple Maze Climb']),
            create_dungeon_region(
                'Fire Upper Maze', 
                ['Fire Temple MQ Maze Upper Chest', 'Fire Temple MQ Maze Side Room', 'Fire Temple MQ Compass Chest', 
                 'GS Fire Temple MQ East Tower Top'], 
                ['Fire Temple Maze Escape']),
            create_dungeon_region(
                'Fire Temple Upper', 
                ['Fire Temple MQ Freestanding Key', 'Fire Temple MQ West Tower Top Chest', 'GS Fire Temple MQ Fire Wall Maze Side Room',
                 'GS Fire Temple MQ Fire Wall Maze Center', 'GS Fire Temple MQ Above Fire Wall Maze']),
            create_dungeon_region(
                'Fire Boss Room', 
                ['Volvagia Heart', 'Volvagia'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Fire Temple Lower', 
                ['Fire Temple Chest Near Boss', 'Fire Temple Fire Dancer Chest', 'Fire Temple Boss Key Chest', 
                 'Fire Temple Big Lava Room Bombable Chest', 'Fire Temple Big Lava Room Open Chest', 'Volvagia Heart', 
                 'Volvagia', 'GS Fire Temple Song of Time Room', 'GS Fire Temple Basement'], 
                ['Fire Temple Exit', 'Fire Temple Early Climb']),
            create_dungeon_region(
                'Fire Temple Middle', 
                ['Fire Temple Boulder Maze Lower Chest', 'Fire Temple Boulder Maze Upper Chest', 
                 'Fire Temple Boulder Maze Side Room', 'Fire Temple Boulder Maze Bombable Pit', 'Fire Temple Scarecrow Chest', 
                 'Fire Temple Map Chest', 'Fire Temple Compass Chest', 'GS Fire Temple Unmarked Bomb Wall', 
                 'GS Fire Temple East Tower Climb', 'GS Fire Temple East Tower Top'], 
                ['Fire Temple Fire Maze Escape']),
            create_dungeon_region(
                'Fire Temple Upper', 
                ['Fire Temple Highest Goron Chest', 'Fire Temple Megaton Hammer Chest'])
        ])

    if world.dungeon_mq['WT']:
        world.regions.extend([
            create_dungeon_region(
                'Water Temple Lobby', 
                ['Water Temple MQ Map Chest', 'Water Temple MQ Central Pillar Chest', 'Morpha Heart', 'Morpha'], 
                ['Water Temple Exit', 'Water Temple Water Level Switch', 'Water Temple Locked Door']),
            create_dungeon_region(
                'Water Temple Lowered Water Levels', 
                ['Water Temple MQ Compass Chest', 'Water Temple MQ Longshot Chest', 
                 'GS Water Temple MQ Lizalfos Hallway', 'GS Water Temple MQ Before Upper Water Switch']),
            create_dungeon_region(
                'Water Temple Dark Link Region', 
                ['Water Temple MQ Boss Key Chest', 'GS Water Temple MQ Serpent River'], 
                ['Water Temple Basement Gates Switch']),
            create_dungeon_region(
                'Water Temple Basement Gated Areas', 
                ['Water Temple MQ Freestanding Key', 'GS Water Temple MQ South Basement', 'GS Water Temple MQ North Basement'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Water Temple Lobby', 
                ['Water Temple Map Chest', 'Water Temple Compass Chest', 'Water Temple Torches Chest', 'Water Temple Dragon Chest', 
                 'Water Temple Central Bow Target Chest', 'Water Temple Boss Key Chest', 'Morpha Heart', 'Morpha', 
                 'GS Water Temple South Basement', 'GS Water Temple Near Boss Key Chest'], 
                ['Water Temple Exit', 'Water Temple Central Pillar', 'Water Temple Upper Locked Door']),
            create_dungeon_region(
                'Water Temple Middle Water Level', 
                ['Water Temple Central Pillar Chest', 'Water Temple Cracked Wall Chest', 'GS Water Temple Central Room']),
            create_dungeon_region(
                'Water Temple Dark Link Region', 
                ['Water Temple Dark Link Chest', 'Water Temple River Chest', 'GS Water Temple Serpent River', 
                 'GS Water Temple Falling Platform Room'])
        ])

    if world.dungeon_mq['SpT']:
        world.regions.extend([
            create_dungeon_region(
                'Spirit Temple Lobby', 
                ['Spirit Temple MQ Entrance Front Left Chest', 'Spirit Temple MQ Entrance Back Left Chest', 
                 'Spirit Temple MQ Entrance Back Right Chest'], 
                ['Spirit Temple Exit', 'Spirit Temple Crawl Passage', 'Spirit Temple Ceiling Passage']),
            create_dungeon_region(
                'Child Spirit Temple', 
                ['Spirit Temple MQ Child Left Chest', 'Spirit Temple MQ Map Chest', 'Spirit Temple MQ Silver Block Hallway Chest'], 
                ['Child Spirit Temple to Shared']),
            create_dungeon_region(
                'Adult Spirit Temple', 
                ['Spirit Temple MQ Child Center Chest', 'Spirit Temple MQ Child Climb South Chest', 'Spirit Temple MQ Lower NE Main Room Chest', 
                 'Spirit Temple MQ Upper NE Main Room Chest', 'Spirit Temple MQ Beamos Room Chest', 'Spirit Temple MQ Ice Trap Chest', 
                 'Spirit Temple MQ Boss Key Chest', 'GS Spirit Temple MQ Sun Block Room', 'GS Spirit Temple MQ Iron Knuckle West', 
                 'GS Spirit Temple MQ Iron Knuckle North'], 
                ['Adult Spirit Temple Descent', 'Adult Spirit Temple to Shared', 'Spirit Temple Climbable Wall', 'Mirror Shield Exit']),
            create_dungeon_region(
                'Spirit Temple Shared', 
                ['Spirit Temple MQ Child Climb North Chest', 'Spirit Temple MQ Compass Chest', 'Spirit Temple MQ Sun Block Room Chest'], 
                ['Silver Gauntlets Exit']),
            create_dungeon_region(
                'Lower Adult Spirit Temple', 
                ['Spirit Temple MQ Lower Adult Left Chest', 'Spirit Temple MQ Lower Adult Right Chest', 
                 'Spirit Temple MQ Entrance Front Right Chest', 'GS Spirit Temple MQ Lower Adult Left', 
                 'GS Spirit Temple MQ Lower Adult Right']),
            create_dungeon_region(
                'Spirit Temple Boss Area', 
                ['Spirit Temple MQ Mirror Puzzle Invisible Chest', 'Twinrova Heart', 'Twinrova']),
            create_dungeon_region(
                'Mirror Shield Hand',
                ['Mirror Shield Chest']),
            create_dungeon_region(
                'Silver Gauntlets Hand',
                ['Silver Gauntlets Chest'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Spirit Temple Lobby', 
                None, 
                ['Spirit Temple Exit', 'Spirit Temple Crawl Passage', 'Spirit Temple Silver Block']),
            create_dungeon_region(
                'Child Spirit Temple', 
                ['Spirit Temple Child Left Chest', 'Spirit Temple Child Right Chest', 'GS Spirit Temple Metal Fence',
                'Spirit Temple Nut Crate'], 
                ['Child Spirit Temple Climb']),
            create_dungeon_region(
                'Child Spirit Temple Climb', 
                ['Spirit Temple Child Climb East Chest', 'Spirit Temple Child Climb North Chest',
                 'GS Spirit Temple Bomb for Light Room'],
                ['Child Spirit Temple Passthrough']),
            create_dungeon_region(
                'Early Adult Spirit Temple', 
                ['Spirit Temple Compass Chest', 'Spirit Temple Early Adult Right Chest', 
                 'Spirit Temple First Mirror Right Chest', 'Spirit Temple First Mirror Left Chest', 
                 'GS Spirit Temple Boulder Room'], 
                ['Adult Spirit Temple Passthrough']),
            create_dungeon_region(
                'Spirit Temple Central Chamber', 
                ['Spirit Temple Map Chest', 'Spirit Temple Sun Block Room Chest', 'Spirit Temple Statue Hand Chest',
                 'Spirit Temple NE Main Room Chest', 'GS Spirit Temple Hall to West Iron Knuckle', 'GS Spirit Temple Lobby'], 
                ['Spirit Temple to Hands', 'Spirit Temple Central Locked Door', 'Spirit Temple Middle Child Door']),
            create_dungeon_region(
                'Spirit Temple Outdoor Hands', 
                ['Silver Gauntlets Chest', 'Mirror Shield Chest']),
            create_dungeon_region(
                'Spirit Temple Beyond Central Locked Door', 
                ['Spirit Temple Near Four Armos Chest', 'Spirit Temple Hallway Left Invisible Chest', 
                 'Spirit Temple Hallway Right Invisible Chest'], 
                ['Spirit Temple Final Locked Door']),
            create_dungeon_region(
                'Spirit Temple Beyond Final Locked Door', 
                ['Spirit Temple Boss Key Chest', 'Spirit Temple Topmost Chest', 'Twinrova Heart', 'Twinrova'])
        ])

    if world.dungeon_mq['ShT']:
        world.regions.extend([
            create_dungeon_region(
                'Shadow Temple Beginning', 
                None,
                ['Shadow Temple Exit', 'Shadow Temple First Pit', 'Shadow Temple Beginning Locked Door']),
            create_dungeon_region(
                'Shadow Temple Dead Hand Area', 
                ['Shadow Temple MQ Compass Chest', 'Shadow Temple MQ Hover Boots Chest']),
            create_dungeon_region(
                'Shadow Temple First Beamos', 
                ['Shadow Temple MQ Map Chest', 'Shadow Temple MQ Early Gibdos Chest', 'Shadow Temple MQ Near Ship Invisible Chest'], 
                ['Shadow Temple Bomb Wall']),
            create_dungeon_region(
                'Shadow Temple Huge Pit', 
                ['Shadow Temple MQ Invisible Blades Visible Chest', 'Shadow Temple MQ Invisible Blades Invisible Chest', 
                 'Shadow Temple MQ Beamos Silver Rupees Chest', 'Shadow Temple MQ Falling Spikes Lower Chest', 
                 'Shadow Temple MQ Falling Spikes Upper Chest', 'Shadow Temple MQ Falling Spikes Switch Chest',
                 'Shadow Temple MQ Invisible Spikes Chest', 'Shadow Temple MQ Stalfos Room Chest', 'GS Shadow Temple MQ Crusher Room'], 
                ['Shadow Temple Hookshot Target']),
            create_dungeon_region(
                'Shadow Temple Wind Tunnel', 
                ['Shadow Temple MQ Wind Hint Chest', 'Shadow Temple MQ After Wind Enemy Chest', 'Shadow Temple MQ After Wind Hidden Chest', 
                 'GS Shadow Temple MQ Wind Hint Room', 'GS Shadow Temple MQ After Wind'], 
                ['Shadow Temple Boat']),
            create_dungeon_region(
                'Shadow Temple Beyond Boat', 
                ['Bongo Bongo Heart', 'Bongo Bongo', 'GS Shadow Temple MQ After Ship', 'GS Shadow Temple MQ Near Boss'], 
                ['Shadow Temple Longshot Target']),
            create_dungeon_region(
                'Shadow Temple Invisible Maze', 
                ['Shadow Temple MQ Spike Walls Left Chest', 'Shadow Temple MQ Boss Key Chest', 
                 'Shadow Temple MQ Bomb Flower Chest', 'Shadow Temple MQ Freestanding Key'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Shadow Temple Beginning', 
                ['Shadow Temple Map Chest', 'Shadow Temple Hover Boots Chest'], 
                ['Shadow Temple Exit', 'Shadow Temple First Pit']),
            create_dungeon_region(
                'Shadow Temple First Beamos', 
                ['Shadow Temple Compass Chest', 'Shadow Temple Early Silver Rupee Chest'], 
                ['Shadow Temple Bomb Wall']),
            create_dungeon_region(
                'Shadow Temple Huge Pit', 
                ['Shadow Temple Invisible Blades Visible Chest', 'Shadow Temple Invisible Blades Invisible Chest', 
                 'Shadow Temple Falling Spikes Lower Chest', 'Shadow Temple Falling Spikes Upper Chest', 
                 'Shadow Temple Falling Spikes Switch Chest', 'Shadow Temple Invisible Spikes Chest', 
                 'Shadow Temple Freestanding Key', 'GS Shadow Temple Like Like Room', 'GS Shadow Temple Crusher Room',
                 'GS Shadow Temple Single Giant Pot'], 
                ['Shadow Temple Hookshot Target']),
            create_dungeon_region(
                'Shadow Temple Wind Tunnel', 
                ['Shadow Temple Wind Hint Chest', 'Shadow Temple After Wind Enemy Chest', 
                 'Shadow Temple After Wind Hidden Chest', 'GS Shadow Temple Near Ship'], 
                ['Shadow Temple Boat']),
            create_dungeon_region(
                'Shadow Temple Beyond Boat', 
                ['Shadow Temple Spike Walls Left Chest', 'Shadow Temple Boss Key Chest', 
                 'Shadow Temple Hidden Floormaster Chest', 'Bongo Bongo Heart', 'Bongo Bongo', 
                 'GS Shadow Temple Tripple Giant Pot'])
        ])

    if world.dungeon_mq['BW']:
        world.regions.extend([
            create_dungeon_region(
                'Bottom of the Well', 
                ['Bottom of the Well MQ Compass Chest', 'Bottom of the Well MQ Map Chest', 'Bottom of the Well MQ Lens Chest', 
                 'Bottom of the Well MQ Dead Hand Freestanding Key', 'Bottom of the Well MQ East Inner Room Freestanding Key', 
                 'GS Well MQ Basement', 'GS Well MQ West Inner Room', 'GS Well MQ Coffin Room'], 
                ['Bottom of the Well Exit'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Bottom of the Well', 
                ['Bottom of the Well Front Left Hidden Wall', 'Bottom of the Well Front Center Bombable', 
                 'Bottom of the Well Right Bottom Hidden Wall', 'Bottom of the Well Center Large Chest', 
                 'Bottom of the Well Center Small Chest', 'Bottom of the Well Back Left Bombable', 
                 'Bottom of the Well Freestanding Key', 'Bottom of the Well Defeat Boss', 'Bottom of the Well Invisible Chest', 
                 'Bottom of the Well Underwater Front Chest', 'Bottom of the Well Underwater Left Chest', 
                 'Bottom of the Well Basement Chest', 'Bottom of the Well Locked Pits', 'Bottom of the Well Behind Right Grate', 
                 'GS Well West Inner Room', 'GS Well East Inner Room', 'GS Well Like Like Cage', 'Bottom of the Well Stick Pot'], 
                ['Bottom of the Well Exit'])
        ])

    if world.dungeon_mq['IC']:
        world.regions.extend([
            create_dungeon_region(
                'Ice Cavern', 
                ['Ice Cavern MQ Map Chest', 'Ice Cavern MQ Compass Chest', 'Ice Cavern MQ Iron Boots Chest', 
                 'Ice Cavern MQ Freestanding PoH', 'Sheik in Ice Cavern', 'GS Ice Cavern MQ Red Ice', 
                 'GS Ice Cavern MQ Ice Block', 'GS Ice Cavern MQ Scarecrow'], 
                ['Ice Cavern Exit'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Ice Cavern', 
                ['Ice Cavern Map Chest', 'Ice Cavern Compass Chest', 'Ice Cavern Iron Boots Chest', 
                 'Ice Cavern Freestanding PoH', 'Sheik in Ice Cavern', 'GS Ice Cavern Spinning Scythe Room', 
                 'GS Ice Cavern Heart Piece Room', 'GS Ice Cavern Push Block Room'], 
                ['Ice Cavern Exit'])
        ])

    if world.dungeon_mq['GTG']:
        world.regions.extend([
            create_dungeon_region(
                'Gerudo Training Grounds Lobby', 
                ['Gerudo Training Grounds MQ Lobby Left Chest', 'Gerudo Training Grounds MQ Lobby Right Chest', 
                 'Gerudo Training Grounds MQ Hidden Ceiling Chest', 'Gerudo Training Grounds MQ Maze Path First Chest',
                 'Gerudo Training Grounds MQ Maze Path Second Chest', 'Gerudo Training Grounds MQ Maze Path Third Chest'], 
                ['Gerudo Training Grounds Exit', 'Gerudo Training Grounds Left Door', 'Gerudo Training Grounds Right Door']),
            create_dungeon_region(
                'Gerudo Training Grounds Right Side', 
                ['Gerudo Training Grounds MQ Dinolfos Chest', 'Gerudo Training Grounds MQ Underwater Silver Rupee Chest']),
            create_dungeon_region(
                'Gerudo Training Grounds Left Side', 
                ['Gerudo Training Grounds MQ First Iron Knuckle Chest'], 
                ['Gerudo Training Grounds Longshot Target']),
            create_dungeon_region(
                'Gerudo Training Grounds Stalfos Room', 
                ['Gerudo Training Grounds MQ Before Heavy Block Chest', 'Gerudo Training Grounds MQ Heavy Block Chest'], 
                ['Gerudo Training Grounds Song of Time Block']),
            create_dungeon_region(
                'Gerudo Training Grounds Back Areas', 
                ['Gerudo Training Grounds MQ Eye Statue Chest', 'Gerudo Training Grounds MQ Second Iron Knuckle Chest', 
                 'Gerudo Training Grounds MQ Flame Circle Chest'], 
                ['Gerudo Training Grounds Rusted Switch', 'Gerudo Training Grounds Loop Around']),
            create_dungeon_region(
                'Gerudo Training Grounds Central Maze Right', 
                ['Gerudo Training Grounds MQ Maze Right Central Chest', 'Gerudo Training Grounds MQ Maze Right Side Chest', 
                 'Gerudo Training Grounds MQ Ice Arrows Chest'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Gerudo Training Grounds Lobby', 
                ['Gerudo Training Grounds Lobby Left Chest', 'Gerudo Training Grounds Lobby Right Chest', 
                 'Gerudo Training Grounds Stalfos Chest', 'Gerudo Training Grounds Beamos Chest'], 
                ['Gerudo Training Grounds Exit', 'Gerudo Training Ground Left Silver Rupees', 'Gerudo Training Ground Beamos', 
                 'Gerudo Training Ground Central Door']),
            create_dungeon_region(
                'Gerudo Training Grounds Central Maze', 
                ['Gerudo Training Grounds Hidden Ceiling Chest', 'Gerudo Training Grounds Maze Path First Chest', 
                 'Gerudo Training Grounds Maze Path Second Chest', 'Gerudo Training Grounds Maze Path Third Chest', 
                 'Gerudo Training Grounds Maze Path Final Chest'], 
                ['Gerudo Training Grounds Right Locked Doors']),
            create_dungeon_region(
                'Gerudo Training Grounds Central Maze Right', 
                ['Gerudo Training Grounds Maze Right Central Chest', 'Gerudo Training Grounds Maze Right Side Chest', 
                 'Gerudo Training Grounds Freestanding Key'], 
                ['Gerudo Training Grounds Maze Exit']),
            create_dungeon_region(
                'Gerudo Training Grounds Lava Room', 
                ['Gerudo Training Grounds Underwater Silver Rupee Chest'], 
                ['Gerudo Training Grounds Maze Ledge', 'Gerudo Training Grounds Right Hookshot Target']),
            create_dungeon_region(
                'Gerudo Training Grounds Hammer Room', 
                ['Gerudo Training Grounds Hammer Room Clear Chest', 'Gerudo Training Grounds Hammer Room Switch Chest'], 
                ['Gerudo Training Grounds Hammer Target', 'Gerudo Training Grounds Hammer Room Clear']),
            create_dungeon_region(
                'Gerudo Training Grounds Eye Statue Lower', 
                ['Gerudo Training Grounds Eye Statue Chest'], 
                ['Gerudo Training Grounds Eye Statue Exit']),
            create_dungeon_region(
                'Gerudo Training Grounds Eye Statue Upper', 
                ['Gerudo Training Grounds Near Scarecrow Chest'], 
                ['Gerudo Training Grounds Eye Statue Drop']),
            create_dungeon_region(
                'Gerudo Training Grounds Heavy Block Room', 
                ['Gerudo Training Grounds Before Heavy Block Chest', 'Gerudo Training Grounds Heavy Block First Chest', 
                 'Gerudo Training Grounds Heavy Block Second Chest', 'Gerudo Training Grounds Heavy Block Third Chest', 
                 'Gerudo Training Grounds Heavy Block Fourth Chest'], 
                ['Gerudo Training Grounds Hidden Hookshot Target'])
        ])

    if world.dungeon_mq['GC']:
        world.regions.extend([
            create_dungeon_region(
                'Ganons Castle Lobby', 
                ['GC MQ Deku Scrub Bombs', 'GC MQ Deku Scrub Arrows', 'GC MQ Deku Scrub Red Potion', 'GC MQ Deku Scrub Green Potion',
                 'GC MQ Deku Scrub Deku Nuts'],
                ['Ganons Castle Exit', 'Ganons Castle Forest Trial', 'Ganons Castle Fire Trial', 'Ganons Castle Water Trial', 
                 'Ganons Castle Shadow Trial', 'Ganons Castle Spirit Trial', 'Ganons Castle Light Trial', 
                 'Ganons Castle Tower']),            
            create_dungeon_region(
                'Ganons Castle Forest Trial', 
                ['Ganons Castle MQ Forest Trial First Chest', 'Ganons Castle MQ Forest Trial Second Chest', 
                 'Ganons Castle MQ Forest Trial Freestanding Key', 'Ganons Castle Forest Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Fire Trial', 
                ['Ganons Castle Fire Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Water Trial', 
                ['Ganons Castle MQ Water Trial Chest', 'Ganons Castle Water Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Shadow Trial', 
                ['Ganons Castle MQ Shadow Trial First Chest', 'Ganons Castle MQ Shadow Trial Second Chest', 
                 'Ganons Castle Shadow Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Spirit Trial', 
                ['Ganons Castle MQ Spirit Trial First Chest', 'Ganons Castle MQ Spirit Trial Second Chest', 
                 'Ganons Castle MQ Spirit Trial Sun Front Left Chest', 'Ganons Castle MQ Spirit Trial Sun Back Left Chest', 
                 'Ganons Castle MQ Spirit Trial Golden Gauntlets Chest', 'Ganons Castle MQ Spirit Trial Sun Back Right Chest', 
                 'Ganons Castle Spirit Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Light Trial', 
                ['Ganons Castle MQ Light Trial Lullaby Chest', 'Ganons Castle Light Trial Clear'])
        ])
    else:
        world.regions.extend([
            create_dungeon_region(
                'Ganons Castle Lobby', 
                ['GC Deku Scrub Bombs', 'GC Deku Scrub Arrows', 'GC Deku Scrub Red Potion', 'GC Deku Scrub Green Potion'],
                ['Ganons Castle Exit', 'Ganons Castle Forest Trial', 'Ganons Castle Fire Trial', 'Ganons Castle Water Trial', 
                 'Ganons Castle Shadow Trial', 'Ganons Castle Spirit Trial', 'Ganons Castle Light Trial', 
                 'Ganons Castle Tower']),            
            create_dungeon_region(
                'Ganons Castle Forest Trial', 
                ['Ganons Castle Forest Trial Chest', 'Ganons Castle Forest Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Fire Trial', 
                ['Ganons Castle Fire Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Water Trial', 
                ['Ganons Castle Water Trial Left Chest', 'Ganons Castle Water Trial Right Chest', 
                 'Ganons Castle Water Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Shadow Trial', 
                ['Ganons Castle Shadow Trial First Chest', 'Ganons Castle Shadow Trial Second Chest', 
                 'Ganons Castle Shadow Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Spirit Trial', 
                ['Ganons Castle Spirit Trial First Chest', 'Ganons Castle Spirit Trial Second Chest', 
                 'Ganons Castle Spirit Trial Clear']),
            create_dungeon_region(
                'Ganons Castle Light Trial', 
                ['Ganons Castle Light Trial First Left Chest', 'Ganons Castle Light Trial Second Left Chest', 
                 'Ganons Castle Light Trial Third Left Chest', 'Ganons Castle Light Trial First Right Chest', 
                 'Ganons Castle Light Trial Second Right Chest', 'Ganons Castle Light Trial Third Right Chest', 
                 'Ganons Castle Light Trail Invisible Enemies Chest', 'Ganons Castle Light Trial Lullaby Chest', 
                 'Ganons Castle Light Trial Clear'])
        ])

    world.initialize_regions()

def create_ow_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Overworld, locations, exits)

def create_interior_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Interior, locations, exits)

def create_dungeon_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Dungeon, locations, exits)

def create_grotto_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Grotto, locations, exits)

def _create_region(name, type, locations=None, exits=None):
    ret = Region(name, type)
    if locations is None:
        locations = []
    if exits is None:
        exits = []

    for exit in exits:
        ret.exits.append(Entrance(exit, ret))
    for location in locations:
        address, address2, default, type, scene, hint = location_table[location]
        ret.locations.append(Location(location, address, address2, default, type, scene, hint, ret))
    return ret

location_table = {'Remove the Cursed Mask': (None, None, None, 'Mask'),
                    'SCT 20 Rupee Chest': (None, None, None, 'Chest'),
                    'Festival Tower Rupee Chest': (None, None, None, 'Chest'),
                    'ECT 100 Rupee Chest': (None, None, None, 'Chest'),
                    'WFT Map Chest': (None, None, None, 'Chest'),
                    'WFT Small Key Chest': (None, None, None, 'Chest'),
                    'WFT Compass Chest': (None, None, None, 'Chest'),
                    'WFT Bow Chest': (None, None, None, 'Chest'),
                    'WFT Boss Key Chest': (None, None, None, 'Chest'),
                    'Clock Town Owl Statue': (None, None, None, 'Statue'),
                    'Milk Road Owl Statue': (None, None, None, 'Statue'),
                    'Swamp Owl Statue': (None, None, None, 'Statue'),
                    'Woodfall Owl Statue': (None, None, None, 'Statue'),
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
                    'Town Deku Salesman': (None, None, None, 'NPC'),
                    'Swamp Deku Salesman': (None, None, None, 'NPC'),
                    'Mountain Deku Salesman': (None, None, None, 'NPC'),
                    'Ocean Deku Salesman': (None, None, None, 'NPC'),
                    'Canyon Deku Salesman': (None, None, None, 'NPC'),
                    'Song from Goron Elder': (None, None, None, 'NPC'),
                    'Love on the Balcony': (None, None, None, 'Collectable'),
                    'Claim Odolwa\'s Remains': (None, None, None, 'Collectable'),
                    'Claim Odolwa\'s Heart': (None, None, None, 'Collectable'),
                    'Claim Goht\'s Remains': (None, None, None, 'Collectable'),
                    'Claim Goht\'s Heart': (None, None, None, 'Collectable'),
                    'Claim Gyorg\'s Remains': (None, None, None, 'Collectable'),
                    'Claim Gyorg\'s Heart': (None, None, None, 'Collectable'),
                    'Claim Odolwa\'s Remains': (None, None, None, 'Collectable'),
                    'Claim Odolwa\'s Heart': (None, None, None, 'Collectable'),
                    'Defeat Odolwa': (None, None, None, 'Event'),
                    'Defeat Goht': (None, None, None, 'Event'),
                    'Defeat Gyorg': (None, None, None, 'Event'),
                    'Defeat Twinmold': (None, None, None, 'Event'),
                    'Song from Giants': (None, None, None, 'Song'),
                    'WFT Lobby Floating Fairy': (None, None, None, 'SF'),
                    'WFT Central Flower Deku Baba': (None, None, None, 'SF'),
                    'WFT Central Flower Corner Pot': (None, None, None, 'SF'),
                    'WFT Deku Flower Elevator Beehive': (None, None, None, 'SF'),
                    'WFT Bridge Skulltula': (None, None, None, 'SF'),
                    'WFT Bridge Room Beehive': (None, None, None, 'SF'),
                    'WFT Dark Puff Battle Arena Chest': (None, None, None, 'SFC'),
                    'WFT Under Poison Bridge': (None, None, None, 'SF'),
                    'WFT Central Flower Bubble Fairy': (None, None, None, 'SF'),
                    'WFT Central Room Switch Chest': (None, None, None, 'SFC'),
                    'WFT Lower East Bubble Fairy': (None, None, None, 'SF'),
                    'WFT Upper East Bubble Fairy': (None, None, None, 'SF'),
                    'WFT West Bubble Fairy': (None, None, None, 'SF'),
                    'WFT Hot Bubble Fairy': (None, None, None, 'SF'),
                    'WFT Lobby Fairy Chest': (None, None, None, 'SFC'),
                    'SH SF1': (None, None, None, 'SF-SH'),
                    'SH SF2': (None, None, None, 'SF-SH'),
                    'SH SF3': (None, None, None, 'SF-SH'),
                    'SH SF4': (None, None, None, 'SF-SH'),
                    'SH SF5': (None, None, None, 'SF-SH'),
                    'SH SF6': (None, None, None, 'SF-SH'),
                    'SH SF7': (None, None, None, 'SF-SH'),
                    'SH SF8': (None, None, None, 'SF-SH'),
                    'SH SF9': (None, None, None, 'SF-SH'),
                    'SH SF10': (None, None, None, 'SF-SH'),
                    'SH SF11': (None, None, None, 'SF-SH'),
                    'SH SF12': (None, None, None, 'SF-SH'),
                    'SH SF13': (None, None, None, 'SF-SH'),
                    'SH SF14': (None, None, None, 'SF-SH'),
                    'SH SF15': (None, None, None, 'SF-SH'),
                    'GB SF1': (None, None, None, 'SF-GB'),
                    'GB SF2': (None, None, None, 'SF-GB'),
                    'GB SF3': (None, None, None, 'SF-GB'),
                    'GB SF4': (None, None, None, 'SF-GB'),
                    'GB SF5': (None, None, None, 'SF-GB'),
                    'GB SF6': (None, None, None, 'SF-GB'),
                    'GB SF7': (None, None, None, 'SF-GB'),
                    'GB SF8': (None, None, None, 'SF-GB'),
                    'GB SF9': (None, None, None, 'SF-GB'),
                    'GB SF10': (None, None, None, 'SF-GB'),
                    'GB SF11': (None, None, None, 'SF-GB'),
                    'GB SF12': (None, None, None, 'SF-GB'),
                    'GB SF13': (None, None, None, 'SF-GB'),
                    'GB SF14': (None, None, None, 'SF-GB'),
                    'GB SF15': (None, None, None, 'SF-GB'),
                    'ST SF1': (None, None, None, 'SF-ST'),
                    'ST SF2': (None, None, None, 'SF-ST'),
                    'ST SF3': (None, None, None, 'SF-ST'),
                    'ST SF4': (None, None, None, 'SF-ST'),
                    'ST SF5': (None, None, None, 'SF-ST'),
                    'ST SF6': (None, None, None, 'SF-ST'),
                    'ST SF7': (None, None, None, 'SF-ST'),
                    'ST SF8': (None, None, None, 'SF-ST'),
                    'ST SF9': (None, None, None, 'SF-ST'),
                    'ST SF10': (None, None, None, 'SF-ST'),
                    'ST SF11': (None, None, None, 'SF-ST'),
                    'ST SF12': (None, None, None, 'SF-ST'),
                    'ST SF13': (None, None, None, 'SF-ST'),
                    'ST SF14': (None, None, None, 'SF-ST'),
                    'ST SF15': (None, None, None, 'SF-ST'),
                    'Open the Moon': (None, None, None, 'Event')}

    # Deku Tree vanilla
    'Deku Tree Lobby Chest': (0x24A7146, None, 0x0823, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree Slingshot Chest': (0x24C20C6, None, 0x00A1, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree Slingshot Room Side Chest': (0x24C20D6, None, 0x5905, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree Compass Chest': (0x25040D6, None, 0x0802, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree Compass Room Side Chest': (0x25040E6, None, 0x5906, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree Basement Chest': (0x24C8166, None, 0x5904, 'Chest', 0x00, 'Deku Tree'),
    # Deku Tree MQ
    'Deku Tree MQ Lobby Chest': (0, None, 0x0823, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree MQ Compass Chest': (0, None, 0x0801, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree MQ Slingshot Chest': (0, None, 0x10A6, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree MQ Slingshot Room Back Chest': (0, None, 0x8522, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree MQ Basement Chest': (0, None, 0x8524, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree MQ Before Spinning Log Chest': (0, None, 0x5905, 'Chest', 0x00, 'Deku Tree'),
    'Deku Tree MQ After Spinning Log Chest': (0, None, 0x5AA0, 'Chest', 0x00, 'Deku Tree'),

    # Dodongo's Cavern shared
    'Chest Above King Dodongo': (0x2EB00BA, None, 0x5020, 'Chest', 0x12, 'Dodongo\'s Cavern'),
    # Dodongo's Cavern vanilla
    'Dodongos Cavern Map Chest': (0x1F2819E, None, 0x0828, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern Compass Chest': (0x1FAF0AA, None, 0x0805, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern Bomb Flower Platform': (0x1F890DE, None, 0x59C6, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern Bomb Bag Chest': (0x1F890CE, None, 0x0644, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern End of Bridge Chest': (0x1F281CE, None, 0x552A, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    # Dodongo's Cavern MQ
    'Dodongos Cavern MQ Map Chest': (0, None, 0x0820, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern MQ Bomb Bag Chest': (0, None, 0x0644, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern MQ Compass Chest': (0, None, 0x1805, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern MQ Larva Room Chest': (0, None, 0x7522, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern MQ Torch Puzzle Room Chest': (0, None, 0x59A3, 'Chest', 0x01, 'Dodongo\'s Cavern'),
    'Dodongos Cavern MQ Under Grave Chest': (0, None, 0x5541, 'Chest', 0x01, 'Dodongo\'s Cavern'),

    # Jabu Jabu's Belly vanilla
    'Boomerang Chest': (0x278A0BA, None, 0x10C1, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly Map Chest': (0x278E08A, None, 0x1822, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly Compass Chest': (0x279608A, None, 0xB804, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    # Jabu Jabu's Belly MQ
    'Jabu Jabus Belly MQ Entry Side Chest': (0, None, 0x8045, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Map Chest': (0, None, 0xB823, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Second Room Lower Chest': (0, None, 0x5042, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Compass Chest': (0, None, 0xB800, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Second Room Upper Chest': (0, None, 0x8907, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Basement North Chest': (0, None, 0x8048, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Basement South Chest': (0, None, 0x8064, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Near Boss Chest': (0, None, 0x852A, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Falling Like Like Room Chest': (0, None, 0x70E9, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'Jabu Jabus Belly MQ Boomerang Room Small Chest': (0, None, 0x5041, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),
    'MQ Boomerang Chest': (0, None, 0x10C6, 'Chest', 0x02, 'Jabu Jabu\'s Belly'),

    # Forest Temple vanilla
    'Forest Temple First Chest': (0x23E5092, None, 0x5843, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Chest Behind Lobby': (0x2415082, None, 0x7840, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Well Chest': (0x244A062, None, 0x5849, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Map Chest': (0x2455076, None, 0x1821, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Outside Hookshot Chest': (0x241F0D6, None, 0x5905, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Falling Room Chest': (0x247E09E, None, 0x5947, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Block Push Chest': (0x245B096, None, 0x8964, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Boss Key Chest': (0xCB0DC2, None, 0x27EE, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Floormaster Chest': (0x2490072, None, 0x7842, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Bow Chest': (0x2415092, None, 0xB08C, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Red Poe Chest': (0x246607E, None, 0x784D, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Blue Poe Chest': (0x246F07E, None, 0x180F, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple Near Boss Chest': (0x2486082, None, 0x592B, 'Chest', 0x03, 'Forest Temple'),
    # Forest Temple MQ
    'Forest Temple MQ First Chest': (0, None, 0x8843, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Chest Behind Lobby': (0, None, 0x7840, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Bow Chest': (0, None, 0xB08C, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ NE Outdoors Lower Chest': (0, None, 0x5841, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ NE Outdoors Upper Chest': (0, None, 0x5845, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Well Chest': (0, None, 0x5849, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Map Chest': (0, None, 0x182D, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Compass Chest': (0, None, 0x180F, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Falling Room Chest': (0, None, 0x8926, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Near Boss Chest': (0, None, 0x592B, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Redead Chest': (0, None, 0x7842, 'Chest', 0x03, 'Forest Temple'),
    'Forest Temple MQ Boss Key Chest': (0, None, 0x27EE, 'Chest', 0x03, 'Forest Temple'), # This needs tested to see if it has changed from vanilla.

    # Fire Temple vanilla
    'Fire Temple Chest Near Boss': (0x230808A, None, 0x5841, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Fire Dancer Chest': (0x2318082, None, 0x7CC0, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Boss Key Chest': (0x238A0D6, None, 0x27EC, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Big Lava Room Bombable Chest': (0x23AD076, None, 0x5842, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Big Lava Room Open Chest': (0x239D0A6, None, 0x5844, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Boulder Maze Lower Chest': (0x2323152, None, 0x5843, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Boulder Maze Upper Chest': (0x2323182, None, 0x5846, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Boulder Maze Side Room': (0x23B40B2, None, 0x5848, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Boulder Maze Bombable Pit': (0x231B0E2, None, 0x584B, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Scarecrow Chest': (0x2339082, None, 0x5ACD, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Map Chest': (0x237E0C2, None, 0x082A, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Compass Chest': (0x23C1082, None, 0x0807, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Highest Goron Chest': (0x2365066, None, 0x5849, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple Megaton Hammer Chest': (0x236C102, None, 0x01A5, 'Chest', 0x04, 'Fire Temple'),
    # Fire Temple MQ
    'Fire Temple MQ Chest Near Boss': (0, None, 0x5847, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Megaton Hammer Chest': (0, None, 0x11A0, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Compass Chest': (0, None, 0x080B, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Maze Lower Chest': (0, None, 0x5CC3, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Maze Upper Chest': (0, None, 0x5CE6, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ West Tower Top Chest': (0, None, 0x5845, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Entrance Hallway Small Chest': (0, None, 0x7542, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Map Chest': (0, None, 0x082C, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Boss Key Chest': (0, None, 0x27E4, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Big Lava Room Bombable Chest': (0, None, 0x5841, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Maze Side Room': (0, None, 0x5848, 'Chest', 0x04, 'Fire Temple'),
    'Fire Temple MQ Freestanding Key': (None, None, 0x1C, 'Collectable', 0x04, 'Fire Temple'), 

    # Water Temple vanilla
    'Water Temple Map Chest': (0x26690A6, None, 0x1822, 'Chest', 0x05, 'Water Temple'),
    'Water Temple Compass Chest': (0x25FC0D2, None, 0x0809, 'Chest', 0x05, 'Water Temple'),
    'Water Temple Torches Chest': (0x26640A6, None, 0x7841, 'Chest', 0x05, 'Water Temple'),
    'Water Temple Dragon Chest': (0x261F0BA, None, 0x584A, 'Chest', 0x05, 'Water Temple'),
    'Water Temple Central Bow Target Chest': (0x266D072, None, 0x5848, 'Chest', 0x05, 'Water Temple'),
    'Water Temple Central Pillar Chest': (0x25EF0D6, None, 0x5846, 'Chest', 0x05, 'Water Temple'),
    'Water Temple Cracked Wall Chest': (0x265B0A6, None, 0x5840, 'Chest', 0x05, 'Water Temple'),
    'Water Temple Boss Key Chest': (0x2657066, None, 0x27E5, 'Chest', 0x05, 'Water Temple'),
    'Water Temple Dark Link Chest': (0x261907A, None, 0x0127, 'Chest', 0x05, 'Water Temple'),
    'Water Temple River Chest': (0x26740DE, None, 0x5843, 'Chest', 0x05, 'Water Temple'),
    # Water Temple MQ
    'Water Temple MQ Central Pillar Chest': (0, None, 0x8846, 'Chest', 0x05, 'Water Temple'),
    'Water Temple MQ Boss Key Chest': (0, None, 0x27E5, 'Chest', 0x05, 'Water Temple'),
    'Water Temple MQ Longshot Chest': (0, None, 0xB120, 'Chest', 0x05, 'Water Temple'),
    'Water Temple MQ Compass Chest': (0, None, 0x1801, 'Chest', 0x05, 'Water Temple'),
    'Water Temple MQ Map Chest': (0, None, 0xB822, 'Chest', 0x05, 'Water Temple'),
    'Water Temple MQ Freestanding Key': (None, None, 0x01, 'Collectable', 0x05, 'Water Temple'), 

    # Spirit Temple vanilla
    'Spirit Temple Child Left Chest': (0x2B190BA, None, 0x5528, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Child Right Chest': (0x2B13182, None, 0x8840, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Compass Chest': (0x2B6B08A, None, 0x3804, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Early Adult Right Chest': (0x2B6207A, None, 0x5847, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple First Mirror Right Chest': (0x2B700C6, None, 0x890D, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple First Mirror Left Chest': (0x2B700D6, None, 0x8F8E, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Map Chest': (0x2B25126, None, 0xB823, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Child Climb East Chest': (0x2B1D122, None, 0x8066, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Child Climb North Chest': (0x2B1D132, None, 0x852C, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Sun Block Room Chest': (0x2B481B2, None, 0x8841, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Statue Hand Chest': (0x2B25136, None, 0x8842, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple NE Main Room Chest': (0x2B25146, None, 0x888F, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Near Four Armos Chest': (0x2B9F076, None, 0x5845, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Hallway Left Invisible Chest': (0x2B900B6, None, 0x6914, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Hallway Right Invisible Chest': (0x2B900C6, None, 0x6915, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Boss Key Chest': (0x2BA4162, None, 0x27EA, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple Topmost Chest': (0x2BCF0FE, None, 0x8CF2, 'Chest', 0x06, 'Spirit Temple'),
    # Spirit Temple MQ
    'Spirit Temple MQ Entrance Front Left Chest': (0, None, 0x507A, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Entrance Back Right Chest': (0, None, 0x807F, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Entrance Front Right Chest': (0, None, 0x885B, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Entrance Back Left Chest': (0, None, 0x885E, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Child Center Chest': (0, None, 0x885D, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Map Chest': (0, None, 0x0820, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Child Left Chest': (0, None, 0x7848, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Child Climb North Chest': (0, None, 0x7066, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Child Climb South Chest': (0, None, 0x884C, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Compass Chest': (0, None, 0xB803, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Lower NE Main Room Chest': (0, None, 0x888F, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Upper NE Main Room Chest': (0, None, 0x6902, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Silver Block Hallway Chest': (0, None, 0x885C, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Sun Block Room Chest': (0, None, 0x8901, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Lower Adult Right Chest': (0, None, 0x5AA7, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Lower Adult Left Chest': (0, None, 0x7AA4, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Beamos Room Chest': (0, None, 0x7979, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Ice Trap Chest': (0, None, 0x5F98, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Boss Key Chest': (0, None, 0x27E5, 'Chest', 0x06, 'Spirit Temple'),
    'Spirit Temple MQ Mirror Puzzle Invisible Chest': (0, None, 0x6852, 'Chest', 0x06, 'Spirit Temple'),

    # Shadow Temple vanilla
    'Shadow Temple Map Chest': (0x27CC0AA, None, 0x1821, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Hover Boots Chest': (0x27DC0CA, None, 0x15E7, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Compass Chest': (0x27EC09E, None, 0x1803, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Early Silver Rupee Chest': (0x27E40F6, None, 0x5842, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Invisible Blades Visible Chest': (0x282212A, None, 0x588C, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Invisible Blades Invisible Chest': (0x282211A, None, 0x6976, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Falling Spikes Lower Chest': (0x2801132, None, 0x5945, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Falling Spikes Upper Chest': (0x2801142, None, 0x5886, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Falling Spikes Switch Chest': (0x2801122, None, 0x8844, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Invisible Spikes Chest': (0x28090EE, None, 0x7889, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Wind Hint Chest': (0x283609A, None, 0x6955, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple After Wind Enemy Chest': (0x28390FE, None, 0x7888, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple After Wind Hidden Chest': (0x28390EE, None, 0x6854, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Spike Walls Left Chest': (0x28130B6, None, 0x588A, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Boss Key Chest': (0x28130A6, None, 0x27EB, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Hidden Floormaster Chest': (0x282508A, None, 0x784D, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple Freestanding Key': (None, None, 0x01, 'Collectable', 0x07, 'Shadow Temple'),
    # Shadow Temple MQ
    'Shadow Temple MQ Compass Chest': (0, None, 0x1801, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Hover Boots Chest': (0, None, 0x15E7, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Early Gibdos Chest': (0, None, 0x0822, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Map Chest': (0, None, 0x7843, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Beamos Silver Rupees Chest': (0, None, 0x892F, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Falling Spikes Switch Chest': (0, None, 0x8844, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Falling Spikes Lower Chest': (0, None, 0x5945, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Falling Spikes Upper Chest': (0, None, 0x5886, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Invisible Spikes Chest': (0, None, 0x7889, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Boss Key Chest': (0, None, 0x27EB, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Spike Walls Left Chest': (0, None, 0x588A, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Stalfos Room Chest': (0, None, 0x79D0, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Invisible Blades Invisible Chest': (0, None, 0x6856, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Invisible Blades Visible Chest': (0, None, 0x588C, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Bomb Flower Chest': (0, None, 0x794D, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Wind Hint Chest': (0, None, 0x6855, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ After Wind Hidden Chest': (0, None, 0x6934, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ After Wind Enemy Chest': (0, None, 0x7888, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Near Ship Invisible Chest': (0, None, 0x684E, 'Chest', 0x07, 'Shadow Temple'),
    'Shadow Temple MQ Freestanding Key': (None, None, 0x06, 'Collectable', 0x07, 'Shadow Temple'), 

    # Bottom of the Well vanilla
    'Bottom of the Well Front Left Hidden Wall': (0x32D317E, None, 0x5848, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Front Center Bombable': (0x32D30FE, None, 0x5062, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Right Bottom Hidden Wall': (0x32D314E, None, 0x5845, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Center Large Chest': (0x32D30EE, None, 0x0801, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Center Small Chest': (0x32D31AE, None, 0x504E, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Back Left Bombable': (0x32D313E, None, 0x5C84, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Defeat Boss': (0x32FB0AA, None, 0x1143, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Invisible Chest': (0x32FB0BA, None, 0x6AD4, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Underwater Front Chest': (0x32D31BE, None, 0x5CD0, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Underwater Left Chest': (0x32D318E, None, 0x5909, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Basement Chest': (0x32E9252, None, 0x0827, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Locked Pits': (0x32F90AA, None, 0x552A, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Behind Right Grate': (0x32D319E, None, 0x554C, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well Freestanding Key': (None, None, 0x01, 'Collectable', 0x08, 'Bottom of the Well'),
    # Bottom of the Well MQ
    'Bottom of the Well MQ Map Chest': (0, None, 0x0823, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well MQ Lens Chest': (0, None, 0xB141, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well MQ Compass Chest': (0, None, 0x1802, 'Chest', 0x08, 'Bottom of the Well'),
    'Bottom of the Well MQ Dead Hand Freestanding Key': (None, None, 0x02, 'Collectable', 0x08, 'Bottom of the Well'), 
    'Bottom of the Well MQ East Inner Room Freestanding Key': (None, None, 0x01, 'Collectable', 0x08, 'Bottom of the Well'),

    # Ice Cavern vanilla
    'Ice Cavern Map Chest': (0x2C4016A, None, 0x0820, 'Chest', 0x09, 'Ice Cavern'),
    'Ice Cavern Compass Chest': (0x2C4E236, None, 0x0801, 'Chest', 0x09, 'Ice Cavern'),
    'Ice Cavern Iron Boots Chest': (0x2C380A2, None, 0x15C2, 'Chest', 0x09, 'Ice Cavern'),
    'Ice Cavern Freestanding PoH': (None, None, 0x01, 'Collectable', 0x09, 'Ice Cavern'),
    # Ice Cavern MQ
    'Ice Cavern MQ Iron Boots Chest': (0, None, 0x15C2, 'Chest', 0x09, 'Ice Cavern'),
    'Ice Cavern MQ Compass Chest': (0, None, 0x0800, 'Chest', 0x09, 'Ice Cavern'),
    'Ice Cavern MQ Map Chest': (0, None, 0xB821, 'Chest', 0x09, 'Ice Cavern'),
    'Ice Cavern MQ Freestanding PoH': (None, None, 0x01, 'Collectable', 0x09, 'Ice Cavern'),

    # Gerudo Training Grounds vanilla
    'Gerudo Training Grounds Lobby Left Chest': (0x28870CA, None, 0x8893, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Lobby Right Chest': (0x28870BA, None, 0x8947, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Stalfos Chest': (0x28970AA, None, 0x8840, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Beamos Chest': (0x28C715E, None, 0x8841, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Hidden Ceiling Chest': (0x28D010E, None, 0x584B, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Maze Path First Chest': (0x28D00CE, None, 0x5AA6, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Maze Path Second Chest': (0x28D00FE, None, 0x59CA, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Maze Path Third Chest': (0x28D00EE, None, 0x5969, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Maze Path Final Chest': (0x28D011E, None, 0x0B2C, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Maze Right Central Chest': (0x28D00BE, None, 0x5D45, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Maze Right Side Chest': (0x28D00DE, None, 0x5968, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Underwater Silver Rupee Chest': (0x28D91D6, None, 0x884D, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Hammer Room Clear Chest': (0x28B91AE, None, 0x7952, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Hammer Room Switch Chest': (0x28B919E, None, 0x5850, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Eye Statue Chest': (0x28AE09E, None, 0x8843, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Near Scarecrow Chest': (0x28D00AE, None, 0x5844, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Before Heavy Block Chest': (0x28A611E, None, 0x7971, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Heavy Block First Chest': (0x28DD0BE, None, 0x7ACF, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Heavy Block Second Chest': (0x28DD0AE, None, 0x788E, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Heavy Block Third Chest': (0x28DD08E, None, 0x6854, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Heavy Block Fourth Chest': (0x28DD09E, None, 0x5F82, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds Freestanding Key': (None, None, 0x01, 'Collectable', 0x0B, 'Gerudo Training Grounds'),
    # Gerudo Training Grounds MQ
    'Gerudo Training Grounds MQ Lobby Right Chest': (0, None, 0x5D47, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Lobby Left Chest': (0, None, 0x5953, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ First Iron Knuckle Chest': (0, None, 0x89A0, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Before Heavy Block Chest': (0, None, 0x7951, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Eye Statue Chest': (0, None, 0x8063, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Flame Circle Chest': (0, None, 0x884E, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Second Iron Knuckle Chest': (0, None, 0x7952, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Dinolfos Chest': (0, None, 0x8841, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Ice Arrows Chest': (0, None, 0xBB24, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Maze Right Central Chest': (0, None, 0x5885, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Maze Path First Chest': (0, None, 0x5986, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Maze Right Side Chest': (0, None, 0x5E48, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Maze Path Third Chest': (0, None, 0x5E49, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Maze Path Second Chest': (0, None, 0x59CA, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Hidden Ceiling Chest': (0, None, 0x5AAB, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Underwater Silver Rupee Chest': (0, None, 0x884D, 'Chest', 0x0B, 'Gerudo Training Grounds'),
    'Gerudo Training Grounds MQ Heavy Block Chest': (0, None, 0x7AA2, 'Chest', 0x0B, 'Gerudo Training Grounds'),

    # Ganon's Castle shared
    'Ganons Tower Boss Key Chest': (0x2F040EE, None, 0x27EB, 'Chest', 0x0A, 'my tower'),
    # Ganon's Castle vanilla
    'Ganons Castle Forest Trial Chest': (0x31F106E, None, 0x7889, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Water Trial Left Chest': (0x31D7236, None, 0x5F87, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Water Trial Right Chest': (0x31D7226, None, 0x5906, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Shadow Trial First Chest': (0x32350CA, None, 0x5888, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Shadow Trial Second Chest': (0x32350BA, None, 0x36C5, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Spirit Trial First Chest': (0x3268132, None, 0x8D72, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Spirit Trial Second Chest': (0x3268142, None, 0x6954, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Light Trial First Left Chest': (0x321B11E, None, 0x588C, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Light Trial Second Left Chest': (0x321B10E, None, 0x5F8B, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Light Trial Third Left Chest': (0x321B12E, None, 0x590D, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Light Trial First Right Chest': (0x321B13E, None, 0x5F8E, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Light Trial Second Right Chest': (0x321B0FE, None, 0x596A, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Light Trial Third Right Chest': (0x321B14E, None, 0x5F8F, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Light Trail Invisible Enemies Chest': (0x321B15E, None, 0x7850, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle Light Trial Lullaby Chest': (0x321B17E, None, 0x8851, 'Chest', 0x0D, 'my castle'),
    # Ganon's Castle MQ
    'Ganons Castle MQ Water Trial Chest': (0, None, 0x59C1, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Forest Trial First Chest': (0, None, 0x8942, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Forest Trial Second Chest': (0, None, 0x8023, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Light Trial Lullaby Chest': (0, None, 0x8904, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Shadow Trial First Chest': (0, None, 0x8940, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Shadow Trial Second Chest': (0, None, 0x8845, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Spirit Trial Golden Gauntlets Chest': (0, None, 0xB6C6, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Spirit Trial Sun Back Right Chest': (0, None, 0x8907, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Spirit Trial Sun Back Left Chest': (0, None, 0x8848, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Spirit Trial Sun Front Left Chest': (0, None, 0x8909, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Spirit Trial First Chest': (0, None, 0x506A, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Spirit Trial Second Chest': (0, None, 0x6954, 'Chest', 0x0D, 'my castle'),
    'Ganons Castle MQ Forest Trial Freestanding Key': (None, None, 0x01, 'Collectable', 0x0D, 'my castle'), 

    # I don't think the addresses matter for Link's Pocket anymore, but they can't be None for some reason
    'Links Pocket': (0x34806FB, 0x34806FF, None, 'Boss', None, 'Link\'s Pocket'), 
    'Queen Gohma': (0xCA315F, 0x2079571, 0x6C, 'Boss', None, 'Deku Tree'),
    'King Dodongo': (0xCA30DF, 0x2223309, 0x6D, 'Boss', None, 'Dodongo\'s Cavern'),
    'Barinade': (0xCA36EB, 0x2113C19, 0x6E, 'Boss', None, 'Jabu Jabu\'s Belly'),
    'Phantom Ganon': (0xCA3D07, 0xD4ED79, 0x66, 'Boss', None, 'Shadow Temple'),
    'Volvagia': (0xCA3D93, 0xD10135, 0x67, 'Boss', None, 'Fire Temple'),
    'Morpha': (0xCA3E1F, 0xD5A3A9, 0x68, 'Boss', None, 'Water Temple'),
    'Twinrova': (0xCA3EB3, 0xD39FF1, 0x69, 'Boss', None, 'Spirit Temple'),
    'Bongo Bongo': (0xCA3F43, 0xD13E19, 0x6A, 'Boss', None, 'Shadow Temple'),
    'Ganon': (None, None, None, 'Boss', None, 'Ganon\'s Castle'),
    # note that the scene for skulltulas is not the actual scene the token appears in
    # rather, it is the index of the grouping used when storing skulltula collection
    # for example, zora river, zora's domain, and zora fountain are all a single 'scene' for skulltulas
    'GS Deku Tree Basement Back Room': (None, None, 0x01, 'GS Token', 0x00, 'Deku Tree'),
    'GS Deku Tree Basement Gate': (None, None, 0x02, 'GS Token', 0x00, 'Deku Tree'),
    'GS Deku Tree Basement Vines': (None, None, 0x04, 'GS Token', 0x00, 'Deku Tree'),
    'GS Deku Tree Compass Room': (None, None, 0x08, 'GS Token', 0x00, 'Deku Tree'),

    'GS Deku Tree MQ Lobby': (None, None, 0x02, 'GS Token', 0x00, 'Deku Tree'),
    'GS Deku Tree MQ Compass Room': (None, None, 0x08, 'GS Token', 0x00, 'Deku Tree'),
    'GS Deku Tree MQ Basement Ceiling': (None, None, 0x04, 'GS Token', 0x00, 'Deku Tree'),
    'GS Deku Tree MQ Basement Back Room': (None, None, 0x01, 'GS Token', 0x00, 'Deku Tree'),

    'GS Dodongo\'s Cavern Vines Above Stairs': (None, None, 0x01, 'GS Token', 0x01, 'Dodongo\'s Cavern'),
    'GS Dodongo\'s Cavern Scarecrow': (None, None, 0x02, 'GS Token', 0x01, 'Dodongo\'s Cavern'),
    'GS Dodongo\'s Cavern Alcove Above Stairs': (None, None, 0x04, 'GS Token', 0x01, 'Dodongo\'s Cavern'),
    'GS Dodongo\'s Cavern Back Room': (None, None, 0x08, 'GS Token', 0x01, 'Dodongo\'s Cavern'),
    'GS Dodongo\'s Cavern East Side Room': (None, None, 0x10, 'GS Token', 0x01, 'Dodongo\'s Cavern'),

    'GS Dodongo\'s Cavern MQ Scrub Room': (None, None, 0x02, 'GS Token', 0x01, 'Dodongo\'s Cavern'),
    'GS Dodongo\'s Cavern MQ Song of Time Block Room': (None, None, 0x08, 'GS Token', 0x01, 'Dodongo\'s Cavern'),
    'GS Dodongo\'s Cavern MQ Lizalfos Room': (None, None, 0x04, 'GS Token', 0x01, 'Dodongo\'s Cavern'),
    'GS Dodongo\'s Cavern MQ Larva Room': (None, None, 0x10, 'GS Token', 0x01, 'Dodongo\'s Cavern'),
    'GS Dodongo\'s Cavern MQ Back Area': (None, None, 0x01, 'GS Token', 0x01, 'Dodongo\'s Cavern'),

    'GS Jabu Jabu Lobby Basement Lower': (None, None, 0x01, 'GS Token', 0x02, 'Jabu Jabu\'s Belly'),
    'GS Jabu Jabu Lobby Basement Upper': (None, None, 0x02, 'GS Token', 0x02, 'Jabu Jabu\'s Belly'),
    'GS Jabu Jabu Near Boss': (None, None, 0x04, 'GS Token', 0x02, 'Jabu Jabu\'s Belly'),
    'GS Jabu Jabu Water Switch Room': (None, None, 0x08, 'GS Token', 0x02, 'Jabu Jabu\'s Belly'),

    'GS Jabu Jabu MQ Tailpasaran Room': (None, None, 0x04, 'GS Token', 0x02, 'Jabu Jabu\'s Belly'),
    'GS Jabu Jabu MQ Invisible Enemies Room': (None, None, 0x08, 'GS Token', 0x02, 'Jabu Jabu\'s Belly'),
    'GS Jabu Jabu MQ Boomerang Room': (None, None, 0x01, 'GS Token', 0x02, 'Jabu Jabu\'s Belly'),
    'GS Jabu Jabu MQ Near Boss': (None, None, 0x02, 'GS Token', 0x02, 'Jabu Jabu\'s Belly'),

    'GS Forest Temple Outdoor East': (None, None, 0x01, 'GS Token', 0x03, 'Forest Temple'),
    'GS Forest Temple First Room': (None, None, 0x02, 'GS Token', 0x03, 'Forest Temple'),
    'GS Forest Temple Outdoor West': (None, None, 0x04, 'GS Token', 0x03, 'Forest Temple'),
    'GS Forest Temple Lobby': (None, None, 0x08, 'GS Token', 0x03, 'Forest Temple'),
    'GS Forest Temple Basement': (None, None, 0x10, 'GS Token', 0x03, 'Forest Temple'),

    'GS Forest Temple MQ First Hallway': (None, None, 0x02, 'GS Token', 0x03, 'Forest Temple'),
    'GS Forest Temple MQ Block Push Room': (None, None, 0x10, 'GS Token', 0x03, 'Forest Temple'),
    'GS Forest Temple MQ Outdoor East': (None, None, 0x01, 'GS Token', 0x03, 'Forest Temple'),
    'GS Forest Temple MQ Outdoor West': (None, None, 0x04, 'GS Token', 0x03, 'Forest Temple'),
    'GS Forest Temple MQ Well': (None, None, 0x08, 'GS Token', 0x03, 'Forest Temple'),

    'GS Fire Temple Song of Time Room': (None, None, 0x01, 'GS Token', 0x04, 'Fire Temple'),
    'GS Fire Temple Basement': (None, None, 0x02, 'GS Token', 0x04, 'Fire Temple'),
    'GS Fire Temple Unmarked Bomb Wall': (None, None, 0x04, 'GS Token', 0x04, 'Fire Temple'),
    'GS Fire Temple East Tower Top': (None, None, 0x08, 'GS Token', 0x04, 'Fire Temple'),
    'GS Fire Temple East Tower Climb': (None, None, 0x10, 'GS Token', 0x04, 'Fire Temple'),

    'GS Fire Temple MQ Above Fire Wall Maze': (None, None, 0x02, 'GS Token', 0x04, 'Fire Temple'),
    'GS Fire Temple MQ Fire Wall Maze Center': (None, None, 0x08, 'GS Token', 0x04, 'Fire Temple'),
    'GS Fire Temple MQ Big Lava Room': (None, None, 0x01, 'GS Token', 0x04, 'Fire Temple'),
    'GS Fire Temple MQ Fire Wall Maze Side Room': (None, None, 0x10, 'GS Token', 0x04, 'Fire Temple'),
    'GS Fire Temple MQ East Tower Top': (None, None, 0x04, 'GS Token', 0x04, 'Fire Temple'),

    'GS Water Temple South Basement': (None, None, 0x01, 'GS Token', 0x05, 'Water Temple'),
    'GS Water Temple Falling Platform Room': (None, None, 0x02, 'GS Token', 0x05, 'Water Temple'),
    'GS Water Temple Central Room': (None, None, 0x04, 'GS Token', 0x05, 'Water Temple'),
    'GS Water Temple Near Boss Key Chest': (None, None, 0x08, 'GS Token', 0x05, 'Water Temple'),
    'GS Water Temple Serpent River': (None, None, 0x10, 'GS Token', 0x05, 'Water Temple'),

    'GS Water Temple MQ Before Upper Water Switch': (None, None, 0x04, 'GS Token', 0x05, 'Water Temple'),
    'GS Water Temple MQ North Basement': (None, None, 0x08, 'GS Token', 0x05, 'Water Temple'),
    'GS Water Temple MQ Lizalfos Hallway': (None, None, 0x01, 'GS Token', 0x05, 'Water Temple'),
    'GS Water Temple MQ Serpent River': (None, None, 0x02, 'GS Token', 0x05, 'Water Temple'),
    'GS Water Temple MQ South Basement': (None, None, 0x10, 'GS Token', 0x05, 'Water Temple'),

    'GS Spirit Temple Hall to West Iron Knuckle': (None, None, 0x01, 'GS Token', 0x06, 'Spirit Temple'),
    'GS Spirit Temple Boulder Room': (None, None, 0x02, 'GS Token', 0x06, 'Spirit Temple'),
    'GS Spirit Temple Lobby': (None, None, 0x04, 'GS Token', 0x06, 'Spirit Temple'),
    'GS Spirit Temple Bomb for Light Room': (None, None, 0x08, 'GS Token', 0x06, 'Spirit Temple'),
    'GS Spirit Temple Metal Fence': (None, None, 0x10, 'GS Token', 0x06, 'Spirit Temple'),

    'GS Spirit Temple MQ Lower Adult Right': (None, None, 0x08, 'GS Token', 0x06, 'Spirit Temple'),
    'GS Spirit Temple MQ Lower Adult Left': (None, None, 0x02, 'GS Token', 0x06, 'Spirit Temple'),
    'GS Spirit Temple MQ Iron Knuckle West': (None, None, 0x04, 'GS Token', 0x06, 'Spirit Temple'),
    'GS Spirit Temple MQ Iron Knuckle North': (None, None, 0x10, 'GS Token', 0x06, 'Spirit Temple'),
    'GS Spirit Temple MQ Sun Block Room': (None, None, 0x01, 'GS Token', 0x06, 'Spirit Temple'),

    'GS Shadow Temple Single Giant Pot': (None, None, 0x01, 'GS Token', 0x07, 'Shadow Temple'),
    'GS Shadow Temple Crusher Room': (None, None, 0x02, 'GS Token', 0x07, 'Shadow Temple'),
    'GS Shadow Temple Tripple Giant Pot': (None, None, 0x04, 'GS Token', 0x07, 'Shadow Temple'),
    'GS Shadow Temple Like Like Room': (None, None, 0x08, 'GS Token', 0x07, 'Shadow Temple'),
    'GS Shadow Temple Near Ship': (None, None, 0x10, 'GS Token', 0x07, 'Shadow Temple'),

    'GS Shadow Temple MQ Crusher Room': (None, None, 0x02, 'GS Token', 0x07, 'Shadow Temple'),
    'GS Shadow Temple MQ Wind Hint Room': (None, None, 0x01, 'GS Token', 0x07, 'Shadow Temple'),
    'GS Shadow Temple MQ After Wind': (None, None, 0x08, 'GS Token', 0x07, 'Shadow Temple'),
    'GS Shadow Temple MQ After Ship': (None, None, 0x10, 'GS Token', 0x07, 'Shadow Temple'),
    'GS Shadow Temple MQ Near Boss': (None, None, 0x04, 'GS Token', 0x07, 'Shadow Temple'),

    'GS Well Like Like Cage': (None, None, 0x01, 'GS Token', 0x08, 'Bottom of the Well'),
    'GS Well East Inner Room': (None, None, 0x02, 'GS Token', 0x08, 'Bottom of the Well'),
    'GS Well West Inner Room': (None, None, 0x04, 'GS Token', 0x08, 'Bottom of the Well'),

    'GS Well MQ Basement': (None, None, 0x01, 'GS Token', 0x08, 'Bottom of the Well'),
    'GS Well MQ Coffin Room': (None, None, 0x04, 'GS Token', 0x08, 'Bottom of the Well'),
    'GS Well MQ West Inner Room': (None, None, 0x02, 'GS Token', 0x08, 'Bottom of the Well'),

    'GS Ice Cavern Push Block Room': (None, None, 0x01, 'GS Token', 0x09, 'Ice Cavern'),
    'GS Ice Cavern Spinning Scythe Room': (None, None, 0x02, 'GS Token', 0x09, 'Ice Cavern'),
    'GS Ice Cavern Heart Piece Room': (None, None, 0x04, 'GS Token', 0x09, 'Ice Cavern'),

    'GS Ice Cavern MQ Scarecrow': (None, None, 0x01, 'GS Token', 0x09, 'Ice Cavern'),
    'GS Ice Cavern MQ Ice Block': (None, None, 0x04, 'GS Token', 0x09, 'Ice Cavern'),
    'GS Ice Cavern MQ Red Ice': (None, None, 0x02, 'GS Token', 0x09, 'Ice Cavern'),

    'GS Hyrule Field Near Gerudo Valley': (None, None, 0x01, 'GS Token', 0x0A, 'Hyrule Field'),
    'GS Hyrule Field near Kakariko': (None, None, 0x02, 'GS Token', 0x0A, 'Hyrule Field'),

    'GS Lon Lon Ranch Back Wall': (None, None, 0x01, 'GS Token', 0x0B, 'Lon Lon Ranch'),
    'GS Lon Lon Ranch Rain Shed': (None, None, 0x02, 'GS Token', 0x0B, 'Lon Lon Ranch'),
    'GS Lon Lon Ranch House Window': (None, None, 0x04, 'GS Token', 0x0B, 'Lon Lon Ranch'),
    'GS Lon Lon Ranch Tree': (None, None, 0x08, 'GS Token', 0x0B, 'Lon Lon Ranch'),

    'GS Kokiri Bean Patch': (None, None, 0x01, 'GS Token', 0x0C, 'Kokiri Forest'),
    'GS Kokiri Know It All House': (None, None, 0x02, 'GS Token', 0x0C, 'Kokiri Forest'),
    'GS Kokiri House of Twins': (None, None, 0x04, 'GS Token', 0x0C, 'Kokiri Forest'),

    'GS Lost Woods Bean Patch Near Bridge': (None, None, 0x01, 'GS Token', 0x0D, 'the Lost Woods'),
    'GS Lost Woods Bean Patch Near Stage': (None, None, 0x02, 'GS Token', 0x0D, 'the Lost Woods'),
    'GS Lost Woods Above Stage': (None, None, 0x04, 'GS Token', 0x0D, 'the Lost Woods'),
    'GS Sacred Forest Meadow': (None, None, 0x08, 'GS Token', 0x0D, 'Sacred Forest Meadow'),

    'GS Outside Ganon\'s Castle': (None, None, 0x01, 'GS Token', 0x0E, 'outside Ganon\'s Castle'),
    'GS Hyrule Castle Grotto': (None, None, 0x02, 'GS Token', 0x0E, 'Hyrule Castle'),
    'GS Hyrule Castle Tree': (None, None, 0x04, 'GS Token', 0x0E, 'Hyrule Castle'),
    'GS Castle Market Guard House': (None, None, 0x08, 'GS Token', 0x0E, 'the Market'),

    'GS Mountain Crater Bean Patch': (None, None, 0x01, 'GS Token', 0x0F, 'Death Mountain Crater'),
    'GS Mountain Trail Bean Patch': (None, None, 0x02, 'GS Token', 0x0F, 'Death Mountain Trail'),
    'GS Mountain Trail Bomb Alcove': (None, None, 0x04, 'GS Token', 0x0F, 'Death Mountain Trail'),
    'GS Mountain Trail Above Dodongo\'s Cavern': (None, None, 0x08, 'GS Token', 0x0F, 'Death Mountain Trail'),
    'GS Mountain Trail Path to Crater': (None, None, 0x10, 'GS Token', 0x0F, 'Death Mountain Trail'),
    'GS Goron City Center Platform': (None, None, 0x20, 'GS Token', 0x0F, 'Goron City'),
    'GS Goron City Boulder Maze': (None, None, 0x40, 'GS Token', 0x0F, 'Goron City'),
    'GS Death Mountain Crater Crate': (None, None, 0x80, 'GS Token', 0x0F, 'Death Mountain Crater'),

    'GS Kakariko House Under Construction': (None, None, 0x08, 'GS Token', 0x10, 'Kakariko Village'),
    'GS Kakariko Skulltula House': (None, None, 0x10, 'GS Token', 0x10, 'Kakariko Village'),
    'GS Kakariko Guard\'s House': (None, None, 0x02, 'GS Token', 0x10, 'Kakariko Village'),
    'GS Kakariko Tree': (None, None, 0x20, 'GS Token', 0x10, 'Kakariko Village'),
    'GS Kakariko Watchtower': (None, None, 0x04, 'GS Token', 0x10, 'Kakariko Village'),
    'GS Kakariko Above Impa\'s House': (None, None, 0x40, 'GS Token', 0x10, 'Kakariko Village'),
    'GS Graveyard Wall': (None, None, 0x80, 'GS Token', 0x10, 'the Graveyard'),
    'GS Graveyard Bean Patch': (None, None, 0x01, 'GS Token', 0x10, 'the Graveyard'),

    'GS Zora River Ladder': (None, None, 0x01, 'GS Token', 0x11, 'Zora River'),
    'GS Zora River Tree': (None, None, 0x02, 'GS Token', 0x11, 'Zora River'),
    'GS Zora\'s Fountain Above the Log': (None, None, 0x04, 'GS Token', 0x11, 'Zora\'s Fountain'),
    'GS Zora River Above Bridge': (None, None, 0x08, 'GS Token', 0x11, 'Zora River'),
    'GS Zora River Near Raised Grottos': (None, None, 0x10, 'GS Token', 0x11, 'Zora River'),
    'GS Zora\'s Fountain Hidden Cave': (None, None, 0x20, 'GS Token', 0x11, 'Zora\'s Fountain'),
    'GS Zora\'s Domain Frozen Waterfall': (None, None, 0x40, 'GS Token', 0x11, 'Zora\'s Domain'),
    'GS Zora\'s Fountain Tree': (None, None, 0x80, 'GS Token', 0x11, 'Zora\'s Fountain'),

    'GS Lake Hylia Bean Patch': (None, None, 0x01, 'GS Token', 0x12, 'Lake Hylia'),
    'GS Lake Hylia Small Island': (None, None, 0x02, 'GS Token', 0x12, 'Lake Hylia'),
    'GS Lake Hylia Lab Wall': (None, None, 0x04, 'GS Token', 0x12, 'Lake Hylia'),
    'GS Lab Underwater Crate': (None, None, 0x08, 'GS Token', 0x12, 'Lake Hylia'),
    'GS Lake Hylia Giant Tree': (None, None, 0x10, 'GS Token', 0x12, 'Lake Hylia'),

    'GS Gerudo Valley Bean Patch': (None, None, 0x01, 'GS Token', 0x13, 'Gerudo Valley'),
    'GS Gerudo Valley Small Bridge': (None, None, 0x02, 'GS Token', 0x13, 'Gerudo Valley'),
    'GS Gerudo Valley Pillar': (None, None, 0x04, 'GS Token', 0x13, 'Gerudo Valley'),
    'GS Gerudo Valley Behind Tent': (None, None, 0x08, 'GS Token', 0x13, 'Gerudo Valley'),

    'GS Gerudo Fortress Archery Range': (None, None, 0x01, 'GS Token', 0x14, 'Gerudo Fortress'),
    'GS Gerudo Fortress Top Floor': (None, None, 0x02, 'GS Token', 0x14, 'Gerudo Fortress'),
    'GS Desert Colossus Bean Patch': (None, None, 0x01, 'GS Token', 0x15, 'Desert Colossus'),
    'GS Wasteland Ruins': (None, None, 0x02, 'GS Token', 0x15, 'Haunted Wasteland'),
    'GS Desert Colossus Hill': (None, None, 0x04, 'GS Token', 0x15, 'Desert Colossus'),
    'GS Desert Colossus Tree': (None, None, 0x08, 'GS Token', 0x15, 'Desert Colossus'),

    'Kokiri Shop Item 1': (shop_address(0, 0), None, 0x30, 'Shop', 0x2D, 'Kokiri Forest'),
    'Kokiri Shop Item 2': (shop_address(0, 1), None, 0x31, 'Shop', 0x2D, 'Kokiri Forest'),
    'Kokiri Shop Item 3': (shop_address(0, 2), None, 0x32, 'Shop', 0x2D, 'Kokiri Forest'),
    'Kokiri Shop Item 4': (shop_address(0, 3), None, 0x33, 'Shop', 0x2D, 'Kokiri Forest'),
    'Kokiri Shop Item 5': (shop_address(0, 4), None, 0x34, 'Shop', 0x2D, 'Kokiri Forest'),
    'Kokiri Shop Item 6': (shop_address(0, 5), None, 0x35, 'Shop', 0x2D, 'Kokiri Forest'),
    'Kokiri Shop Item 7': (shop_address(0, 6), None, 0x36, 'Shop', 0x2D, 'Kokiri Forest'),
    'Kokiri Shop Item 8': (shop_address(0, 7), None, 0x37, 'Shop', 0x2D, 'Kokiri Forest'),
    'Kakariko Potion Shop Item 1': (shop_address(1, 0), None, 0x30, 'Shop', 0x30, 'Kakariko Village'),
    'Kakariko Potion Shop Item 2': (shop_address(1, 1), None, 0x31, 'Shop', 0x30, 'Kakariko Village'),
    'Kakariko Potion Shop Item 3': (shop_address(1, 2), None, 0x32, 'Shop', 0x30, 'Kakariko Village'),
    'Kakariko Potion Shop Item 4': (shop_address(1, 3), None, 0x33, 'Shop', 0x30, 'Kakariko Village'),
    'Kakariko Potion Shop Item 5': (shop_address(1, 4), None, 0x34, 'Shop', 0x30, 'Kakariko Village'),
    'Kakariko Potion Shop Item 6': (shop_address(1, 5), None, 0x35, 'Shop', 0x30, 'Kakariko Village'),
    'Kakariko Potion Shop Item 7': (shop_address(1, 6), None, 0x36, 'Shop', 0x30, 'Kakariko Village'),
    'Kakariko Potion Shop Item 8': (shop_address(1, 7), None, 0x37, 'Shop', 0x30, 'Kakariko Village'),
    'Bombchu Shop Item 1': (shop_address(2, 0), None, 0x30, 'Shop', 0x32, 'the Market'),
    'Bombchu Shop Item 2': (shop_address(2, 1), None, 0x31, 'Shop', 0x32, 'the Market'),
    'Bombchu Shop Item 3': (shop_address(2, 2), None, 0x32, 'Shop', 0x32, 'the Market'),
    'Bombchu Shop Item 4': (shop_address(2, 3), None, 0x33, 'Shop', 0x32, 'the Market'),
    'Bombchu Shop Item 5': (shop_address(2, 4), None, 0x34, 'Shop', 0x32, 'the Market'),
    'Bombchu Shop Item 6': (shop_address(2, 5), None, 0x35, 'Shop', 0x32, 'the Market'),
    'Bombchu Shop Item 7': (shop_address(2, 6), None, 0x36, 'Shop', 0x32, 'the Market'),
    'Bombchu Shop Item 8': (shop_address(2, 7), None, 0x37, 'Shop', 0x32, 'the Market'),
    'Castle Town Potion Shop Item 1': (shop_address(3, 0), None, 0x30, 'Shop', 0x31, 'the Market'),
    'Castle Town Potion Shop Item 2': (shop_address(3, 1), None, 0x31, 'Shop', 0x31, 'the Market'),
    'Castle Town Potion Shop Item 3': (shop_address(3, 2), None, 0x32, 'Shop', 0x31, 'the Market'),
    'Castle Town Potion Shop Item 4': (shop_address(3, 3), None, 0x33, 'Shop', 0x31, 'the Market'),
    'Castle Town Potion Shop Item 5': (shop_address(3, 4), None, 0x34, 'Shop', 0x31, 'the Market'),
    'Castle Town Potion Shop Item 6': (shop_address(3, 5), None, 0x35, 'Shop', 0x31, 'the Market'),
    'Castle Town Potion Shop Item 7': (shop_address(3, 6), None, 0x36, 'Shop', 0x31, 'the Market'),
    'Castle Town Potion Shop Item 8': (shop_address(3, 7), None, 0x37, 'Shop', 0x31, 'the Market'),
    'Castle Town Bazaar Item 1': (shop_address(4, 0), None, 0x30, 'Shop', 0x2C, 'the Market'),
    'Castle Town Bazaar Item 2': (shop_address(4, 1), None, 0x31, 'Shop', 0x2C, 'the Market'),
    'Castle Town Bazaar Item 3': (shop_address(4, 2), None, 0x32, 'Shop', 0x2C, 'the Market'),
    'Castle Town Bazaar Item 4': (shop_address(4, 3), None, 0x33, 'Shop', 0x2C, 'the Market'),
    'Castle Town Bazaar Item 5': (shop_address(4, 4), None, 0x34, 'Shop', 0x2C, 'the Market'),
    'Castle Town Bazaar Item 6': (shop_address(4, 5), None, 0x35, 'Shop', 0x2C, 'the Market'),
    'Castle Town Bazaar Item 7': (shop_address(4, 6), None, 0x36, 'Shop', 0x2C, 'the Market'),
    'Castle Town Bazaar Item 8': (shop_address(4, 7), None, 0x37, 'Shop', 0x2C, 'the Market'),
    'Kakariko Bazaar Item 1': (shop_address(5, 0), None, 0x38, 'Shop', 0x2C, 'Kakariko Village'),
    'Kakariko Bazaar Item 2': (shop_address(5, 1), None, 0x39, 'Shop', 0x2C, 'Kakariko Village'),
    'Kakariko Bazaar Item 3': (shop_address(5, 2), None, 0x3A, 'Shop', 0x2C, 'Kakariko Village'),
    'Kakariko Bazaar Item 4': (shop_address(5, 3), None, 0x3B, 'Shop', 0x2C, 'Kakariko Village'),
    'Kakariko Bazaar Item 5': (shop_address(5, 4), None, 0x3D, 'Shop', 0x2C, 'Kakariko Village'),
    'Kakariko Bazaar Item 6': (shop_address(5, 5), None, 0x3E, 'Shop', 0x2C, 'Kakariko Village'),
    'Kakariko Bazaar Item 7': (shop_address(5, 6), None, 0x3F, 'Shop', 0x2C, 'Kakariko Village'),
    'Kakariko Bazaar Item 8': (shop_address(5, 7), None, 0x40, 'Shop', 0x2C, 'Kakariko Village'),
    'Zora Shop Item 1': (shop_address(7, 0), None, 0x30, 'Shop', 0x2F, 'Zora\'s Domain'),
    'Zora Shop Item 2': (shop_address(7, 1), None, 0x31, 'Shop', 0x2F, 'Zora\'s Domain'),
    'Zora Shop Item 3': (shop_address(7, 2), None, 0x32, 'Shop', 0x2F, 'Zora\'s Domain'),
    'Zora Shop Item 4': (shop_address(7, 3), None, 0x33, 'Shop', 0x2F, 'Zora\'s Domain'),
    'Zora Shop Item 5': (shop_address(7, 4), None, 0x34, 'Shop', 0x2F, 'Zora\'s Domain'),
    'Zora Shop Item 6': (shop_address(7, 5), None, 0x35, 'Shop', 0x2F, 'Zora\'s Domain'),
    'Zora Shop Item 7': (shop_address(7, 6), None, 0x36, 'Shop', 0x2F, 'Zora\'s Domain'),
    'Zora Shop Item 8': (shop_address(7, 7), None, 0x37, 'Shop', 0x2F, 'Zora\'s Domain'),
    'Goron Shop Item 1': (shop_address(8, 0), None, 0x30, 'Shop', 0x2E, 'Goron City'),
    'Goron Shop Item 2': (shop_address(8, 1), None, 0x31, 'Shop', 0x2E, 'Goron City'),
    'Goron Shop Item 3': (shop_address(8, 2), None, 0x32, 'Shop', 0x2E, 'Goron City'),
    'Goron Shop Item 4': (shop_address(8, 3), None, 0x33, 'Shop', 0x2E, 'Goron City'),
    'Goron Shop Item 5': (shop_address(8, 4), None, 0x34, 'Shop', 0x2E, 'Goron City'),
    'Goron Shop Item 6': (shop_address(8, 5), None, 0x35, 'Shop', 0x2E, 'Goron City'),
    'Goron Shop Item 7': (shop_address(8, 6), None, 0x36, 'Shop', 0x2E, 'Goron City'),
    'Goron Shop Item 8': (shop_address(8, 7), None, 0x37, 'Shop', 0x2E, 'Goron City'),

    'DC Deku Scrub Deku Nuts': (None, None, 0x30, 'NPC', 0x01, 'Dodongo\'s Cavern'), 
    'DC Deku Scrub Deku Sticks': (None, None, 0x31, 'NPC', 0x01, 'Dodongo\'s Cavern'), 
    'DC Deku Scrub Deku Seeds': (None, None, 0x33, 'NPC', 0x01, 'Dodongo\'s Cavern'), 
    'DC Deku Scrub Deku Shield': (None, None, 0x34, 'NPC', 0x01, 'Dodongo\'s Cavern'), 
    'Jabu Deku Scrub Deku Nuts': (None, None, 0x30, 'NPC', 0x02, 'Jabu Jabu\'s Belly'), 
    'GC Deku Scrub Bombs': (None, None, 0x37, 'NPC', 0x0D, 'Ganon\'s Castle'), 
    'GC Deku Scrub Arrows': (None, None, 0x33, 'NPC', 0x0D, 'Ganon\'s Castle'), 
    'GC Deku Scrub Red Potion': (None, None, 0x39, 'NPC', 0x0D, 'Ganon\'s Castle'), 
    'GC Deku Scrub Green Potion': (None, None, 0x3A, 'NPC', 0x0D, 'Ganon\'s Castle'), 

    'DT MQ Deku Scrub Deku Shield': (None, None, 0x34, 'NPC', 0x00, 'Deku Tree'), 
    'DC MQ Deku Scrub Deku Sticks': (None, None, 0x31, 'NPC', 0x01, 'Dodongo\'s Cavern'), 
    'DC MQ Deku Scrub Deku Seeds': (None, None, 0x33, 'NPC', 0x01, 'Dodongo\'s Cavern'), 
    'DC MQ Deku Scrub Deku Shield': (None, None, 0x34, 'NPC', 0x01, 'Dodongo\'s Cavern'), 
    'DC MQ Deku Scrub Red Potion': (None, None, 0x39, 'NPC', 0x01, 'Dodongo\'s Cavern'), 
    'GC MQ Deku Scrub Deku Nuts': (None, None, 0x30, 'NPC', 0x0D, 'Ganon\'s Castle'), 
    'GC MQ Deku Scrub Bombs': (None, None, 0x37, 'NPC', 0x0D, 'Ganon\'s Castle'), 
    'GC MQ Deku Scrub Arrows': (None, None, 0x33, 'NPC', 0x0D, 'Ganon\'s Castle'), 
    'GC MQ Deku Scrub Red Potion': (None, None, 0x39, 'NPC', 0x0D, 'Ganon\'s Castle'), 
    'GC MQ Deku Scrub Green Potion': (None, None, 0x3A, 'NPC', 0x0D, 'Ganon\'s Castle'), 

    'HF Grotto Deku Scrub Piece of Heart': (None, None, 0x3E, 'GrottoNPC', 0x01, 'Hyrule Field'), 
    'ZR Grotto Deku Scrub Red Potion': (None, None, 0x39, 'GrottoNPC', 0x02, 'Zora\'s River'), 
    'ZR Grotto Deku Scrub Green Potion': (None, None, 0x3A, 'GrottoNPC', 0x02, 'Zora\'s River'),
    'SFM Grotto Deku Scrub Red Potion': (None, None, 0x39, 'GrottoNPC', 0x03, 'Sacred Forest Meadow'), 
    'SFM Grotto Deku Scrub Green Potion': (None, None, 0x3A, 'GrottoNPC', 0x03, 'Sacred Forest Meadow'),
    'LH Grotto Deku Scrub Deku Nuts': (None, None, 0x30, 'GrottoNPC', 0x04, 'Lake Hylia'), 
    'LH Grotto Deku Scrub Bombs': (None, None, 0x37, 'GrottoNPC', 0x04, 'Lake Hylia'), 
    'LH Grotto Deku Scrub Arrows': (None, None, 0x33, 'GrottoNPC', 0x04, 'Lake Hylia'), 
    'Valley Grotto Deku Scrub Red Potion': (None, None, 0x39, 'GrottoNPC', 0x05, 'Gerudo Valley'), 
    'Valley Grotto Deku Scrub Green Potion': (None, None, 0x3A, 'GrottoNPC', 0x05, 'Gerudo Valley'),
    'LW Deku Scrub Deku Nuts': (None, None, 0x30, 'NPC', 0x5B, 'Lost Woods'), 
    'LW Deku Scrub Deku Sticks': (None, None, 0x31, 'NPC', 0x5B, 'Lost Woods'), 
    'LW Deku Scrub Deku Stick Upgrade': (None, None, 0x77, 'NPC', 0x5B, 'Lost Woods'), 
    'LW Grotto Deku Scrub Arrows': (None, None, 0x33, 'GrottoNPC', 0x06, 'Lost Woods'), 
    'LW Grotto Deku Scrub Deku Nut Upgrade': (None, None, 0x79, 'GrottoNPC', 0x06, 'Lost Woods'), 
    'Desert Grotto Deku Scrub Red Potion': (None, None, 0x39, 'GrottoNPC', 0x07, 'Desert Colossus'), 
    'Desert Grotto Deku Scrub Green Potion': (None, None, 0x3A, 'GrottoNPC', 0x07, 'Desert Colossus'), 
    'DMC Deku Scrub Bombs': (None, None, 0x37, 'NPC', 0x61, 'Death Mountain Crater'), 
    'DMC Grotto Deku Scrub Deku Nuts': (None, None, 0x30, 'GrottoNPC', 0x08, 'Death Mountain Crater'), 
    'DMC Grotto Deku Scrub Bombs': (None, None, 0x37, 'GrottoNPC', 0x08, 'Death Mountain Crater'), 
    'DMC Grotto Deku Scrub Arrows': (None, None, 0x33, 'GrottoNPC', 0x08, 'Death Mountain Crater'),
    'Goron Grotto Deku Scrub Deku Nuts': (None, None, 0x30, 'GrottoNPC', 0x09, 'Goron City'), 
    'Goron Grotto Deku Scrub Bombs': (None, None, 0x37, 'GrottoNPC', 0x09, 'Goron City'), 
    'Goron Grotto Deku Scrub Arrows': (None, None, 0x33, 'GrottoNPC', 0x09, 'Goron City'), 
    'LLR Grotto Deku Scrub Deku Nuts': (None, None, 0x30, 'GrottoNPC', 0x0A, 'Lon Lon Ranch'), 
    'LLR Grotto Deku Scrub Bombs': (None, None, 0x37, 'GrottoNPC', 0x0A, 'Lon Lon Ranch'), 
    'LLR Grotto Deku Scrub Arrows': (None, None, 0x33, 'GrottoNPC', 0x0A, 'Lon Lon Ranch'), 
}
