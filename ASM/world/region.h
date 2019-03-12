#ifndef REGION_H
#define REGION_H

#include <stdint.h>
#include <stdbool.h>
#include "state.h"
#include "location.h"
#include "regionlist.h"

typedef int exit_e;
typedef int region_group_e;
typedef bool (*rule_f)(state_t*);

typedef struct {
    location_e          location;
    rule_f              rule;
    item_e              item;
    bool                active;
} location_rule_t;

typedef struct {
    region_e            location;
    rule_f              rule;
} exit_rule_t;

typedef struct
{
    region_e            region_name;
    bool                mq;
    region_group_e      group;
    location_e         *locations;
    int32_t             loc_count;
    exit_rule_t        *exits;
    int32_t             exit_count;


} world_region_t;

#endif // !REGION_H