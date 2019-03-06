from collections import namedtuple
import logging
import random
from Utils import random_choices
from Item import ItemFactory


# TODO: This needs to include all the items that will always
# be included in the item pool, no matter which options are set.
alwaysitems = [
    "Mirror Shield",
    "Deku Mask",
    "Goron Mask",
    "Zora Mask",
    "Light Arrows",
    "Hookshot"]

extraitems = [
    "Kokiri Sword",
    "Gilded Sword",
    "Great Fairy Sword",
    "Hylian Shield",
    "Fierce Deity Mask",
    "Bow",
    "Large Quiver",
    "Largest Quiver",
    "Fire Arrows",
    "Ice Arrows",
    "Powder Keg",
    "Pictograph Box",
    "Lens of Truth",
    "Bomb Bag",
    "Big Bomb Bag",
    "Biggest Bomb Bag",
    "Adult Wallet",
    "Giant Wallet"
]

extra_masks = [
    "Postman's Hat",
    "All Night Mask",
    "Blast Mask",
    "Stone Mask",
    "Great Fairy Mask",
    "Keaton Mask",
    "Bremen Mask",
    "Bunny Hood",
    "Don Gero's Mask",
    "Mask of Scents",
    "Romani Mask",
    "Circus Leader Mask",
    "Kafei Mask",
    "Couple's Mask",
    "Mask of Truth",
    "Kamaro's Mask",
    "Gibdo Mask",
    "Garo Mask",
    "Captain's Hat",
    "Giant Mask"
]

# TODO: This contains most useful items so that
# the player has a higher chance finding them.
# I'm guessing finding the duplicate results in a bluepee or something?
easy_items = ([
    'Biggoron Sword',
    'Kokiri Sword',
    'Boomerang',
    'Lens of Truth',
    'Hammer',
    'Iron Boots',
    'Goron Tunic',
    'Zora Tunic',
    'Hover Boots',
    'Mirror Shield',
    'Fire Arrows',
    'Light Arrows',
    'Dins Fire',
    'Progressive Hookshot',
    'Progressive Strength Upgrade',
    'Progressive Scale',
    'Progressive Wallet',
    'Magic Meter',
    'Deku Stick Capacity',
    'Deku Nut Capacity',
    'Bow',
    'Slingshot',
    'Bomb Bag',
    'Double Defense'] +
    # The heart containers/pieces of heart should
    # be added so that the result is 13 full hearts
    # AND that the amount of items of 'easy_items' is
    # equal to that of 'normal_items'
    ['Heart Container'] * 16 +
    ['Piece of Heart'] * 3)

# TODO: Together with always_items, these should
# complete the regular set of items found in the game.
normal_items = (
    ['Heart Container'] * 4 +
    ['Piece of Heart'] * 52)


stray_fairy_locations = (
    ["WF-SF{0}".format(i) for i in range(1, 15)] +
    ["SH-SF{0}".format(i) for i in range(1, 15)] +
    ["GB-SF{0}".format(i) for i in range(1, 15)] +
    ["ST-SF{0}".format(i) for i in range(1, 15)])

item_difficulty_max = {
    'plentiful': {},
    'balanced': {},
    'scarce': {
        'Bombchus': 3,
        'Bombchus (5)': 1,
        'Bombchus (10)': 2,
        'Bombchus (20)': 0,
        'Magic Meter': 1,
        'Double Defense': 0,
        'Deku Stick Capacity': 1,
        'Deku Nut Capacity': 1,
        'Bow': 2,
        'Slingshot': 2,
        'Bomb Bag': 2,
        'Heart Container': 0,
    },
    'minimal': {
        'Bombchus': 1,
        'Bombchus (5)': 1,
        'Bombchus (10)': 0,
        'Bombchus (20)': 0,
        'Nayrus Love': 0,
        'Magic Meter': 1,
        'Double Defense': 0,
        'Deku Stick Capacity': 0,
        'Deku Nut Capacity': 0,
        'Bow': 1,
        'Slingshot': 1,
        'Bomb Bag': 1,
        'Heart Container': 0,
        'Piece of Heart': 0,
    },
}


