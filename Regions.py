import collections
from BaseClasses import Region, Location, Entrance, RegionType, Dungeon
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
       [],
       ItemFactory('Boss Key (Woodfall Temple)'),
       ItemFactory(['Small Key (Woodfall Temple)'] * 1),
       ItemFactory(['Map (Woodfall Temple)', 'Compass (Woodfall Temple)']))

    SH = make_dungeon(
        'Snowhead Temple',
        [],
        ItemFactory('Boss Key (Snowhead Temple)'),
        ItemFactory(['Small Key (Snowhead Temple)'] * 3),
        ItemFactory(['Map (Snowhead Temple)', 'Compass (Snowhead Temple)']))

    GB = make_dungeon(
        'Great Bay Temple',
        [],
        ItemFactory('Boss Key (Great Bay Temple)'),
        ItemFactory(['Small Key (Great Bay Temple)'] * 1),
        ItemFactory(['Map (Great Bay Temple)', 'Compass (Great Bay Temple)']))

    ST = make_dungeon(
        'Stone Tower Temple',
        [],
        ItemFactory('Boss Key (Stone Tower Temple)'),
        ItemFactory(['Small Key (Stone Tower Temple)'] * 2),
        ItemFactory(['Map (Stone Tower Temple)', 'Compass (Stone Tower Temple)']))

    world.dungeons = [WF, SH, GB, ST]


