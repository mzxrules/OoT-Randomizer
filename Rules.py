import collections
import logging


def set_rules(world):
    global_rules(world)
    '''
    if world.bridge == 'medallions':
        # require all medallions to form the bridge
        set_rule(world.get_entrance('Rainbow Bridge'), lambda state: state.has('Forest Medallion') and state.has('Fire Medallion') and state.has('Water Medallion') and state.has('Shadow Medallion') and state.has('Spirit Medallion') and state.has('Light Medallion'))
    elif world.bridge == 'vanilla':
        # require only what vanilla did to form the bridge
        set_rule(world.get_entrance('Rainbow Bridge'), lambda state: state.has('Light Arrows') and state.has('Shadow Medallion') and state.has('Spirit Medallion'))
    elif world.bridge == 'dungeons':
        # require all medallions and stones to form the bridge
        set_rule(world.get_entrance('Rainbow Bridge'), lambda state: state.has('Forest Medallion') and state.has('Fire Medallion') and state.has('Water Medallion') and state.has('Shadow Medallion') and state.has('Spirit Medallion') and state.has('Light Medallion') and state.has('Kokiri Emerald') and state.has('Goron Ruby') and state.has('Zora Sapphire'))
    '''

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
    set_rule(world.get_location('Snowhead GF Reward'), lambda state: state.has('SH SF', 15))
    set_rule(world.get_location('Great Bay GF Reward'), lambda state: state.has('GB SF', 15))
    set_rule(world.get_location('Stone Tower GF Reward'), lambda state: state.has('ST SF', 15))

    set_rule(world.get_location('Clock Town Mailbox HP'), lambda state: state.can_use('Postman Hat'))

    # set_rule(world.get_location('Swamp Business Scrub'), lambda state: state.has('Town Title Deed') and state.form('Human'))
    # set_rule(world.get_location('Mountain Business Scrub'), lambda state: state.has('Swamp Title Deed') and state.form('Deku'))
    # set_rule(world.get_location('Ocean Business Scrub'), lambda state: state.has('Mountain Title Deed') and state.form('Goron'))
    # set_rule(world.get_location('Canyon Business Scrub'), lambda state: state.has('Ocean Title Deed') and state.form('Zora'))
    # for each of these, I think the title deed checks can simply be put on the locations they gate
    # unless there's one that gates a few things, but I can't think of that offhand

    set_rule(world.get_location('Song From HMS'), lambda state: state.has('Ocarina of Time'))
    set_rule(world.get_location('Remove the Cursed Mask'), lambda state: state.has('Ocarina of Time'))

    # RevelationOrange started adding rules here (plus a few changes in rules above)
    # location names used are mostly guesses and can absolutely be changed later
    # item names used are also guesses, as are some state function names probly
    # location names may be longer than necessary so as to be descriptive, like we can change 'South Clock Town Hookshot
    # Ledge Rupee Chest' if we want lol

    ### SOUTH CLOCK TOWN
    set_rule(world.get_location('Clock Town Business Scrub Item'), lambda state: state.has('Moons Tear'))
    set_rule(world.get_location('Clock Town Business Scrub Trade Done'), lambda state: state.has('Moons Tear'))
    set_rule(world.get_location('Clock Tower Platform HP'), lambda state: state.form('Human') or state.form('Zora') or (state.form('Deku') and (state.has('Moons Tear') or state.can('Gainer'))))

    set_rule(world.get_location('Festival Tower Rupee Chest'), lambda state: state.can_use('Hookshot') or (state.form('Deku') and state.has('Moons Tear')))
    set_rule(world.get_location('SCT 20 Rupee Chest'), lambda state: state.can_use('Hookshot')
                or (state.form('Deku') and state.has('Moons Tear') and (state.form('Human') or state.form('Zora'))))

    set_rule(world.get_location('Dropped Ocarina'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Song From Skull Kid'), lambda state: state.can_pop_balloon())
    # is this right? it looks like the check is just to hit skull kid in the air, functionally the same as popping a balloon lol
    set_rule(world.get_entrance('End of First Cycle'), lambda state: state.has('Song of Time'))
    set_rule(world.get_entrance('Moon Portal'),
             lambda state: [state.has(x) for x in ['Oath to Order', 'Odolwas Remains', 'Ghots Remains', 'Gyorgs Remains', 'Twinmolds Remains']].count(True) == 5)
    set_rule(world.get_entrance('To Clock Tower Rooftop'), lambda state: state.form('Human') or state.form('Zora') or (state.form('Deku') and (state.has('Moons Tear') or state.can('Gainer'))))

    set_rule(world.get_location('Clock Town Owl Statue'), lambda state: state.form('Human'))

    set_rule(world.get_entrance('Clock Town North Gate'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or state.can('Clock Town Guard Skip'))


    ### LAUNDRY POOL
    set_rule(world.get_location('Listen To Guru Guru'), lambda state: state.form('Human') or state.form('Zora') or state.form('Goron'))
    set_rule(world.get_location('Don Gero Town Frog'), lambda state: state.can_use('Don Gero Mask'))

    # set_rule(world.get_entrance('Curiosity Backroom Entrance'), lambda state: state.event('Something about the a+k quest'))
    # set_rule(world.get_location('Keaton Mask From Kafei'), lambda state: state.event('Something about the a+k quest'))
    # set_rule(world.get_location('Letter From Kafei'), lambda state: state.event('Something about the a+k quest'))
    # set_rule(world.get_location('Pendant From Kafei'), lambda state: state.event('Something about the a+k quest'))
    # *sigh* this quest
    # todo: gestures vaguely at everything about this quest


    ### WEST CLOCK TOWN
    set_rule(world.get_location('Rosa Sisters HP'), lambda state: state.can_use('Kamaro Mask'))

    # you might not need to be human to get this, but I'd bet the shop owner won't sell to other forms, at least deku
    # set_rule(world.get_location('Buy Bomb Bag'), lambda state: True)
    # this can be tested easily

    # obviously, this and similar 'tests' might not be necessary at all
    # set_rule(world.get_location('Bank 200 Rupee Prize'), lambda state: True)
    # set_rule(world.get_location('Bank HP'), lambda state: True)

    # set_rule(world.get_location('Hidden Owl Statue'), lambda state: state.can_do_some_glitch_or_something())
    # I actually have no idea what the check is here lol

    set_rule(world.get_location('Buy Bigger Bomb Bag'), lambda state: state.form('Human') or state.form('Zora') or state.has('Adult Wallet'))
    # adult wallet is a req because if you don't rescue the old lady from sakon, the big bomb bag shows up in the
    # curiosity shop on the final day (still might be form restrictions?)

    set_rule(world.get_location('Sword School HP'), lambda state: state.form('Human'))

    # i swear this should be an optional trick, it's so hard without the bunny hood lol
    # set_rule(world.get_location('Counting Is Hard'), lambda state: True)
    # sigh alright we'll make this open lol

    set_rule(world.get_location('Buy All Night Mask'), lambda state: state.form('Human') and state.has('Giants Wallet'))
    # you need to save the bomb lady from sakon and this will be in the curio shop on the final day for 500 rupees
    # being human might be a hard req, but you can probly buy it as zora (todo: test that)

    set_rule(world.get_location('Deliver Letter to Mama To Postman'), lambda state: state.has('Letter to Mama'))

    set_rule(world.get_entrance('Clock Town West Gate'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or state.can('Clock Town Guard Skip'))


    ### NORTH CLOCK TOWN
    # I don't know that this item matters at all or if we should even have a spot for it
    # but we can if we want, you get it the same way you get the code in the first cycle, you just have to be human to
    # get the actual notebook from them I think
    set_rule(world.get_location('Bomber Notebook'), lambda state: state.can_pop_balloon() and state.form('Human'))

    set_rule(world.get_location('Bomber Code'), lambda state: state.can_pop_balloon() and (state.form('Human') or state.form('Deku')))
    # set_rule(world.get_location('Bomber Code'), lambda state: state.has('Magic Meter') and state.form('Deku'))
    # for the bomber code, it's essentially only can_reach('pop NCT balloon'), you don't need to be human
    # you know, for the popping the balloon test, that might just be a general state.can('pop balloon')
    # since it shows up in several places, and the NCT balloon isn't any different than others (I believe, lol)

    # since getting the blast mask just involves slashing sakon, it might be possible to get it with other forms? like
    # maybe zora? probly not goron though
    # also you might need to be link to talk to the lady after, so maybe it is only human
    set_rule(world.get_location('Foil Sakon'), lambda state: state.form('Human') or state.form('Zora'))

    set_rule(world.get_location('NCT Tree HP'), lambda state: state.form('Human') or state.form('Zora'))
    # I thought deku could get this for some reason
    # also lol of course goron can't, shoulda known

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
    # the thing the great fairy gives you depends on the cycle... I think? so I'm not sure how to
    # handle this/these checks
    # also, is goron the only form that can't get a stray fairy? it might be able to anyway, by getting the laundry pool
    # fairy and then falling into the water lol

    # set_rule(world.get_location('Magic from NCT Great Fairy'), lambda state: state.form('Deku'))
    # I'll have to test how this happens, I haven't played in so long
    # first cycle she gives you magic because you're stuck as deku, afterwards she gives you the mask because you're human
    # right?
    # so what if you start as goron or zora? not sure how that all works

    set_rule(world.get_entrance('Clock Town North Gate'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or state.can('Clock Town Guard Skip'))

    ### EAST CLOCK TOWN
    set_rule(world.get_location('ECT 100 Rupee Chest'), lambda state: state.form('Human') or state.can('Goron Boost') or state.can('Gainer') or state.form('Zora'))
    # I need to figure out all the actual requirements for this, including tricks, so this one is tentative
    # also the trick names are guesses for sure

    set_rule(world.get_location('Treasure Chest Game Goron Prize'), lambda state: state.form('Goron'))
    # oooh I didn't think about it before, do we want to include all the prizes for this?
    set_rule(world.get_location('Treasure Chest Game Human Prize'), lambda state: state.form('Human'))
    set_rule(world.get_location('Treasure Chest Game Zora Prize'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Treasure Chest Game Deku Prize'), lambda state: state.form('Deku'))

    set_rule(world.get_entrance('Bomber Bouncer'), lambda state: state.has('Bomber Code'))
    set_rule(world.get_location('Bomber Tunnel Chest'), lambda state: state.can_blast() and (state.form('Human') or state.form('Zora')))
    set_rule(world.get_entrance('Tunnel Balloon From ECT'), lambda state: state.can_pop_balloon())
    set_rule(world.get_entrance('Tunnel Balloon From Observatory'), lambda state: state.can_pop_balloon() or state.form('Human'))
    # set_rule(world.get_location('Moon Cry'), lambda state: True)
    set_rule(world.get_location('Watch Business Scrub Fly'), lambda state: state.event('Traded Town Title Deed'))

    set_rule(world.get_location('Honey and Darling Grand Champion'), lambda state: state.has('Bomb Bag') and state.has('Bow') and state.form('Human'))
    set_rule(world.get_location('Town Shooting Gallery Quiver Prize'), lambda state: state.can_use('Bow'))
    set_rule(world.get_location('Town Shooting Gallery HP Prize'), lambda state: state.can_use('Bow') or state.options('NoHardestArchery'))

    set_rule(world.get_location('Expert Person Solver Takes the Case'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora'))

    set_rule(world.get_entrance('To Stock Pot Inn Secret Entrance'), lambda state: state.form('Deku'))
    set_rule(world.get_location('Stock Pot Inn Key'), lambda state: state.any_form_but('Deku'))
    set_rule(world.get_location('Have you seen this man?'), lambda state: state.can_use('Kafei Mask'))
    set_rule(world.get_location('Your Room Rupee Chest'), lambda state: state.has('Inn Key'))
    set_rule(world.get_location('Anjus Room Rupee Chest'), lambda state: state.has('Inn Key') or state.form('Deku'))
    # ok, so these chests
    # the one for your room requires the room key regardless, right?
    # the anju room one is accessible only after midnight on the 3rd day, so you just need to get into the inn somehow
    # but leaving the regular entrance open means it looks like you can always get to that chest
    # so I think what we do is just put the restrictions on the actual checks- conceptually wrong, but it works fine
    # the other option would be to create another logical area ex: 'Stock Pot Inn After Hours'
    # and the item checks there would be open
    # which we can do, either way works
    set_rule(world.get_location('Grandma Stories HP 1'), lambda state: state.can_use('All Night Mask'))
    set_rule(world.get_location('Grandma Stories HP 2'), lambda state: state.can_use('All Night Mask'))

    set_rule(world.get_location('Toilet Hand HP'), lambda state: state.has_paper())
    # you need some kind of paper, so any title deed, or a letter from the various subquests that involve letters
    # that's a lot of different ways to be able to do that, so we may need to have inventory record any subquest item
    # that can be obtained as obtained, so we can just do state.has('any paper') or something
    # for now I'll just leave it as the clock town title deed check, the easiest one to do
    # todo: test everything that can be used as paper and record reqs to get them, OR them all together for this check
    # man, this one is involved lol
    # actually you know what, I'm just gonna add state.has_paper()

    set_rule(world.get_entrance('To Milk Bar'), lambda state: state.can_use('Romani Mask'))
    set_rule(world.get_location('Milk Bar Performance'), lambda state: False not in [state.form(f) for f in ['Human', 'Deku', 'Goron', 'Zora']] and state.has('Ocarina'))
    set_rule(world.get_location('Delivery to Mama Kafei'), lambda state: state.has('Letter to Mama'))
    # so a note about doing checks for stuff like 'Letter to Mama' and stuff that resets when you save
    # it makes it a hell of a lot easier to be able to do checks for temp items like this
    # but it also probably means setting rules for these items and having locations for them
    # which means we'd have to have some kind of marker for them so they don't get mixed in to the pool
    # possibly issue in the future, just something to note for now

    set_rule(world.get_location('Mayor HP'), lambda state: state.can_use('Couples Mask'))

    set_rule(world.get_entrance('Clock Town East Gate'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or state.can('Clock Town Guard Skip'))

    ### TERMINA FIELD
    set_rule(world.get_entrance('Astral Observatory Fence'), lambda state: (state.has('Magic Beans') and state.has_bottle()) or state.can('Goron Boost'))

    set_rule(world.get_entrance('TF to Obs Over Fence Maybe'), lambda state: state.can('Goron Boost'))
    # I don't know if there's actually a way to get over this fence from TF, might only be the other way, so I might
    # have remove this later

    set_rule(world.get_location('Learn Kamaro Dance'), lambda state: state.form('Human') or state.form('Goron'))
    # so you have to be able to jump to their platform, which rules out goron and probably deku?
    # (actually maybe not if the goron can do some weird trick or something)
    # dunno if there's a form requirement when you actually talk to them, but I'm gonna assume human for now
    # todo: test form requirements

    set_rule(world.get_entrance('TF Mountain Icicles'), lambda state: state.can_use('Bow') or state.form('Goron'))
    set_rule(world.get_entrance('TF Great Bay Gate'), lambda state: (state.form('Human') and state.has('Eponas Song'))
                                                                    or state.can('Some Goron Trick probly'))

    set_rule(world.get_location('Moons Tear'), lambda state: state.event('Moon Cry'))

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
             lambda state: state.event('Swamp Gossip Check') and state.event('Mountain Gossip Check')
                           and state.event('Ocean Gossip Check') and state.event('Canyon Gossip Check'))

    set_rule(world.get_location('TF Peahat Grotto HP'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora'))
    # how many ways to kill a peahat? lol
    # for now I'm gonna assume deku can't, but everyone else can

    # set_rule(world.get_location('TF Dodongo Grotto HP'), lambda state: True)
    # ways to kill a dodongo? might be anyone actually

    set_rule(world.get_entrance('To TF Business Scrub Grotto'), lambda state: state.event('Saw Scrub Fly In'))
    set_rule(world.get_location('TF Business Scrub Grotto HP'), lambda state: state.has('Adult Wallet'))
    # giving the moon's tear to the scrub is part of the connection requirement to get to the grotto, but once there
    # you just need the adult's wallet

    set_rule(world.get_location('TF Beehive Grotto HP'), lambda state: (state.can_blast() or state.form('Goron'))
                                                                                  and state.can_use('Bow') and state.form('Zora'))
    # boulder to get through, then shoot the bees, then drop to the bottom of the pool as zora
    # actually shooting the bees might be possible as zora
    # bees might just be more balloons lol
    # todo: test this hp

    # set_rule(world.get_location('TF Chest In The Grass'), lambda state: True)
    # set_rule(world.get_location('TF Deku Baba Pit Chest'), lambda state: True)
    set_rule(world.get_location('TF Chest On A Stump'), lambda state: state.can_use('Hookshot'))

    # set_rule(world.get_location(''), lambda state: state)
    # apparently if you look at some guys standing in the field through the telescope, there will be pits where they
    # each were? dunno what's in them, but we might need to record those
    # todo: test this

    set_rule(world.get_entrance('To East Pillar Grotto'),
             lambda state: state.has_bottle() and state.has('Magic Beans') and (state.form('Human') or state.form('Zora')))
    # it's an open check once you're there, you just need a bottle, bean, water, and be able to jump to it from the bean


    ### SOUTHERN SWAMP

    ## Path to Swamp
    set_rule(world.get_location('Swamp Path Bat Tree HP'), lambda state: state.can_pop_balloon() or state.form('Human'))
    # the req for this is just to make it up the tree without getting knocked off by the birds, so unless there's some
    # way of cheesing the birds I don't know about, you just have to be able to kill them
    # ...you know, birds are just balloons that try to kill you tbh

    set_rule(world.get_location('Swamp Tingle Woodfall Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Swamp Tingle Snowhead Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Swamp Tingle Pic'), lambda state: state.can_use('Picto Box'))

    # set_rule(world.get_location('Swamp Path Rupee Pit Chest'), lambda state: True)
    # there's apparently 20 rupees in a pit, it's probly just open, but I need to play again to check the details

    set_rule(world.get_location('Swamp Shooting Gallery Quiver Prize'), lambda state: state.can_use('Bow'))
    set_rule(world.get_location('Swamp Shooting Gallery HP Prize'), lambda state: state.can_use('Bow'))
    # or state.options('NoHardestArchery')
    # that doesn't work now that I think about it
    # it means if the option is checked, this is treated as open, obviously wrong
    # otherwise nothing can be placed there
    # so todo: determine how to restrict progression items from this spot if the option is selected
    # (there's probly a mechanism for this in testrunner's build)

    set_rule(world.get_entrance('Swamp Path To Southern Swamp (Cleaned)'), lambda state: state.event('Defeat Odolwa'))

    ## Southern Swamp
    set_rule(world.get_location('Swamp Tourist Roof HP'), lambda state: state.has('Town Title Deed') or state.can('Goron Boost'))
    # set_rule(world.get_location('Bottle From Kotate'), lambda state: True)
    # set_rule(world.get_location('Save Koume'), lambda state: True)
    set_rule(world.get_location('Swamp Owl Statue'), lambda state: state.form('Human'))
    set_rule(world.get_location('Kill Swamp Big Octo'), lambda state: state.can_use('Bow') or state.can_use('Hookshot') or state.form('Zora'))
    set_rule(world.get_location('Kill Swamp Big Octo From Palace'), lambda state: state.can_use('Bow') or state.can_use('Hookshot'))
    # what are all the ways this you can kill the big octo? note, using the boat cruise to kill it will be a separate
    # check located in the tourist center

    set_rule(world.get_entrance('Swamp Big Octo From Tourist Region'), lambda state: state.event('Swamp Big Octo Dead'))
    set_rule(world.get_entrance('Swamp Big Octo From Octo Region'), lambda state: state.event('Swamp Big Octo Dead'))

    # swamp tourist center
    set_rule(world.get_location('Picto Box'), lambda state: state.event('Saved Koume'))
    set_rule(world.get_location('Pictograph Contest Winner'), lambda state: state.has('Tingle Pic') or state.has('Deku King Pic'))
    set_rule(world.get_location('Kill Swamp Big Octo With Boat'), lambda state: state.event('Saved Koume'))
    set_rule(world.get_entrance('Swamp Boat Ride'), lambda state: state.event('Saved Koume'))

    # potion shop and lost woods
    set_rule(world.get_location('Red Potion To Help Koume'), lambda state: state.event('Checked Koume'))
    set_rule(world.get_location('Saved Koume'), lambda state: state.has_bottle())

    # swamp tourist center clean water
    set_rule(world.get_location('Swamp Boat Archery HP'), lambda state: state.can_use('Bow') and state.event('Defeat Odolwa'))

    set_rule(world.get_entrance('Octo Grotto Clean Exit'), lambda state: state.event('Defeat Odolwa'))
    set_rule(world.get_entrance('Poisoned To Swamp Spider House'), lambda state: state.can_use('Fire Arrows'))
    set_rule(world.get_entrance('Poisoned Lower Octo Region Trick To Upper Midpoint'), lambda state: state.can('Some Jumping Trick') and state.form('Human'))
    # I've seen this done as human, dunno the details, but the check is going to essentially look like this
    set_rule(world.get_entrance('Poisoned Octo Upper Near Palace To Midpoint'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Poisoned Octo Upper Midpoint To Near Palace'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Poisoned Octo Upper Midpoint To Kaepora'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Poisoned Octo Kaepora To Midpoint'), lambda state: state.form('Deku'))
    set_rule(world.get_location('Song From Kaepora Gaebora'), lambda state: state.has('Ocarina'))
    # form req?

    ## Deku Palace
    set_rule(world.get_entrance('Poisoned Outer Palace To Octo Upper'), lambda state: state.form('Deku') or state.can('Gainer'))
    # does gainer work here? or is it strictly deku

    set_rule(world.get_entrance('Poisoned Palace To Butler Race'), lambda state: state.form('Deku') or (state.has_hearts(6) and (state.form('Human') or state.form('Zora'))))
    set_rule(world.get_entrance('Poisoned Outer Palace To Lower Courtyard'), lambda state: state.form('Deku') or (state.can('Deku Palace Guard Skip')))
    # not sure how the trick to get past the palace guards works, but it's essentially that option plus form(s)

    set_rule(world.get_entrance('Poisoned Outer Palace To Upper Courtyard'), lambda state: state.has_bottle() and state.has('Magic Beans')
                                    and (state.form('Deku') or (state.has_hearts(6) and state.any_form_but('Goron'))))
    # set_rule(world.get_entrance('To Magic Beans'), lambda state: True)
    set_rule(world.get_location('Magic Beans'), lambda state: state.form('Human'))
    # will he sell you the beans even if you don't have a bottle? it seems like he should
    # todo: find out
    set_rule(world.get_entrance('Magic Bean Grotto Clean Exit'), lambda state: state.event('Defeat Odolwa'))

    # set_rule(world.get_location('Deku Palace Courtyard HP'), lambda state: True)
    set_rule(world.get_entrance('Poisoned Deku Palace Lower Courtyard To Upper'), lambda state: state.can('Deku Palace Coutryard Trick'))
    # not sure of the details on this, but I'm pretty sure it exists
    set_rule(world.get_entrance('Poisoned Deku Palace Upper Courtyard To Throne Room Cage Region'), lambda state: state.form('Deku'))
    set_rule(world.get_location('Song From Monkey'), lambda state: state.form('Deku') and state.has('Ocarina'))
    # probly need to test the reqs for this, but apparently you need to talk to the monkey as link and then show him an
    # instrument that isn't the ocarina to learn it? I dunno
    # todo: test requirements for this

    set_rule(world.get_entrance('Butler Race Clean Exit'), lambda state: state.event('Defeat Odolwa'))

    # post woodfall palace
    set_rule(world.get_location('Return Deku Princess'), lambda state: state.form('Deku') and state.has('Deku Princess'))
    set_rule(world.get_location('Butler Race Prize'), lambda state: state.form('Human') and state.event('Returned Deku Princess') and state.event('Defeat Odolwa'))
    # you know, I have no idea what the actual requirements are to do this lol
    # once you can get here, you can attempt the race, but I figure goron can't do it, zora probly not
    # so it's human and/or deku? todo: figure this out lol

    ## Swamp Spider House
    # oh god, so many spots
    # lots of them are probly just open though
    # I'mma get to this later, I'll do both the spider houses together
    set_rule(world.get_location('Swamp Spider House Reward'),
             lambda state: state.has_bottle() and state.form('Deku') and state.has('Sonata of Awakening') and state.can_pop_balloon() and state.can_use('Bomb Bag'))
    # there might be some other requirements to get all the skulls here, but I'm pretty sure you at least need a
    # bottle and to use deku flowers
    set_rule(world.get_entrance('Swamp Spider House Clean Exit'), lambda state: state.event('Defeat Odolwa'))

    ## Outside Woodfall Area
    # todo: where can the hookshot get you in this area?
    set_rule(world.get_location('Outside Woodfall 20 Rupee Chest'),
             lambda state: state.form('Deku') or (state.form('Human') and (state.has('Hookshot') or state.has_hearts(5))) or (state.form('Zora') and state.has_hearts(5)))
    # I think you can get to this one by toughing out the poison water as well as just being deku
    # or also with the hookshot? also do ice arrows freeze poison water?
    # todo: test ways to get to this chest
    set_rule(world.get_entrance('Poisoned Outside Woodfall Entrance To Woodfall Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Poisoned Outside Woodfall Entrance To Fountain Platform'), lambda state: (state.form('Human') or state.form('Zora')) and state.has_hearts(8))

    set_rule(world.get_location('Outside Woodfall 5 Rupee Chest'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_location('Woodfall Owl Statue (Poisoned)'), lambda state: state.form('Human'))
    set_rule(world.get_entrance('Poisoned Owl Platform To Entrance'), lambda state: state.form('Deku') or (state.has_hearts(10) and state.any_form_but('Goron')))
    set_rule(world.get_entrance('Poisoned Owl Platform To Fountain Platform'), lambda state: state.form('Deku') or (state.has_hearts(4) and state.any_form_but('Goron')))
    set_rule(world.get_entrance('Poisoned Owl Platform To Temple Platform'), lambda state: state.form('Deku') and state.has('Sonata Of Awakening'))

    set_rule(world.get_entrance('Poisoned Woodfall Temple Platform To Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Poisoned Woodfall Temple Platform To Entrance'), lambda state: (state.form('Human') or state.form('Zora')) and state.has_hearts(5))

    set_rule(world.get_location('Outside Woodfall HP'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_entrance('Poisoned Fountain Platform To Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Poisoned Fountain Platform To Entrance'), lambda state: state.form('Deku') or (state.has_hearts(10) and state.any_form_but('Goron')))
    set_rule(world.get_entrance('Poisoned Fountain Platform To Fountain'), lambda state: state.form('Deku') or state.can('Gainer'))
    # dunno if gainer actually works here, but it seems like the kind of spot where it would

    set_rule(world.get_location('Woodfall GF Reward'), lambda state: state.has('WF SF', 15))
    set_rule(world.get_entrance('Woodfall Fountain Clean Exit'), lambda state: state.event('Defeat Odolwa'))


    ### WOODFALL TEMPLE

    ## Lobby
    set_rule(world.get_location('WF Stray Fairy Entrance'), lambda state: state.stray_fairy_req(state.any_form_but('Goron')))

    set_rule(world.get_location('WF Stray Fairy Lobby Chest'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Poisoned Entrance To Central Room'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Boss Warp'), lambda state: state.has('Odolwas Remains'))

    ## First Floor
    set_rule(world.get_location('WF Stray Fairy Poisoned Central Room Deku Baba'), lambda state: state.stray_fairy_req())
    set_rule(world.get_entrance('WF Poisoned Central Room SW To Fairy Region'), lambda state: state.can_use('Bow') and state.can_use('Great Fairy Mask'))
    # set_rule(world.get_location('WF Stray Fairy Central Room Upper Bubble'), lambda state: True)

    set_rule(world.get_location('WF Poisoned Central Room Gate Torch Using Fire Arrows'), lambda state: state.can_use('Fire Arrows'))
    set_rule(world.get_location('WF Clean Poison Water Using Fire Arrows'), lambda state: state.can_use('Fire Arrows'))
    set_rule(world.get_entrance('WF Clean Poison Water Using Fire Arrows Exit'), lambda state: state.can_use('Fire Arrows'))
    set_rule(world.get_entrance('WF Poisoned Central Room SW To Push Block Room'), lambda state: state.has('Small Key (Woodfall Temple)'))
    set_rule(world.get_entrance('WF Poisoned Central Room SW To Upper'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_location('WF Stray Fairy Poisoned Central Room SE Corner'), lambda state: state.stray_fairy_req())
    set_rule(world.get_entrance('WF Poisoned Central Room Fairy Platform To SW'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Poisoned Central Room Fairy Platform To East'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Poisoned Central Room Fairy Platform To Upper'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Poisoned Central Room East To Fairy Platform'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Poisoned Central Room East To Upper'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Poisoned Central Room East To Ladder Up'), lambda state: state.event('WF Central Room Ladder Switch'))
    set_rule(world.get_entrance('WF Poisoned Central Room Upper To Fairy Region'),
             lambda state: state.stray_fairy_req(state.can_pop_balloon() or state.form('Human')))
    set_rule(world.get_location('WF Stray Fairy Poisoned Central Room Upper Switch Chest'),
             lambda state: state.form('Deku') and state.any_form_but('Deku') and state.stray_fairy_req())
    # for reference: these two are good examples of how the stray fairy req fxn works
    set_rule(world.get_location('WF Poisoned Central Room Ladder Switch'), lambda state: state.any_form_but('Deku'))
    set_rule(world.get_location('WF Clean Poison Water'), lambda state: state.can_use('Bow'))
    set_rule(world.get_entrance('WF Clean Poison Water Exit'), lambda state: state.can_use('Bow'))
    set_rule(world.get_entrance('WF Poisoned Central Room Upper To Pre Boss Room'), lambda state: state.event('WF Central Room Gate Torch Lit'))
    set_rule(world.get_entrance('WF Poisoned Central Room Upper To SW'), lambda state: state.any_form_but('Goron'))

    # set_rule(world.get_location('WF Stray Fairy Elevator Room'), lambda state: True)
    # this fairy is an open check because it's in its own logical region, with two exits leading to it that form the
    # actual checks
    set_rule(world.get_location('WF Activate Elevator From Poisoned West Lower'), lambda state: state.can_use('Bow'))
    set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To Fairy Region'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
    set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To North Upper'), lambda state: (state.event('WF Elevator On') and state.form('Deku')))
    set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To SW Upper'), lambda state: (state.event('WF Elevator On') and state.form('Deku')))
    set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To East Lower'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Poisoned Elevator Room West Lower To Key Chest'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    # set_rule(world.get_location('WF Elevator Room Key Chest'), lambda state: True)
    set_rule(world.get_location('WF Activate Elevator From Poisoned East Lower'), lambda state: state.can_use('Bow'))
    # ^ example of the same event needing to go in multiple spots; need to change to a logical region and have only a single item location?
    set_rule(world.get_entrance('WF Poisoned Elevator Room East Lower To West Lower'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Poisoned Elevator Room North Upper To West Lower'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Poisoned Elevator Room North Upper To East Lower'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Poisoned Elevator Room North Upper To Key Chest'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Poisoned Elevator Room North Upper To Fairy Region'),
             lambda state: state.form('Human') or state.form('Zora') or (state.form('Deku') and state.has('Magic Meter')))
    set_rule(world.get_entrance('WF Poisoned Elevator Room SW Upper To West Lower'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Poisoned Elevator Room SW Upper To East Lower'), lambda state: state.can_use('Hookshot'))

    set_rule(world.get_location('WF Map Chest'),
             lambda state: state.form('Deku') or state.can_use('Bomb Bag') or state.form('Goron'))
    # possibly the blast mask can be used as well? in which case just change this to can_blast()
    # can this actually be done strictly with deku? todo: more testing on this I think

    ## Push Block Bridge Room
    set_rule(world.get_location('WF Stray Fairy Poisoned Push Block Room Hive'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
    set_rule(world.get_location('WF Stray Fairy Poisoned Push Block Room Skulltula'), lambda state: state.stray_fairy_req())
    set_rule(world.get_entrance('WF Poisoned Push Block Room Lower To Compass Room'), lambda state: state.can_use('Deku Sticks') or state.can_use('Fire Arrows'))
    set_rule(world.get_entrance('WF Poisoned Push Block Room Lower To Upper'), lambda state: state.can_use('Deku Sticks') or state.can_use('Bow'))
    set_rule(world.get_entrance('WF Poisoned Push Block Room Upper To Lower'), lambda state: state.can_use('Deku Sticks') or state.can_use('Bow'))
    # yep, you can in fact light the right torches (aside from the compass room one) and hit the spider web with just the bow
    # though honestly can_use('deku sticks') should maybe just be form('Human'); though for entrance rando, maybe not
    set_rule(world.get_entrance('WF Poisoned Push Block Room Lower To Fairy Region'),
             lambda state: state.stray_fairy_req(state.has_hearts(7) and (state.form('Human') or state.form('Zora'))))

    set_rule(world.get_entrance('WF Cleaned Push Block Room Lower To Fairy Region'), lambda state: state.stray_fairy_req(state.form('Human') or state.form('Zora')))

    # set_rule(world.get_location('WF Stray Fairy Push Block Room Underwater'), lambda state: True)
    # set_rule(world.get_location('WF Compass Chest'), lambda state: True)
    # turns out anyone can kill dragonflies lol, so this is an open check
    set_rule(world.get_entrance('WF Compass Room Clean Exit'), lambda state: state.event('Cleaned WF'))

    ## Dark Puff Gauntlet and Dragonfly Room
    set_rule(world.get_location('WF Stray Fairy Dark Puffs'), lambda state: state.stray_fairy_req())
    set_rule(world.get_entrance('WF Dark Puff Gauntlet To Dragonfly Room'), lambda state: state.can_use('Deku Sticks') or state.can_use('Fire Arrows'))
    set_rule(world.get_entrance('WF Dragonfly Room West To NE'), lambda state: state.form('Deku'))
    # we /may/ want to require a way to kill the dragonflies here beyond deku flowering them? just because it might be
    # too much of a pain normally; or not, who knows
    set_rule(world.get_entrance('WF Dragonfly Room West To Central Room SW'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Dragonfly Room West To Central Room East'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Dragonfly Room West To Central Room Fairy Platform'), lambda state: state.any_form_but('Goron'))

    ## Upper 1st Floor
    set_rule(world.get_location('WF Bow Chest'), lambda state: state.can_kill_lizalfos())
    set_rule(world.get_entrance('WF Bow Room Clean Exit'), lambda state: state.event('Cleaned WF'))
    set_rule(world.get_location('WF Boss Key Chest'), lambda state: state.can_kill_gekkos())
    set_rule(world.get_location('WF Don Gero Frog'), lambda state: state.can_use('Don Gero Mask'))
    set_rule(world.get_entrance('WF Boss Key Room Clean Exit'), lambda state: state.event('Cleaned WF'))
    # set_rule(world.get_location(''), lambda state: state)

    ## Pre-Boss Room
    set_rule(world.get_entrance('WF Pre Boss Room South To Fairy 1'), lambda state: state.stray_fairy_req())
    set_rule(world.get_entrance('WF Pre Boss Room South To Fairy 2'), lambda state: state.stray_fairy_req())
    # yes this is actually an open check, the ledge juts out far enough that any form can angle a jump to it
    # including goron lol, it's a bit tricky but you can roll and land on it
    # I actually didn't test deku, but deku can obviously make it regardless lol
    # which actually means the one in the lower alcove on that side is also just open
    set_rule(world.get_entrance('WF Pre Boss Room South To Fairy 3'),
             lambda state: state.stray_fairy_req(state.form('Deku')) or (state.can_pop_balloon() and state.can_use('Great Fairy Mask')))
    set_rule(world.get_entrance('WF Pre Boss Room South To Bubble Fairy'), lambda state: (state.can_use('Bow') and state.stray_fairy_req(state.form('Deku')))
                                                                            or (state.can_pop_balloon() and state.can_use('Great Fairy Mask')))
    set_rule(world.get_entrance('WF Pre Boss Room South To North'), lambda state: state.form('Deku') and (state.can_use('Hookshot') or state.can_use('Bow')))
    set_rule(world.get_entrance('WF Pre Boss Room North To Fairy 1'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
    set_rule(world.get_entrance('WF Pre Boss Room North To Fairy 2'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
    set_rule(world.get_entrance('WF Pre Boss Room North To Fairy 3'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
    set_rule(world.get_entrance('WF Pre Boss Room North To Bubble Fairy'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
    set_rule(world.get_entrance('WF Pre Boss Room North To South'), lambda state: state.form('Deku'))

    ## Boss: Odolwa
    set_rule(world.get_location('Defeat Odolwa'), lambda state: state.can_use('Bow'))
    set_rule(world.get_location('Odolwa HC'), lambda state: state.can_use('Bow'))
    set_rule(world.get_entrance('WF Odolwa Boss Exit'), lambda state: state.can_use('Bow'))
    # todo: figure out all the ways to kill odolwa
    # you probly hard need to use the bow, which means most other checks aren't needed
    # but yeah, gotta figure out all the ways to beat this
    # set_rule(world.get_location('Odolwas Remains'), lambda state: True)

    ## Post Odolwa Princess Room
    set_rule(world.get_location('Deku Princess'), lambda state: state.has_bottle() and state.form('Human'))

    # Cleaned Rooms
    set_rule(world.get_location('WF Stray Fairy Cleaned Central Room Deku Baba'), lambda state: state.stray_fairy_req())
    set_rule(world.get_location('WF Cleaned Central Room Gate Torch Using Fire Arrows'), lambda state: state.can_use('Fire Arrows'))
    set_rule(world.get_entrance('WF Cleaned Central Room SW To Push Block Room'), lambda state: state.has('Small Key (Woodfall Temple)'))
    set_rule(world.get_entrance('WF Cleaned Central Room SW To Upper'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Cleaned Central Room SW To Fairy Region'), lambda state: state.can_use('Bow') and state.can_use('Great Fairy Mask'))
    set_rule(world.get_location('WF Stray Fairy Cleaned Central Room SE Corner'), lambda state: state.stray_fairy_req())
    set_rule(world.get_entrance('WF Cleaned Central Room Fairy Platform To SW'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Cleaned Central Room Fairy Platform To East'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Cleaned Central Room Fairy Platform To Upper'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Cleaned Central Room East To Fairy Platform'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Cleaned Central Room East To Upper'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Cleaned Central Room East To Ladder Up'), lambda state: state.event('WF Central Room Ladder Switch'))
    set_rule(world.get_entrance('WF Cleaned Central Room Upper To Fairy Region'),
             lambda state: state.stray_fairy_req(state.can_pop_balloon() or state.form('Human')))
    set_rule(world.get_location('WF Stray Fairy Cleaned Central Room Upper Switch Chest'),
             lambda state: state.form('Deku') and state.any_form_but('Deku') and state.stray_fairy_req())
    set_rule(world.get_location('WF Cleaned Central Room Ladder Switch'), lambda state: state.any_form_but('Deku'))
    set_rule(world.get_entrance('WF Cleaned Central Room Upper To Pre Boss Room'),
             lambda state: state.event('WF Central Room Gate Torch Lit'))
    set_rule(world.get_entrance('WF Cleaned Central Room Upper To SW'), lambda state: state.any_form_but('Goron'))

    set_rule(world.get_location('WF Activate Elevator From Cleaned West Lower'), lambda state: state.can_use('Bow'))
    set_rule(world.get_entrance('WF Cleaned Elevator Room West Lower To Fairy Region'), lambda state: state.can_pop_balloon() and state.can_use('Great Fairy Mask'))
    set_rule(world.get_entrance('WF Cleaned Elevator Room West Lower To North Upper'), lambda state: (state.event('WF Elevator On') and state.form('Deku')))
    set_rule(world.get_entrance('WF Cleaned Elevator Room West Lower To SW Upper'), lambda state: (state.event('WF Elevator On') and state.form('Deku')))
    set_rule(world.get_entrance('WF Cleaned Elevator Room West Lower To East Lower'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Cleaned Elevator Room West Lower To Key Chest'), lambda state: state.form('Deku') or state.can_use('Hookshot'))
    set_rule(world.get_location('WF Activate Elevator From Cleaned East Lower'), lambda state: state.can_use('Bow'))
    # ^ example of the same event needing to go in multiple spots; need to change to a logical region and have only a single item location?
    set_rule(world.get_entrance('WF Cleaned Elevator Room East Lower To West Lower'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Cleaned Elevator Room North Upper To West Lower'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Cleaned Elevator Room North Upper To East Lower'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_entrance('WF Cleaned Elevator Room North Upper To Key Chest'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Cleaned Elevator Room North Upper To Fairy Region'),
             lambda state: state.form('Human') or state.form('Zora') or (state.form('Deku') and state.has('Magic Meter')))
    set_rule(world.get_entrance('WF Cleaned Elevator Room SW Upper To West Lower'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('WF Cleaned Elevator Room SW Upper To East Lower'), lambda state: state.can_use('Hookshot'))

    set_rule(world.get_location('WF Stray Fairy Cleaned Push Block Room Hive'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
    set_rule(world.get_location('WF Stray Fairy Cleaned Push Block Room Skulltula'), lambda state: state.stray_fairy_req())
    set_rule(world.get_entrance('WF Cleaned Push Block Room Lower To Compass Room'), lambda state: state.can_use('Deku Sticks') or state.can_use('Fire Arrows'))
    set_rule(world.get_entrance('WF Cleaned Push Block Room Lower To Upper'), lambda state: state.can_use('Deku Sticks') or state.can_use('Bow'))
    set_rule(world.get_entrance('WF Cleaned Push Block Room Upper To Lower'), lambda state: state.can_use('Deku Sticks') or state.can_use('Bow'))
    set_rule(world.get_entrance('WF Cleaned Push Block Room Lower To Fairy Region'), lambda state: state.stray_fairy_req((state.form('Human') or state.form('Zora'))))

    ## Cleaned swamp areas
    set_rule(world.get_entrance('Cleaned To Swamp Spider House'), lambda state: state.can_use('Fire Arrows'))

    set_rule(world.get_entrance('Cleaned Tourist Region Trick To Upper Midpoint'), lambda state: state.can('Some Jumping Trick') and state.form('Human'))

    set_rule(world.get_entrance('Cleaned Outer Palace To Tourist Upper'), lambda state: state.form('Deku') or state.can('Gainer'))
    set_rule(world.get_entrance('Cleaned Outer Palace To Lower Courtyard'), lambda state: state.form('Deku') or (state.can('Deku Palace Guard Skip')))
    set_rule(world.get_entrance('Cleaned Palace To Butler Race'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('Cleaned Outer Palace To Upper Courtyard'), lambda state: state.has_bottle() and state.has('Magic Beans'))
    set_rule(world.get_entrance('Cleaned Deku Palace Lower Courtyard To Upper'), lambda state: state.can('Deku Palace Courtyard Trick'))
    set_rule(world.get_entrance('Cleaned Deku Palace Upper Courtyard To Throne Room Cage Region'), lambda state: state.form('Deku'))

    set_rule(world.get_entrance('Cleaned Octo Upper Near Palace To Midpoint'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Cleaned Octo Upper Midpoint To Near Palace'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Cleaned Octo Upper Midpoint To Kaepora'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Cleaned Octo Kaepora To Midpoint'), lambda state: state.form('Deku'))

    set_rule(world.get_location('Outside Woodfall 20 Rupee Chest'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('Cleaned Outside Woodfall Entrance To Woodfall Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Cleaned Outside Woodfall Entrance To Fountain Platform'), lambda state: state.form('Human') or state.form('Zora'))
    set_rule(world.get_location('Woodfall Owl Statue (Cleaned)'), lambda state: state.form('Human'))
    set_rule(world.get_entrance('Cleaned Owl Platform To Entrance'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('Cleaned Owl Platform To Fountain Platform'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('Cleaned Owl Platform To Temple Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Cleaned Woodfall Temple Platform To Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Cleaned Woodfall Temple Platform To Entrance'), lambda state: True)
    set_rule(world.get_entrance('Cleaned Fountain Platform To Owl Platform'), lambda state: state.form('Deku'))
    set_rule(world.get_entrance('Cleaned Fountain Platform To Entrance'), lambda state: state.any_form_but('Goron'))
    set_rule(world.get_entrance('Cleaned Fountain Platform To Fountain'), lambda state: state.form('Deku') or state.can('Gainer'))


    ### MOUNTAIN VILLAGE

    ## Mountain Village
    set_rule(world.get_location('Goron Mask'), lambda state: state.has('Song of Healing') and state.can_use('Lens of Truth'))
    # this probly needs to be investigated (do you actually need the lens once you've gotten the ghost there?) and we
    # should determine how we want to track this check, since you have to follow the ghost through various areas
    # I kiiiind of want to add a ton of extra stuff for myself to do, like world state checks that just don't get
    # shuffled in so it's easy to do like state.world('HasLedGhostToSprings') or whatever
    # stuff that would strictly be used by the crawler to determine placement
    # we'll see

    set_rule(world.get_location('Goron Grave Hot Spring Water'), lambda state: state.has_bottle())
    # something is definitely gonna have to be tweaked in order to keep this (and the goron elder) check in, especially
    # accounting for entrance shuffle
    # I think only goron is fast enough to make it from here to the elder, but if entrances are shuffled, there needs
    # to be a way to check that the distance between the two is short enough (and depending on the length, maybe a
    # different form can make it)
    # I think the way to do this is to have checks set here and at the elder, and then add a function to the crawler
    # that checks the distance between the two
    # also, to note, the more I encounter checks that require you to do things across multiple rooms/areas, the more
    # I'm convinced we'll need to use 'fake' item checks, just to keep track of the world state, like set a rule for
    # starting to follow the goron ghost in one spot and another for catching up, and then another for meeting up with
    # him at the grave
    # anyway

    set_rule(world.get_location('Don Gero Mask'), lambda state: state.has('Rock Sirloin'))
    # gonna need some way to check that you can actually get the sirloin to this guy after entrance shuffle, lol

    set_rule(world.get_location('Mountain Village 20 Rupee Chest Behind Waterfall'), lambda state: state.event('Beat Ghot') and state.lens_req())

    set_rule(world.get_location('Mountain Village 20 Rupee Pit'), lambda state: state.event('Beat Ghot') and (state.form('Goron') or state.lens_req()))
    # this one may not be a chest, I should check it

    set_rule(world.get_location('Gilded Sword'), lambda state: state.event('Beat Ghot') and state.has('Gold Dust'))
    # it's probly best to just assume you can always get the razor sword

    set_rule(world.get_location('Mountain Village Keaton HP'), lambda state: state.can_use('Keaton Mask') and state.event('Beat Ghot'))

    set_rule(world.get_location('Don Gero HP'), lambda state: state.event('Beat Ghot') and state.can_kill_gekkos() and state.has('Ice Arrows'))
    # maybe need to check the reqs on this, but I think we can assume if you can beat ghot and both gekkos,
    # you can get to all the frogs and get this HP

    ## Frozen Lake
    set_rule(world.get_location('Mountain Tingle Snowhead Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Mountain Tingle Romani Ranch Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Mountain Tingle Pic'), lambda state: state.can_use('Picto Box'))
    set_rule(world.get_location('First Half Goron Lullaby'), lambda state: (state.can_blast() or state.form('Goron')) and state.can_use('Hot Spring Water'))
    # not sure if he'll actually teach you the half song if you're not a goron todo: test form requirements

    set_rule(world.get_location('Frozen Lake HP'), lambda state: state.event('Beat Ghot') and state.form('Zora'))

    set_rule(world.get_location('Frozen Lake Bombchu Pit'), lambda state: state.event('Beat Ghot') and state.form('Goron'))
    # I should check this one too, dunno if it's a chest or what; also is goron the only one who can get to this pit?

    set_rule(world.get_location('Goron Race Gold Dust Bottle'), lambda state: state.event('Beat Ghot') and state.form('Goron'))
    # set_rule(world.get_location(''), lambda state: state)

    ## Goron Village
    set_rule(world.get_location('Biggest Bomb Bag'), lambda state: state.form('Goron') and state.has('Adult Wallet'))
    # set_rule(world.get_location('Lens of Truth'), lambda state: True)
    set_rule(world.get_location('Lens of Truth Cave Invisible Chest'), lambda state: state.lens_req())
    set_rule(world.get_location('Lens of Truth Cave Boulder Chest'), lambda state: state.can_blast())

    set_rule(world.get_location('Learn Goron Lullaby'), lambda state: state.form('Goron') and state.has('First Half Goron Lullaby'))
    set_rule(world.get_location('Rock Sirloin'), lambda state: state.can_use('Deku Stick') and state.form('Goron'))
    # set_rule(world.get_location(''), lambda state: state)

    ## Snowhead and Path To
    set_rule(world.get_location('Path To Snowhead HP'), lambda state: state.form('Goron') and state.can_use('Hookshot') and state.lens_req())
    set_rule(world.get_location('Snowhead Owl Statue'), lambda state: state.form('Human'))


    ### SNOWHEAD TEMPLE

    ## 1st Floor and Basement
    set_rule(world.get_location('SH Stray Fairy 1 Bridge And Freezard Room'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
    set_rule(world.get_location('SH Stray Fairy 2 Bridge And Freezard Room'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
    set_rule(world.get_location('SH Stray Fairy Basement Switch'), lambda state: state.form('Goron'))
    # set_rule(world.get_location('SH Push Block Key Chest'), lambda state: True)
    # set_rule(world.get_location('SH Compass Chest'), lambda state: True)
    # do you have to actually do anything in this room, or is the chest just there already? I forget

    set_rule(world.get_location('SH Bridge and Freezard Room Key Chest'), lambda state: state.can_use('Fire Arrows'))
    set_rule(world.get_location('SH Stray Fairy Chest In Compass Room'), lambda state: state.can_use('Fire Arrows') or state.can_use('Hookshot'))

    set_rule(world.get_location('SH Stray Fairy Compass Room Bombable'),
             lambda state: (state.can_use('Fire Arrows') or state.can_use('Hookshot')) and state.can_use('Bomb Bag') and state.stray_fairy_req())
    # I bet there's a way to cheese this one

    set_rule(world.get_location('SH Stray Fairy Push Block Room'), lambda state: state.can_use('Fire Arrows'))
    # this check will need to be changed depending on the logical regions defined- probly have a path of regions from
    # the compass room leading here, plus an exit from the lower part of the room to the chest/torches part gated by
    # the hookshot

    set_rule(world.get_location('SH Stray Fairy Behind Central Pillar Room'), lambda state: state.can_use('Fire Arrows'))
    # set_rule(world.get_location(''), lambda state: state)

    ## 2nd Floor
    # set_rule(world.get_location('SH Map Chest'), lambda state: True)
    # set_rule(world.get_location('SH Stray Fairy Map Chest Room'), lambda state: True)
    set_rule(world.get_location('SH Icicle Drop Room Key Chest'), lambda state: state.can_use('Bow') and (state.can_blast() or state.form('Goron')))
    set_rule(world.get_location('SH Stray Fairy Icicle Drop Room'), lambda state: state.can_use('Bow') and state.lens_req())
    set_rule(world.get_location('SH Stray Fairy Goron Switch Room Ceiling'), lambda state: state.can_pop_balloon() and state.lens_req())

    set_rule(world.get_location('SH Fire Arrows Chest'), lambda state: state.can_use('Bow'))
    # I bet there are other ways of beating the wizrobe, just not sure how

    set_rule(world.get_location('SH Stray Fairy Elevator Room Lens Platforms'), lambda state: state.can_use('Lens of Truth') and (state.form('Human') or state.form('Zora')))
    # set_rule(world.get_location(''), lambda state: state)

    ## 3rd Floor
    set_rule(world.get_location('SH Stray Fairy 3F Snowman Room'), lambda state: state.can_pop_balloon() and state.lens_req())
    # can you just jump to this one? I forget

    ## 4th Floor
    set_rule(world.get_location('SH Stray Fairy 1 Lizalfos Room'), lambda state: state.can_kill_lizalfos())
    set_rule(world.get_location('SH Stray Fairy 2 Lizalfos Room'), lambda state: state.can_kill_lizalfos())

    set_rule(world.get_location('SH Stray Fairy Hidden Alcove'), lambda state: state.can_use('Lens of Truth') and (state.form('Deku') or state.form('Human')))
    # there might be other ways to do this, not sure

    set_rule(world.get_location('SH Boss Key Chest'), lambda state: state.can_use('Bow'))

    ## Boss: Ghot
    set_rule(world.get_location('Ghots Remains'), lambda state: state.can_use('Bow') and state.has('Fire Arrows') and state.form('Goron'))
    # I know there are various ways to do this boss, but I'm not sure exactly what, so for now let's just require goron form


    ### ROMANI RANCH AREA

    ## Milk Road
    set_rule(world.get_location('Milk Road Keaton HP'), lambda state: state.can_use('Keaton Mask'))
    set_rule(world.get_location('Milk Road Tingle Romani Ranch Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Milk Road Tingle Other Map'), lambda state: state.can_pop_balloon())
    # whoops, left in a dupe, gotta look up what map this actually is
    set_rule(world.get_location('Milk Road Tingle Pic'), lambda state: state.can_use('Picto Box'))
    set_rule(world.get_location('Milk Road Owl Statue'), lambda state: state.form('Human'))

    ## Romani Ranch
    set_rule(world.get_location('Bunny Hood'), lambda state: state.can_use('Bremen Mask'))
    set_rule(world.get_location('Learn Eponas Song'), lambda state: state.can_use('Bow') and state.form('Human'))
    # form reqs?

    # set_rule(world.get_location('Dog Track 50 Rupee Chest'), lambda state: True)
    set_rule(world.get_location('Romani Ranch Bottle'), lambda state: state.can_use('Bow'))
    set_rule(world.get_location('Dog Track HP'), lambda state: state.dog_track_MoT_req())
    set_rule(world.get_location('Romani Mask'), lambda state: state.can_use('Bow'))

    ## Gorman Bros.
    set_rule(world.get_location('Garo Mask'), lambda state: state.has('Eponas Song'))


    ### GREAT BAY

    ## Great Bay North
    set_rule(world.get_location('Zora Mask'), lambda state: state.form('Human'))
    set_rule(world.get_location('Great Bay Owl Statue'), lambda state: state.form('Human'))
    set_rule(world.get_location('Great Bay Tingle Great Bay Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Great Bay Tingle Ikana Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Great Bay Tingle Pic'), lambda state: state.can_use('Picto Box'))
    # set_rule(world.get_location('Rupee Pit'), lambda state: True)

    set_rule(world.get_location('Ocean Spider House HP'), lambda state: state.can_use('Bow') and state.has('Hookshot') and state.has('Captains Hat'))
    # the captain's hat can be used to get the code or whatever from the stalchildren, or you can trial and
    # error it with arrows
    # so we can maybe make it an option to need the captain's hat, but for now I'm just going to require it

    set_rule(world.get_location('Ocean Spider House Giant Wallet'), lambda state: state.can_use('Fire Arrows') and state.has('Hookshot') and state.has('Bomb Bag'))
    # todo these later

    set_rule(world.get_location('Great Bay Lab Fish Feeding HP'), lambda state: state.has_bottle())
    set_rule(world.get_location('Great Bay Seahorse From Fisherman'), lambda state: state.has('Picto Box') and state.has_bottle())
    set_rule(world.get_location('Learn New Wave Bossa Nova'), lambda state: state.form('Zora') and state.has('Zora Egg', 7))
    set_rule(world.get_location('Great Bay High Cliff HP'), lambda state: state.can_use('Hookshot') and state.has('Spring Water') and state.has('Magic Beans'))
    set_rule(world.get_location('Great Bay Jumping Game HP'), lambda state: state.event('Beat Gyorg') and state.can_use('Hookshot') and (state.form('Human') or state.form('Zora')))

    ## Great Bay South
    set_rule(world.get_location('Great Bay Like Like HP'), lambda state: state.form('Zora'))
    # set_rule(world.get_location('Great Bay Bombchu Pit'), lambda state: True)
    set_rule(world.get_location('Great Bay Temple Owl Statue'), lambda state: state.form('Human'))
    set_rule(world.get_location('Zora Hall 5 Rupees From Stagehand'), lambda state: True)
    set_rule(world.get_location('Zora Hall 20 Rupees From Lulu Stalker'), lambda state: state.has_bottle())
    set_rule(world.get_location('Beaver Race Bottle'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Beaver Race HP'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Zora Hall Song HP'), lambda state: state.form('Human'))
    # set_rule(world.get_location(''), lambda state: state)

    ## Gerudo Fortress
    set_rule(world.get_location('Gerudo Fortress Entrance Harbor 20 Rupee Chest 1'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Gerudo Fortress Entrance Harbor 20 Rupee Chest 2'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Gerudo Fortress Entrance Harbor 20 Rupee Chest 3'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Gerudo Fortress Cage Maze 20 Rupee Chest'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Gerudo Fortress Cage Maze HP'), lambda state: state.form('Goron') or state.can_use('Bunny Hood'))
    # I /think/ you need the goron form to be fast enough to make this? maybe there are ways to cheese this

    set_rule(world.get_location('Gerudo Fortress Tower Hub 20 Rupee Chest'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_location('Hookshot'), lambda state: state.can_use('Bow'))
    set_rule(world.get_location('Zora Egg 1'), lambda state: state.has_bottle() and state.form('Zora') and state.can_use('Hookshot'))
    set_rule(world.get_location('Zora Egg 2'), lambda state: state.has_bottle() and state.form('Zora') and state.can_use('Hookshot'))
    set_rule(world.get_location('Zora Egg 3'), lambda state: state.has_bottle() and state.form('Zora') and state.can_use('Hookshot'))
    set_rule(world.get_location('Zora Egg 4'), lambda state: state.has_bottle() and state.form('Zora') and state.can_use('Hookshot'))
    set_rule(world.get_location('Gerudo Fortress 100 Rupee Chest'), lambda state: state.can_use('Hookshot') or state.can_use('Bow') or state.can_use('Stone Mask'))
    # set_rule(world.get_location(''), lambda state: state)

    ## Pinnacle Rock
    set_rule(world.get_location('Zora Egg 5'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Zora Egg 6'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Zora Egg 7'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Pinnacle Rock Eel HP'), lambda state: state.form('Zora'))


    ### GREAT BAY TEMPLE
    # note about this temple: there's a lot of stuff you might be able to reach with ice arrows rather than hookshoting
    # to a chest
    # this will probly need extensive testing

    set_rule(world.get_location('GB Stray Fairy Entrance Room'), lambda state: state.can_use('Deku Stick'))
    set_rule(world.get_location('GB Stray Fairy Flywheel Room Underwater'),
             lambda state: (state.form('Zora') or (state.can_pop_balloon() and state.can_use('Great Fairy Mask'))) and state.stray_fairy_req())

    set_rule(world.get_location('GB Stray Fairy Flywheel Room Big Skulltula'), lambda state: state.form('Zora'))
    # zoras can deal with big skulls by themselves, right? no need to add any other checks

    set_rule(world.get_location('GB Stray Fairy Big Whirlpool Hub Barrel'), lambda state: state)
    set_rule(world.get_location('GB Stray Fairy Big Whirlpool Hub Bottom'),
             lambda state: state.stray_fairy_req() and (state.form('Zora') or (state.can_pop_balloon() and state.can_use('Great Fairy Mask'))))
    set_rule(world.get_location('GB Map Chest'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_location('GB Stray Fairy Map Room'), lambda state: (state.can_pop_balloon() or state.form('Zora')) and state.stray_fairy_req())
    set_rule(world.get_location('GB Stray Fairy Tunnel To Compass Room'), lambda state: state.form('Zora') and state.stray_fairy_req())
    set_rule(world.get_location('GB Compass Chest'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_location('GB Compass Room Key Chest'), lambda state: state.form('Zora'))

    set_rule(world.get_location('GB Stray Fairy Compass Room'), lambda state: state.can_pop_balloon() and state.stray_fairy_req())
    # ugh, test this check, there are probly lots of ways to do it
    # todo: lots of testing on this one

    set_rule(world.get_location('GB Ice Arrows Chest'), lambda state: state.can_use('Hookshot'))
    # todo: look up all the ways of killing Wort

    set_rule(world.get_location('GB Boss Key Chest'), lambda state: state.can_kill_gekkos() and state.has('Ice Arrows'))
    set_rule(world.get_location('GB Stray Fairy First Green Crank Room'), lambda state: state.can_use('Hookshot') and state.has('Ice Arrows'))
    set_rule(world.get_location('GB Stray Fairy Waterfall Room 1'), lambda state: state.can_use('Hookshot') and state.has('Ice Arrows'))
    set_rule(world.get_location('GB Stray Fairy Waterfall Room 2'), lambda state: state.can_use('Hookshot') and state.has('Ice Arrows') and state.has('Fire Arrows'))
    # including fire arrows here for sanity, otherwise you'd have to reenter the room or maybe dungeon if you messed up

    set_rule(world.get_location('GB Stray Fairy Final Crank Room 1'), lambda state: state.form('Zora') and state.stray_fairy_req())
    set_rule(world.get_location('GB Stray Fairy Final Crank Room 2'), lambda state: state.form('Zora') and state.stray_fairy_req())
    # I think just zora is enough for the second one? might have to test that

    set_rule(world.get_location('GB Stray Fairy Before Gyorg Room 1'), lambda state: state.form('Zora') and state.stray_fairy_req())
    set_rule(world.get_location('GB Stray Fairy Before Gyorg Room 2'), lambda state: (state.can_pop_balloon() or state.form('Zora')) and state.stray_fairy_req())

    ## Boss: Gyorg
    set_rule(world.get_location('Gyorgs Remains'), lambda state: state.form('Zora') and state.can_use('Bow'))


    ### IKANA CANYON
    set_rule(world.get_location('Ikana Entrance Bombchu Pit'), lambda state: state.form('Goron'))
    # todo: check this spot in the game

    set_rule(world.get_location('Stone Mask'), lambda state: state.can_epona() and state.has_bottle() and state.can_use('Lens of Truth'))

    set_rule(world.get_location('Ikana Graveyard Bombchu Pit'), lambda state: state.can_blast())
    # todo: test if blast mask works here

    set_rule(world.get_location('Ikana Graveyard Dampe 30 Rupee Prize'), lambda state: state.can_pop_balloon() or state.form('Human'))

    set_rule(world.get_location('Captains Hat'), lambda state: state.has('Sonata of Awakening') and (state.can_use('Bow') or state.can_use('Bunny Hood')))
    # oh jeez, there are various glitches to get this chest huh?
    # todo: reaseach this chest

    set_rule(world.get_location('Ikana Graveyard First Night Grave 50 Rupee Chest'), lambda state: state.can_use('Captains Hat'))
    set_rule(world.get_location('Learn Song of Storms'), lambda state: state.can_use('Captains Hat') and state.has('Bow') and state.has('Fire Arrows'))
    set_rule(world.get_location('Ikana Graveyard Second Night Grave HP'), lambda state: state.can_use('Captains Hat') and state.lens_req() and state.can_blast())
    set_rule(world.get_location('Ikana Graveyard Third Night Grave Bottle'), lambda state: state.can_use('Captains Hat') and state.can_use('Bow'))

    set_rule(world.get_location('Ikana Canyon Owl Statue'), lambda state: state.can_use('Bow') and state.has('Ice Arrows') and state.has('Hookshot'))
    set_rule(world.get_location('Ikana Tingle Ikana Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Ikana Tingle Clock Town Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Ikana Tingle Pic'), lambda state: state.can_use('Picto Box'))
    # really this check depends on the logical area the statue is in; if it's just in the whole map, then there's a
    # bunch of reqs, but if it's in the upper region, then it's open
    # I'll leave it open for now, but we'll have to check in on this at some point
    # same with tingle actually

    set_rule(world.get_location('Ikana Secret Shrine HP'), lambda state: state.has_hearts(16) and state.can_use('Light Arrows') and state.can_kill_lizalfos() and state.has('Hookshot'))

    set_rule(world.get_location('Gibdo Mask'), lambda state: state.can_use('Bomb Bag') and state.form('Human') and state.has('Song of Healing'))

    set_rule(world.get_location('Ghost Hut HP'), lambda state: state.can_use('Bow'))
    # idek if you actually need the bow to do this, but probly; if not, the check is just for human form

    ## Beneath the Well
    set_rule(world.get_location('Beneath the Well 50 Rupee Chest 1'),
             lambda state: state.can_use('Gibdo Mask') and state.has_bottle() and state.has('Blue Potion') and state.lens_req())
    set_rule(world.get_location('Beneath the Well 50 Rupee Chest 2'),
             lambda state: state.can_use('Gibdo Mask') and state.has_bottle() and state.has('Magic Beans', 5) and state.can_use('Deku Sticks'))
    set_rule(world.get_location('Mirror Shield'),
             lambda state: state.can_use('Gibdo Mask') and state.has_bottle() and state.has('Blue Potion') and
                           state.has('Magic Beans') and state.has('Bow') and state.has('Bomb Bag') and
                           (state.has('Eponas Song') or state.has('Romani Mask')) and state.has('Fire Arrows'))
    # not actually as bad as I initially thought
    # the mirror shield is a bit much lol

    ## Ikana Castle
    set_rule(world.get_location('Ikana Castle Pillar HP'), lambda state: state.form('Human') and state.form('Deku') and state.has('Bow'))
    set_rule(world.get_location('Learn Elegy of Emptiness'), lambda state: state.can_use('Bow') and state.has('Fire Arrows') and state.has('Mirror Shield'))
    # set_rule(world.get_location(''), lambda state: state)

    ## Stone Tower Climb
    set_rule(world.get_location('Stone Tower Owl Statue'),
             lambda state: state.form('Human') and state.form('Goron') and state.form('Zora') and state.has('Hookshot') and state.has('Elegy of Emptiness'))


    ### STONE TOWER TEMPLE
    ## Regular
    set_rule(world.get_location('ST Stray Fairy Entryway 1'), lambda state: state.can_use('Bow') and state.stray_fairy_req())
    set_rule(world.get_location('ST Map Chest'), lambda state: state.can_use('Bomb Bag') and (state.has('Mirror Shield') or state.can_use('Light Arrows')) and state.form('Goron'))
    set_rule(world.get_location('ST Map Room Key Chest'), lambda state: state.can_use('Bomb Bag') and state.form('Goron'))
    set_rule(world.get_location('ST Stray Fairy Map Room'), lambda state: state.can_use('Bomb Bag') and state.has('Hookshot'))
    set_rule(world.get_location('ST Pool Room Key Chest'), lambda state: state.form('Human') or state.form('Zora'))
    set_rule(world.get_location('ST Compass Chest'), lambda state: (state.form('Zora') and state.can_use('Mirror Shield')) or state.can_use('Light Arrows'))
    set_rule(world.get_location('ST Stray Fairy Mirror Network Room 1'), lambda state: (state.form('Goron') and state.can_use('Mirror Shield')) or state.can_use('Light Arrows'))
    set_rule(world.get_location('ST Stray Fairy Mirror Network Room 2'), lambda state: (state.form('Goron') and state.can_use('Mirror Shield')) or state.can_use('Light Arrows'))
    set_rule(world.get_location('ST Stray Fairy Lava Room Center Chest'), lambda state: state.form('Deku'))
    set_rule(world.get_location('ST Stray Fairy Lava Room Switch Chest'), lambda state: state.form('Goron'))

    set_rule(world.get_location('ST Light Arrows Chest'), lambda state: state.form('Human') or state.form('Zora'))
    # todo: what forms/items can beat the garo master?

    set_rule(world.get_location('ST Stray Fairy Pool Room Eyegore'), lambda state: state.can_use('Hookshot'))
    set_rule(world.get_location('ST Stray Fairy Pool Room Behind Sun Block'), lambda state: state.can_use('Bomb Bag') and state.can_use('Light Arrows'))
    # set_rule(world.get_location(''), lambda state: state)

    ## Inverted
    set_rule(world.get_location('ST Stray Fairy Inverted Entryway'), lambda state: state.can_use('Light Arrows') and state.can_reach(state.get_location('ST Entryway')))
    set_rule(world.get_location('ST Inverted Compass Room Key Chest'), lambda state: state.can_use('Light Arrows') and state.form('Deku'))
    set_rule(world.get_location('ST Stray Fairy Inverted Compass Room 1'),
             lambda state: state.can_reach(state.get_location('ST Compass Room')) and state.form('Zora') and state.can_use('Light Arrows') and state.form('Deku'))
    set_rule(world.get_location('ST Stray Fairy Inverted Compass Room 2'),
             lambda state: state.can_reach(state.get_location('ST Compass Room')) and state.can_use('Fire Arrows')
                           and state.can_use('Light Arrows') and state.form('Deku') and state.has('Elegy of Emptiness'))
    set_rule(world.get_location('ST Stray Fairy Compass Room'),
             lambda state: state.can_reach(state.get_location('ST Compass Room')) and state.can_use('Light Arrows'))
    set_rule(world.get_location('ST Stray Fairy Wizrobe Room'), lambda state: state.can_use('Bow') and state.can_use('Hookshot'))
    set_rule(world.get_location('ST Inverted Map Room Key'), lambda state: state.has('Elegy of Emptiness'))
    set_rule(world.get_location('ST Boss Key Chest'), lambda state: state.can_use('Light Arrows'))
    set_rule(world.get_location('ST Stray Fairy Entryway 2'),
             lambda state: state.can_reach(state.get_location('ST Entryway')) and (state.can_use('Light Arrow') or state.can_use('Stone Mask')))
    set_rule(world.get_location('ST Stray Fairy Post Garo Master Room'), lambda state: state.can_reach(state.get_location('ST Post Garo Master Room')) and state.can_use('Bow'))
    # set_rule(world.get_location('Giants Mask'), lambda state: ([state.can_use(x) for x in ['Bow', 'Hookshot', 'Bomb Bag']].count(True) > 0) or state.form('Zora') or (state.form('Deku') and state.has('Magic Meter')))
    # leaving this as an open check because you need lights to get to the eyegore, which can beat him already
    # unless there's a possible path say in entrance shuffle that could allow you to reach here another way
    # figure that out later, that'll take more defined region logic

    ## Boss: Twinmold
    set_rule(world.get_location('Twinmodls Remains'), lambda state: state.can_use('Giants Mask') or state.can_use('Bow'))


    ### THE MOON
    set_rule(world.get_location('Moon Odolwa Child HP'), lambda state: state.form('Deku'))
    set_rule(world.get_location('Moon Ghot Child HP'), lambda state: state.form('Goron'))
    set_rule(world.get_location('Moon Gyorg Child HP'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Moon Twinmold Child Bombchu Chest'), lambda state: state.can_use('Light Arrows') and state.has('Hookshot') and state.can_kill_lizalfos())
    set_rule(world.get_location('Moon Twinmold Child HP'), lambda state: state.can_use('Light Arrows') and state.has('Hookshot') and state.can_kill_lizalfos() and state.can_use('Bombchus'))
    set_rule(world.get_location('Fierce Deity Mask'), lambda state: state.has('Mask', 20))
    # we still need to determine how to deal with the counting of the masks for this section, but I'll leave it like this for now


# ooh ooh
# maybe have a gate at the clock tower roof that requires the ocarina, to go back to south clock town on the first day
# maayyybe
# to force placement of the ocarina somewhere you can get to it in the first cycle
# depends on how crawling through the graph works
# todo: go through and put in checks (that shouldn't get shuffled!) for various steps of quests
# like, 'looked at skull kid in telescope' to be used to get the moon's tear, or all the various steps in the a+k quest
