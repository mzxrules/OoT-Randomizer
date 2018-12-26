import collections
import logging


def set_rules(world):
    world.get_region('South Clock Town').can_reach = lambda state: True
    global_rules(world)

def set_rule(spot, rule):
    spot.access_rule = rule

def set_always_allow(spot, rule):
    spot.always_allow = rule


def add_rule(spot, rule, combine='and'):
    old_rule = spot.access_rule
    if combine == 'or':
        spot.access_rule = lambda state: rule(state) or old_rule(state)
    else:
        spot.access_rule = lambda state: rule(state) and old_rule(state)


def forbid_item(location, item):
    old_rule = location.item_rule
    location.item_rule = lambda i: i.name != item and old_rule(i)


def item_in_locations(state, item, locations):
    for location in locations:
        if item_name(state, location) == item:
            return True
    return False

def item_name(state, location):
    location = state.world.get_location(location)
    if location.item is None:
        return None
    return location.item.name


def global_rules(world):
    set_rule(world.get_entrance('Clock Tower Twisted Hallway'), False)
    set_rule(world.get_location('First Nut'), lambda state: state.form('Deku'))
    # set_rule(world.get_location('Clock Town GF Reward'), lambda state: state.has('CT SF', 1))
    set_rule(world.get_location('Woodfall GF Reward'), lambda state: state.has('WF SF', 15))
    set_rule(world.get_location('Snowhead GF Reward'), lambda state: state.has('SH SF', 15))
    set_rule(world.get_location('Great Bay GF Reward'), lambda state: state.has('GB SF', 15))
    set_rule(world.get_location('Stone Tower GF Reward'), lambda state: state.has('ST SF', 15))

    set_rule(world.get_location('Clock Town Mailbox HP'), lambda state: state.can_use('Postman Hat'))

    set_rule(world.get_location('Swamp Deku Salesman'), lambda state: state.has('Town Title Deed') and state.form('Human'))
    set_rule(world.get_location('Mountain Deku Salesman'), lambda state: state.has('Swamp Title Deed') and state.form('Deku'))
    set_rule(world.get_location('Ocean Deku Salesman'), lambda state: state.has('Mountain Title Deed') and state.form('Goron'))
    set_rule(world.get_location('Canyon Deku Salesman'), lambda state: state.has('Ocean Title Deed') and state.form('Zora'))

    set_rule(world.get_location('Song From HMS'), lambda state: state.has('Ocarina of Time'))
    set_rule(world.get_location('Item From HMS'), lambda state: state.has('Ocarina of Time'))


    ### SOUTH CLOCK TOWN
    set_rule(world.get_location('Clock Town Deku Salesman'), lambda state: state.has('Moons Tear'))
    set_rule(world.get_location('Clock Tower Platform HP'), lambda state: state.form('Human') or state.form('Zora') or (state.form('Deku') and (state.has('Moons Tear') or state.can('Gainer'))))

    set_rule(world.get_location('Festival Tower Rupee Chest'), lambda state: state.can_use('Hookshot') or (state.form('Deku') and state.has('Moons Tear')))
    set_rule(world.get_location('SCT 20 Rupee Chest'), lambda state: state.can_use('Hookshot')
                or (state.form('Deku') and state.has("Moon's Tear") and (state.form('Human') or state.form('Zora'))))

    set_rule(world.get_location('Dropped Ocarina'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Song From Skull Kid'), lambda state: state.can_pop_balloon() and state.has('Ocarina of Time'))
    set_rule(world.get_entrance('End of First Cycle'), lambda state: state.has('Song of Time'))
    set_rule(world.get_entrance('Moon Portal'),
             lambda state: [state.has(x) for x in ["Oath to Order", "Odolwa's Remains", "Goht's Remains", "Gyorg's Remains", "Twinmold's Remains"]].count(True) == 5)
    set_rule(world.get_entrance('To Clock Tower Rooftop'), lambda state: state.form('Human') or state.form('Zora') or (state.form('Deku') and (state.has("Moon's Tear") or state.can("Gainer"))))

    set_rule(world.get_location('Clock Town Owl Statue'), lambda state: state.form('Human'))

    set_rule(world.get_entrance('Clock Town North Gate'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or state.can('Clock Town Guard Skip'))

    ### LAUNDRY POOL
    set_rule(world.get_location('Listen To Guru Guru'), lambda state: state.form('Human') or state.form('Zora') or state.form('Goron'))
    set_rule(world.get_location('Town Frog'), lambda state: state.can_use('Don Gero Mask'))

    ### WEST CLOCK TOWN
    set_rule(world.get_location('Rosa Sisters HP'), lambda state: state.can_use('Kamaro Mask'))
    set_rule(world.get_location('Buy Bigger Bomb Bag'), lambda state: state.form('Human') or state.form('Zora') or state.has('Adult Wallet'))
    set_rule(world.get_location('Sword School HP'), lambda state: state.form('Human'))
    set_rule(world.get_location('Buy All Night Mask'), lambda state: state.form('Human') and state.has('Giants Wallet'))
    set_rule(world.get_location('Deliver Letter to Mama To Postman'), lambda state: state.has('Letter to Mama'))
    set_rule(world.get_entrance('Clock Town West Gate'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or state.can('Clock Town Guard Skip'))

    ### NORTH CLOCK TOWN
    set_rule(world.get_location('Bomber Notebook'), lambda state: state.can_pop_balloon() and state.form('Human'))
    set_rule(world.get_location('Bomber Code'), lambda state: state.can_pop_balloon() and (state.form('Human') or state.form('Deku')))
    set_rule(world.get_location('Foil Sakon'), lambda state: state.form('Human') or state.form('Zora'))
    set_rule(world.get_location('NCT Tree HP'), lambda state: state.form('Human') or state.form('Zora'))
    set_rule(world.get_location('Clock Town Tingle Clock Town Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Clock Town Tingle Woodfall Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Clock Town Tingle Pic'), lambda state: state.can_use('Picto Box'))
    set_rule(world.get_location('NCT Keaton HP'), lambda state: state.can_use('Keaton Mask'))

    set_rule(world.get_entrance('To Deku Playground'), lambda state: state.form('Deku') or state.can('Gainer'))
    # I'm sure there are various ways to get over this fence aside from deku
    # todo: find ways of bypassing this fence
    set_rule(world.get_location('Deku Playground HP'), lambda state: state.form('Deku'))

    set_rule(world.get_location('Clock Town GF Magic Bar'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_location('Clock Town GF Mask'), lambda state: state.has('Deku Mask'))
    set_rule(world.get_entrance('Clock Town North Gate'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or state.can('Clock Town Guard Skip'))
    # set_rule(world.get_location('Magic from NCT Great Fairy'), lambda state: state.form('Deku'))

    ### EAST CLOCK TOWN
    set_rule(world.get_location('ECT 100 Rupee Chest'), lambda state: state.form('Human') or state.can('Goron Boost') or state.can('Gainer') or state.form('Zora'))
    set_rule(world.get_location('Treasure Chest Game Goron Prize'), lambda state: state.form('Goron'))
    set_rule(world.get_location('Treasure Chest Game Human Prize'), lambda state: state.form('Human'))
    set_rule(world.get_location('Treasure Chest Game Zora Prize'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Treasure Chest Game Deku Prize'), lambda state: state.form('Deku'))

    set_rule(world.get_entrance('Bomber Bouncer'), lambda state: state.has('Bomber Code'))
    set_rule(world.get_location('Bomber Tunnel Chest'), lambda state: state.can_blast() and (state.form('Human') or state.form('Zora')))
    set_rule(world.get_entrance('Tunnel Balloon From ECT'), lambda state: state.can_pop_balloon())
    set_rule(world.get_entrance('Tunnel Balloon From Observatory'), lambda state: state.can_pop_balloon() or state.form('Human'))
    set_rule(world.get_location('Watch Deku Salesman Fly'), lambda state: state.has('Traded Town Title Deed'))

    set_rule(world.get_location('Honey and Darling Grand Champion'), lambda state: state.has('Bomb Bag') and state.has('Bow') and state.form('Human'))
    set_rule(world.get_location('Town Shooting Gallery Quiver Prize'), lambda state: state.can_use('Bow'))
    set_rule(world.get_location('Town Shooting Gallery HP Prize'), lambda state: state.can_use('Bow'))
#     add_rule(world.get_location('Town Shooting Gallery HP Prize'),
#              lambda state: state.options('NoHardestArchery'), 'or')
    set_rule(world.get_location('Expert Person Solver Takes the Case'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora'))

    set_rule(world.get_entrance('To Stock Pot Inn Secret Entrance'), lambda state: state.form('Deku'))
    set_rule(world.get_location('Stock Pot Inn Key'), lambda state: state.any_form_but('Deku'))
    # requires the ability to use the secret entrance
    set_rule(world.get_location('Have you seen this man?'), lambda state: state.can_use('Kafei Mask'))
    set_rule(world.get_location('Your Room Rupee Chest'), lambda state: state.has('Room Key'))
    # set_rule(world.get_location('Anjus Room Rupee Chest'), lambda state: state.has('Room Key') or state.form('Deku'))
    set_rule(world.get_location('Grandma Stories HP 1'), lambda state: state.can_use('All Night Mask'))
    set_rule(world.get_location('Grandma Stories HP 2'), lambda state: state.can_use('All Night Mask'))

    set_rule(world.get_location('Toilet Hand HP'), lambda state: state.has_paper())
    set_rule(world.get_entrance('To Milk Bar'), lambda state: state.can_use('Romani Mask'))
    set_rule(world.get_location('Milk Bar Performance'), lambda state: False not in [state.form(f) for f in ['Human', 'Deku', 'Goron', 'Zora']] and state.has('Ocarina'))
    set_rule(world.get_location('Delivery to Mama Kafei'), lambda state: state.has('Letter to Mama'))
    set_rule(world.get_location('Mayor HP'), lambda state: state.can_use('Couples Mask'))
    set_rule(world.get_entrance('Clock Town East Gate'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or state.can('Clock Town Guard Skip'))

    ### TERMINA FIELD
    set_rule(world.get_entrance('Astral Observatory Fence'), lambda state: (state.has('Magic Beans') and state.has_bottle()) or state.can('Goron Boost'))
    set_rule(world.get_entrance('TF To Observatory Over Fence'), lambda state: state.can('Goron Boost') and state.has('Ocarina of Time'))
    set_rule(world.get_location('Learn Kamaro Dance'), lambda state: state.form('Human') or state.form('Goron'))
    set_rule(world.get_entrance('TF Mountain Icicles'), lambda state: state.can_use('Bow'))
    set_rule(world.get_entrance('TF Great Bay Gate'), lambda state: (state.form('Human') and state.has('Eponas Song'))
                                                                    or state.can('Goron Boost'))

    set_rule(world.get_location('Moon Tear Crater'), lambda state: state.has('Moon Cry'))

    set_rule(world.get_entrance('To Mountain Gossips'), lambda state: state.can_blast() or state.form('Goron'))
    set_rule(world.get_location('Swamp Gossip Check'), lambda state: (state.form('Deku') and state.has('Sonata of Awakening'))
            or (state.form('Goron') and state.has('Goron Lullaby')) or (state.form('Zora') and state.has('New Wave Bossa Nova')))
    set_rule(world.get_location('Mountain Gossip Check'), lambda state: (state.form('Deku') and state.has('Sonata of Awakening'))
            or (state.form('Goron') and state.has('Goron Lullaby')) or (state.form('Zora') and state.has('New Wave Bossa Nova')))
    set_rule(world.get_location('Ocean Gossip Check'), lambda state: (state.form('Deku') and state.has('Sonata of Awakening'))
            or (state.form('Goron') and state.has('Goron Lullaby')) or (state.form('Zora') and state.has('New Wave Bossa Nova')))
    set_rule(world.get_location('Canyon Gossip Check'), lambda state: (state.form('Deku') and state.has('Sonata of Awakening'))
            or (state.form('Goron') and state.has('Goron Lullaby')) or (state.form('Zora') and state.has('New Wave Bossa Nova')))
    set_rule(world.get_location('4 Gossip Stone HP'),
             lambda state: state.has('Swamp Gossip Check') and state.has('Mountain Gossip Check')
                           and state.has('Ocean Gossip Check') and state.has('Canyon Gossip Check'))

    set_rule(world.get_location('TF Peahat Grotto HP'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora'))
    set_rule(world.get_entrance('To TF Deku Salesman Grotto'), lambda state: state.has('Saw Scrub Fly In'))
    set_rule(world.get_location('TF Deku Salesman Grotto HP'), lambda state: state.has('Adult Wallet'))

    set_rule(world.get_location('TF Beehive Grotto HP'), lambda state: (state.can_blast() or state.form('Goron'))
                                                                                  and state.can_use('Bow') and state.form('Zora'))
    set_rule(world.get_location('TF Chest On A Stump'), lambda state: state.can_use('Hookshot'))

    set_rule(world.get_entrance('To East Pillar Grotto'),
             lambda state: state.has_bottle() and state.has('Magic Beans') and (state.form('Human') or state.form('Zora')))

    ### SOUTHERN SWAMP
    set_rule(world.get_location('Swamp Path Bat Tree HP'), lambda state: state.can_pop_balloon() or state.form('Human'))
    set_rule(world.get_location('Swamp Tingle Woodfall Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Swamp Tingle Snowhead Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Swamp Tingle Pic'), lambda state: state.can_use('Picto Box'))
    set_rule(world.get_location('Swamp Shooting Gallery Quiver Prize'), lambda state: state.can_use('Bow'))
    set_rule(world.get_location('Swamp Shooting Gallery HP Prize'), lambda state: state.can_use('Bow'))

    ## Southern Swamp
    set_rule(world.get_location('Swamp Tourist Roof HP'), lambda state: (state.has('Town Title Deed') and state.form('Human')) or state.can('Goron Boost'))
    set_rule(world.get_location('Swamp Owl Statue'), lambda state: state.form('Human'))
    set_rule(world.get_entrance('Swamp Octo By Tourist Centre'), lambda state: state.can_use('Bow') or state.can_use('Hookshot') or state.form('Zora'))
    set_rule(world.get_entrance('Poison Swamp Octo By Spider House'), lambda state: state.can_use('Bow') or state.can_use('Hookshot'))

    # swamp tourist center
    set_rule(world.get_location('Picto Box'), lambda state: state.has('Saved Koume'))
    set_rule(world.get_location('Pictograph Contest Winner'), lambda state: state.has('Tingle Pic') or state.has('Deku King Pic'))
    set_rule(world.get_entrance('Swamp Boat Ride'), lambda state: state.has('Saved Koume'))

    # potion shop and lost woods
    set_rule(world.get_location('Red Potion To Help Koume'), lambda state: state.has('Checked Koume'))
    set_rule(world.get_location('Saved Koume'), lambda state: state.has_bottle())

    # swamp tourist center clean water
    set_rule(world.get_location('Swamp Boat Archery HP'), lambda state: state.can_use('Bow') and state.has('Defeat Odolwa'))

    set_rule(world.get_entrance('To Swamp Spider House'), lambda state: state.can_use('Fire Arrows'))
    set_rule(world.get_entrance('Lower Swamp To Soaring Pedestal'), lambda state: state.form('Deku') and state.form('Human'))
    set_rule(world.get_entrance('Deku Palace To Soaring Pedestal'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Woodfall To Soaring Pedestal'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Soaring Pedestal To Deku Palace Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Soaring Pedestal To Woodfall Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_location('Song From Kaepora Gaebora'), lambda state: state.has('Ocarina'))

    ## Deku Palace
    set_rule(world.get_entrance('Deku Palace Secret Exit To Woodfall'), lambda state: state.form('Deku') or state.can('Gainer'))
    set_rule(world.get_entrance('To Butler Race'), lambda state: state.form('Deku') or (state.has_hearts(6) and (state.form('Human') or state.form('Zora'))))
    set_rule(world.get_entrance('Outer Deku Palace To Courtyard'), lambda state: state.form('Deku') or (state.can('Deku Palace Guard Skip')))
    set_rule(world.get_entrance('Outer Deku Palace To Upper Courtyard'), lambda state: state.has_bottle() and state.has('Magic Beans')
        and (state.form('Deku') or (state.has_hearts(6) and state.any_form_but('Goron'))))
    set_rule(world.get_location('Beans From Bean Seller'), lambda state: state.form('Human'))

    set_rule(world.get_entrance('Deku Palace Lower To Upper Courtyard'), lambda state: state.can('Deku Palace Coutryard Trick'))
    set_rule(world.get_entrance('Deku Palace Royal Chamber Back Entrance'), lambda state: state.form('Deku'))
    set_rule(world.get_location('Song From Monkey'), lambda state: state.form('Deku') and state.has('Ocarina'))

    # post woodfall palace
    set_rule(world.get_location('Return Deku Princess'), lambda state: state.form('Deku') and state.has('Deku Princess'))
    set_rule(world.get_location('Butler Race Prize'), lambda state: state.form('Human') and state.has('Returned Deku Princess') and state.has('Defeat Odolwa'))

    set_rule(world.get_location('Swamp Spider House Reward'),
             lambda state: state.has_bottle() and state.form('Deku') and state.has('Sonata of Awakening') and state.can_pop_balloon() and state.can_use('Bomb Bag'))

    ## Outside Woodfall Area
    set_rule(world.get_location('Woodfall Red Rupee Chest'),
             lambda state: state.form('Deku') or (state.form('Human') and (state.has('Hookshot') or state.has_hearts(5))) or (state.form('Zora') and state.has_hearts(5)))
    set_rule(world.get_entrance('Woodfall Entrance To Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Woodfall Entrance To Fountain Platform'), lambda state: (state.form('Human') or state.form('Zora')) and state.has_hearts(8))

    set_rule(world.get_location('Woodfall Blupee Chest'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_location('Woodfall Owl Statue'), lambda state: state.form('Human'))
    set_rule(world.get_entrance('Woodfall Owl Platform To Entrance'), lambda state: state.form('Deku') or (state.has_hearts(10) and state.any_form_but('Goron')))
    set_rule(world.get_entrance('Woodfall Owl Platform To Fountain Platform'), lambda state: state.form('Deku') or (state.has_hearts(4) and state.any_form_but('Goron')))
    set_rule(world.get_entrance('Woodfall Owl Platform To Temple Platform'), lambda state: state.form('Deku') and state.has('Sonata Of Awakening'))

    set_rule(world.get_entrance('Woodfall Temple Platform To Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Woodfall Temple Platform To Entrance'), lambda state: (state.form('Human') or state.form('Zora')) and state.has_hearts(5))

    set_rule(world.get_location('Woodfall HP Chest'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_entrance('Fountain Platform To Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Fountain Platform To Entrance'), lambda state: state.form('Deku') or (state.has_hearts(10) and state.any_form_but('Goron')))
    set_rule(world.get_entrance('Fountain Platform To Fountain'), lambda state: state.form('Deku') or state.can('Gainer'))

    set_rule(world.get_location('Woodfall GF Reward'), lambda state: state.has('WF SF', 15))

    ### WOODFALL TEMPLE

    ## Lobby
    set_rule(world.get_location('WF Lobby SF'), lambda state: state.stray_fairy_req(state.any_form_but('Goron')))

    set_rule(world.get_location('WF Lobby SF Chest'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Lobby To Central Room'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Boss Warp'), lambda state: state.has("Odolwa's Remains"))

#     ## First Floor
#     set_rule(world.get_location('WF Central Deku Baba SF'), lambda state: state.stray_fairy_req())
#     set_rule(world.get_entrance('WF Poisoned Central Room SW To Fairy Region'), lambda state: state.can_use('Bow') and state.can_use('Great Fairy Mask'))
#     # set_rule(world.get_location('WF Stray Fairy Central Room Upper Bubble'), lambda state: True)

#     set_rule(world.get_location('WF Poisoned Central Room Gate Torch Using Fire Arrows'), lambda state: state.can_use('Fire Arrows'))
#     set_rule(world.get_location('WF Clean Poison Water Using Fire Arrows'), lambda state: state.can_use('Fire Arrows'))
#     set_rule(world.get_entrance('WF Clean Poison Water Using Fire Arrows Exit'), lambda state: state.can_use('Fire Arrows'))
#     set_rule(world.get_entrance('WF Poisoned Central Room SW To Push Block Room'), lambda state: state.has('Small Key (Woodfall Temple)'))
#     set_rule(world.get_entrance('WF Central Room Lower To Upper'), lambda state: state.can_use('Hookshot'))
#     set_rule(world.get_location('WF Stray Fairy Poisoned Central Room SE Corner'), lambda state: state.stray_fairy_req())
#     set_rule(world.get_entrance('WF Poisoned Central Room Fairy Platform To SW'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Poisoned Central Room Fairy Platform To East'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Poisoned Central Room Fairy Platform To Upper'), lambda state: state.can_use('Hookshot'))
#     set_rule(world.get_entrance('WF Poisoned Central Room East To Fairy Platform'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Poisoned Central Room East To Upper'), lambda state: state.can_use('Hookshot'))
#     set_rule(world.get_entrance('WF Poisoned Central Room East To Ladder Up'), lambda state: state.has('WF Central Room Ladder Switch'))
#     set_rule(world.get_entrance('WF Poisoned Central Room Upper To Fairy Region'),
#              lambda state: state.stray_fairy_req(state.can_pop_balloon() or state.form('Human')))
#     set_rule(world.get_location('WF Stray Fairy Poisoned Central Room Upper Switch Chest'),
#              lambda state: state.form('Deku') and state.any_form_but('Deku') and state.stray_fairy_req())
#     # for reference: these two are good examples of how the stray fairy req fxn works
#     set_rule(world.get_location('WF Poisoned Central Room Ladder Switch'), lambda state: state.any_form_but('Deku'))
#     set_rule(world.get_entrance('WF Wooden Flower Torch Shot'), lambda state: state.can_use('Bow'))
#     set_rule(world.get_entrance('WF Poisoned Central Room Upper To Pre Boss Room'), lambda state: state.has('WF Central Room Gate Torch Lit'))
#     set_rule(world.get_entrance('WF Poisoned Central Room Upper To SW'), lambda state: state.any_form_but('Goron'))

#     # set_rule(world.get_location('WF Stray Fairy Elevator Room'), lambda state: True)
#     # this fairy is an open check because it's in its own logical region, with two exits leading to it that form the
#     # actual checks
#     set_rule(world.get_location('WF Activate Elevator From Poisoned West Lower'), lambda state: state.can_use('Bow'))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To Fairy Region'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To North Upper'), lambda state: (state.has('WF Elevator On') and state.form('Deku')))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To SW Upper'), lambda state: (state.has('WF Elevator On') and state.form('Deku')))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To East Lower'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To Key Chest'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
#     # set_rule(world.get_location('WF Elevator Room Key Chest'), lambda state: True)
#     set_rule(world.get_location('WF Activate Elevator From Poisoned East Lower'), lambda state: state.can_use('Bow'))
#     # ^ example of the same event needing to go in multiple spots; need to change to a logical region and have only a single item location?
#     set_rule(world.get_entrance('WF Poisoned Elevator Room East Lower To West Lower'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room North Upper To West Lower'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room North Upper To East Lower'), lambda state: state.can_use('Hookshot'))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room North Upper To Key Chest'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room North Upper To Fairy Region'),
#              lambda state: state.form('Human') or state.form('Zora') or (state.form('Deku') and state.has('Magic Meter')))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room SW Upper To West Lower'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Poisoned Elevator Room SW Upper To East Lower'), lambda state: state.can_use('Hookshot'))

#     set_rule(world.get_location('WF Map Chest'),
#              lambda state: state.form('Deku') or state.can_use('Bomb Bag') or state.form('Goron'))
#     # possibly the blast mask can be used as well? in which case just change this to can_blast()
#     # can this actually be done strictly with deku? todo: more testing on this I think

#     ## Push Block Bridge Room
#     set_rule(world.get_location('WF Stray Fairy Poisoned Push Block Room Hive'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
#     set_rule(world.get_location('WF Stray Fairy Poisoned Push Block Room Skulltula'), lambda state: state.stray_fairy_req())
#     set_rule(world.get_entrance('WF Poisoned Push Block Room Lower To Compass Room'), lambda state: state.can_use('Deku Sticks') or state.can_use('Fire Arrows'))
#     set_rule(world.get_entrance('WF Poisoned Push Block Room Lower To Upper'), lambda state: state.can_use('Deku Sticks') or state.can_use('Bow'))
#     set_rule(world.get_entrance('WF Poisoned Push Block Room Upper To Lower'), lambda state: state.can_use('Deku Sticks') or state.can_use('Bow'))
#     # yep, you can in fact light the right torches (aside from the compass room one) and hit the spider web with just the bow
#     # though honestly can_use('deku sticks') should maybe just be form('Human'); though for entrance rando, maybe not
#     set_rule(world.get_entrance('WF Poisoned Push Block Room Lower To Fairy Region'),
#              lambda state: state.stray_fairy_req(state.has_hearts(7) and (state.form('Human') or state.form('Zora'))))

#     set_rule(world.get_entrance('WF Cleaned Push Block Room Lower To Fairy Region'), lambda state: state.stray_fairy_req(state.form('Human') or state.form('Zora')))
#     ## Dark Puff Gauntlet and Dragonfly Room
#     set_rule(world.get_location('WF Stray Fairy Dark Puffs'), lambda state: state.stray_fairy_req())
#     set_rule(world.get_entrance('WF Dark Puff Gauntlet To Dragonfly Room'), lambda state: state.can_use('Deku Sticks') or state.can_use('Fire Arrows'))
#     set_rule(world.get_entrance('WF Dragonfly Room West To NE'), lambda state: state.form('Deku'))
#     # we /may/ want to require a way to kill the dragonflies here beyond deku flowering them? just because it might be
#     # too much of a pain normally; or not, who knows
#     set_rule(world.get_entrance('WF Dragonfly Room West To Central Room SW'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Dragonfly Room West To Central Room East'), lambda state: state.any_form_but('Goron'))
#     set_rule(world.get_entrance('WF Dragonfly Room West To Central Room Fairy Platform'), lambda state: state.any_form_but('Goron'))

#     ## Upper 1st Floor
#     set_rule(world.get_location('WF Bow Chest'), lambda state: state.can_kill_lizalfos())
#     set_rule(world.get_location('WF Boss Key Chest'), lambda state: state.can_kill_gekkos())
#     set_rule(world.get_location('Woodfall Temple Frog'), lambda state: state.can_use('Don Gero Mask'))
#     # set_rule(world.get_location(''), lambda state: state)

#     ## Pre-Boss Room
#     set_rule(world.get_entrance('WF Pre Boss Room South To Fairy 1'), lambda state: state.stray_fairy_req())
#     set_rule(world.get_entrance('WF Pre Boss Room South To Fairy 2'), lambda state: state.stray_fairy_req())
#     set_rule(world.get_entrance('WF Pre Boss Room South To Fairy 3'),
#              lambda state: state.stray_fairy_req(state.form('Deku')) or (state.can_pop_balloon() and state.can_use('Great Fairy Mask')))
#     set_rule(world.get_entrance('WF Pre Boss Room South To Bubble Fairy'), lambda state: (state.can_use('Bow') and state.stray_fairy_req(state.form('Deku')))
#                                                                             or (state.can_pop_balloon() and state.can_use('Great Fairy Mask')))
#     set_rule(world.get_entrance('WF Pre Boss Room South To North'), lambda state: state.form('Deku') and (state.can_use('Hookshot') or state.can_use('Bow')))
#     set_rule(world.get_entrance('WF Pre Boss Room North To Fairy 1'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
#     set_rule(world.get_entrance('WF Pre Boss Room North To Fairy 2'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
#     set_rule(world.get_entrance('WF Pre Boss Room North To Fairy 3'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
#     set_rule(world.get_entrance('WF Pre Boss Room North To Bubble Fairy'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
#     set_rule(world.get_entrance('WF Pre Boss Room North To South'), lambda state: state.form('Deku'))

#     ## Boss: Odolwa
#     set_rule(world.get_location('Defeat Odolwa'), lambda state: state.can_use('Bow'))
#     set_rule(world.get_location('Odolwa HC'), lambda state: state.can_use('Bow'))
#     set_rule(world.get_entrance('WF Odolwa Boss Exit'), lambda state: state.can_use('Bow'))
#     # todo: figure out all the ways to kill odolwa
#     # you probly hard need to use the bow, which means most other checks aren't needed
#     # but yeah, gotta figure out all the ways to beat this
#     # set_rule(world.get_location('Odolwas Remains'), lambda state: True)

#     ## Post Odolwa Princess Room
#     set_rule(world.get_location('Deku Princess'), lambda state: state.has_bottle() and state.form('Human'))

    ### MOUNTAIN VILLAGE

    ## MV Path
    set_rule(world.get_entrance('Mountain Snowball Block'), lambda state: state.can_use('Fire Arrows') or state.can_blast() or state.form('Goron'))
    set_rule(world.get_entrance('Mountain Snowball Block Backwards'), lambda state: state.any_form_but('Deku'))

    ## Mountain Village
    set_rule(world.get_location('Gift From Hungry Goron'), lambda state: state.has('Rock Sirloin'))
    set_rule(world.get_location('Mountain Village Owl Statue'), lambda state: state.form('Human'))
    set_rule(world.get_entrance('Frozen MV Lower To Top'), lambda state: state.lens_req() and state.any_form_but('Goron'))
    set_rule(world.get_location('Razor Sword Upgrade'), lambda state: state.has('Defeat Goht') and state.has('Adult Wallet') and state.has('Razor Sword'))
    set_rule(world.get_location('Gilded Sword Upgrade'), lambda state: state.has('Defeat Goht') and state.has('Adult Wallet') and state.has('Gold Dust'))
    set_rule(world.get_entrance('Smithy Thawed Exit'), lambda state: state.has('Defeat Goht'))
    set_rule(world.get_location('Item From Darmani'), lambda state: state.has('Song of Healing') and state.can_use('Lens of Truth') and state.has('Led Darmani Up'))

    set_rule(world.get_location('Goron Grave Hot Spring Water'), lambda state: state.has_bottle())
    set_rule(world.get_location('Mountain Village Waterfall Chest'), lambda state: state.lens_req())

    set_rule(world.get_location('Mountain Village Keaton Quiz'), lambda state: state.can_use('Keaton Mask'))

    set_rule(world.get_location('Frog Choir HP'), lambda state: state.has('Defeat Goht') and
                    (False not in [state.has(x) for x in ['Town Frog', 'Woodfall Temple Frog', 'Swamp Frog', 'Great Bay Temple Frog']]))
    # event names TBD

    ## Frozen Lake
    set_rule(world.get_location('Mountain Tingle Snowhead Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Mountain Tingle Romani Ranch Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Mountain Tingle Pic'), lambda state: state.can_use('Picto Box'))
    # depending on how this gets implemented, we may need separate this further, since the actor might be entirely different each day
    # need to also verify that we've heard the Baby Goron Crying event
    # TODO: need to code this DRYer
    set_rule(world.get_location('Lullaby Intro First Day'),
             lambda state: ((state.can_blast() or state.form('Goron')) and state.can_use('Hot Spring Water')) or state.can_use('Fire Arrows'))
    set_rule(world.get_location('Lullaby Intro Second Day'),
             lambda state: ((state.can_blast() or state.form('Goron')) and state.can_use('Hot Spring Water')) or state.can_use('Fire Arrows'))
    set_rule(world.get_location('Lullaby Intro Final Day'),
             lambda state: ((state.can_blast() or state.form('Goron')) and state.can_use('Hot Spring Water')) or state.can_use('Fire Arrows'))
    # not sure if he'll actually teach you the half song if you're not a goron todo: test form requirements
    set_rule(world.get_entrance('Melted MV Path From Village To Grotto'),
             lambda state: state.form('Goron'))

    set_rule(world.get_entrance('Frozen Lake To Grotto Platform'), lambda state: state.form('Goron'))
    set_rule(world.get_entrance('Frozen Lake Grotto Platform To Goron Race Platform'), lambda state: state.form('Goron'))
    set_rule(world.get_entrance('Frozen Lake Grotto Platform To Grotto'), lambda state: state.can_blast())
    # set_rule(world.get_location('Mountain Lake Grotto Chest'), lambda state: True)
    set_rule(world.get_entrance('Mountain Lake Grotto Thawed Exit'), lambda state: state.has('Defeat Ghot'))

    set_rule(world.get_entrance('Frozen Lake Goron Race Platform To Goron Race'), lambda state: state.can_use('Powder Keg'))

    set_rule(world.get_entrance('Frozen Lake To Hot Spring'), lambda state: state.can_use('Hot Spring Water') or state.can_use('Fire Arrows'))

    set_rule(world.get_location('Mountain Lake HP Chest'),
             lambda state: state.has('Defeat Goht') and state.form('Zora'))
    set_rule(world.get_location('Mountain Lake Red Rupee Chest'),
             lambda state: state.has('Defeat Goht') and state.form('Zora'))
    # I should check this one too, dunno if it's a chest or what; also is goron the only one who can get to this pit?
    # is this the same as the 'frozen lake grotto'? tbd (I'll find out once I finish this area, ez); if it is, then no check here, it's just the open check in the grotto as above

    set_rule(world.get_location('Goron Race Prize'), lambda state: state.has('Defeat Goht') and state.form('Goron'))
    # set_rule(world.get_location(''), lambda state: state)

    ## Goron Village
    set_rule(world.get_location('Biggest Bomb Bag'), lambda state: state.form('Goron') and state.has('Adult Wallet'))
    set_rule(world.get_location('Mountain Deku Salesman HP'), lambda state: state.has('Swamp Title Deed') and state.form('Deku'))
    # form requirements maybe? dunno

    set_rule(world.get_entrance('Frozen Goron Village Outer To Lens Cave Region'), lambda state: (state.form('Human') or state.form('Zora')))
    # scrub can't make the jumps, right?
    set_rule(world.get_entrance('Frozen Lens Cave Region To Goron Village'), lambda state: (
        state.form('Human') or state.form('Zora')) and state.lens_req())

    # set_rule(world.get_location('Lens of Truth Chest'), lambda state: True)
    set_rule(world.get_location('Lens of Truth Cave Invisible Chest'), lambda state: state.lens_req())
    set_rule(world.get_location('Lens of Truth Cave Boulder Chest'), lambda state: state.can_blast())

    set_rule(world.get_location('Song From Baby Goron'), lambda state: state.form('Goron') and state.has('Lullaby Intro'))
    set_rule(world.get_location('Rock Sirloin'), lambda state: state.can_use('Deku Stick') and state.form('Goron'))
    set_rule(world.get_entrance('Goron Village Inner Thawed Exit'), lambda state: state.has('Defeat Goht'))

    ## Snowhead and Path To
    set_rule(world.get_location('Path To Snowhead HP'), lambda state: state.can_use('Hookshot') and state.can_use('Lens of Truth')
                                                                      and (state.form('Human') or state.form('Zora')))
    # would anyone really want to let logic place stuff here without the lens?
    set_rule(world.get_entrance('Snowhead Path MV Side To Mid'), lambda state: state.form('Goron'))
    set_rule(world.get_entrance('Snowhead Path Mid To MV Side'), lambda state: state.form('Goron'))
    set_rule(world.get_entrance('Snowhead Path Mid To SH Side'), lambda state: state.form('Goron'))
    set_rule(world.get_entrance('Snowhead Path SH Side To Mid'), lambda state: state.form('Goron'))

    set_rule(world.get_location('Snowhead Owl Statue'), lambda state: state.form('Human'))
    set_rule(world.get_entrance('Outside SH Owl To Central'), lambda state: state.form('Goron') and state.has('Goron Lullaby'))
    # set_rule(world.get_entrance('Frozen Outside SH Central To Owl'), lambda state: True)
    # it's only for entrance rando, but I can't test this entrance atm, since you'd have to load in from SH or the fairy
    # fountain; can you just roll across? todo: test getting back across the narrow part with the goron still there
    set_rule(world.get_entrance('Outside SH Central To Entrance'), lambda state: True)
    # so you can definitely just walk up here and avoid the snowballs, but maybe it's too much of a pain? I dunno,
    # do we want to hard or optionally require anything here?


    ### SNOWHEAD TEMPLE

#     ## 1st Floor and Basement
#     set_rule(world.get_location('SH Stray Fairy 1 Bridge And Freezard Room'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
#     set_rule(world.get_location('SH Stray Fairy 2 Bridge And Freezard Room'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
#     set_rule(world.get_location('SH Stray Fairy Basement Switch'), lambda state: state.form('Goron'))
#     # set_rule(world.get_location('SH Push Block Key Chest'), lambda state: True)
#     # set_rule(world.get_location('SH Compass Chest'), lambda state: True)
#     # do you have to actually do anything in this room, or is the chest just there already? I forget

#     set_rule(world.get_location('SH Bridge and Freezard Room Key Chest'), lambda state: state.can_use('Fire Arrows'))
#     set_rule(world.get_location('SH Stray Fairy Chest In Compass Room'), lambda state: state.can_use('Fire Arrows') or state.can_use('Hookshot'))

#     set_rule(world.get_location('SH Stray Fairy Compass Room Bombable'),
#              lambda state: (state.can_use('Fire Arrows') or state.can_use('Hookshot')) and state.can_use('Bomb Bag') and state.stray_fairy_req())
#     # I bet there's a way to cheese this one

#     set_rule(world.get_location('SH Stray Fairy Push Block Room'), lambda state: state.can_use('Fire Arrows'))
#     # this check will need to be changed depending on the logical regions defined- probly have a path of regions from
#     # the compass room leading here, plus an exit from the lower part of the room to the chest/torches part gated by
#     # the hookshot

#     set_rule(world.get_location('SH Stray Fairy Behind Central Pillar Room'), lambda state: state.can_use('Fire Arrows'))
#     # set_rule(world.get_location(''), lambda state: state)

#     ## 2nd Floor
#     # set_rule(world.get_location('SH Map Chest'), lambda state: True)
#     # set_rule(world.get_location('SH Stray Fairy Map Chest Room'), lambda state: True)
#     set_rule(world.get_location('SH Icicle Drop Room Key Chest'), lambda state: state.can_use('Bow') and (state.can_blast() or state.form('Goron')))
#     set_rule(world.get_location('SH Stray Fairy Icicle Drop Room'), lambda state: state.can_use('Bow') and state.lens_req())
#     set_rule(world.get_location('SH Stray Fairy Goron Switch Room Ceiling'), lambda state: state.can_pop_balloon() and state.lens_req())

#     set_rule(world.get_location('SH Fire Arrows Chest'), lambda state: state.can_use('Bow'))
#     # I bet there are other ways of beating the wizrobe, just not sure how

#     set_rule(world.get_location('SH Stray Fairy Elevator Room Lens Platforms'), lambda state: state.can_use('Lens of Truth') and (state.form('Human') or state.form('Zora')))
#     # set_rule(world.get_location(''), lambda state: state)

#     ## 3rd Floor
#     set_rule(world.get_location('SH Stray Fairy 3F Snowman Room'), lambda state: state.can_pop_balloon() and state.lens_req())
#     # can you just jump to this one? I forget

#     ## 4th Floor
#     set_rule(world.get_location('SH Stray Fairy 1 Lizalfos Room'), lambda state: state.can_kill_lizalfos())
#     set_rule(world.get_location('SH Stray Fairy 2 Lizalfos Room'), lambda state: state.can_kill_lizalfos())

#     set_rule(world.get_location('SH Stray Fairy Hidden Alcove'), lambda state: state.can_use('Lens of Truth') and (state.form('Deku') or state.form('Human')))
#     # there might be other ways to do this, not sure

#     set_rule(world.get_location('SH Boss Key Chest'), lambda state: state.can_use('Bow'))

#     ## Boss: Ghot
#     set_rule(world.get_location('Ghots Remains'), lambda state: state.can_use('Bow') and state.has('Fire Arrows') and state.form('Goron'))
#     # I know there are various ways to do this boss, but I'm not sure exactly what, so for now let's just require goron form


#     ### ROMANI RANCH AREA

#     ## Milk Road
#     set_rule(world.get_location('Milk Road Keaton HP'), lambda state: state.can_use('Keaton Mask'))
#     set_rule(world.get_location('Milk Road Tingle Romani Ranch Map'), lambda state: state.can_pop_balloon())
#     set_rule(world.get_location('Milk Road Tingle Other Map'), lambda state: state.can_pop_balloon())
#     # whoops, left in a dupe, gotta look up what map this actually is
#     set_rule(world.get_location('Milk Road Tingle Pic'), lambda state: state.can_use('Picto Box'))
#     set_rule(world.get_location('Milk Road Owl Statue'), lambda state: state.form('Human'))

#     ## Romani Ranch
#     set_rule(world.get_location('Bunny Hood'), lambda state: state.can_use('Bremen Mask'))
#     set_rule(world.get_location('Learn Eponas Song'), lambda state: state.can_use('Bow') and state.form('Human'))
#     # form reqs?

#     # set_rule(world.get_location('Dog Track 50 Rupee Chest'), lambda state: True)
#     set_rule(world.get_location('Romani Ranch Bottle'), lambda state: state.can_use('Bow'))
#     set_rule(world.get_location('Dog Track HP'), lambda state: state.dog_track_MoT_req())
#     set_rule(world.get_location('Romani Mask'), lambda state: state.can_use('Bow'))

#     ## Gorman Bros.
#     set_rule(world.get_location('Garo Mask'), lambda state: state.has('Eponas Song'))


#     ### GREAT BAY

#     ## Great Bay North
#     set_rule(world.get_location('Zora Mask'), lambda state: state.form('Human'))
#     set_rule(world.get_location('Great Bay Owl Statue'), lambda state: state.form('Human'))
#     set_rule(world.get_location('Great Bay Tingle Great Bay Map'), lambda state: state.can_pop_balloon())
#     set_rule(world.get_location('Great Bay Tingle Ikana Map'), lambda state: state.can_pop_balloon())
#     set_rule(world.get_location('Great Bay Tingle Pic'), lambda state: state.can_use('Picto Box'))
#     # set_rule(world.get_location('Rupee Pit'), lambda state: True)

#     set_rule(world.get_location('Ocean Spider House HP'), lambda state: state.can_use('Bow') and state.has('Hookshot') and state.has('Captains Hat'))
#     # the captain's hat can be used to get the code or whatever from the stalchildren, or you can trial and
#     # error it with arrows
#     # so we can maybe make it an option to need the captain's hat, but for now I'm just going to require it

#     set_rule(world.get_location('Ocean Spider House Giant Wallet'), lambda state: state.can_use('Fire Arrows') and state.has('Hookshot') and state.has('Bomb Bag'))
#     # todo these later

#     set_rule(world.get_location('Great Bay Lab Fish Feeding HP'), lambda state: state.has_bottle())
#     set_rule(world.get_location('Great Bay Seahorse From Fisherman'), lambda state: state.has('Picto Box') and state.has_bottle())
#     set_rule(world.get_location('Learn New Wave Bossa Nova'), lambda state: state.form('Zora') and state.has('Zora Egg', 7))
#     set_rule(world.get_location('Great Bay High Cliff HP'), lambda state: state.can_use('Hookshot') and state.has('Spring Water') and state.has('Magic Beans'))
#     set_rule(world.get_location('Great Bay Jumping Game HP'), lambda state: state.has('Beat Gyorg') and state.can_use('Hookshot') and (state.form('Human') or state.form('Zora')))

#     ## Great Bay South
#     set_rule(world.get_location('Great Bay Like Like HP'), lambda state: state.form('Zora'))
#     # set_rule(world.get_location('Great Bay Bombchu Pit'), lambda state: True)
#     set_rule(world.get_location('Great Bay Temple Owl Statue'), lambda state: state.form('Human'))
#     set_rule(world.get_location('Zora Hall 5 Rupees From Stagehand'), lambda state: True)
#     set_rule(world.get_location('Zora Hall 20 Rupees From Lulu Stalker'), lambda state: state.has_bottle())
#     set_rule(world.get_location('Beaver Race Bottle'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Beaver Race HP'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Zora Hall Song HP'), lambda state: state.form('Human'))
#     # set_rule(world.get_location(''), lambda state: state)

#     ## Gerudo Fortress
#     set_rule(world.get_location('Gerudo Fortress Entrance Harbor 20 Rupee Chest 1'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Gerudo Fortress Entrance Harbor 20 Rupee Chest 2'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Gerudo Fortress Entrance Harbor 20 Rupee Chest 3'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Gerudo Fortress Cage Maze 20 Rupee Chest'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Gerudo Fortress Cage Maze HP'), lambda state: state.form('Goron') or state.can_use('Bunny Hood'))
#     # I /think/ you need the goron form to be fast enough to make this? maybe there are ways to cheese this

#     set_rule(world.get_location('Gerudo Fortress Tower Hub 20 Rupee Chest'), lambda state: state.can_use('Hookshot'))
#     set_rule(world.get_location('Hookshot'), lambda state: state.can_use('Bow'))
#     set_rule(world.get_location('Zora Egg 1'), lambda state: state.has_bottle() and state.form('Zora') and state.can_use('Hookshot'))
#     set_rule(world.get_location('Zora Egg 2'), lambda state: state.has_bottle() and state.form('Zora') and state.can_use('Hookshot'))
#     set_rule(world.get_location('Zora Egg 3'), lambda state: state.has_bottle() and state.form('Zora') and state.can_use('Hookshot'))
#     set_rule(world.get_location('Zora Egg 4'), lambda state: state.has_bottle() and state.form('Zora') and state.can_use('Hookshot'))
#     set_rule(world.get_location('Gerudo Fortress 100 Rupee Chest'), lambda state: state.can_use('Hookshot') or state.can_use('Bow') or state.can_use('Stone Mask'))
#     # set_rule(world.get_location(''), lambda state: state)

#     ## Pinnacle Rock
#     set_rule(world.get_location('Zora Egg 5'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Zora Egg 6'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Zora Egg 7'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Pinnacle Rock Eel HP'), lambda state: state.form('Zora'))


#     ### GREAT BAY TEMPLE
#     # note about this temple: there's a lot of stuff you might be able to reach with ice arrows rather than hookshoting
#     # to a chest
#     # this will probly need extensive testing

#     set_rule(world.get_location('GB Stray Fairy Entrance Room'), lambda state: state.can_use('Deku Stick'))
#     set_rule(world.get_location('GB Stray Fairy Flywheel Room Underwater'),
#              lambda state: (state.form('Zora') or (state.can_pop_balloon() and state.can_use('Great Fairy Mask'))) and state.stray_fairy_req())

#     set_rule(world.get_location('GB Stray Fairy Flywheel Room Big Skulltula'), lambda state: state.form('Zora'))
#     # zoras can deal with big skulls by themselves, right? no need to add any other checks

#     set_rule(world.get_location('GB Stray Fairy Big Whirlpool Hub Barrel'), lambda state: state)
#     set_rule(world.get_location('GB Stray Fairy Big Whirlpool Hub Bottom'),
#              lambda state: state.stray_fairy_req() and (state.form('Zora') or (state.can_pop_balloon() and state.can_use('Great Fairy Mask'))))
#     set_rule(world.get_location('GB Map Chest'), lambda state: state.can_use('Hookshot'))
#     set_rule(world.get_location('GB Stray Fairy Map Room'), lambda state: (state.can_pop_balloon() or state.form('Zora')) and state.stray_fairy_req())
#     set_rule(world.get_location('GB Stray Fairy Tunnel To Compass Room'), lambda state: state.form('Zora') and state.stray_fairy_req())
#     set_rule(world.get_location('GB Compass Chest'), lambda state: state.can_use('Hookshot'))
#     set_rule(world.get_location('GB Compass Room Key Chest'), lambda state: state.form('Zora'))

#     set_rule(world.get_location('GB Stray Fairy Compass Room'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
#     # ugh, test this check, there are probly lots of ways to do it
#     # todo: lots of testing on this one

#     set_rule(world.get_location('GB Ice Arrows Chest'), lambda state: state.can_use('Hookshot'))
#     # todo: look up all the ways of killing Wort

#     set_rule(world.get_location('GB Boss Key Chest'), lambda state: state.can_kill_gekkos() and state.has('Ice Arrows'))
#     set_rule(world.get_location('GB Stray Fairy First Green Crank Room'), lambda state: state.can_use('Hookshot') and state.has('Ice Arrows'))
#     set_rule(world.get_location('GB Stray Fairy Waterfall Room 1'), lambda state: state.can_use('Hookshot') and state.has('Ice Arrows'))
#     set_rule(world.get_location('GB Stray Fairy Waterfall Room 2'), lambda state: state.can_use('Hookshot') and state.has('Ice Arrows') and state.has('Fire Arrows'))
#     # including fire arrows here for sanity, otherwise you'd have to reenter the room or maybe dungeon if you messed up

#     set_rule(world.get_location('GB Stray Fairy Final Crank Room 1'), lambda state: state.form('Zora') and state.stray_fairy_req())
#     set_rule(world.get_location('GB Stray Fairy Final Crank Room 2'), lambda state: state.form('Zora') and state.stray_fairy_req())
#     # I think just zora is enough for the second one? might have to test that

#     set_rule(world.get_location('GB Stray Fairy Before Gyorg Room 1'), lambda state: state.form('Zora') and state.stray_fairy_req())
#     set_rule(world.get_location('GB Stray Fairy Before Gyorg Room 2'), lambda state: (state.can_pop_balloon() or state.form('Zora')) and state.stray_fairy_req())

#     ## Boss: Gyorg
#     set_rule(world.get_location('Gyorgs Remains'), lambda state: state.form('Zora') and state.can_use('Bow'))


#     ### IKANA CANYON
#     set_rule(world.get_location('Ikana Entrance Bombchu Pit'), lambda state: state.form('Goron'))
#     # todo: check this spot in the game

#     set_rule(world.get_location('Stone Mask'), lambda state: state.can_epona() and state.has_bottle() and state.can_use('Lens of Truth'))

#     set_rule(world.get_location('Ikana Graveyard Bombchu Pit'), lambda state: state.can_blast())
#     # todo: test if blast mask works here

#     set_rule(world.get_location('Ikana Graveyard Dampe 30 Rupee Prize'), lambda state: state.can_pop_balloon() or state.form('Human'))

#     set_rule(world.get_location('Captains Hat'), lambda state: state.has('Sonata of Awakening') and (state.can_use('Bow') or state.can_use('Bunny Hood')))
#     # oh jeez, there are various glitches to get this chest huh?
#     # todo: reaseach this chest

#     set_rule(world.get_location('Ikana Graveyard First Night Grave 50 Rupee Chest'), lambda state: state.can_use('Captains Hat'))
#     set_rule(world.get_location('Learn Song of Storms'), lambda state: state.can_use('Captains Hat') and state.has('Bow') and state.has('Fire Arrows'))
#     set_rule(world.get_location('Ikana Graveyard Second Night Grave HP'), lambda state: state.can_use('Captains Hat') and state.lens_req() and state.can_blast())
#     set_rule(world.get_location('Ikana Graveyard Third Night Grave Bottle'), lambda state: state.can_use('Captains Hat') and state.can_use('Bow'))

#     set_rule(world.get_location('Ikana Canyon Owl Statue'), lambda state: state.can_use('Bow') and state.has('Ice Arrows') and state.has('Hookshot'))
#     set_rule(world.get_location('Ikana Tingle Ikana Map'), lambda state: state.can_pop_balloon())
#     set_rule(world.get_location('Ikana Tingle Clock Town Map'), lambda state: state.can_pop_balloon())
#     set_rule(world.get_location('Ikana Tingle Pic'), lambda state: state.can_use('Picto Box'))
#     # really this check depends on the logical area the statue is in; if it's just in the whole map, then there's a
#     # bunch of reqs, but if it's in the upper region, then it's open
#     # I'll leave it open for now, but we'll have to check in on this at some point
#     # same with tingle actually

#     set_rule(world.get_location('Ikana Secret Shrine HP'), lambda state: state.has_hearts(16) and state.can_use('Light Arrows') and state.can_kill_lizalfos() and state.has('Hookshot'))

#     set_rule(world.get_location('Gibdo Mask'), lambda state: state.can_use('Bomb Bag') and state.form('Human') and state.has('Song of Healing'))

#     set_rule(world.get_location('Ghost Hut HP'), lambda state: state.can_use('Bow'))
#     # idek if you actually need the bow to do this, but probly; if not, the check is just for human form

#     ## Beneath the Well
#     set_rule(world.get_location('Beneath the Well 50 Rupee Chest 1'),
#              lambda state: state.can_use('Gibdo Mask') and state.has_bottle() and state.has('Blue Potion') and state.lens_req())
#     set_rule(world.get_location('Beneath the Well 50 Rupee Chest 2'),
#              lambda state: state.can_use('Gibdo Mask') and state.has_bottle() and state.has('Magic Beans', 5) and state.can_use('Deku Sticks'))
#     set_rule(world.get_location('Mirror Shield'),
#              lambda state: state.can_use('Gibdo Mask') and state.has_bottle() and state.has('Blue Potion') and
#                            state.has('Magic Beans') and state.has('Bow') and state.has('Bomb Bag') and
#                            (state.has('Eponas Song') or state.has('Romani Mask')) and state.has('Fire Arrows'))
#     # not actually as bad as I initially thought
#     # the mirror shield is a bit much lol

#     ## Ikana Castle
#     set_rule(world.get_location('Ikana Castle Pillar HP'), lambda state: state.form('Human') and state.form('Deku') and state.has('Bow'))
#     set_rule(world.get_location('Learn Elegy of Emptiness'), lambda state: state.can_use('Bow') and state.has('Fire Arrows') and state.has('Mirror Shield'))
#     # set_rule(world.get_location(''), lambda state: state)

#     ## Stone Tower Climb
#     set_rule(world.get_location('Stone Tower Owl Statue'),
#              lambda state: state.form('Human') and state.form('Goron') and state.form('Zora') and state.has('Hookshot') and state.has('Elegy of Emptiness'))


#     ### STONE TOWER TEMPLE
#     ## Regular
#     set_rule(world.get_location('ST Stray Fairy Entryway 1'), lambda state: state.can_use('Bow') and state.stray_fairy_req())
#     set_rule(world.get_location('ST Map Chest'), lambda state: state.can_use('Bomb Bag') and (state.has('Mirror Shield') or state.can_use('Light Arrows')) and state.form('Goron'))
#     set_rule(world.get_location('ST Map Room Key Chest'), lambda state: state.can_use('Bomb Bag') and state.form('Goron'))
#     set_rule(world.get_location('ST Stray Fairy Map Room'), lambda state: state.can_use('Bomb Bag') and state.has('Hookshot'))
#     set_rule(world.get_location('ST Pool Room Key Chest'), lambda state: state.form('Human') or state.form('Zora'))
#     set_rule(world.get_location('ST Compass Chest'), lambda state: (state.form('Zora') and state.can_use('Mirror Shield')) or state.can_use('Light Arrows'))
#     set_rule(world.get_location('ST Stray Fairy Mirror Network Room 1'), lambda state: (state.form('Goron') and state.can_use('Mirror Shield')) or state.can_use('Light Arrows'))
#     set_rule(world.get_location('ST Stray Fairy Mirror Network Room 2'), lambda state: (state.form('Goron') and state.can_use('Mirror Shield')) or state.can_use('Light Arrows'))
#     set_rule(world.get_location('ST Stray Fairy Lava Room Center Chest'), lambda state: state.form('Deku'))
#     set_rule(world.get_location('ST Stray Fairy Lava Room Switch Chest'), lambda state: state.form('Goron'))

#     set_rule(world.get_location('ST Light Arrows Chest'), lambda state: state.form('Human') or state.form('Zora'))
#     # todo: what forms/items can beat the garo master?

#     set_rule(world.get_location('ST Stray Fairy Pool Room Eyegore'), lambda state: state.can_use('Hookshot'))
#     set_rule(world.get_location('ST Stray Fairy Pool Room Behind Sun Block'), lambda state: state.can_use('Bomb Bag') and state.can_use('Light Arrows'))
#     # set_rule(world.get_location(''), lambda state: state)

#     ## Inverted
#     set_rule(world.get_location('ST Stray Fairy Inverted Entryway'), lambda state: state.can_use('Light Arrows') and state.can_reach(state.get_location('ST Entryway')))
#     set_rule(world.get_location('ST Inverted Compass Room Key Chest'), lambda state: state.can_use('Light Arrows') and state.form('Deku'))
#     set_rule(world.get_location('ST Stray Fairy Inverted Compass Room 1'),
#              lambda state: state.can_reach(state.get_location('ST Compass Room')) and state.form('Zora') and state.can_use('Light Arrows') and state.form('Deku'))
#     set_rule(world.get_location('ST Stray Fairy Inverted Compass Room 2'),
#              lambda state: state.can_reach(state.get_location('ST Compass Room')) and state.can_use('Fire Arrows')
#                            and state.can_use('Light Arrows') and state.form('Deku') and state.has('Elegy of Emptiness'))
#     set_rule(world.get_location('ST Stray Fairy Compass Room'),
#              lambda state: state.can_reach(state.get_location('ST Compass Room')) and state.can_use('Light Arrows'))
#     set_rule(world.get_location('ST Stray Fairy Wizrobe Room'), lambda state: state.can_use('Bow') and state.can_use('Hookshot'))
#     set_rule(world.get_location('ST Inverted Map Room Key'), lambda state: state.has('Elegy of Emptiness'))
#     set_rule(world.get_location('ST Boss Key Chest'), lambda state: state.can_use('Light Arrows'))
#     set_rule(world.get_location('ST Stray Fairy Entryway 2'),
#              lambda state: state.can_reach(state.get_location('ST Entryway')) and (state.can_use('Light Arrow') or state.can_use('Stone Mask')))
#     set_rule(world.get_location('ST Stray Fairy Post Garo Master Room'), lambda state: state.can_reach(state.get_location('ST Post Garo Master Room')) and state.can_use('Bow'))
#     # set_rule(world.get_location('Giants Mask'), lambda state: ([state.can_use(x) for x in ['Bow', 'Hookshot', 'Bomb Bag']].count(True) > 0) or state.form('Zora') or (state.form('Deku') and state.has('Magic Meter')))
#     # leaving this as an open check because you need lights to get to the eyegore, which can beat him already
#     # unless there's a possible path say in entrance shuffle that could allow you to reach here another way
#     # figure that out later, that'll take more defined region logic

#     ## Boss: Twinmold
#     set_rule(world.get_location('Twinmodls Remains'), lambda state: state.can_use('Giants Mask') or state.can_use('Bow'))


#     ### THE MOON
#     set_rule(world.get_location('Moon Odolwa Child HP'), lambda state: state.form('Deku'))
#     set_rule(world.get_location('Moon Ghot Child HP'), lambda state: state.form('Goron'))
#     set_rule(world.get_location('Moon Gyorg Child HP'), lambda state: state.form('Zora'))
#     set_rule(world.get_location('Moon Twinmold Child Bombchu Chest'), lambda state: state.can_use('Light Arrows') and state.has('Hookshot') and state.can_kill_lizalfos())
#     set_rule(world.get_location('Moon Twinmold Child HP'), lambda state: state.can_use('Light Arrows') and state.has('Hookshot') and state.can_kill_lizalfos() and state.can_use('Bombchus'))
#     set_rule(world.get_location('Fierce Deity Mask'), lambda state: state.has('Mask', 20))
#     # we still need to determine how to deal with the counting of the masks for this section, but I'll leave it like this for now


# # ooh ooh
# # maybe have a gate at the clock tower roof that requires the ocarina, to go back to south clock town on the first day
# # maayyybe
# # to force placement of the ocarina somewhere you can get to it in the first cycle
# # depends on how crawling through the graph works
# # todo: go through and put in checks (that shouldn't get shuffled!) for various steps of quests
# # like, 'looked at skull kid in telescope' to be used to get the moon's tear, or all the various steps in the a+k quest
