from collections import namedtuple
import logging
import random

from Items import ItemFactory

#This file sets the item pools for various modes. Timed modes and triforce hunt are enforced first, and then extra items are specified per mode to fill in the remaining space.
#Some basic items that various modes require are placed here, including pendants and crystals. Medallion requirements for the two relevant entrances are also decided.
alwaysitems = (['Kokiri Sword', 'Gilded Sword', 'Great Fairy Sword', 'Hylian Shield', 'Mirror Shield'] +
              ['Deku Mask', 'Goron Mask', 'Zora Mask', 'Fierce Deity Mask'] +
              ['Postmans Hat', 'Blast Mask', 'Great Fairy Mask', 'All Night Mask', 'Stone Mask'] +
              ['Keaton Mask', 'Bremen Mask', 'Bunny Hood', 'Don Geros Mask', 'Mask of Scents'] +
              ['Romani Mask', 'Circus Leader Mask', 'Couple Mask', 'Mask of Truth'] +
              ['Kamaros Mask', 'Garo Mask', 'Captains Hat', 'Gibdo Mask', 'Giant Mask'] +
              ['Bow', 'Large Quiver', 'Largest Quiver'] + ['Fire Arrows', 'Ice Arrows', 'Light Arrows'] +
              ['Powder Keg', 'Pictograph Box', 'Lens of Truth', 'Hookshot'] +
              ['Bomb Bag', 'Big Bomb Bag', ] + ['Bottle'] * 2 + ['Bottle with Gold Dust'] +
              ['Bottle with Red Potion'] + ['Bottle with Milk'] + ['Bottle with Chateau Romani'] +
              ['Piece of Heart'] * 52 + ['Heart Container'] * 4 + ['Adult Wallet', 'Giant Wallet'])
notmapcompass = ['Ice Trap'] * 8
rewardlist = ['Odolwa\'s Remains', 'Goht\'s Remains', 'Gyorg\'s Remains', 'Twinmold\'s Remains']
songlist = ['Song of Time', 'Song of Healing', 'Song of Soaring', 'Eponas Song','Song of Storms', 'Sonata of Awakening', 'Goron Lullaby', 'New Wave Bossa Nova', 'Elegy of Emptiness', 'Oath to Order']
# TODO: this could need to be aligned with the location_table
stray_fairy_locations = (['WF-SF1', 'WF-SF2', 'WF-SF3', 'WF-SF4', 'WF-SF5', 'WF-SF6', 'WF-SF7', 'WF-SF8', 'WF-SF9', 'WF-SF10', 'WF-SF11', 'WF-SF12', 'WF-SF13', 'WF-SF14', 'WF-SF15'] +
                        ['SH-SF1', 'SH-SF2', 'SH-SF3', 'SH-SF4', 'SH-SF5', 'SH-SF6', 'SH-SF7', 'SH-SF8', 'SH-SF9', 'SH-SF10', 'SH-SF11', 'SH-SF12', 'SH-SF13', 'SH-SF14', 'SH-SF15'] +
                        ['GB-SF1', 'GB-SF2', 'GB-SF3', 'GB-SF4', 'GB-SF5', 'GB-SF6', 'GB-SF7', 'GB-SF8', 'GB-SF9', 'GB-SF10', 'GB-SF11', 'GB-SF12', 'GB-SF13', 'GB-SF14', 'GB-SF15'] +
                        ['ST-SF1', 'ST-SF2', 'ST-SF3', 'ST-SF4', 'ST-SF5', 'ST-SF6', 'ST-SF7', 'ST-SF8', 'ST-SF9', 'ST-SF10', 'ST-SF11', 'ST-SF12', 'ST-SF13', 'ST-SF14', 'ST-SF15'])
tradeitems = (['Moon Tear', 'Town Title Deed', 'Swamp Title Deed', 'Mountain Title Deed', 'Ocean Title Deed'] +


WF_vanilla = (['Recovery Heart'] * 2)
SH_vanilla = (['Recovery Heart'] * 2)
GB_vanilla = (['Recovery Heart'] * 2)
ST_vanilla = (['Recovery Heart'] * 2)
PF_vanilla = (['Recovery Heart'] * 2)

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
    ['Rupees (5)'] * 13
    + ['Rupees (20)'] * 5
    + ['Rupees (50)'] * 7
    + ['Rupees (200)'] * 3)

