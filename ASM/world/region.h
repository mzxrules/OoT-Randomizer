#ifndef REGION_H
#define REGION_H

#include <stdint.h>
#include <stdbool.h>
#include "rules.h"
#include "regionlist.h"
#include "locationlist.h"


typedef int region_group_e;


typedef struct
{
    location_e          k;
    char               *name;
    location_type_e     type;
    location_hint_e     hint;
    uint8_t             scene;
    uint8_t             var; //default

    region_e            region;
    rule_f              rule;
    item_e              item;
    bool                active;

} location_t;

typedef struct
{
    location_e k;
    uint8_t scene;
    rule_f va_rule;
    rule_f mq_rule;

} location_conflict_t;

typedef struct {
    location_e          location;
} location_rule_t;

typedef struct {
    region_e            start;
    region_e            dest;
    rule_f              rule;
} exit_rule_t;

typedef struct
{
    region_e            k;
    char               *name;
    bool                mq;
    //region_group_e      group;
    location_e         *locations;
    int32_t             loc_count;
    exit_rule_t        *exits;
    int32_t             exit_count;

} world_region_t;

#endif // !REGION_H