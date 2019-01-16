#include "gfx.h"
#include "dpad.h"

static _Bool display_active = 1;
static int16_t alpha_level = 0;

//unknown 00 is a pointer to some vector transformation when the sound is tied to an actor. actor + 0x3E, when not tied to an actor (map), always 80104394
//unknown 01 is always 4 in my testing
//unknown 02 is a pointer to some kind of audio configuration Always 801043A0 in my testing
//unknown 03 is always a3 in my testing
//unknown 04 is always a3 + 0x08 in my testing (801043A8)
//typedef void(*playsfx_t)(uint16_t sfx, z64_xyzf_t *unk_00_, int8_t unk_01_ , float *unk_02_, float *unk_03_, float *unk_04_);
//typedef void(*usebutton_t)(z64_game_t *game, z64_link_t *link, uint8_t item, uint8_t button);

//#define z64_playsfx   ((playsfx_t)      0x800C806C)
//#define z64_usebutton ((usebutton_t)    0x8038C9A0)


uint8_t handle_dpad(z2_game_t* game, z2_link_t* link, uint8_t buttonIndex)
{
    alpha_level += 0x80;
    if (buttonIndex < 4)
        return get_item_button_press(game, link, buttonIndex);
    if (extern_mask_usability)
    {
        alpha_level -= 0x80;
        return 0xFF;
    }

    uint16_t pad_pressed = game->common.input[0].pad_pressed;
    if (pad_pressed & DPAD_L && z2_file.masks[5] == 0x32)
        return 0x32;
    else if (pad_pressed & DPAD_D && z2_file.masks[11] == 0x33)
        return 0x33;
    else if (pad_pressed & DPAD_R && z2_file.masks[17] == 0x34)
        return 0x34;
    return 0xFF;
}

//allows tweaking scale and position with a memory viewer
static uint32_t spr_sc = 16;
static uint32_t spr_xy[3][2] = 
{
    {260, 63},
    {270, 77},
    {285, 64}
};

void draw_dpad() {
    z64_disp_buf_t *db = &(z2_game.common.gfx->overlay);
    if (extern_mask_usability)
        alpha_level -= 0x4F;
    if (alpha_level < 0)
        alpha_level = 0;
    if (alpha_level > 0xFF)
        alpha_level = 0xFF;
    if (display_active) {
        gSPDisplayList(db->p++, &initial_display_list);
        gDPPipeSync(db->p++);
        gDPSetCombineMode(db->p++, G_CC_MODULATEIA_PRIM, G_CC_MODULATEIA_PRIM);
        uint16_t alpha = alpha_level;
        gDPSetPrimColor(db->p++, 0, 0, 0xFF, 0xFF, 0xFF, alpha);

        sprite_load(db, &dpad_sprite, 0, 1);
        sprite_draw(db, &dpad_sprite, 0, 271, 64, 16, 16);
        
        if (z2_file.masks[5] == 0x32)
        {
            sprite_load(db, &dpad_item_sprites, 0, 1);
            sprite_draw(db, &dpad_item_sprites, 0, spr_xy[0][0], spr_xy[0][1], spr_sc, spr_sc);
        }
        
        if (z2_file.masks[11] == 0x33)
        {
            sprite_load(db, &dpad_item_sprites, 1, 1);
            sprite_draw(db, &dpad_item_sprites, 0, spr_xy[1][0], spr_xy[1][1], spr_sc, spr_sc);
        }

        if (z2_file.masks[17] == 0x34)
        {
            sprite_load(db, &dpad_item_sprites, 2, 1);
            sprite_draw(db, &dpad_item_sprites, 0, spr_xy[2][0], spr_xy[2][1], spr_sc, spr_sc);
        }
        gDPPipeSync(db->p++);
    }
}