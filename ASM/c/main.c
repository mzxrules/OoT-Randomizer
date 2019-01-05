#include "gfx.h"
#include "dpad.h"
#include "z2.h"

void c_init() {
    gfx_init();
    dpad_init();
}

extern void game_update_start(z2_game_t* game);

void game_state_update_custom(z2_game_t* game)
{
    game_update_start(game);
}