#include "region.h"
#include "state.h"
#include "ItemList.h"

bool TRUE_F(state_t *state)
{
    return true;
}

/*
world_region_t region = 
{
    .region_name = 4,
    .group = 0,
    .locations = (location_rule_t[]){
        { 
            .location = 5,
            .active = false,
            .mq = true,
            .rule = TRUE_F,
            .item = ITEM_E_NONE,
        }
    },
    .exits = (exit_rule_t[]) {
        {
            .location = 3,
            .rule = TRUE_F,
        }
    }
};*/