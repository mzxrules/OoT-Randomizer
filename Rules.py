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
    set_rule(world.get_location('First Nut'), lambda state: state.form('Deku'))
    set_rule(world.get_location('Clock Town GF Reward'), lambda state: state.has('CT SF', 1))
    set_rule(world.get_location('Woodfall GF Reward'), lambda state: state.has('WF SF', 15))
    set_rule(world.get_location('Snowhead GF Reward'), lambda state: state.has('SH SF', 15))
    set_rule(world.get_location('Great Bay GF Reward'), lambda state: state.has('GB SF', 15))
    set_rule(world.get_location('Stone Tower GF Reward'), lambda state: state.has('ST SF', 15))

    set_rule(world.get_entrance('Bomber Tunnel'), lambda state: state.has('Bomber Code'))
    set_rule(world.get_entrance('Astral Observatory Fence'), lambda state: state.has('Magic Beans') or state.can('Goron Boost'))
    set_rule(world.get_location('Swamp Business Scrub'), lambda state: state.has('Town Title Deed'))
    set_rule(world.get_location('Mountain Business Scrub'), lambda state: state.has('Swamp Title Deed'))
    set_rule(world.get_location('Ocean Business Scrub'), lambda state: state.has('Mountain Title Deed'))
    set_rule(world.get_location('Canyon Business Scrub'), lambda state: state.has('Ocean Title Deed'))
    set_rule(world.get_location('Song From Mask Salesman'), lambda state: state.has('Ocarina of Time'))
    set_rule(world.get_location('Remove the Cursed Mask'), lambda state: state.has('Ocarina of Time'))
    set_rule(world.get_location('Tunnel Balloon From Observatory'), lambda state: state.form('Human') or (state.form('Deku') and state.has('Magic Meter')) or state.form('Zora'))
    # leaving the human form check by itself here should work, since this balloon you can just go and slash
    # and I'm pretty sure you always have the sword in human form

    set_rule(world.get_location('Tunnel Balloon From ECT'), lambda state: state.can_pop_balloon())
    # @Vlix
    # that's right, zora link should be able to slice it, good call
    # other human items, hmm... hookshot probly? maybe bombs? lol that'd be a pain; yeah we'll have to do some testing
    # to see what can be used there (hookshot makes a lot of sense though, I'll add that for now)
    # todo: test what else can be used to break these balloons

    # RevelationOrange started adding rules here (plus a few changes in rules above)
    # location names used are mostly guesses and can absolutely be changed later
    # item names used are also guesses, as are some state function names probly
    # location names may be longer than necessary so as to be descriptive, like we can change 'South Clock Town Hookshot
    # Ledge Rupee Chest' if we want lol

    ### SOUTH CLOCK TOWN
    set_rule(world.get_location('Clock Town Business Scrub'), lambda state: state.has('Moons Tear'))
    set_rule(world.get_location('Clock Tower Platform HP'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora') or (state.form('Deku') and state.can_reach(world.get_location('Clock Town Business Scrub'))))
    # @Vlix
    # oh dang, goron link can't just hop up that small ledge? or maybe he doesn't even fit on it, heh
    # gotta test to see ways of getting on there todo: find ways of getting up to that platform in various forms
    # ah, just thought of adding deku form as I was reading through, nice lol

    set_rule(world.get_location('Festival Tower Rupee Chest'), lambda state: (state.has('Hookshot') and state.form('Human')) or (state.form('Deku') and state.can_reach(world.get_location('Clock Town Business Scrub'))))
    set_rule(world.get_location('South Clock Town Hookshot Ledge Rupee Chest'), lambda state: state.has('Hookshot') and state.form('Human'))

    # set_rule(world.get_location('Ocarina of Time'), lambda state: (state.form('Deku') and state.has('Magic Meter')) or (state.has('Bow') and state.form('Human')) or state.form('Zora'))
    set_rule(world.get_location('Ocarina of Time'), lambda state: state.can_pop_balloon())
    # is this right? it looks like the check is just to hit skull kid in the air, functionally the same as popping a balloon lol


    ### LAUNDRY POOL
    set_rule(world.get_location('Bremen Mask From Guru Guru'), lambda state: state.form('Human') or state.form('Zora') or state.form('Goron'))


    ### WEST CLOCK TOWN
    set_rule(world.get_location('Rosa Sisters HP'), lambda state: state.has('Kamaro Mask') and state.form('Human'))

    # you might not need to be human to get this, but I'd bet the shop owner won't sell to other forms, at least deku
    # set_rule(world.get_location('Bomb Bag'), lambda state: True)
    # this can be tested easily

    # obviously, this and similar 'tests' might not be necessary at all
    # set_rule(world.get_location('Adult Wallet from bank'), lambda state: True)
    # set_rule(world.get_location('Bank HP'), lambda state: True)

    set_rule(world.get_location('Big Bomb Bag'), lambda state: state.form('Human') or state.form('Zora') or state.has('Adult Wallet'))
    # adult wallet is a req because if you don't rescue the old lady from sakon, the big bomb bag shows up in the
    # curiosity shop on the final day (still might be form restrictions?)

    set_rule(world.get_location('Sword School HP'), lambda state: state.form('Human'))

    # i swear this should be an optional trick, it's so hard without the bunny hood lol
    # set_rule(world.get_location('Postman Game HP'), lambda state: True)
    # sigh alright we'll make this open lol

    set_rule(world.get_location('All Night mask'), lambda state: (state.form('Human') or state.form('Zora')) and state.has('Giants Wallet'))
    # you need to save the bomb lady from sakon and this will be in the curio shop on the final day for 500 rupees
    # being human might be a hard req, but you can probly buy it as zora (todo: test that)


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
    set_rule(world.get_location('Blast Mask'), lambda state: state.form('Human') or state.form('Zora'))

    set_rule(world.get_location('North Clock Town Tree HP'), lambda state: state.form('Human') or state.form('Zora'))
    # I thought deku could get this for some reason
    # also lol of course goron can't, shoulda known

    set_rule(world.get_location('Tingle Clock Town Map'), lambda state: state.can_pop_balloon())
    set_rule(world.get_location('Tingle Woodfall Map'), lambda state: state.can_pop_balloon())
    # it's not the same balloon as for bombers, but the same checks apply

    set_rule(world.get_location('Keaton HP'), lambda state: state.has('Keaton Mask') and state.form('Human'))
    set_rule(world.get_location('Deku Scrub Playground HP'), lambda state: state.form('Deku'))

    set_rule(world.get_location('Great Fairy Mask'), lambda state: state.has('Deku Mask'))
    # actually, the great fairy stuff probly needs to be tested
    # what she gives to what forms, what she gives in first vs other cycles
    # because right now we have rules set for 'Clock Town GF Reward', 'Great Fairy Mask', and 'Magic from NCT Great Fairy' lol

    # set_rule(world.get_location('Magic from NCT Great Fairy'), lambda state: state.form('Deku'))
    # I'll have to test how this happens, I haven't played in so long
    # first cycle she gives you magic because you're stuck as deku, afterwards she gives you the mask because you're human
    # right?
    # so what if you start as goron or zora? not sure how that all works


    ### EAST CLOCK TOWN
    set_rule(world.get_location('East Clock Town 100 Rupee Chest'), lambda state: state.form('Human') or state.can('Goron Boost') or state.can('Gainer') or state.form('Zora'))
    # I need to figure out all the actual requirements for this, including tricks, so this one is tentative
    # also the trick names are guesses for sure

    set_rule(world.get_location('Clock Town Maze Minigame HP'), lambda state: state.form('Goron'))
    # oooh I didn't think about it before, do we want to include all the prizes for this?
    set_rule(world.get_location('Clock Town Maze Minigame 50 Rupees'), lambda state: state.form('Human'))
    set_rule(world.get_location('Clock Town Maze Minigame 20 Rupees'), lambda state: state.form('Zora'))
    set_rule(world.get_location('Clock Town Maze Minigame 10 Deku Nuts'), lambda state: state.form('Deku'))

    set_rule(world.get_location('Bomber Hideout 100 Rupee Chest'), lambda state: state.can_blast())
    # I feel like the goron might be able to just punch this todo: test if goron punch works here

    set_rule(world.get_location('Honey and Darling HP'), lambda state: state.has('Bomb Bag') and state.has('Bow') and state.form('Human'))
    set_rule(world.get_location('Clock Town Shooting Gallery Quiver Prize'), lambda state: state.has('Bow') and state.form('Human'))
    set_rule(world.get_location('Clock Town Shooting Gallery HP Prize'), lambda state: state.has('Bow') and state.form('Human'))

    set_rule(world.get_location('Kafei Mask'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora'))

    # 2 silver rupee chests in the stock pot in, jeez I forgot about these if I ever even knew about them
    # set_rule(world.get_location('Your Room Rupee Chest'), lambda state: True)
    # is human the only form where you get the key? I forget, but I think that's all you need to get this chest
    # set_rule(world.get_location('Anju Room Rupee Chest'), lambda state: True)
    # for this one, you just need to be able to get inside the inn after midnight on day 3
    # so either the room key or the deku flower
    # and these musings only apply to getting INTO these rooms, so the tests here are open
    # the relevant tests will be for the connecting areas

    set_rule(world.get_location('Grandma Stories HP 1'), lambda state: state.has('All Night Mask') and state.form('Human'))
    set_rule(world.get_location('Grandma Stories HP 2'), lambda state: state.has('All Night Mask') and state.form('Human'))

    # set_rule(world.get_location('Toilet Hand HP'), lambda state: state.has('Town Title Deed'))
    set_rule(world.get_location('Toilet Hand HP'), lambda state: state.has_paper())
    # you need some kind of paper, so any title deed, or a letter from the various subquests that involve letters
    # that's a lot of different ways to be able to do that, so we may need to have inventory record any subquest item
    # that can be obtained as obtained, so we can just do state.has('any paper') or something
    # for now I'll just leave it as the clock town title deed check, the easiest one to do
    # todo: test everything that can be used as paper and record reqs to get them, OR them all together for this check
    # man, this one is involved lol
    # actually you know what, I'm just gonna add state.has_paper()

    set_rule(world.get_location('Milk Bar Troupe Leaders Mask'), lambda state: [state.form(f) for f in ['Human', 'Deku', 'Goron', 'Zora']].count(True) == 4)
    set_rule(world.get_location('Milk Bar Bottle From Madame Aroma'), lambda state: state.has('Letter to Mama'))
    # so a note about doing checks for stuff like 'Letter to Mama' and stuff that resets when you save
    # it makes it a hell of a lot easier to be able to do checks for temp items like this
    # but it also probably means setting rules for these items and having locations for them
    # which means we'd have to have some kind of marker for them so they don't get mixed in to the pool
    # possibly issue in the future, just something to note for now


    ### TERMINA FIELD
    set_rule(world.get_location('Kamaro Mask'), lambda state: state.form('Human'))
    # so you have to be able to jump to their platform, which rules out goron and probably deku?
    # (actually maybe not if the goron can do some weird trick or something)
    # dunno if there's a form requirement when you actually talk to them, but I'm gonna assume human for now
    # todo: test form requirements

    # set_rule(world.get_location('Moons Tear'), lambda state: True)
    # pretty sure this is just open, even the deku can use the telescope

    set_rule(world.get_location('4 Gossip Stone HP'), lambda state: (state.can_blast() or state.form('Goron'))
        and (state.has('Sonata of Awakening') or state.has('Goron Lullaby') or state.has('New Wave Bossa Nova'))
        and (state.form('Deku') or state.form('Goron') or state.form('Zora')))

    set_rule(world.get_location('Termina Field Peahat Grotto HP'), lambda state: state.form('Human') or state.form('Goron') or state.form('Zora'))
    # how many ways to kill a peahat? lol
    # for now I'm gonna assume deku can't, but everyone else can

    # set_rule(world.get_location('Termina Field Dodongo Grotto HP'), lambda state: True)
    # ways to kill a dodongo? might be anyone actually

    set_rule(world.get_location('Termina Field Business Scrub Grotto HP'), lambda state: state.has('Adult Wallet'))
    # giving the moon's tear to the scrub is part of the connection requirement to get to the grotto, but once there
    # you just need the adult's wallet

    set_rule(world.get_location('Termina Field Beehive Grotto HP'), lambda state: (state.can_blast() or state.form('Goron'))
                                                                                  and state.has('Bow') and state.form('Zora'))
    # boulder to get through, then shoot the bees, then drop to the bottom of the pool as zora
    # actually shooting the bees might be possible as zora
    # todo: test this hp

    # set_rule(world.get_location('Termina Field Freestanding 20 Rupee Chest'), lambda state: True)
    # set_rule(world.get_location('Termina Field Deku Baba Pit 20 Rupee Chest'), lambda state: True)
    set_rule(world.get_location('Termina Field Hookshot Stump 20 Rupee Chest'), lambda state: state.has('Hookshot') and state.form('Human'))

    # set_rule(world.get_location(''), lambda state: state)
    # apparently if you look at some guys standing in the field through the telescope, there will be pits where they
    # each were? dunno what's in them, but we might need to record those

    # set_rule(world.get_location('Termina Field East Pillar Bombchu Pit'), lambda state: True)
    # it's an open check once you're there, you just need a bottle, bean, water, and be able to jump to it from the bean

    # set_rule(world.get_location(''), lambda state: state)

# ooh ooh
# maybe have a gate at the clock tower roof that requires the ocarina, to go back to south clock town on the first day
# maayyybe
# to force placement of the ocarina somewhere you can get to it in the first cycle
# depends on how crawling through the graph works
