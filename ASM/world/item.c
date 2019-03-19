#include "itemlist.h"
#include <stdbool.h>



bool is_progressive_item(item_e item)
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

bool is_bottle(item_e item)
{
    //fixme
    return item == BOTTLE;
}