DT_vanilla = (
    ['Recovery Heart'] * 2)

DC_vanilla = (
    ['Rupees (20)'])

FoT_vanilla = (
    ['Recovery Heart'] +
    ['Arrows (10)'] +
    ['Arrows (30)'])

FiT_vanilla = (
    ['Rupees (200)'])

SpT_vanilla = (
    ['Deku Shield'] * 2 +
    ['Recovery Heart'] +
    ['Bombs (20)'])

ShT_vanilla = (
    ['Arrows (30)'])

BW_vanilla = (
    ['Recovery Heart'] +
    ['Bombs (10)'] +
    ['Rupees (200)'] +
    ['Deku Nuts (5)'] +
    ['Deku Nuts (10)'] +
    ['Deku Shield'] +
    ['Hylian Shield'])

GTG_vanilla = (
    ['Arrows (30)'] * 3 +
    ['Rupees (200)'])

GC_vanilla = (
    ['Rupees (5)'] * 3 +
    ['Arrows (30)'])


normal_bottles = [
    'Bottle',
    'Bottle with Milk',
    'Bottle with Red Potion',
    'Bottle with Green Potion',
    'Bottle with Blue Potion',
    'Bottle with Fairy',
    'Bottle with Fish',
    'Bottle with Bugs',
    'Bottle with Poe',
    'Bottle with Big Poe']

normal_bottle_count = 6


normal_rupees = (
    ['Rupees (5)'] * 13 +
    ['Rupees (20)'] * 5 +
    ['Rupees (50)'] * 7 +
    ['Rupees (200)'] * 3)

shopsanity_rupees = (
    ['Rupees (5)'] * 2 +
    ['Rupees (20)'] * 10 +
    ['Rupees (50)'] * 10 +
    ['Rupees (200)'] * 5 +
    ['Progressive Wallet'])

vanilla_shop_items = {
    'Trading Post Item 1': 'Buy Red Potion [30]',  # Price: 30
    'Trading Post Item 2': 'Buy Green Potion [30]',  # Price: 30
    'Trading Post Item 3': 'Buy Hylian Shield [80]',  # Price: 80
    'Trading Post Item 4': 'Buy Fairy\'s Spirit',  # Price: 50
    'Trading Post Item 5': 'Buy Deku Stick',  # Price: 10
    'Trading Post Item 6': 'Buy Arrows (30)',  # Price: 30
    'Trading Post Item 7': 'Buy Deku Nut (10)',  # Price: 30
    'Trading Post Item 8': 'Buy Arrows (50)',  # Price: 40
    'Bomb Shop Item 1': 'Buy Bombs (10) [30]',  # Price: 30
    'Bomb Shop Item 2': 'Buy Bombchus (10)',  # Price: 40
    'Bomb Shop Item 3': 'Buy Bomb Bag',  # Price: 50
    # Not sure how to signify the Big Bomb Bag, opted for 0
    'Bomb Shop Item 0': 'Buy Big Bomb Bag',  # Price: 90
    'Magic Hag\'s Potion Shop Item 1': 'Buy Blue Potion',  # Price: 60
    'Magic Hag\'s Potion Shop Item 2': 'Buy Green Potion [10]',  # Price: 10
    'Magic Hag\'s Potion Shop Item 3': 'Buy Red Potion [20]',  # Price: 20
    'Goron Shop (Winter) Item 1': 'Buy Bombs (10) [40]',  # Price: 40
    'Goron Shop (Winter) Item 2': 'Buy Arrows (10) [40]',  # Price: 40
    'Goron Shop (Winter) Item 3': 'Buy Red Potion [80]',  # Price: 80
    'Goron Shop (Spring) Item 1': 'Buy Bombs (10) [20]',  # Price: 20
    'Goron Shop (Spring) Item 2': 'Buy Arrows (10) [20]',  # Price: 20
    'Goron Shop (Spring) Item 3': 'Buy Red Potion [50]',  # Price: 50
    'Zora Shop Item 1': 'Buy Hylian Shield [90]',  # Price: 90
    'Zora Shop Item 2': 'Buy Arrows (10) [20]',  # Price: 20
    'Zora Shop Item 3': 'Buy Red Potion [60]'  # Price: 60
    # TODO: Fill out the rest
}


