#ifndef DUNGEONLIST_H
#define DUNGEONLIST_H

#include <stdint.h>


typedef struct
{
    int8_t scene;
    int8_t boss_key;
    int8_t small_key;
    int8_t small_key_mq;
    int8_t dungeon_item;
} dungeon_table_entry;

extern dungeon_table_entry dungeon_table[];

#endif // !DUNGEONLIST_H
