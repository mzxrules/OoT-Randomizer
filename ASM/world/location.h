#include <stdint.h>
#include <stdbool.h> 
#include "locationlist.h"

#ifndef LOCATION_H
#define LOCATION_H


typedef struct
{
    location_e k;
    char* name;
    bool mq;
    location_type_e type;
    location_hint_e hint;
    uint8_t scene;
    uint8_t var; //default
    //uint32_t var2;
    //uint32_t var3;

} location_t;

#endif