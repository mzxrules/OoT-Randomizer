#include <stdint.h>
#include "world.h"
#include "region.h"
#include "itempool.h"
#include "util.h"
#include "random.h"


void fill_restrictive(world_t *world,
    location_e *locations, int loc_count,
    item_e *itempool, int item_count)


{
    while (item_count > 0 && loc_count > 0)
    {
        //option.check_beatable_only
        item_e item_to_place = itempool[--item_count]; //pop item
        rng_shuffle_list(locations, sizeof(location_e), loc_count);

        // generate the max states that include every remaining item
        // this will allow us to place this item in a reachable location
        //maximum_exploration_state_list = State.get_states_with_items(base_state_list, itempool + unplaced_items)
        //
        //this basically collects all items
    }
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