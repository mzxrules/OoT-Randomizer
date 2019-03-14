#ifndef LOCATION_H
#define LOCATION_H

#include <stdint.h>
#include <stdbool.h> 
#include "locationlist.h"


typedef struct
{
    location_e k;
    char* name;
    location_type_e type;
    location_hint_e hint;
    uint8_t scene;
    uint8_t var; //default

} location_t;

#endif