#include "item.h"
#include "state.h"
#include <stdbool.h>


bool item_is_progressive_item(item_e item)
{
    if (item >= SMALL_KEY_FOREST_TEMPLE && item <= SMALL_KEY_GANONS_CASTLE)
        return true;
    return item == SMALL_KEY
        || item == GOLD_SKULLTULA_TOKEN
        || item == PROGRESSIVE_HOOKSHOT
        || item == PROGRESSIVE_STRENGTH_UPGRADE
        || item == PROGRESSIVE_WALLET
        || item == PROGRESSIVE_SCALE;
}

bool display_as_bottle_item(item_e item)
{
    return item >= BOTTLE_WITH_RED_POTION && item <= BOTTLE_WITH_POE;
}

bool item_is_bombchu(item_e item)
{
    return item == BOMBCHUS
        || item == BOMBCHUS_5
        || item == BOMBCHUS_10
        || item == BOMBCHUS_20;
}

bool item_is_bottle(item_e item)
{
    //fixme
    return item == BOTTLE;
}

bool item_is_key(item_e item)
{
    return item_table[item].type == ITEM_TYPE_SMALLKEY
        || item_table[item].type == ITEM_TYPE_BOSSKEY;
}

bool item_is_smallkey(item_e item)
{
    return item_table[item].type == ITEM_TYPE_SMALLKEY
        || item_table[item].type == ITEM_TYPE_FORTRESS_SMALLKEY;
}

bool item_is_bosskey(item_e item)
{
    return item_table[item].type == ITEM_TYPE_BOSSKEY;
}

bool item_is_map(item_e item)
{
    return item_table[item].type == ITEM_TYPE_MAP;
}

bool item_is_compass(item_e item)
{
    return item_table[item].type == ITEM_TYPE_COMPASS;
}

bool item_is_dungeonitem(item_e item)
{
    return item_table[item].type == ITEM_TYPE_SMALLKEY
        || item_table[item].type == ITEM_TYPE_BOSSKEY
        || item_table[item].type == ITEM_TYPE_MAP
        || item_table[item].type == ITEM_TYPE_COMPASS;
}

bool item_is_majoritem(item_e item)
{
    item_info_t i = item_table[item];
    if (i.type == ITEM_TYPE_TOKEN)
        return options.bridge == OPTION_TOKENS;

    if (i.type == ITEM_TYPE_EVENT
        || i.type == ITEM_TYPE_SHOP
        || i.fill != ITEM_FILL_ADVANCEMENT)
        return false;

    if (!options.bombchus_in_logic && item_is_bombchu(item))
        return false;

    if (item_is_map(item) || item_is_compass(item))
        return false;

    if (options.shuffle_smallkeys == OPTION_DUNGEON
        && item_is_smallkey(item))
        return false;

    if (options.shuffle_bosskeys == OPTION_DUNGEON
        && item_is_bosskey(item))
        return false;

    return true;
}