min_shop_items = (
    ['Buy Deku Shield'] +
    ['Buy Hylian Shield'] +
    ['Buy Goron Tunic'] +
    ['Buy Zora Tunic'] +
    ['Buy Deku Nut (5)'] * 2 + ['Buy Deku Nut (10)'] +
    ['Buy Deku Stick (1)'] * 2 +
    ['Buy Deku Seeds (30)'] +
    ['Buy Arrows (10)'] * 2 + ['Buy Arrows (30)'] + ['Buy Arrows (50)'] +
    ['Buy Bombchu (5)'] + ['Buy Bombchu (10)'] * 2 + ['Buy Bombchu (20)'] +
    ['Buy Bombs (5) [25]'] + ['Buy Bombs (5) [35]'] + ['Buy Bombs (10)'] + ['Buy Bombs (20)'] +
    ['Buy Green Potion'] +
    ['Buy Red Potion [30]'] +
    ['Buy Blue Fire'] +
    ['Buy Fairy\'s Spirit'] +
    ['Buy Bottle Bug'] +
    ['Buy Fish'])


vanilla_deku_scrubs = {
    'ZR Grotto Deku Scrub Red Potion': 'Buy Red Potion [30]',
    'ZR Grotto Deku Scrub Green Potion': 'Buy Green Potion',
    'SFM Grotto Deku Scrub Red Potion': 'Buy Red Potion [30]',
    'SFM Grotto Deku Scrub Green Potion': 'Buy Green Potion',
    'LH Grotto Deku Scrub Deku Nuts': 'Buy Deku Nut (5)',
    'LH Grotto Deku Scrub Bombs': 'Buy Bombs (5) [35]',
    'LH Grotto Deku Scrub Arrows': 'Buy Arrows (30)',
    'Valley Grotto Deku Scrub Red Potion': 'Buy Red Potion [30]',
    'Valley Grotto Deku Scrub Green Potion': 'Buy Green Potion',
    'LW Deku Scrub Deku Nuts': 'Buy Deku Nut (5)',
    'LW Deku Scrub Deku Sticks': 'Buy Deku Stick (1)',
    'LW Grotto Deku Scrub Arrows': 'Buy Arrows (30)',
    'Desert Grotto Deku Scrub Red Potion': 'Buy Red Potion [30]',
    'Desert Grotto Deku Scrub Green Potion': 'Buy Green Potion',
    'DMC Deku Scrub Bombs': 'Buy Bombs (5) [35]',
    'DMC Grotto Deku Scrub Deku Nuts': 'Buy Deku Nut (5)',
    'DMC Grotto Deku Scrub Bombs': 'Buy Bombs (5) [35]',
    'DMC Grotto Deku Scrub Arrows': 'Buy Arrows (30)',
    'Goron Grotto Deku Scrub Deku Nuts': 'Buy Deku Nut (5)',
    'Goron Grotto Deku Scrub Bombs': 'Buy Bombs (5) [35]',
    'Goron Grotto Deku Scrub Arrows': 'Buy Arrows (30)',
    'LLR Grotto Deku Scrub Deku Nuts': 'Buy Deku Nut (5)',
    'LLR Grotto Deku Scrub Bombs': 'Buy Bombs (5) [35]',
    'LLR Grotto Deku Scrub Arrows': 'Buy Arrows (30)',
}