def create_regions(world):
    # TODO: finish out this whole thing (what I'm currently working on)
    world.regions = [
        create_ow_region('Beginning', ['First Nut'], ['Cursed Underground']),
        create_interior_region('Deku Flower Tutorial Area', [], ['Clock Tower Twisted Hallway']),
        create_interior_region('Clock Tower Basement',
            ['Item From HMS',
            # 'Defeat Odolwa', 'Defeat Goht', 'Defeat Gyorg', 'Defeat Twinmold',
            # 'Odolwas Remains', 'Gohts Remains', 'Gyorgs Remains', 'Twinmolds Remains',
            'Song From HMS'],
            ['Clock Tower Exit', 'Clock Tower Twisted Hallway Backwards']),

        create_ow_region('South Clock Town',
            ['SCT 20 Rupee Chest', 'Festival Tower Rupee Chest',
            'Clock Town Owl Statue', 'Clock Tower Platform HP', 'Clock Town Business Scrub Item', 'Clock Town Business Scrub Trade Done'],
            ['To Clock Tower Basement', 'To Clock Tower Rooftop', 'South Mailbox',
            'SCT Top Exit to WCT', 'SCT Bottom Exit to WCT', 'SCT Exit to NCT',
            'SCT Bottom Exit to ECT', 'SCT Top Exit to ECT',
            'Clock Town South Gate', 'SCT Exit to Laundry Pool']),
        create_interior_region('Clock Tower Rooftop', ['Dropped Ocarina', 'Song From Skull Kid'], ['End of First Cycle', 'Moon Portal']),

        create_ow_region('East Clock Town',
            ['ECT 100 Rupee Chest', 'Deliver Letter to Mama To Postman'],
            ['To Honey and Darling', 'To Treasure Chest Shop', 'To Town Shooting Gallery', 'East Mailbox',
            'To Milk Bar', 'To Stock Pot Inn', 'To Stock Pot Inn Secret Entrance', 'To Mayors Office',
            'Bomber Bouncer', 'ECT Top Exit to SCT', 'ECT Bottom Exit to SCT',
            'ECT Exit to NCT', 'Clock Town East Gate']),
        create_interior_region('Honey and Darling',
            ['Honey and Darling Bombchu Bowling Prize', 'Honey and Darling Archery Prize',
            'Honey and Darling Basket Bomb Throw Prize', 'Honey and Darling Grand Champion'],
            ['Honey and Darling Exit']),
        create_interior_region('Treasure Chest Shop',
            ['Treasure Chest Game Goron Prize', 'Treasure Chest Game Human Prize',
             'Treasure Chest Game Zora Prize', 'Treasure Chest Game Deku Prize'], ['Treasure Chest Shop Exit']),
        create_interior_region('Town Shooting Gallery', ['Town Shooting Gallery Quiver Prize', 'Town Shooting Gallery HP Prize'], ['Town Shooting Gallery Exit']),
        create_interior_region('Milk Bar', ['Milk Bar Performance', 'Delivery to Mama Kafei'], ['Milk Bar Exit']),
        create_interior_region('Stock Pot Inn',
            ['Stock Pot Inn Key', 'Have you seen this man?',
            'Grandma Stories HP 1', 'Grandma Stories HP 2',
            'Toilet Hand HP', 'Your Room Rupee Chest', 'Anjus Room Rupee Chest',
            'We Shall Greet The Morning Together'],
            ['Stock Pot Inn Roof Exit', 'Stock Pot Inn Front Door']),
        create_interior_region('Mayors Office', ['Expert Person Solver Takes the Case', 'Mayor HP'], ['Mayors Office Exit']),
        create_interior_region('Bomber Tunnel', ['Bomber Tunnel Chest'], ['Bomber Tunnel Exit', 'Tunnel Balloon From ECT']),
        create_interior_region('Astral Observatory', ['Moon Cry', 'Watch Business Scrub Fly'], ['Tunnel Balloon From Observatory', 'Astral Observatory Exit']),
        create_ow_region('Astral Observatory Deck', ['Moons Tear'], ['Observatory Deck to Inside', 'Astral Observatory Fence']),

        create_ow_region('West Clock Town',
            ['Bank 200 Rupee Prize', 'Bank HP', 'Rosa Sisters HP',
            'Hidden Owl Statue', 'Deliver Letter to Mama To Postman'],
            ['To Curiosity Shop', 'To Trading Post', 'To Bomb Shop',
            'To Post Office', 'To Lottery Shop', 'To Swordsmans School',
             'Clock Town West Gate', 'WCT Top Exit to SCT', 'WCT Bottom Exit to SCT']),
        create_ow_region('Mailbox', ['Deliver Letter to Kafei', 'Clock Town Mailbox HP']),
        create_interior_region('Curiosity Shop', ['Buy All Night Mask', 'Buy Bigger Bomb Bag'], ['Curiosity Shop Exit']),
        create_interior_region('Trading Post', [], ['Trading Post Exit']),
        create_interior_region('Bomb Shop', ['Buy Bomb Bag', 'Buy Bigger Bomb Bag'], ['Bomb Shop Exit']),
        create_interior_region('Post Office', ['Deliver Letter to Mama To Postman', 'Counting Is Hard'], ['Post Office Exit']),
        create_interior_region('Lottery Shop', [], ['Lottery Shop Exit']),
        create_interior_region('Swordsmans School', ['Sword School HP'], ['Swordsmans School Exit']),

        create_ow_region('North Clock Town',
            ['Bomber Notebook', 'Bomber Code', 'NCT Tree HP', 'Clock Town Tingle Clock Town Map',
            'Clock Town Tingle Woodfall Map', 'Foil Sakon', 'NCT Keaton HP', 'Clock Town Tingle Pic'],
            ['To GF Clock Town', 'To Deku Playground', 'Clock Town North Gate',
            'NCT Exit to SCT', 'NCT Exit to ECT', 'North Mailbox']),
        # TODO: Don't know how to handle the clock town stray fairy right now
        # I think for now, we could just place checks on the fairy herself
        # But later we'll have Stray Fairy Pickups in the pool
        create_interior_region('Clock Town Fairy Shrine', ['Clock Town GF Magic Bar', 'Clock Town GF Mask'], ['Clock Town Fairy Shrine Exit']),
        create_interior_region('Deku Playground', ['Deku Challenge Day 1', 'Deku Challenge Day 2', 'Deku Challenge Day 3', 'Deku Playground HP'], ['Deku Playground Exit']),

        create_ow_region('Laundry Pool',
            ['Don Gero Town Frog', 'Listen To Guru Guru'],
            ['Curiosity Backroom Entrance', 'Laundry Pool Exit to SCT']),
        create_interior_region('Curiosity Shop Backroom', ['Keaton Mask From Kafei', 'Letter From Kafei', 'Pendant From Kafei'], ['Clock Town']),

        create_ow_region('Termina Field',
            ['Learn Kamaro Dance', 'TF Chest In The Grass', 'TF Chest On A Stump'],
            ['TF To Swamp', 'South Gate To Clock Town',
            'TF Mountain Icicles', 'North Gate To Clock Town',
            'TF Great Bay Gate', 'West Gate To Clock Town',
            'TF To Ikana', 'East Gate To Clock Town', 'TF To Obs Over Fence Maybe',
            'To TF Peahat Grotto', 'To TF Beehive Grotto', 'To East Pillar Grotto', 'To TF Business Scrub Grotto',
            'To Swamp Gossips', 'To Mountain Gossips', 'To Ocean Gossips',
            'To Canyon Gossips', 'To Dodongo Grotto', 'To TF Deku Baba Pit', 'TF To Milk Road']),
        create_grotto_region('TF Peahat Grotto', ['TF Peahat Grotto HP'], ['TF Peahat Grotto Exit']),
        create_grotto_region('TF Beehive Grotto', ['TF Beehive Grotto HP'], ['TF Beehive Grotto Exit']),
        create_grotto_region('TF East Pillar Grotto', ['TF East Pillar Bombchu Pit Chest'], ['TF East Pillar Grotto Exit']),
        create_grotto_region('TF Business Scrub Grotto', ['TF Business Scrub Grotto HP'], ['TF Business Scrub Grotto Exit']),
        create_grotto_region('Swamp Gossips', ['Swamp Gossip Check', '4 Gossip Stone HP'], ['Swamp Gossips Exit']),
        create_grotto_region('Mountain Gossips', ['Mountain Gossip Check', '4 Gossip Stone HP'], ['Mountain Gossips Exit']),
        create_grotto_region('Oceans Gossips', ['Ocean Gossip Check', '4 Gossip Stone HP'], ['Oceans Gossips Exit']),
        create_grotto_region('Canyon Gossips', ['Canyon Gossip Check', '4 Gossip Stone HP'], ['Canyon Gossips Exit']),
        create_grotto_region('TF Dodongo Grotto', ['TF Dodongo Grotto HP'], ['TF Dodongo Grotto Exit']),
        create_grotto_region('TF Deku Baba Pit', ['TF Deku Baba Pit Chest'], ['TF Deku Baba Pit Exit']),

        create_ow_region('Swamp Path', ['Swamp Path Bat Tree HP', 'Swamp Tingle Woodfall Map', 'Swamp Tingle Snowhead Map', 'Swamp Tingle Pic'],
                         ['Swamp Path To Termina Field', 'To Swamp Shooting Gallery',
                          'Swamp Path To Southern Swamp (Poisoned)', 'Swamp Path To Southern Swamp (Cleaned)',
                          'To Swamp Path Rupee Pit']),
        create_grotto_region('Swamp Path Rupee Pit', ['Swamp Path Rupee Pit Chest'], ['Swamp Path Rupee Pit Exit']),
        create_interior_region('Swamp Shooting Gallery', ['Swamp Shooting Gallery Quiver Prize', 'Swamp Shooting Gallery HP Prize'], ['Swamp Shooting Gallery Exit']),

        create_ow_region('Swamp Tourist Region (Poisoned)', ['Swamp Tourist Roof HP', 'Swamp Owl Statue', 'Kill Swamp Big Octo'],
                         ['Poisoned Tourist Region To Swamp Path', 'Swamp Big Octo From Tourist Region',
                          'Poisoned To Swamp Tourist Centre', 'Poisoned To Potion Shop', 'Poisoned To Lost Woods']),
        create_interior_region('Swamp Tourist Centre', ['Swamp Tourist Free Product (?)', 'Pictograph Contest Winner',
                                'Picto Box', 'Kill Swamp Big Octo With Boat', 'Swamp Boat Archery HP'], ['Swamp Boat Ride',
                                'Tourist Centre Poison Exit', 'Tourist Centre Clean Exit']),
        create_interior_region('Swamp Potion Shop', ['Red Potion To Help Koume'], ['Swamp Potion Shop Poison Exit',
                                                                                   'Swamp Potion Shop Clean Exit']),
        create_ow_region('Lost Woods', ['Checked Koume', 'Saved Koume'], ['Lost Woods Exit', 'But like, a LOT of them']),
        # oh jeez, we have to have an exit here for every exit in lost woods don't we? lol
        # also not actually sure if lost woods should be ow or interior
        # oh god and there are 3 maps for this huh? -__-
        create_ow_region('Swamp Octo Region Lower (Poisoned)', ['Kill Swamp Big Octo From Palace'],
                         ['Swamp Big Octo From Octo Region', 'Octo Region to Deku Palace',
                          'Poisoned To Swamp Spider House', 'Poisoned Lower Octo Region Trick To Upper Midpoint', 'Poisoned To Octo Region Grotto']),
        create_grotto_region('Octo Region Grotto', ['Octo Grotto 20 Rupee Chest'], ['Octo Grotto Clean Exit', 'Octo Grotto Poison Exit']),
        create_interior_region('Swamp Spider House', ['spiders', 'so many spiders', 'Swamp Spider House Reward'], ['Swamp Spider House Clean Exit', 'Swamp Spider House Poison Exit']),
        # a note about this poisoned region, while in the previous section of the swamp any form could get around, now
        # only deku can get around without needing health due to the poisoned water, so to deal with that, do with put
        # a heart requirement on the entrance to here? split it up into logical regions requiring health?
        # things to ponder

        create_ow_region('Swamp Deku Palace Outer Region (Poisoned)', [], ['Poisoned Outer Palace To Lower Octo',
                        'Poisoned Outer Palace To Octo Upper', 'Poisoned Outer Palace To Lower Courtyard', 'Poisoned Palace To Butler Race',
                        'Poisoned Outer Palace To Upper Courtyard']),
        create_interior_region('Butler Race', ['Butler Race Prize'], ['Butler Race Clean Exit', 'Butler Race Poison Exit']),

        create_ow_region('Swamp Deku Palace Lower Courtyard (Poisoned)', ['Deku Palace Courtyard HP'], ['Poisoned Deku Palace Lower Courtyard To Outer Region',
            'Poisoned Deku Palace Lower Courtyard To Main Throne Room', 'Poisoned To Magic Beans', 'Poisoned Deku Palace Lower Courtyard To Upper']),
        create_grotto_region('Magic Bean Grotto', ['Magic Beans'], ['Magic Bean Grotto Clean Exit', 'Magic Bean Grotto Poison Exit']),

        create_ow_region('Swamp Deku Palace Upper Courtyard (Poisoned)', [], ['Poisoned Deku Palace Upper Courtyard To Lower',
            'Poisoned Deku Palace Upper Courtyard To Outer Region', 'Poisoned Deku Palace Upper Courtyard To Throne Room Cage Region']),
        create_interior_region('Swamp Deku Palace Throne Room', ['Return Deku Princess'], ['Swamp Deku Palace Throne Room Clean Exit', 'Swamp Deku Palace Throne Room Poison Exit']),
        create_interior_region('Swamp Deku Palace Cage Room', ['Song From Monkey'], ['Swamp Deku Palace Cage Room Clean Exit', 'Swamp Deku Palace Cage Room Poison Exit']),
        # the throne room, is that actually a different map for poisoned vs clean water? todo: find out

        create_ow_region('Swamp Octo Region Upper Near Palace (Poisoned)', [], ['Poisoned Octo Upper Near Palace To Lower',
                                    'Poisoned Octo Upper To Deku Palace', 'Poisoned Octo Upper Near Palace To Midpoint']),
        create_ow_region('Swamp Octo Region Upper Midpoint (Poisoned)', [], ['Poisoned Octo Upper Midpoint To Near Palace',
                                    'Poisoned Octo Upper Midpoint To Lower', 'Poisoned Octo Upper Midpoint To Kaepora']),
        create_ow_region('Swamp Octo Kaepora Region (Poisoned)', ['Song From Kaepora Gaebora'], ['Poisoned Octo Kaepora To Lower',
                                    'Poisoned Octo Kaepora To Midpoint', 'Poisoned Octo Kaepora To Woodfall']),

        create_ow_region('Outside Woodfall Entrance Region (Poisoned)', ['Outside Woodfall 20 Rupee Chest'],
                         ['Poisoned Outside Woodfall Entrance To Woodfall Owl Platform', 'Poisoned Outside Woodfall Entrance To Fountain Platform']),
        create_ow_region('Woodfall Owl Platform (Poisoned)', ['Outside Woodfall 5 Rupee Chest', 'Woodfall Owl Statue (Poisoned)'],
                         ['Poisoned Owl Platform To Entrance', 'Poisoned Owl Platform To Fountain Platform', 'Poisoned Owl Platform To Temple Platform']),
        create_ow_region('Outside Woodfall Temple Platform (Poisoned)', [], ['Poisoned Woodfall Temple Platform To Owl Platform',
                        'Poisoned Woodfall Temple Platform To Entrance', 'Poisoned Woodfall Temple Platform Into Temple']),
        create_ow_region('Outside Woodfall Fairy Fountain Platform (Poisoned)', ['Outside Woodfall HP'],
                         ['Poisoned Fountain Platform To Owl Platform', 'Poisoned Fountain Platform To Entrance', 'Poisoned Fountain Platform To Fountain']),
        create_interior_region('Woodfall Fairy Shrine', ['Woodfall GF Reward'], ['Woodfall Fountain Clean Exit', 'Woodfall Fountain Poison Exit']),

        # create_ow_region('Boat Ride', [], ['Poison Swamp']),
        # should this actually be its own region? idek
        # ugh maybe it should, it might have loading zones or smth ugh

        # also todo: figure out what the actual loading zones are because I'm about to create an unholy mess of logical regions - RO
        create_dungeon_region('WF Entrance Room (Poisoned)', ['WF Stray Fairy Entrance', 'WF Stray Fairy Lobby Chest'],
                              ['WF Poisoned Front Exit', 'WF Poisoned Entrance To Central Room', 'WF Boss Warp']),
        # actually dunno if this room needs poisoned/clean versions, but I'll just leave it like this for now

        create_dungeon_region('WF Central Room SW Region (Poisoned)', ['WF Stray Fairy Poisoned Central Room Deku Baba',
                    'WF Clean Poison Water Using Fire Arrows', 'WF Poisoned Central Room Gate Torch Using Fire Arrows'],
                      ['WF Poisoned Central Room SW To Entrance Room', 'WF Poisoned Central Room SW To Push Block Room',
                       'WF Poisoned Central Room SW To Fairy Platform', 'WF Poisoned Central Room SW To Upper',
                       'WF Clean Poison Water Using Fire Arrows Exit', 'WF Poisoned Central Room SW To Fairy Region']),
        create_dungeon_region('WF Central Room Fairy Platform (Poisoned)', ['WF Stray Fairy Poisoned Central Room SE Corner'],
                      ['WF Poisoned Central Room Fairy Platform To SW', 'WF Poisoned Central Room Fairy Platform To East',
                       'WF Poisoned Central Room Fairy Platform To Upper']),
        create_dungeon_region('WF Central Room East Region (Poisoned)', [], ['WF Poisoned Central Room East To Fairy Platform',
                        'WF Poisoned Central Room East To Upper', 'WF Poisoned Central Room East To Ladder Up',
                        'WF Poisoned Central Room East To Elevator Room']),
        create_dungeon_region('WF Central Room Upper Region (Poisoned)', ['WF Stray Fairy Poisoned Central Room Upper Switch Chest',
                                            'WF Poisoned Central Room Ladder Switch', 'WF Clean Poison Water'],
                        ['WF Poisoned Central Room Upper To Pre Boss Room', 'WF Poisoned Central Room Upper To Dragonfly Room',
                         'WF Poisoned Central Room Upper To Elevator Room', 'WF Poisoned Central Room Upper To Fairy Platform',
                         'WF Poisoned Central Room Upper To East', 'WF Poisoned Central Room Upper To SW', 'WF Clean Poison Water Exit',
                         'WF Poisoned Central Room Upper To Fairy Region']),
        create_dungeon_region('WF Central Room Upper Bubble Fairy Region', ['WF Stray Fairy Central Room Upper Bubble'], []),

        create_dungeon_region('WF Elevator Room West Lower (Poisoned)', ['WF Activate Elevator From Poisoned West Lower'],
                              ['WF Poisoned Elevator Room West Lower To Fairy Region', 'WF Poisoned Elevator Room West Lower To North Upper',
                               'WF Poisoned Elevator Room West Lower To SW Upper', 'WF Poisoned Elevator Room West Lower To East Lower',
                               'WF Poisoned Elevator Room West Lower To Key Chest', 'WF Poisoned Elevator Room West Lower To Central Room']),
        create_dungeon_region('WF Elevator Room East Lower (Poisoned)', ['WF Activate Elevator From Poisoned East Lower'], ['WF Poisoned Elevator Room East Lower To Map Room',
                                'WF Poisoned Elevator Room East Lower To West Lower']),
        create_dungeon_region('WF Elevator Room Key Chest Region (Poisoned)', ['WF Poisoned Elevator Room Key Chest'], []),
        create_dungeon_region('WF Elevator Room North Upper (Poisoned)', [], ['WF Poisoned Elevator Room North Upper To West Lower',
                        'WF Poisoned Elevator Room North Upper To East Lower', 'WF Poisoned Elevator Room North Upper To Key Chest',
                        'WF Poisoned Elevator Room North Upper To Fairy Region']),
        create_dungeon_region('WF Elevator Room SW Upper (Poisoned)', [], ['WF Poisoned Elevator Room SW Upper To Central Room',
                        'WF Poisoned Elevator Room SW Upper To Bow Room', 'WF Poisoned Elevator Room SW Upper To West Lower',
                        'WF Poisoned Elevator Room SW Upper To East Lower']),
        create_dungeon_region('WF Elevator Room Stray Fairy Region', ['WF Stray Fairy Elevator Room'], []),

        create_dungeon_region('WF Map Room (Poisoned)', [], ['WF Poisoned Map Room Exit', 'WF Poisoned Map Room To Chest']),
        create_dungeon_region('WF Map Room (Cleaned)', [], ['WF Cleaned Map Room Exit', 'WF Cleaned Map Room To Chest']),
        create_dungeon_region('WF Map Room Chest Region', ['WF Map Chest'], []),
        # I don't know if this room actually has poisoned/clean versions, todo: check loading zones
        # in general, it's not too hard to switch between the two
        # split rooms are like this, two regions each with their own exit, no need to set a rule
        # single rooms have two exits, one of which needs a rule

        create_dungeon_region('WF Push Block Room Lower (Poisoned)', ['WF Stray Fairy Poisoned Push Block Room Hive', 'WF Stray Fairy Poisoned Push Block Room Skulltula'],
                              ['WF Poisoned Push Block Room Lower To Central Room', 'WF Poisoned Push Block Room Lower To Compass Room',
                               'WF Poisoned Push Block Room Lower To Upper', 'WF Poisoned Push Block Room Lower To Fairy Region']),
        create_dungeon_region('WF Push Block Room Top Region (Poisoned)', [], ['WF Poisoned Push Block Room Upper To Dark Puffs', 'WF Poisoned Push Block Room Upper To Lower']),
        create_dungeon_region('WF Push Block Room Fairy Region', ['WF Stray Fairy Push Block Room Underwater'], []),

        create_dungeon_region('WF Compass Room', ['WF Compass Chest'], ['WF Compass Room Clean Exit', 'WF Compass Room Poison Exit']),

        create_dungeon_region('WF Dark Puff Gauntlet', ['WF Stray Fairy Dark Puffs'],
                              ['WF Dark Puff Gauntlet To Push Block Room', 'WF Dark Puff Gauntlet To Dragonfly Room']),

        create_dungeon_region('WF Dragonfly Room West', [], ['WF Dragonfly Room NE To Dark Puffs', 'WF Dragonfly Room West To NE',
                                'WF Dragonfly Room West To Central Room SW', 'WF Dragonfly Room West To Central Room East',
                                'WF Dragonfly Room West To Central Room Fairy Platform']),
        # the falling through the floor spots aren't loading zones, are they? if not, there needs to be cleaned/poisoned
        # rooms here; if so, there need to be cleaned/poisoned exits
        create_dungeon_region('WF Dragonfly Room NE', [], ['WF Dragonfly Room NE To West', 'WF Dragonfly Room NE To Central Room']),

        create_dungeon_region('WF Bow Room', ['WF Bow Chest'], ['WF Bow Room Clean Exit', 'WF Bow Room Poison Exit']),
        # I'm assuming here that this room doesn't have different versions, so it has 2 exits to poisoned/cleaned

        create_dungeon_region('WF Boss Key Room', ['WF Boss Key Chest', 'WF Don Gero Frog'], ['WF Boss Key Room Clean Exit', 'WF Boss Key Room Poison Exit']),

        create_dungeon_region('WF Pre Boss Room South', [], ['WF Pre Boss Room South To Central Room', 'WF Pre Boss Room South To Fairy 1',
                                'WF Pre Boss Room South To Fairy 2', 'WF Pre Boss Room South To Fairy 3', 'WF Pre Boss Room South To Bubble Fairy',
                                'WF Pre Boss Room South To North']),
        create_dungeon_region('WF Pre Boss Room North', [], ['WF Pre Boss Room North To Boss Chamber', 'WF Pre Boss Room North To Fairy 1',
                                'WF Pre Boss Room North To Fairy 2', 'WF Pre Boss Room North To Fairy 3', 'WF Pre Boss Room North To Bubble Fairy',
                                'WF Pre Boss Room North To South']),
        create_dungeon_region('WF Stray Fairy Pre Boss Room Alcoves 1 Fairy Region', ['WF Stray Fairy Pre Boss Room Alcoves 1'], []),
        create_dungeon_region('WF Stray Fairy Pre Boss Room Alcoves 2 Fairy Region', ['WF Stray Fairy Pre Boss Room Alcoves 2'], []),
        create_dungeon_region('WF Stray Fairy Pre Boss Room Alcoves 3 Fairy Region', ['WF Stray Fairy Pre Boss Room Alcoves 3'], []),
        create_dungeon_region('WF Stray Fairy Pre Boss Room Bubble Fairy Region', ['WF Stray Fairy Pre Boss Room Bubble'], []),

        create_dungeon_region('WF Boss Room', ['Defeat Odolwa', 'Odolwa HC'], ['WF Odolwa Boss Exit']),

        create_interior_region('Post Odolwa Giants Region', ['Song From Giants', 'Odolwas Remains'], ['Post Odolwa Exit']),
        # so I'm not fully sure if this is how it works, but I don't know how else to do it, so I'll leave it like this
        # for now; the post odolwa exit will lead to the princess room

        create_dungeon_region('WF Princess Room', ['Deku Princess'], ['WF Princess Exit']),

        # Cleaned Rooms
        create_dungeon_region('WF Central Room SW Region (Cleaned)', ['WF Stray Fairy Cleaned Central Room Deku Baba',
                                'WF Cleaned Central Room Gate Torch Using Fire Arrows'],
                              ['WF Cleaned Central Room SW To Entrance Room', 'WF Cleaned Central Room SW To Push Block Room',
                               'WF Cleaned Central Room SW To Fairy Platform', 'WF Cleaned Central Room SW To Upper',
                               'WF Cleaned Central Room SW To Fairy Region']),
        create_dungeon_region('WF Central Room Fairy Platform (Cleaned)', ['WF Stray Fairy Cleaned Central Room SE Corner'],
                              ['WF Cleaned Central Room Fairy Platform To SW', 'WF Cleaned Central Room Fairy Platform To East',
                               'WF Cleaned Central Room Fairy Platform To Upper']),
        create_dungeon_region('WF Central Room East Region (Cleaned)', [], ['WF Cleaned Central Room East To Fairy Platform',
                               'WF Cleaned Central Room East To Upper', 'WF Cleaned Central Room East To Ladder Up',
                               'WF Cleaned Central Room East To Elevator Room']),
        create_dungeon_region('WF Central Room Upper Region (Cleaned)', ['WF Stray Fairy Cleaned Central Room Upper Switch Chest',
                               'WF Cleaned Central Room Ladder Switch'], ['WF Cleaned Central Room Upper To Pre Boss Room',
                               'WF Cleaned Central Room Upper To Dragonfly Room', 'WF Cleaned Central Room Upper To Elevator Room',
                               'WF Cleaned Central Room Upper To Fairy Platform', 'WF Cleaned Central Room Upper To East',
                               'WF Cleaned Central Room Upper To SW', 'WF Cleaned Central Room Upper To Fairy Region']),

        create_dungeon_region('WF Elevator Room West Lower (Cleaned)', ['WF Activate Elevator From Cleaned West Lower'],
                              ['WF Cleaned Elevator Room West Lower To Fairy Region', 'WF Cleaned Elevator Room West Lower To North Upper',
                               'WF Cleaned Elevator Room West Lower To SW Upper', 'WF Cleaned Elevator Room West Lower To East Lower',
                               'WF Cleaned Elevator Room West Lower To Key Chest', 'WF Cleaned Elevator Room West Lower To Central Room']),
        create_dungeon_region('WF Elevator Room East Lower (Cleaned)', ['WF Activate Elevator From Cleaned East Lower'],
                              ['WF Cleaned Elevator Room East Lower To Map Room',
                               'WF Cleaned Elevator Room East Lower To West Lower']),
        create_dungeon_region('WF Elevator Room Key Chest Region (Cleaned)', ['WF Cleaned Elevator Room Key Chest'], []),
        create_dungeon_region('WF Elevator Room North Upper (Cleaned)', [],
                              ['WF Cleaned Elevator Room North Upper To West Lower',
                               'WF Cleaned Elevator Room North Upper To East Lower',
                               'WF Cleaned Elevator Room North Upper To Key Chest',
                               'WF Cleaned Elevator Room North Upper To Fairy Region']),
        create_dungeon_region('WF Elevator Room SW Upper (Cleaned)', [],
                              ['WF Cleaned Elevator Room SW Upper To Central Room',
                               'WF Cleaned Elevator Room SW Upper To Bow Room',
                               'WF Cleaned Elevator Room SW Upper To West Lower',
                               'WF Cleaned Elevator Room SW Upper To East Lower']),

        create_dungeon_region('WF Push Block Room Lower (Cleaned)',
                              ['WF Stray Fairy Cleaned Push Block Room Hive', 'WF Stray Fairy Cleaned Push Block Room Skulltula'],
                              ['WF Cleaned Push Block Room Lower To Central Room',
                               'WF Cleaned Push Block Room Lower To Compass Room',
                               'WF Cleaned Push Block Room Lower To Upper',
                               'WF Cleaned Push Block Room Lower To Fairy Region']),
        create_dungeon_region('WF Push Block Room Top Region (Cleaned)', [],
                              ['WF Cleaned Push Block Room Upper To Dark Puffs',
                               'WF Cleaned Push Block Room Upper To Lower']),


        # Post woodfall cleaned swamp areas
        create_ow_region('Swamp Tourist Region (Cleaned)', ['Swamp Tourist Roof HP', 'Swamp Owl Statue'], ['Cleaned Tourist Region To Swamp Path',
                        'Cleaned To Swamp Tourist Centre', 'Cleaned To Potion Shop', 'Cleaned To Lost Woods', 'Cleaned To Swamp Spider House',
                        'Cleaned Tourist Region Trick To Upper Midpoint', 'Cleaned To Octo Region Grotto', 'Cleaned Tourist Region To Kaepora']),
        create_ow_region('Swamp Deku Palace Outer Region (Cleaned)', [], ['Cleaned Outer Palace To Tourist Lower',
                        'Cleaned Outer Palace To Tourist Upper', 'Cleaned Outer Palace To Lower Courtyard',
                        'Cleaned Palace To Butler Race', 'Cleaned Outer Palace To Upper Courtyard']),
        create_ow_region('Swamp Deku Palace Lower Courtyard (Cleaned)', ['Deku Palace Courtyard HP'],
                         ['Cleaned Deku Palace Lower Courtyard To Outer Region',
                          'Cleaned Deku Palace Lower Courtyard To Main Throne Room', 'Cleaned To Magic Beans',
                          'Cleaned Deku Palace Lower Courtyard To Upper']),
        create_ow_region('Swamp Deku Palace Upper Courtyard (Cleaned)', [], ['Cleaned Deku Palace Upper Courtyard To Lower',
                        'Cleaned Deku Palace Upper Courtyard To Outer Region', 'Cleaned Deku Palace Upper Courtyard To Throne Room Cage Region']),
        create_ow_region('Swamp Octo Region Upper Near Palace (Cleaned)', [],
                         ['Cleaned Octo Upper Near Palace To Lower',
                          'Cleaned Octo Upper To Deku Palace', 'Cleaned Octo Upper Near Palace To Midpoint']),
        create_ow_region('Swamp Octo Region Upper Midpoint (Cleaned)', [],
                         ['Cleaned Octo Upper Midpoint To Near Palace',
                          'Cleaned Octo Upper Midpoint To Lower', 'Cleaned Octo Upper Midpoint To Kaepora']),
        create_ow_region('Swamp Octo Kaepora Region (Cleaned)', ['Song From Kaepora Gaebora'],
                         ['Cleaned Octo Kaepora To Lower',
                          'Cleaned Octo Kaepora To Midpoint', 'Cleaned Octo Kaepora To Woodfall']),
        create_ow_region('Outside Woodfall Entrance Region (Cleaned)', ['Outside Woodfall 20 Rupee Chest'],
                         ['Cleaned Outside Woodfall Entrance To Woodfall Owl Platform',
                          'Cleaned Outside Woodfall Entrance To Fountain Platform']),
        create_ow_region('Woodfall Owl Platform (Cleaned)',
                         ['Outside Woodfall 5 Rupee Chest', 'Woodfall Owl Statue (Cleaned)'],
                         ['Cleaned Owl Platform To Entrance', 'Cleaned Owl Platform To Fountain Platform',
                          'Cleaned Owl Platform To Temple Platform']),
        create_ow_region('Outside Woodfall Temple Platform (Cleaned)', [],
                         ['Cleaned Woodfall Temple Platform To Owl Platform',
                          'Cleaned Woodfall Temple Platform To Entrance',
                          'Cleaned Woodfall Temple Platform Into Temple']),
        create_ow_region('Outside Woodfall Fairy Fountain Platform (Cleaned)', ['Outside Woodfall HP'],
                         ['Cleaned Fountain Platform To Owl Platform', 'Cleaned Fountain Platform To Entrance',
                          'Cleaned Fountain Platform To Fountain']),

        create_ow_region('Beyond The Icicles', [], ['TF To Mountain', 'TF Mountain Icicles Backwards']),
        create_ow_region('Path to Mountain Village South', [], ['Mountain Snowball Block', 'TF From Mountain']),
        create_ow_region('Path to Mountain Village North', [], ['Mountain Path North Exit', 'Mountain Snowball Block Backwards']),
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
        create_ow_region('Snowhead', [], ['Goron Blizzard']),
        create_ow_region('Snowhead Spire', [], ['GF Snowhead', 'Snowhead Temple Entrance']),
        create_interior_region('Snowhead Fairy Shrine', ['Snowhead GF Reward'], ['Snowhead Spire']),

        create_dungeon_region('SH Lobby'),

        create_ow_region('Beyond Great Bay Gate', [], ['TF To Great Bay Coast', 'TF Great Bay Gate Backwards']),
        create_ow_region('Great Bay Coast', [], ['TF From Great Bay Coast']),
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
        create_ow_region('Great Bay Fairy Ledge', [], ['GF Great Bay']),
        create_interior_region('Great Bay Fairy Shrine', ['Great Bay GF Reward'], ['Great Bay Fairy Exit']),

        create_ow_region('Path to Ikana'),
        create_ow_region('Ikana Graveyard', ['Captains Chest'],
            ['SoS Grave Grotto', 'HP Grave Grotto', 'Dampe Grave Grotto', 'Dampe Door']),
        create_interior_region('Dampe Grave'),
        create_grotto_region('Storms Grave'),
        create_grotto_region('Heart Piece Grave'),
        create_ow_region('Ikana Canyon Lower'),
        create_ow_region('Ikana Canyon', [], ['GF Stone Tower']),
        create_interior_region('Sakon Hideout'),
        create_interior_region('Secret Shrine'),
        create_interior_region('Poe Sister House'),
        create_interior_region('Spoop Cave'),
        create_interior_region('Music Box House'),
        create_interior_region('Bottom of the Well'),
        create_ow_region('Ikana Castle'),
        create_interior_region('Stone Tower Fairy Shrine', ['Stone Tower GF Reward'], ['Ikana Canyon']),
        create_ow_region('Stone Tower'),
    ]
    world.regions.extend([
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

def _create_region(name, type, locations=None, exits=None, scene_listing=0x0, scene_name='Grottos'):
    ret = Region(name, type)
    if locations is None:
        locations = []
    if exits is None:
        exits = []

    for exit in exits:
        ret.exits.append(Entrance(exit, ret))
    for location in locations:
        # address, address2, default, type, scene_listing, scene_name = location_table[location]
        location_lookup = location_table[location]
        address, address2, default, type = location_lookup[:4]
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
                    'Woodfall Owl Statue (Poisoned)': (None, None, None, 'Statue'),     # Should probably get deprecated out, we'll see how it plays out
                    'Woodfall Owl Statue (Cleaned)': (None, None, None, 'Statue'),
                    'Woodfall Warp Opened': (None, None, None, 'Event'),
                    'Swamp Owl Statue': (0x28372EE, None, 0x07, 'Statue'),
                    'Swamp Warp Opened': (None, None, None, 'Event'),
                    'Ikana Canyon Owl Statue': (0x2055422, None, 0x08, 'Statue'),
                    'Ikana Canyon Warp Opened': (None, None, None, 'Event'),
                    'Stone Tower Owl Statue': (0x2BA92AE, None, 0x09, 'Statue'),
                    'Stone Tower Warp Opened': (None, None, None, 'Event'),

                    'Song From Skull Kid': (None, None, None, 'Song'),
                    'Song From HMS': (None, None, None, 'Song'),
                    'Song From Romani': (None, None, None, 'Song'),
                    'Song From Monkey': (None, None, None, 'Song'),
                    'Song From Kaepora Gaebora': (None, None, None, 'Song'),
                    'Song From Baby Goron': (None, None, None, 'Song'),
                    'Song From Baby Zoras': (None, None, None, 'Song'),
                    'Song From Composer Grave': (None, None, None, 'Song'),
                    'Song From Igos': (None, None, None, 'Song'),
                    'Song From Giants': (None, None, None, 'Song'),

                    'First Nut': (None, None, None, 'Chest'),
                    'SCT 20 Rupee Chest': (0x2E5C284, None, 0x5080, 'Chest'),
                    'Festival Tower Rupee Chest': (0x2E5C344, None, 0x50A1, 'Chest'),
                    'ECT 100 Rupee Chest': (0x2DE4434, None, 0x50CA, 'Chest'),
                    'Clock Town Mailbox HP': (None, None, None, 'Chest'), # ?
                    'Your Room Rupee Chest': (None, None, None, 'Chest'),
                    'Anjus Room Rupee Chest': (None, None, None, 'Chest'),
                    'Bomber Tunnel Chest': (None, None, None, 'Chest'),

                    'TF Chest On A Stump': (0x25C5D44, None, 0x5080, 'Chest', 0x26, 'Termina Field'),
                    'TF Chest In The Grass': (0x25C5D54, None, 5081, 'Chest', 0x26, 'Termina Field'),
                    'Termina Field Underwater Chest': (0x25C5D64, None, 0x5082, 'Chest', 0x26, 'Termina Field'),
                    'TF Peahat Grotto HP': (None, None, None, 'Chest'),
                    'TF Dodongo Grotto HP': (None, None, None, 'Chest'),
                    'TF Deku Baba Pit Chest': (None, None, None, 'Chest'),

                    'Outside Woodfall 5 Rupee Chest': (0x2884224, None, 0x5042, 'Chest', 0x3F, 'Woodfall'),
                    'Outside Woodfall 20 Rupee Chest': (0x2884234, None, 0x5080, 'Chest', 0x3F, 'Woodfall'),
                    'Outside Woodfall HP': (0x2884244, None, 0x0180, 'Chest', 0x3F, 'Woodfall'),

                    'WF Map Chest': (None, None, None, 'Chest'),
                    'WF Poisoned Elevator Room Key Chest': (None, None, None, 'Chest'),
                    'WF Compass Chest': (None, None, None, 'Chest'),
                    'WF Bow Chest': (None, None, None, 'Chest'),
                    'WF Boss Key Chest': (None, None, None, 'Chest'),
                    'WF Stray Fairy Lobby Chest': (None, None, None, 'Chest'),
                    'WF Stray Fairy Poisoned Central Room Upper Switch Chest': (None, None, None, 'Chest'),
                    'WF Stray Fairy Dark Puffs': (None, None, None, 'Chest'),

                    'Lens Grotto Lens Chest': (0x2EB808C, None, 0x841, 'Chest', 0x00, 'Grottos'),
                    'Lens Grotto Invisible Chest': (0x2EB809C, None, 0x6083, 'Chest', 0x00, 'Grottos'),
                    'Lens Grotto Chest Under Rock': (0x2EB80CC, None, 0x50A6, 'Chest', 0x00, 'Grottos'),

                    'Mountain Village Waterfall Chest': (0x2BDD2D4, None, 0x6080, 'Chest'),
                    'Goron Village Path Winter HP': (0x2C232A8, None, 0x186, 'Chest'),
                    'Goron Village Path Underwater Crevice': (0x2C3412C, None, 0x5080, 'Chest'),
                    'Goron Village Path HP Chest': (0x2C3418C, None, 0x186, 'Chest'),

                    # Snowhead Temple Chests

                    'Path to Beavers Deku Flower Chest': (0x271541C, None, 0x5081, 'Chest', 0x38, 'Zora Cape'),
                    'Path to Beavers Chest': (0x271543C, None, 0x5082, 'Chest', 0x38, 'Zora Cape'),
                    'Zora Cape Sea Floor Chest': (0x271547C, None, 0x50A0, 'Chest', 0x38, 'Zora Cape'),

                    # Pinnacle Rock
                    # TODO: Add spots to all sea snakes to randomize Zora Eggs???

                    'Pirate Fortress Chest Under Pipe': (0x2740188, None, 0x5080, 'Chest', 0x34, 'Pirate Fortress Entrance'),
                    'Pirate Fortress Chest By Coast Gate': (0x2740198, None, 0x5081, 'Chest', 0x34, 'Pirate Fortress Entrance'),
                    'Pirate Fortress Chest By Entry Tunnel': (0x27401A8, None, 0x5082, 'Chest', 0x34, 'Pirate Fortress Entrance'),

                    'Pirate Fortress Floor Chest': (0x20A2248, None, 0x5080, 'Chest', 0x0D, 'Inner Pirate Fortress'),
                    'Pirate Fortress Roof Chest': (0x20A2258, None, 0x5081, 'Chest', 0x0D, 'Inner Pirate Fortress'),

                    'Pirate Fortress Chest Between Caged Push Blocks': (0x23F00D0, None, 0x5081, 'Chest', 0x1C, 'Pirate Fortress Interior Rooms'),
                    'Pirate Fortress Tunnel Red Rupee Chest': (0x23E6240, None, 0x5084, 'Chest', 0x1C, 'Pirate Fortress Interior Rooms'),
                    'Pirate Fortress Tunnel Blupee Chest': (0x23E6250, None, 0x5046, 'Chest', 0x1C, 'Pirate Fortress Interior Rooms'),
                    'Pirate Fortress Hookshot Chest': (0x238B13C, None, 0x0822, 'Chest', 0x1C, 'Pirate Fortress Interior Rooms'),
                    'Pirate Fortress Fish Guarded Chest': (0x23BB048, None, 0x5080, 'Chest', 0x1C, 'Pirate Fortress Interior Rooms'),
                    'Pirate Fortress Silver Booty': (0x23BB048, None, 0x00C3, 'Chest', 0x1C, 'Pirate Fortress Interior Rooms'),

                    # Great Bay Temple Chests

                    # TODO: Ikana Graveyard Locations
                    'Captains Chest': (None, None, None, 'Chest'),

                    # TODO: Secret Shrine Locations

                    # TODO: Misc Ikana Locations: Poe Sisters, Ikana Castle, Well

                    # TODO: Inverted Stone Tower Chests

                    # Stone Tower Temple Chests

                    # Inverted Stone Tower Temple Chests

                    # Moon Trial Chests

                    # Grotto Chests
                    'TF East Pillar Bombchu Pit Chest': (None, None, None, 'Grotto Chest'),
                    'Swamp Path Rupee Pit Chest': (None, None, None, 'Grotto Chest'),
                    'Octo Grotto 20 Rupee Chest': (None, None, None, 'Grotto Chest'),

                    'Clock Tower Platform HP': (None, None, None, 'Collectable'),
                    'Dropped Ocarina': (None, None, None, 'Collectable'),
                    'NCT Tree HP': (0x2DE4434, None, 0xA06, 'Collectable'),
                    'Moons Tear': (None, None, None, 'Collectable'),
                    'TF Beehive Grotto HP': (None, None, None, 'Collectable'),
                    'Swamp Path Bat Tree HP': (0x27C12BC, None, 0x106, 'Collectable'),
                    'Swamp Tourist Roof HP': (None, None, None, 'Collectable'),
                    'Deku Palace Courtyard HP': (None, None, None, 'Collectable'),
                    # TODO:
                    # 'Scarecrow On The Coast': (0x26DEE44, None, 0x??, 'Collectable'),
                    # 'Scarecrow On The Coast Post Gyorg': (0x26DE0E0, None, 0x??, 'Collectable'),
                    # TODO:
                    'Zora Cape Lake Bottom HP': (None, None, None, 'Collectable', 0x38, 'Zora Cape'),
                    'Love In Pirate Jail': (0x23E62A0, None, 0xC06, 'Collectable'),

                    'Odolwa HC': (None, None, None, 'Collectable'),
                    'Goht HC': (None, None, None, 'Collectable'),
                    'Gyorg HC': (None, None, None, 'Collectable'),
                    'Twinmold HC': (None, None, None, 'Collectable'),

                    # TODO: Add 3 Spots to replace Stray Fairy Chests
                    'WF Stray Fairy Entrance': (None, None, None, 'Fairy'),
                    'WF Stray Fairy Poisoned Central Room SE Corner': (None, None, None, 'Pot'),
                    'WF Stray Fairy Elevator Room': (None, None, None, 'Bees'),
                    'WF Stray Fairy Poisoned Push Block Room Hive': (None, None, None, 'Bees'),
                    'WF Stray Fairy Push Block Room Underwater': (None, None, None, 'Bubble Fairy'),
                    'WF Stray Fairy Central Room Upper Bubble': (None, None, None, 'Bubble Fairy'),
                    'WF Stray Fairy Pre Boss Room Alcoves 1': (None, None, None, 'Bubble Fairy'),
                    'WF Stray Fairy Pre Boss Room Alcoves 2': (None, None, None, 'Bubble Fairy'),
                    'WF Stray Fairy Pre Boss Room Alcoves 3': (None, None, None, 'Bubble Fairy'),
                    'WF Stray Fairy Pre Boss Room Bubble': (None, None, None, 'Bubble Fairy'),
                    'WF Stray Fairy Poisoned Central Room Deku Baba': (None, None, None, 'Enemy'),
                    'WF Stray Fairy Poisoned Push Block Room Skulltula': (None, None, None, 'Enemy'),

                    # TODO: Snowhead Stray Fairy Spots
                    # TODO: Great Bay Stray Fairy Spots
                    # TODO: Stone Tower Stray Fairy Spots

                    'Clock Town Business Scrub Item': (None, None, None, 'Deku'),
                    'Clock Town Business Scrub Trade Done': (None, None, None, 'Deku'),
                    'Swamp Deku Salesman': (None, None, None, 'Deku'),
                    'Mountain Deku Salesman': (None, None, None, 'Deku'),
                    'Ocean Deku Salesman': (None, None, None, 'Deku'),
                    'Canyon Deku Salesman': (None, None, None, 'Deku'),

                    'Item From HMS': (None, None, None, 'NPC'),
                    'Honey and Darling Bombchu Bowling Prize': (None, None, None, 'NPC'),
                    'Honey and Darling Archery Prize': (None, None, None, 'NPC'),
                    'Honey and Darling Basket Bomb Throw Prize': (None, None, None, 'NPC'),
                    'Honey and Darling Grand Champion': (None, None, None, 'NPC'),
                    'Treasure Chest Game Goron Prize': (None, None, None, 'NPC'),
                    'Treasure Chest Game Human Prize': (None, None, None, 'NPC'),
                    'Treasure Chest Game Zora Prize': (None, None, None, 'NPC'),
                    'Treasure Chest Game Deku Prize': (None, None, None, 'NPC'),
                    'Town Shooting Gallery Quiver Prize': (None, None, None, 'NPC'),
                    'Town Shooting Gallery HP Prize': (None, None, None, 'NPC'),
                    'Milk Bar Performance': (None, None, None, 'NPC'),
                    'Delivery to Mama Kafei': (None, None, None, 'NPC'),
                    'Stock Pot Inn Key': (None, None, None, 'NPC'),
                    'Grandma Stories HP 1': (None, None, None, 'NPC'),
                    'Grandma Stories HP 2': (None, None, None, 'NPC'),
                    'Toilet Hand HP': (None, None, None, 'NPC'),
                    'We Shall Greet The Morning Together': (None, None, None, 'NPC'),
                    'Expert Person Solver Takes the Case': (None, None, None, 'NPC'),
                    'Mayor HP': (None, None, None, 'NPC'),
                    'Bank 200 Rupee Prize': (None, None, None, 'NPC'),
                    'Bank HP': (None, None, None, 'NPC'),
                    'Rosa Sisters HP': (None, None, None, 'NPC'),
                    'Counting Is Hard': (None, None, None, 'NPC'),
                    'Sword School HP': (None, None, None, 'NPC'),
                    'Bomber Notebook': (None, None, None, 'NPC'),
                    'Bomber Code': (None, None, None, 'NPC'),
                    'NCT Keaton HP': (None, None, None, 'NPC'),
                    'Clock Town GF Mask': (None, None, None, 'NPC'),
                    'Deku Challenge Day 1': (None, None, None, 'NPC'),
                    'Deku Challenge Day 2': (None, None, None, 'NPC'),
                    'Deku Challenge Day 3': (None, None, None, 'NPC'),
                    'Deku Playground HP': (None, None, None, 'NPC'),
                    'Listen To Guru Guru': (None, None, None, 'NPC'),
                    'Keaton Mask From Kafei': (None, None, None, 'NPC'),
                    'Letter From Kafei': (None, None, None, 'NPC'),
                    'Pendant From Kafei': (None, None, None, 'NPC'),
                    'Deliver Letter to Mama To Postman': (None, None, None, 'NPC'),
                    'Learn Kamaro Dance': (None, None, None, 'NPC'),
                    'TF Business Scrub Grotto HP': (None, None, None, 'NPC'),
                    '4 Gossip Stone HP': (None, None, None, 'NPC'),
                    'Swamp Shooting Gallery Quiver Prize': (None, None, None, 'NPC'),
                    'Swamp Shooting Gallery HP Prize': (None, None, None, 'NPC'),
                    'Swamp Tourist Free Product (?)': (None, None, None, 'NPC'),
                    'Pictograph Contest Winner': (None, None, None, 'NPC'),
                    'Picto Box': (None, None, None, 'NPC'),
                    'Swamp Boat Archery HP': (None, None, None, 'NPC'),
                    'Red Potion To Help Koume': (None, None, None, 'NPC'),
                    'Swamp Spider House Reward': (None, None, None, 'NPC'),
                    'Butler Race Prize': (None, None, None, 'NPC'),
                    'Magic Beans': (None, None, None, 'NPC'),
                    'Song From Goron Elder': (None, None, None, 'NPC'),
                    'Frog Choir': (None, None, None, 'NPC'),
                    # TODO:
                    # 'Fisherman Torch Game': (0x26DEDC4, None, 0x??, 'NPC'),
                    'Reunite Seahorse': (None, None, None, 'NPC'),
                    'Beaver Bottle': (None, None, None, 'NPC'),
                    'Beaver HP': (None, None, None, 'NPC'),

                    'Buy All Night Mask': (None, None, None, 'Shop'),
                    'Buy Bigger Bomb Bag': (None, None, None, 'Shop'),
                    'Buy Bomb Bag': (None, None, None, 'Shop'),
                    'Deku Princess': (None, None, None, 'Bottle'),
                    'Clock Town Tingle Woodfall Map': (None, None, None, 'Tingle'),
                    'Clock Town Tingle Clock Town Map': (None, None, None, 'Tingle'),
                    'Swamp Tingle Woodfall Map': (None, None, None, 'Tingle'),
                    'Swamp Tingle Snowhead Map': (None, None, None, 'Tingle'),
                    'spiders': (None, None, None, 'Unknown'), # ?
                    'so many spiders': (None, None, None, 'Unknown'), # ?

                    'Odolwas Remains': (None, None, None, 'Remains'),
                    'Gohts Remains': (None, None, None, 'Remains'),
                    'Gyorgs Remains': (None, None, None, 'Remains'),
                    'Twinmolds Remains': (None, None, None, 'Remains'),

                    'Clock Town GF Magic Bar': (None, None, None, 'Fairy Reward'),
                    'Woodfall GF Reward': (None, None, None, 'Fairy Reward'),
                    'Snowhead GF Reward': (None, None, None, 'Fairy Reward'),
                    'Great Bay GF Reward': (None, None, None, 'Fairy Reward'),
                    'Stone Tower GF Reward': (None, None, None, 'Fairy Reward'),

                    'Kill Swamp Big Octo': (None, None, None, 'Obstacle'),
                    'Kill Swamp Big Octo With Boat': (None, None, None, 'Obstacle'),
                    'Kill Swamp Big Octo From Palace': (None, None, None, 'Obstacle'),
                    'WF Clean Poison Water Using Fire Arrows': (None, None, None, 'Obstacle'),
                    'WF Poisoned Central Room Gate Torch Using Fire Arrows': (None, None, None, 'Obstacle'),
                    'WF Poisoned Central Room Ladder Switch': (None, None, None, 'Obstacle'),
                    'WF Clean Poison Water': (None, None, None, 'Obstacle'),
                    'WF Activate Elevator From Poisoned West Lower': (None, None, None, 'Obstacle'),
                    'WF Activate Elevator From Poisoned East Lower': (None, None, None, 'Obstacle'),
                    'WF Stray Fairy Cleaned Central Room Deku Baba': (None, None, None, 'Unknown'),
                    'WF Cleaned Central Room Gate Torch Using Fire Arrows': (None, None, None, 'Unknown'),
                    'WF Stray Fairy Cleaned Central Room SE Corner': (None, None, None, 'Unknown'),
                    'WF Stray Fairy Cleaned Central Room Upper Switch Chest': (None, None, None, 'Unknown'),
                    'WF Cleaned Central Room Ladder Switch': (None, None, None, 'Unknown'),
                    'WF Activate Elevator From Cleaned West Lower': (None, None, None, 'Unknown'),
                    'WF Activate Elevator From Cleaned East Lower': (None, None, None, 'Unknown'),
                    'WF Cleaned Elevator Room Key Chest': (None, None, None, 'Unknown'),
                    'WF Stray Fairy Cleaned Push Block Room Hive': (None, None, None, 'Unknown'),
                    'WF Stray Fairy Cleaned Push Block Room Skulltula': (None, None, None, 'Unknown'),

                    'Have you seen this man?': (None, None, None, 'Event'),
                    'Moon Cry': (None, None, None, 'Event'),
                    'Watch Business Scrub Fly': (None, None, None, 'Event'),
                    'Deliver Letter to Kafei': (None, None, None, 'Event'),
                    'Foil Sakon': (None, None, None, 'Event'),
                    'Clock Town Tingle Pic': (None, None, None, 'Event'),
                    'Don Gero Town Frog': (None, None, None, 'Event'),
                    'Swamp Gossip Check': (None, None, None, 'Event'),
                    'Mountain Gossip Check': (None, None, None, 'Event'),
                    'Ocean Gossip Check': (None, None, None, 'Event'),
                    'Canyon Gossip Check': (None, None, None, 'Event'),
                    'Swamp Tingle Pic': (None, None, None, 'Event'),
                    'Checked Koume': (None, None, None, 'Event'),
                    'Saved Koume': (None, None, None, 'Event'),
                    'Return Deku Princess': (None, None, None, 'Event'),
                    'WF Don Gero Frog': (None, None, None, 'Event'),

                    'Defeat Odolwa': (None, None, None, 'Event'),
                    'Defeat Goht': (None, None, None, 'Event'),
                    'Defeat Gyorg': (None, None, None, 'Event'),
                    'Defeat Twinmold': (None, None, None, 'Event'),
                    'Open the Moon': (None, None, None, 'Event')}

'''
    ### generated a list of all the location names I've used so far
    #TODO: Shops
    # Castle Town Potion Shop Item 1': (shop_address(3, 0), None, 0x30, 'Shop', 0x31, 'the Market'),
'''