shopsanity_rupees = (
    ['Rupees (5)'] * 2
    + ['Rupees (20)'] * 10
    + ['Rupees (50)'] * 10
    + ['Rupees (200)'] * 5
    + ['Progressive Wallet'])

vanilla_shop_items = {
    'Trading Post Item 1': 'Buy Hylian Shield',
    # TODO: Fill out the rest
}

titledeeds = {
    'Sad Moon Crater': 'Moon\'s Tear',
    # TODO: fill out the rest
}

npc_items = {
    # TODO: List all locations which give items by NPC, and set them to give that specific item
}

eventlocations = {
    'Majora': 'Majora\'s Mask'
}

junk_pool = (
    8 *  ['Bombs (5)'] +
    2 *  ['Bombs (10)'] +
    8 *  ['Arrows (5)'] +
    2 *  ['Arrows (10)'] +
    5 *  ['Deku Stick (1)'] +
    5 *  ['Deku Nuts (5)'] +
    10 * ['Rupees (5)'] +
    4 *  ['Rupees (20)'] +
    20 * ['Ice Trap'])
def get_junk_item(count=1):
    ret_junk = []
    for _ in range(count):
        ret_junk.append(random.choice(junk_pool))

    return ret_junk


def generate_itempool(world):
    # set up item pool
    (pool, placed_items) = get_pool_core(world)
    world.itempool = ItemFactory(pool, world)
    for (location, item) in placed_items.items():
        world.push_item(location, ItemFactory(item, world))
        world.get_location(location).event = True

    fill_bosses(world)

    world.initialize_items()

'''
This is where we decide what items to place and how
'''
def get_pool_core(world):
    pool = []
    placed_items = {}
    '''
        # Used to place an item randomly into the pool
        pool.append('Kokiri Sword')
        # Used to place a specific item in a specific location
         placed_items['Kokiri Sword Chest'] = 'Kokiri Sword'
         # Adds x items to the pool which are not progression items
        pool.extend(get_junk_item(37))
        # locations_with_items is a list of key value pairs where
        #   the key is the location name for an item
        #   the value is the item being placed at that location
        placed_items.update(locations_with_items)
        # tells the logic that you start out with the given item
        world.state.collect(item)
    '''
    pool.extend(songlist)

    if world.shuffle_mapcompass == 'remove':
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
    return (pool, placed_items)

def fill_songs(world, attempts=15):
    songs = ItemFactory(songlist)
    song_locations = [world.get_location('Song from Skull Kid'), world.get_location('Song from HMS'), world.get_location('Song from Owl Tablet'), world.get_location('Song from Romani'), world.get_location('Song at Grave'), world.get_location('Song from Monkey'), world.get_location('Song from Baby Goron'), world.get_location('Song from Goron Elder'), world.get_location('Song from Zora Eggs'), world.get_location('Song from Igos'), world.get_location('Song from the Giants')]
    placed_prizes = [loc.item.name for loc in song_locations if loc.item is not None]
    unplaced_prizes = [song for song in songs if song.name not in placed_prizes]
    empty_song_locations = [loc for loc in song_locations if loc.item is None]

    while attempts:
        attempts -= 1
        try:
            prizepool = list(unplaced_prizes)
            prize_locs = list(empty_song_locations)
            random.shuffle(prizepool)
            random.shuffle(prize_locs)
            fill_restrictive(world, world.get_all_state(keys=True), prize_locs, prizepool) #TODO: Set keys to true once keys are properly implemented
        except FillError:
            logging.getLogger('').info("Failed to place songs. Will retry %s more times", attempts)
            for location in empty_song_locations:
                location.item = None
            continue
        break
    else:
        raise FillError('Unable to place songs')

def fill_bosses(world, bossCount=4):
    boss_rewards = ItemFactory(rewardlist)
    boss_locations = [world.get_location('Odolwa'), world.get_location('Goht'), world.get_location('Gyorg'), world.get_location('Twinmold')]
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
        world.push_item(loc, item, False)
        world.get_location(loc).event = True