deku_scrubs_items = (
    ['Deku Nuts (5)'] * 5 +
    ['Deku Stick (1)'] +
    ['Bombs (5)'] * 5 +
    ['Recovery Heart'] * 4 +
    ['Rupees (5)'] * 4) # ['Green Potion']


rewardlist = [
    "Odolwa's Remains",
    "Goht's Remains",
    "Gyorg's Remains",
    "Twinmold's Remains"]


songlist = [
    "Song of Time",
    "Song of Healing",
    "Song of Soaring",
    "Epona's Song",
    "Song of Storms",
    "Sonata of Awakening",
    "Goron Lullaby",
    "New Wave Bossa Nova",
    "Elegy of Emptiness",
    "Oath to Order"]


tradeitems = [
    "Moon's Tear",
    'Town Title Deed',
    'Swamp Title Deed',
    'Mountain Title Deed',
    'Ocean Title Deed',
    'Room Key',
    'Letter to Kafei',
    'Pendant of Memories'
    'Special Delivery to Mama'
]


trade_items = {
    'Moon Tear Crater': "Moon's Tear",
    'Clock Town Deku Salesman': 'Land Title Deed',
    'Swamp Deku Salesman': 'Swamp Title Deed',
    'Mountain Deku Salesman': 'Mountain Title Deed',
    'Ocean Deku Salesman': 'Ocean Title Deed',
    'Canyon Deku Salesman': 'Rupees (200)',
    'Have you seen this man?': 'Letter To Kafei',
    'Item From Kafei': 'Pendant of Memories',
    'Keaton Mask From Kafei': 'Kafei Mask',  # Why is this a Kafei Mask? Shouldn't this be the Keaton Mask?
    'Letter From Kafei': 'Letter To Mama',
    'We Shall Greet The Morning Together': "Couple's Mask"
}

# TODO: This is copied from the old MM list.
# Not sure what the idea was of this list.
npc_items = {
    # TODO: List all locations which give items by NPC,
    # and set them to give that specific item
    'Gift From Hungry Goron': "Don Gero's Mask",

}

# TODO: Copied from the old MM list.
# eventlocations = {
#     'Majora': "Majora's Mask"
# }

# TODO: This is a list of events that result in an item or event trigger
# It seems these are hardlocked into place when generating the item pool.
eventlocations = {
    'Ganon': 'Triforce',
    'Zeldas Letter': 'Zeldas Letter',
    'Magic Bean Salesman': 'Magic Bean',
    'King Zora Moves': 'Bottle',
    'Master Sword Pedestal': 'Master Sword',
    'Epona': 'Epona',
    'Deku Baba Sticks': 'Deku Stick Drop',
    'Goron City Stick Pot': 'Deku Stick Drop',
    'Zoras Domain Stick Pot': 'Deku Stick Drop',
    'Deku Baba Nuts': 'Deku Nut Drop',
    'Zoras Domain Nut Pot': 'Deku Nut Drop',
    'Gerudo Fortress Carpenter Rescue': 'Carpenter Rescue',
    'Haunted Wasteland Bombchu Salesman': 'Bombchus',
    'Ganons Castle Forest Trial Clear': 'Forest Trial Clear',
    'Ganons Castle Fire Trial Clear': 'Fire Trial Clear',
    'Ganons Castle Water Trial Clear': 'Water Trial Clear',
    'Ganons Castle Shadow Trial Clear': 'Shadow Trial Clear',
    'Ganons Castle Spirit Trial Clear': 'Spirit Trial Clear',
    'Ganons Castle Light Trial Clear': 'Light Trial Clear'
}


junk_pool_base = [
    ('Bombs (5)',       8),
    ('Bombs (10)',      2),
    ('Arrows (5)',      8),
    ('Arrows (10)',     2),
    ('Deku Stick (1)',  5),
    ('Deku Nuts (5)',   5),
    ('Deku Seeds (30)', 5),
    ('Rupees (5)',      10),
    ('Rupees (20)',     4),
    ('Rupees (50)',     1),
]
junk_pool = []


