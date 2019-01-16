#ifndef DPAD_H
#define DPAD_H

#include "z2.h"

#define BLOCK_DPAD (0x00000001 | \
	0x00000002 | \
    0x00000080 | \
    0x00000400 | \
    0x10000000 | \
    0x20000000)


//z64_link.state_flags_1

#define CAN_USE_DPAD       (((0 & BLOCK_DPAD) == 0) && \
                           (z2_file.file_index!=0xFF))
//((z64_event_state_1 & 0x20) == 0) && 
#define DPAD_L 0x0200
#define DPAD_R 0x0100
#define DPAD_D 0x0400

uint8_t handle_dpad(z2_game_t* game, z2_link_t* link, uint8_t buttonIndex);
void draw_dpad();

//8012364C //Test if button item is being used
extern uint8_t get_item_button_press(z2_game_t* game, z2_link_t* link, uint8_t buttonIndex);
asm(".equ get_item_button_press, 0x8012364C");

extern uint8_t extern_mask_usability;

#endif