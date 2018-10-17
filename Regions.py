import collections
from BaseClasses import Region, Location, Entrance, RegionType


def create_regions(world):
    # TODO: finish out this whole thing (what I'm currently working on)
    world.regions = [
        create_ow_region('Beginning',[], ['Cursed Underground']),
        create_interior_region('Deku Flower Tutorial Area', [], ['Clock Tower Twisted Hallway']),
        create_interior_region('Clock Tower Basement',
            ['Remove the Cursed Mask', 'Song from HMS'],
            ['Clock Tower Exit', 'Clock Tower Twisted Hallway Backwards']),

        # TODO: Suffix Entrance to all of these
        create_ow_region('South Clock Town',
            ['SCT 20 Rupee Chest', 'Festival Tower Rupee Chest',
            'Clock Town Owl Statue', 'Clock Tower Platform HP', 'Clock Town Business Scrub'],
            ['To Clock Tower Basement', 'To Clock Tower Rooftop', 'South Mailbox',
            'SCT Top Exit to WCT', 'SCT Bottom Exit to WCT', 'SCT Exit to NCT',
            'SCT Bottom Exit to ECT', 'SCT Top Exit to ECT',
            'Clock Town South Gate', 'SCT Exit to Laundry Pool']),
        create_interior_region('Clock Tower Rooftop', ['Dropped Ocarina', 'Song from Skull Kid'], ['End of First Cycle', 'Moon Portal']),

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
        create_interior_region('Astral Observatory', ['Moon Cry'], ['Tunnel Balloon From Observatory', 'Astral Observatory Exit']),
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
            ['Bombers Notebook', 'Bomber Code', 'NCT Tree HP', 'Clock Town Tingle Clock Town Map',
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
            ['TF to Swamp', 'South Gate to Clock Town',
            'TF Mountain Icicles', 'North Gate to Clock Town',
            'TF Great Bay Gate', 'West Gate to Clock Town',
            'TF to Ikana', 'East Gate to Clock Town', 'TF to Obs Over Fence Maybe',
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
                          'Swamp Path To Southern Swamp (Poisoned)', 'Swamp Path To Southern Swamp (Clean)',
                          'To Swamp Path Rupee Pit']),
        create_grotto_region('Swamp Path Rupee Pit', ['Swamp Path Rupee Pit Chest'], ['Swamp Path Rupee Pit Exit']),
        create_interior_region('Swamp Shooting Gallery', ['Swamp Shooting Gallery Quiver Prize', 'Swamp Shooting Gallery HP Prize'], ['Swamp Shooting Gallery Exit']),

        create_ow_region('Swamp Tourist Region (Poisoned)', ['Swamp Tourist Roof HP', 'Swamp Owl Statue', 'Kill Swamp Big Octo'],
                         ['Tourist Region to Swamp path', 'Swamp Big Octo From Tourist Region',
                          'To Swamp Tourist Centre', 'To Potion Shop', 'To Lost Woods']),
        create_interior_region('Swamp Tourist Centre', ['Swamp Tourist Free Product (?)', 'Pictograph Contest Winner',
                                'Picto Box', 'Kill Swamp Big Octo With Boat'], ['Swamp Boat Ride', 'Tourist Centre Exit']),
        create_interior_region('Swamp Potion Shop', ['Red Potion To Help Koume'], ['Swamp Potion Shop Exit']),
        create_ow_region('Lost Woods', ['Checked Koume', 'Saved Koume'], ['Lost Woods Exit', 'But like, a LOT of them']),
        # oh jeez, we have to have an exit here for every exit in lost woods don't we? lol
        # also not actually sure if lost woods should be ow or interior
        create_ow_region('Swamp Octo Region Lower (Poisoned)', ['Kill Swamp Big Octo From Palace'],
                         ['Swamp Big Octo From Octo Region', 'Octo Region to Deku Palace',
                          'To Swamp Spider House', 'Lower Octo Region Trick To Upper Midpoint', 'To Octo Region Grotto']),
        create_grotto_region('Octo Region Grotto', ['Octo Grotto 20 Rupee Chest'], ['Octo Grotto Clean Exit', 'Octo Grotto Poison Exit']),
        create_interior_region('Swamp Spider House', ['spiders', 'so many spiders', 'Swamp Spider House Reward'], ['Swamp Spider House Clean Exit', 'Swamp Spider House Poisoned Exit']),
        # a note about this poisoned region, while in the previous section of the swamp any form could get around, now
        # only deku can get around without needing health due to the poisoned water, so to deal with that, do with put
        # a heart requirement on the entrance to here? split it up into logical regions requiring health?
        # things to ponder

        create_ow_region('Swamp Deku Palace Outer Region (Poisoned)', [], ['Poisoned Outer Palace To Lower Octo',
                        'Poisoned Outer Palace To Octo Upper', 'Poisoned Outer Palace To Lower Courtyard', 'Poisoned Palace To Butler Race',
                        'Poisoned Outer Palace To Upper Courtyard']),
        create_interior_region('Butler Race', ['Butler Race Prize'], ['Butler Race Clean Exit', 'Butler Race Poisoned Exit']),

        create_ow_region('Swamp Deku Palace Lower Courtyard (Poisoned)', ['Deku Palace Courtyard HP'], ['Poisoned Deku Palace Lower Courtyard To Outer Region',
            'Poisoned Deku Palace Lower Courtyard To Main Throne Room', 'To Magic Beans', 'Deku Palace Lower Courtyard To Upper']),
        create_grotto_region('Magic Bean Grotto', ['Magic Beans'], ['Magic Bean Grotto Clean Exit', 'Magic Bean Grotto Poisoned Exit']),

        create_ow_region('Swamp Deku Palace Upper Courtyard (Poisoned)', [], ['Deku Palace Upper Courtyard To Lower',
            'Deku Palace Upper Courtyard To Outer Region', 'Deku Palace Upper Courtyard To Throne Room Cage Region']),
        create_interior_region('Swamp Deku Palace Throne Room', ['Return Deku Princess'], ['Swamp Deku Palace Throne Room Clean Exit', 'Swamp Deku Palace Throne Room Poisoned Exit']),
        create_interior_region('Swamp Deku Palace Cage Room', ['Song From Monkey'], ['Swamp Deku Palace Cage Room Clean Exit', 'Swamp Deku Palace Cage Room Poisoned Exit']),
        # the throne room, is that actually a different map for poisoned vs clean water? todo: find out

        create_ow_region('Swamp Octo Region Upper Near Palace (Poisoned)', [], ['Poisoned Octo Upper Near Palace To Lower',
                                    'Poisoned Octo Upper To Deku Palace', 'Poisoned Octo Upper Near Palace To Midpoint']),
        create_ow_region('Swamp Octo Region Upper Midpoint (Poisoned)', [], ['Poisoned Octo Upper Midpoint To Near Palace',
                                    'Poisoned Octo Upper Midpoint To Lower', 'Poisoned Octo Upper Midpoint To Kaepora']),
        create_ow_region('Swamp Octo Kaepora Region (Poisoned)', ['Song From Kaepora Gaebora'], ['Posoned Octo Kaepora To Lower',
                                    'Poisoned Octo Kaepora To Midpoint', 'Poisoned Octo Kaepora To Woodfall']),
        # exit 'Poisoned Octo Upper To Deku Palace': thinking- entrance rando, coming in from tourist swamp (getting
        # through the octos isn't a loading zone, right? oh lordy), the exit into the outer palace from lower and upper
        # parts of this region are different loading zones, right? which means splitting the upper region up further
        # might be necessary; if the player can trick up to the upper part, a check still needs to be made to see if
        # they can get across to the deku palace exit (and the SoS learn spot, both hard requiring deku I believe)
        # I'll leave it as the 3 pieces for the upper region, they can be combined later easily enough

        create_ow_region('Outside Woodfall Entrance Region (Poisoned)', ['Outside Woodfall 20 Rupee Chest'],
                         ['Poisoned Outside Woodfall Entrance To Woodfall Owl Platform', 'Poisoned Outside Woodfall Entrance To Fountain Platform']),
        create_ow_region('Woodfall Owl Platform (Poisoned)', ['Outside Woodfall 5 Rupee Chest', 'Woodfall Owl Statue (Poisoned)'],
                         ['Poisoned Owl Platform To Entrance', 'Poisoned Owl Platform To Fountain Platform', 'Poisoned Owl Platform To Temple Platform']),
        create_ow_region('Outside Woodfall Temple Platform (Poisoned)', [], ['Poisoned Woodfall Temple Platform To Owl Platform',
                        'Poisoned Woodfall Temple Platform To Entrance', 'Poisoned Woodfall Temple Platform Into Temple']),
        create_ow_region('Outside Woodfall Fairy Fountain Platform (Poisoned)', ['Outside Woodfall HP'],
                         ['Poisoned Fountain Platform To Owl Platform', 'Poisoned Fountain Platform To Entrance', 'Poisoned Fountain Platform To Fountain']),
        create_interior_region('Woodfall Fairy Shrine', ['Woodfall GF Reward'], ['Woodfall Fountain Clean Exit', 'Woodfall Fountain Poisoned Exit']),

        # create_ow_region('Boat Ride', [], ['Poison Swamp']),
        # should this actually be its own region? idek
        # ugh maybe it should, it might have loading zones or smth ugh

        # TODO All of the Woodfall area
        # also todo: figure out what the actual loading zones are because I'm about to create an unholy mess of logical regions - RO
        create_dungeon_region('WF Entrance Room (Poisoned)', ['WF Stray Fairy Entrance', 'WF Stray Fairy Lobby Chest'],
                              ['WF Poisoned Front Exit', 'WF Poisoned Entrance To Central Room', 'WF Boss Warp']),
        # actually dunno if this room needs poisoned/clean versions, but I'll just leave it like this for now

        create_dungeon_region('WF Central Room SW Region (Poisoned)', ['WF Stray Fairy Cleaned Central Room Deku Baba',
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
        create_dungeon_region('WF Central Room Upper Region (Poisoned)', [ 'WF Stray Fairy Central Room Upper Switch Chest',
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
        create_dungeon_region('WF Map Room (Cleaned)', [], ['WF Clean Map Room Exit', 'WF Clean Map Room To Chest']),
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

        create_dungeon_region('WF Compass Room', ['WF Compass Chest'], ['WF Compass Room Clean Exit', 'WF Compass Room Poisoned Exit']),

        create_dungeon_region('WF Dark Puff Gauntlet', ['WF Stray Fairy Dark Puffs'],
                              ['WF Dark Puff Gauntlet To Push Block Room', 'WF Dark Puff Gauntlet To Dragonfly Room']),

        create_dungeon_region('WF Dragonfly Room West', [], ['WF Dragonfly Room NE To Dark Puffs', 'WF Dragonfly Room West To NE',
                                'WF Dragonfly Room West To Central Room SW', 'WF Dragonfly Room West To Central Room East',
                                'WF Dragonfly Room West To Central Room Fairy Platform']),
        # the falling through the floor spots aren't loading zones, are they? if not, there needs to be cleaned/poisoned
        # rooms here; if so, there need to be cleaned/poisoned exits
        create_dungeon_region('WF Dragonfly Room NE', [], ['WF Dragonfly Room NE To West', 'WF Dragonfly Room NE To Central Room']),

        create_dungeon_region('WF Bow Room', ['WF Bow Chest'], ['WF Bow Room Clean Exit', 'WF Bow Room Poisoned Exit']),
        # I'm assuming here that this room doesn't have different versions, so it has 2 exits to poisoned/cleaned

        create_dungeon_region('WF Boss Key Room', ['WF Boss Key Chest', 'WF Don Gero Frog'], ['WF Boss Key Room Clean Exit', 'WF Boss Key Room Poisoned Exit']),

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

        create_dungeon_region('WF Boss Room', ['Beat Odolwa', 'Odolwa HC'], ['WF Odolwa Boss Exit']),

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
        #

        # create_ow_region('Mountain Icicles', [], ['Termina Field North Exit', 'Termina Field From Mountain']),
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

def _create_region(name, type, locations=None, exits=None):
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

# TODO: addresses, SO many addresses, and more
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

test = '''
# TODO: Curiosity Shop
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
# TODO: Bomb Shop
'Castle Town Bazaar Item 5': (shop_address(4, 4), None, 0x34, 'Shop', 0x2C, 'the Market'),
'Castle Town Bazaar Item 6': (shop_address(4, 5), None, 0x35, 'Shop', 0x2C, 'the Market'),
'Castle Town Bazaar Item 7': (shop_address(4, 6), None, 0x36, 'Shop', 0x2C, 'the Market'),
'Castle Town Bazaar Item 8': (shop_address(4, 7), None, 0x37, 'Shop', 0x2C, 'the Market'),
## TODO: Convert to Trading Post
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
'''