def get_junk_item(count=1):
    junk_items, junk_weights = zip(*junk_pool)
    return random_choices(junk_items, weights=junk_weights, k=count)


def replace_max_item(items, item, max):
    count = 0
    for i, val in enumerate(items):
        if val == item:
            if count >= max:
                items[i] = get_junk_item()[0]
            count += 1


# TODO: not sure there are ice traps in MM?
def generate_itempool(world):
    junk_pool[:] = list(junk_pool_base)
    if world.junk_ice_traps == 'on':
        junk_pool.append(('Ice Trap', 10))
    elif world.junk_ice_traps in ['mayhem', 'onslaught']:
        junk_pool[:] = [('Ice Trap', 1)]

    for location, item in eventlocations.items():
        world.push_item(location, ItemFactory(item, world))
        world.get_location(location).locked = True

    # set up item pool
    (pool, placed_items) = get_pool_core(world)
    world.itempool = ItemFactory(pool, world)
    for (location, item) in placed_items.items():
        world.push_item(location, ItemFactory(item, world))
        world.get_location(location).locked = True

    choose_trials(world)
    fill_bosses(world)

    world.initialize_items()


def get_pool_core(world):
    pool = []
    placed_items = {}

    if world.shuffle_kokiri_sword:
        pool.append('Kokiri Sword')
    else:
        placed_items['Kokiri Sword Chest'] = 'Kokiri Sword'

    if world.open_fountain:
        bottle = random.choice(normal_bottles)
        pool.append(bottle)
    else:
        pool.append('Bottle with Letter')

    if world.shuffle_weird_egg:
        pool.append('Weird Egg')
    else:
        placed_items['Malon Egg'] = 'Weird Egg'

    if world.shuffle_ocarinas:
        pool.extend(['Ocarina'] * 2)
    else:
        placed_items['Gift from Saria'] = 'Ocarina'
        placed_items['Ocarina of Time'] = 'Ocarina'

    if world.bombchus_in_logic:
        pool.extend(['Bombchus'] * 5)
    else:
        pool.extend(['Bombchus (5)'] + ['Bombchus (10)'] * 2)
        pool.extend(['Bombchus (10)'])
        pool.extend(['Bombchus (20)'])

    pool.extend(['Ice Trap'] * 6)

    if world.gerudo_fortress == 'open':
        placed_items['Gerudo Fortress North F1 Carpenter'] = 'Recovery Heart'
        placed_items['Gerudo Fortress North F2 Carpenter'] = 'Recovery Heart'
        placed_items['Gerudo Fortress South F1 Carpenter'] = 'Recovery Heart'
        placed_items['Gerudo Fortress South F2 Carpenter'] = 'Recovery Heart'
    elif world.shuffle_smallkeys == 'keysanity':
        if world.gerudo_fortress == 'fast':
            pool.append('Small Key (Gerudo Fortress)')
            placed_items['Gerudo Fortress North F2 Carpenter'] = 'Recovery Heart'
            placed_items['Gerudo Fortress South F1 Carpenter'] = 'Recovery Heart'
            placed_items['Gerudo Fortress South F2 Carpenter'] = 'Recovery Heart'
        else:
            pool.extend(['Small Key (Gerudo Fortress)'] * 4)
    else:
        if world.gerudo_fortress == 'fast':
            placed_items['Gerudo Fortress North F1 Carpenter'] = 'Small Key (Gerudo Fortress)'
            placed_items['Gerudo Fortress North F2 Carpenter'] = 'Recovery Heart'
            placed_items['Gerudo Fortress South F1 Carpenter'] = 'Recovery Heart'
            placed_items['Gerudo Fortress South F2 Carpenter'] = 'Recovery Heart'
        else:
            placed_items['Gerudo Fortress North F1 Carpenter'] = 'Small Key (Gerudo Fortress)'
            placed_items['Gerudo Fortress North F2 Carpenter'] = 'Small Key (Gerudo Fortress)'
            placed_items['Gerudo Fortress South F1 Carpenter'] = 'Small Key (Gerudo Fortress)'
            placed_items['Gerudo Fortress South F2 Carpenter'] = 'Small Key (Gerudo Fortress)'

    if world.shuffle_gerudo_card and world.gerudo_fortress != 'open':
        pool.append('Gerudo Membership Card')
    else:
        placed_items['Gerudo Fortress Membership Card'] = 'Gerudo Membership Card'

    if world.shopsanity == 'off':
        placed_items.update(vanilla_shop_items)
        if world.bombchus_in_logic:
            placed_items['Kokiri Shop Item 8'] = 'Buy Bombchu (5)'
            placed_items['Castle Town Bazaar Item 4'] = 'Buy Bombchu (5)'
            placed_items['Kakariko Bazaar Item 4'] = 'Buy Bombchu (5)'
        pool.extend(normal_rupees)

    else:
        remain_shop_items = list(vanilla_shop_items.values())
        pool.extend(min_shop_items)
        for item in min_shop_items:
            remain_shop_items.remove(item)

        shop_slots_count = len(remain_shop_items)
        shop_nonitem_count = len(world.shop_prices)
        shop_item_count = shop_slots_count - shop_nonitem_count

        pool.extend(random.sample(remain_shop_items, shop_item_count))
        pool.extend(get_junk_item(shop_nonitem_count))
        if world.shopsanity == '0':
            pool.extend(normal_rupees)
        else:
            pool.extend(shopsanity_rupees)

    if world.shuffle_scrubs != 'off':
        pool.extend(['Deku Nuts (5)', 'Deku Stick (1)', 'Deku Shield'])
        pool.append('Deku Nuts (5)')
        pool.extend(['Bombs (5)', 'Recovery Heart', 'Rupees (5)'])
        pool.extend(deku_scrubs_items)
        for _ in range(7):
            pool.append('Arrows (30)' if random.randint(0,3) > 0 else 'Deku Seeds (30)')

    else:
        placed_items['DC Deku Scrub Deku Nuts'] = 'Buy Deku Nut (5)'
        placed_items['DC Deku Scrub Deku Sticks'] = 'Buy Deku Stick (1)'
        placed_items['DC Deku Scrub Deku Seeds'] = 'Buy Deku Seeds (30)'
        placed_items['DC Deku Scrub Deku Shield'] = 'Buy Deku Shield'
        placed_items['Jabu Deku Scrub Deku Nuts'] = 'Buy Deku Nut (5)'
        placed_items['GC Deku Scrub Bombs'] = 'Buy Bombs (5) [35]'
        placed_items['GC Deku Scrub Arrows'] = 'Buy Arrows (30)'
        placed_items['GC Deku Scrub Red Potion'] = 'Buy Red Potion [30]'
        placed_items['GC Deku Scrub Green Potion'] = 'Buy Green Potion'
        placed_items.update(vanilla_deku_scrubs)

    pool.extend(alwaysitems)

    pool.extend(DT_vanilla)
    pool.extend(DC_vanilla)
    pool.extend(FoT_vanilla)
    pool.extend(FiT_vanilla)
    placed_items['Spirit Temple Nut Crate'] = 'Deku Nut Drop'
    pool.extend(SpT_vanilla)
    pool.extend(ShT_vanilla)
    placed_items['Bottom of the Well Stick Pot'] = 'Deku Stick Drop'
    pool.extend(BW_vanilla)
    pool.extend(GTG_vanilla)
    pool.extend(GC_vanilla)

    for _ in range(normal_bottle_count):
        bottle = random.choice(normal_bottles)
        pool.append(bottle)

    earliest_trade = tradeitemoptions.index(world.logic_earliest_adult_trade)
    latest_trade = tradeitemoptions.index(world.logic_latest_adult_trade)
    if earliest_trade > latest_trade:
        earliest_trade, latest_trade = latest_trade, earliest_trade
    tradeitem = random.choice(tradeitems[earliest_trade:latest_trade+1])
    pool.append(tradeitem)

    pool.extend(songlist)
    if world.start_with_fast_travel:
        pool.remove('Prelude of Light')
        pool.remove('Serenade of Water')
        pool.remove('Farores Wind')
        world.state.collect(ItemFactory('Prelude of Light'))
        world.state.collect(ItemFactory('Serenade of Water'))
        world.state.collect(ItemFactory('Farores Wind'))
        pool.extend(get_junk_item(3))

    if world.shuffle_mapcompass == 'remove' or world.shuffle_mapcompass == 'startwith':
        for item in [item for dungeon in world.dungeons for item in dungeon.dungeon_items]:
            world.state.collect(item)
            pool.extend(get_junk_item())
    if world.shuffle_smallkeys == 'remove':
        for item in [item for dungeon in world.dungeons for item in dungeon.small_keys]:
            world.state.collect(item)
            pool.extend(get_junk_item())
    if world.shuffle_bosskeys == 'remove':
        for item in [item for dungeon in world.dungeons for item in dungeon.boss_key]:
            world.state.collect(item)
            pool.extend(get_junk_item())
    if not world.keysanity:
        world.state.collect(ItemFactory('Small Key (Fire Temple)'))
    world.state.collect(ItemFactory('Small Key (Water Temple)'))

    if world.item_pool_value == 'plentiful':
        pool.extend(easy_items)
    else:
        pool.extend(normal_items)

    if not world.shuffle_kokiri_sword:
        replace_max_item(pool, 'Kokiri Sword', 0)

    if world.junk_ice_traps == 'off':
        replace_max_item(pool, 'Ice Trap', 0)
    elif world.junk_ice_traps == 'onslaught':
        for item in [item for item, weight in junk_pool_base] + ['Recovery Heart', 'Bombs (20)', 'Arrows (30)']:
            replace_max_item(pool, item, 0)

    for item,max in item_difficulty_max[world.item_pool_value].items():
        replace_max_item(pool, item, max)

    if world.start_with_wallet:
        replace_max_item(pool, 'Progressive Wallet', 0)
        for i in [1, 2, 3]: # collect wallets
            world.state.collect(ItemFactory('Progressive Wallet'))

    return (pool, placed_items)


