#include "world.h"
#include "dungeonlist.h"
#include <stdint.h>

dungeon_table_entry dungeon_table[] =
{
    {
        .scene = DUNGEON_DEKU_TREE,
        .boss_key = 0,
        .small_key = 0,
        .small_key_mq = 0,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_DODONGOS_CAVERN,
        .boss_key = 0,
        .small_key = 0,
        .small_key_mq = 0,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_JABU_JABUS_BELLY,
        .boss_key = 0,
        .small_key = 0,
        .small_key_mq = 0,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_FOREST_TEMPLE,
        .boss_key = 1,
        .small_key = 5,
        .small_key_mq = 6,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_FIRE_TEMPLE,
        .boss_key = 1,
        .small_key = 8,
        .small_key_mq = 5,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_WATER_TEMPLE,
        .boss_key = 1,
        .small_key = 6,
        .small_key_mq = 2,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_SPIRIT_TEMPLE,
        .boss_key = 1,
        .small_key = 5,
        .small_key_mq = 7,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_SHADOW_TEMPLE,
        .boss_key = 1,
        .small_key = 5,
        .small_key_mq = 6,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_BOTTOM_OF_THE_WELL,
        .boss_key = 0,
        .small_key = 3,
        .small_key_mq = 2,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_ICE_CAVERN,
        .boss_key = 0,
        .small_key = 0,
        .small_key_mq = 0,
        .dungeon_item = 1,
    },
    {
        .scene = DUNGEON_GANONS_TOWER,
        .boss_key = 0,
        .small_key = 0,
        .small_key_mq = 0,
        .dungeon_item = 0,
    },
    {
        .scene = DUNGEON_GERUDO_TRAINING_GROUNDS,
        .boss_key = 0,
        .small_key = 9,
        .small_key_mq = 3,
        .dungeon_item = 0,
    },
    {
        .scene = DUNGEON_THIEVES_HIDEOUT,
        .boss_key = 0,
        .small_key = 0,
        .small_key_mq = 0,
        .dungeon_item = 0,
    },
    {
        .scene = DUNGEON_GANONS_CASTLE,
        .boss_key = 1,
        .small_key = 2,
        .small_key_mq = 3,
        .dungeon_item = 0,
    },
};