#include "chests.h"
#include "n64.h"
#include "gfx.h"

#define BROWN_FRONT_TEXTURE 0x06001798
#define BROWN_BASE_TEXTURE 0x06002798
#define GOLD_FRONT_TEXTURE 0x06002F98
#define GOLD_BASE_TEXTURE 0x06003798

#define GUILDED_CHEST 0
#define BROWN_CHEST 1
#define GOLD_CHEST 2

#define CHEST_BASE 1
#define CHEST_LID 3

uint32_t CHEST_SIZE_MATCH_CONTENTS = 0;

extern void* CHEST_FRONT_TEXTURE;
extern void* CHEST_BASE_TEXTURE;

extern Mtx_t* write_matrix_stack_top(z64_gfx_t* gfx);
asm(".equ write_matrix_stack_top, 0x800AB900");


int get_chest_type(z64_actor_t* actor)
{
    uint8_t scene = z64_game.scene_index;
    uint8_t item_id = (actor->variable & 0x0FE0) >> 5;
    override_t override = lookup_override(actor, scene, item_id);

    if (!CHEST_SIZE_MATCH_CONTENTS || override.value.item_id == 0)
    {
        // If no override, return either Gold or Brown
        uint8_t type = ((uint8_t*)actor)[0x01E9];
        if (type == 2)
            return GOLD_CHEST;
        return BROWN_CHEST;
    }

    item_row_t *item_row = get_item_row(override.value.item_id);
    return item_row->chest_type;
}

void draw_chest(z64_game_t* game, int part, void* unk, void* unk2,
    z64_actor_t *actor, Gfx **opa_ptr)
{
    if (part != CHEST_BASE && part != CHEST_LID)
        return;

    z64_gfx_t *gfx = game->common.gfx;
    int chest_type = get_chest_type(actor);

    //write matrix
    Mtx_t *mtx = write_matrix_stack_top(gfx);
    gSPMatrix((*opa_ptr)++, mtx, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);

    int dlist;

    if (part == CHEST_BASE)
    {
        if (chest_type == GOLD_CHEST)
            dlist = 0x06000AE8;
        else
            dlist = 0x060006F0;

    }
    else //(part == CHEST_LID)
    {
        if (chest_type == GOLD_CHEST)
            dlist = 0x06001678;
        else
            dlist = 0x060010C0;
    }

    if (chest_type != GOLD_CHEST)
    {
        //set texture type
        void* frontTexture;
        void* baseTexture;

        if (chest_type == GUILDED_CHEST)
        {
            frontTexture = &CHEST_FRONT_TEXTURE;
            baseTexture = &CHEST_BASE_TEXTURE;
        }
        else
        {
            frontTexture = (void*)BROWN_FRONT_TEXTURE;
            baseTexture = (void*)BROWN_BASE_TEXTURE;
        }

        //the brown chest's base and lid dlist has been modified to jump to
        //segment 09 in order to dynamically set the chest front and base textures
        gfx->poly_opa.d -= 4;
        gDPSetTextureImage(gfx->poly_opa.d, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, frontTexture);
        gSPEndDisplayList(gfx->poly_opa.d + 1);
        gDPSetTextureImage(gfx->poly_opa.d + 2, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, baseTexture);
        gSPEndDisplayList(gfx->poly_opa.d + 3);

        gMoveWd((*opa_ptr)++, G_MW_SEGMENT, 9 * sizeof(int), gfx->poly_opa.d);
    }
    gSPDisplayList((*opa_ptr)++, dlist);
}