# TODO: I think the MM equivalent would be the masked kids
# on the moon? This'd be used when they are required, or not, or partially?
# > This should be adjusted together with the 'skipped_trials' in World.py.
def choose_trials(world):
    if world.trials_random:
        world.trials = random.randint(0, 6)
    num_trials = int(world.trials)
    choosen_trials = random.sample(['Forest', 'Fire', 'Water', 'Spirit', 'Shadow', 'Light'], num_trials)
    for trial in world.skipped_trials:
        if trial not in choosen_trials:
            world.skipped_trials[trial] = True


# TODO: Randomizing these would create a teleporter to the boss room of the
# remains received? Might break? Might not? Might be redundant? Needs more attention.
def fill_bosses(world, bossCount=4):
    boss_rewards = ItemFactory(rewardlist, world)
    boss_locations = [
        world.get_location('Remains From Odolwa'),
        world.get_location('Remains From Goht'),
        world.get_location('Remains From Gyorg'),
        world.get_location('Remains From Twinmold')
        ]

    placed_prizes = [loc.item.name for loc in boss_locations if loc.item is not None]
    unplaced_prizes = [item for item in boss_rewards if item.name not in placed_prizes]
    empty_boss_locations = [loc for loc in boss_locations if loc.item is None]
    prizepool = list(unplaced_prizes)
    prize_locs = list(empty_boss_locations)

    while bossCount:
        bossCount -= 1
        random.shuffle(prizepool)
        random.shuffle(prize_locs)
        item = prizepool.pop()
        loc = prize_locs.pop()
        world.push_item(loc, item)
