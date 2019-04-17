#include <stdint.h>
#include <stdbool.h>
#include <n64.h>
#include "world.h"
#include "region.h"

//self.keysanity = self.shuffle_smallkeys != 'dungeon'
//self.check_beatable_only = not self.all_reachable


//         self.can_take_damage = True

static void initialize_world()
{
    for (int scene = 0; scene < 14; scene++)
    {
        bool scene_mq = options.dungeon_mq[scene];

        //resolve regions
        region_list_t region_list;
        if (scene_mq)
        {
            region_list = mq_only_regions[scene];
        }
        else
        {
            region_list = va_only_regions[scene];
        }
        for (int i = 0; i < region_list.count; i++)
        {
            region_t region = region_list.values[i];
            world_regions[region.k] = region;
        }

        //resolve location conflicts
        for (int i = 0; i < location_conflicts[scene].count; i++)
        {
            location_conflict_t item = location_conflicts[scene].values[i];
            if (scene_mq)
            {
                location_table[item.k].rule = item.mq_rule;
            }
            else
            {
                location_table[item.k].rule = item.va_rule;
            }
        }
    }
}


void initialize()
{
    options.keysanity = true;
    options.shuffle_weird_egg = true;
    options.shuffle_song_items = true;
    options.big_poe_count = 10;
    initialize_world();
}
