#ifndef DPAD_H
#define DPAD_H

#include "z2.h"

#define BLOCK_DPAD (0x00000001 | \
	0x00000002 | \
    0x00000080 | \
    0x00000400 | \
    0x10000000 | \
    0x20000000)

//#define DISPLAY_DPAD       (z64_file.iron_boots || z64_file.hover_boots || z64_file.items[0x07] == 0x07 || z64_file.items[0x08] == 0x08)
#define DISPLAY_DPAD 1

//z64_link.state_flags_1

#define CAN_USE_DPAD       (((0 & BLOCK_DPAD) == 0) && \
                           (z2_file.file_index!=0xFF) && \
                           DISPLAY_DPAD)
//((z64_event_state_1 & 0x20) == 0) && 
#define DPAD_L 0x0200
#define DPAD_R 0x0100
#define DPAD_D 0x0400

void handle_dpad();
void draw_dpad();
void dpad_init();

#endif