#include <stdint.h>
#include "world.h"
#include "region.h"
#include "itempool.h"
#include "util.h"
#include "random.h"

static state_t maximum_exploration_state;
void fill_restrictive(world_t *world,
    location_e *locations, int32_t *loc_count,
    item_e *itempool, int32_t *itempool_count,
    int32_t count) 
{
    item_e unplaced_items[20];
    int32_t unplaced_items_count = 0;

    while (*itempool_count > 0 && *loc_count > 0)
    {
        //if remaining count is 0, return. Negative means unbounded.
        if (count == 0)
            break;

        //get an item and remove it from the itempool
        item_e item_to_place = itempool[--(*itempool_count)]; //pop item
        rng_shuffle_list(locations, sizeof(location_e), *loc_count);

        // generate the max states that include every remaining item
        // this will allow us to place this item in a reachable location
        state_get_states_with_items(&maximum_exploration_state,
            &(world->state), itempool /*+ unplaced_items */, itempool_count);

        //
        //this basically collects all items


        bool perform_access_check = true;
        if (options.check_beatable_only)
        {
            // if any world can not longer be beatable with the remaining items
            // then we must check for reachability no matter what.
            // This way the reachability test is monotonic. If we were to later
            // stop checking, then we could place an item needed in one world
            // in an unreachable place in another world
            //perform_access_check = not State.can_beat_game(maximum_exploration_state_list)
            
            perform_access_check =
                !can_beat_game(&maximum_exploration_state);
        }

        // find a location that the item can be places. It must be a valid location
        // in the world we are placing it (possibly checking for reachability)
        location_e spot_to_fill = LOCATION_NONE;
        for (int i = 0; i < *loc_count; i++)
        {
            location_e location = locations[i];
        }
    }
}

void fill_restrictive_all(world_t *world,
    location_e *locations, int32_t *loc_count,
    item_e *itempool, int32_t *itempool_count,
    int32_t count)
{
    fill_restrictive(world, locations, loc_count, itempool, itempool_count, *itempool_count);
}

void distribute_items_restrictive(world_t *world)
{
    //song_locations
    //shop_locations

    // If not passed in, then get a shuffled list of locations to fill in
    //if not fill_locations:

    location_e fill_locations[LOCATION_MAX];
    int num_locs = 0;
    for (int i = 0; i < LOCATION_MAX; i++)
    {
        if (location_table[i].active 
            && location_table[i].type != LOCATION_TYPE_SHOP
            && location_table[i].type != LOCATION_TYPE_SONG
            && location_table[i].type != LOCATION_TYPE_GOSSIPSTONE)
        {
            fill_locations[num_locs++] = location_table[i].k;
        }
    }

    //Generate the itempools
    //shopitempool
    //songitempool

    //if worlds[0].shuffle_song_items:
    //itempool.extend(songitempool)
    //    fill_locations.extend(song_locations)

    item_e itempool[LOCATION_MAX];
    memcpy(itempool, itempool_test, sizeof(itempool_test));
}