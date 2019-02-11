#ifndef GFX_H
#define GFX_H

#include <n64.h>
#include "z2.h"

extern Gfx initial_display_list[]; 

typedef struct {
    uint8_t *buf;
    uint16_t tile_w;
    uint16_t tile_h;
    uint16_t tile_count;
    uint8_t im_fmt;
    uint8_t im_siz;
    uint8_t bytes_per_texel;
} sprite_t;

//sprite_t stones_sprite;
//sprite_t medals_sprite;
//sprite_t items_sprite;
//sprite_t quest_items_sprite;
//sprite_t font_sprite;
sprite_t dpad_sprite;
sprite_t dpad_item_sprites;

extern uint8_t dpad_mask_icons[3][0x1000];

//void disp_buf_init(z64_disp_buf_t *db, Gfx *buf, int size);
void gfx_init();

void sprite_load(z64_disp_buf_t *db, sprite_t *sprite,
        int start_tile, int tile_count);
void sprite_draw(z64_disp_buf_t *db, sprite_t *sprite, int tile_index,
        int left, int top, int width, int height);

extern void load_icon_item_texture(int32_t* vrom, int32_t index, void* texture, int32_t size);
asm(".equ load_icon_item_texture, 0x80178E3C");

#endif
