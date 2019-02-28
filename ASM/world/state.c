#include "state.h"
#include "util.h"
#include <stdint.h>
#include <stdbool.h>


bool can_reach(state_t *self, void *location)
{
    return true;
}

bool can_child_attack(state_t *self)
{
    return
        has(self, SLINGSHOT)
        || has(self, BOOMERANG)
        || has_sticks(self)
        || has_explosives(self)
        || has(self, KOKIRI_SWORD)
        || (has(self, DINS_FIRE) && has(self, MAGIC_METER));
}

bool has_nuts(state_t *self)
{
    return
        has(self, BUY_DEKU_NUT_5)
        || has(self, BUY_DEKU_NUT_10)
        || has(self, DEKU_NUT_DROP);
}

bool can_stun_deku(state_t *self)
{
    return
        is_adult(self)
        || can_child_attack(self)
        || has_nuts(self)
        || has(self, BUY_DEKU_SHIELD);
}

bool has_blue_fire(state_t *self)
{
    return true; //fix
}

bool has_ocarina(state_t *self)
{
    return
        has(self, OCARINA)
        || has(self, FAIRY_OCARINA)
        || has(self, OCARINA_OF_TIME);
}

bool can_play(state_t *self, state_items_e song)
{
    return
        has_ocarina(self)
        && has(self, song);
}


state_items_e magic_items[] =
{ DINS_FIRE, FARORES_WIND, NAYRUS_LOVE, LENS_OF_TRUTH };
state_items_e adult_items[] =
{ BOW, HAMMER, IRON_BOOTS, HOVER_BOOTS, MAGIC_BEAN };
state_items_e magic_arrows[] =
{ FIRE_ARROWS, LIGHT_ARROWS };

bool can_use(state_t *self, state_items_e item)
{
    for (int i = 0; i < array_size(magic_items); i++)
    {
        if (magic_items[i] == item)
        {
            return has(self, item) && has(self, MAGIC_METER);
        }
    }

    for (int i = 0; i < array_size(adult_items); i++)
    {
        if (adult_items[i] == item)
        {
            return has(self, item) && is_adult(self);
        }
    }

    for (int i = 0; i < array_size(magic_arrows); i++)
    {
        if (magic_arrows[i] == item)
        {
            return has(self, item)
                && is_adult(self)
                && has(self, BOW)
                && has(self, MAGIC_METER);
        }
    }

    if (item == HOOKSHOT)
    {
        return has(self, PROGRESSIVE_HOOKSHOT);
    }
    else if (item == LONGSHOT)
    {
        return has_c(self, PROGRESSIVE_HOOKSHOT, 2);
    }
    else if (item == SILVER_GAUNTLETS)
    {
        return has_c(self, PROGRESSIVE_STRENGTH_UPGRADE, 2);
    }
    else if (item == GOLDEN_GAUNTLETS)
    {
        return has_c(self, PROGRESSIVE_STRENGTH_UPGRADE, 3);
    }
    else if (item == SCARECROW)
    {
        return has(self, PROGRESSIVE_HOOKSHOT)
            && is_adult(self)
            && has_ocarina(self);
    }
    else if (item == DISTANT_SCARECROW)
    {
        return has_c(self, PROGRESSIVE_HOOKSHOT, 2)
            && is_adult(self)
            && has_ocarina(self);
    }
    return has(self, item);
}

bool can_buy_bombchus(state_t *self)
{
    return
        has(self, BUY_BOMBCHU_5)
        || has(self, BUY_BOMBCHU_10)
        || has(self, BUY_BOMBCHU_20);
    //fixme: can reach
}

bool has_bombchus_item(state_t *self)
{
    return true; //fixme
}

bool can_blast_or_smash(state_t *self)
{
    return
        has_explosives(self)
        || (is_adult(self) && has(self, HAMMER));
}

bool can_see_with_lens(state_t *self)
{
    return has(self, MAGIC_METER) && has(self, LENS_OF_TRUTH);
}

bool has_projectile(state_t *self, state_age_e age)
//default age is either
{
    bool result = has_explosives(self);

    bool child_r =
        //(age & AGE_CHILD) &&
        (has(self, SLINGSHOT) || has(self, BOOMERANG));
    bool adult_r =
        (has(self, BOW) || has(self, PROGRESSIVE_HOOKSHOT));

    if (age == AGE_BOTH)
        return result | (child_r && adult_r);
    
    return result
        || ((age & AGE_CHILD) && child_r)
        || ((age & AGE_ADULT) && adult_r);
}

bool has_GoronTunic(state_t *self)
{
    return has(self, GORON_TUNIC)
        || has(self, BUY_GORON_TUNIC);
}

bool has_ZoraTunic(state_t *self)
{
    return has(self, ZORA_TUNIC)
        || has(self, BUY_ZORA_TUNIC);
}

bool can_leave_forest(state_t *self)
{
    return true; //fixme
}

bool can_finish_adult_trades(state_t *self)
{
    if (has(self, CLAIM_CHECK))
    {
        return true;
    }

    bool zora_reach = //fixme logic_zora_with_hovers
        can_play(self, ZELDAS_LULLABY)
        || has(self, HOVER_BOOTS); 

    bool zora_thawed = zora_reach && has_blue_fire(self);
    bool carpenter_access =
        has(self, EPONA)
        || has_c(self, PROGRESSIVE_HOOKSHOT, 2);

    bool first_half =
        carpenter_access
        && (has(self, POACHERS_SAW)
            || has(self, ODD_MUSHROOM)
            || has(self, COJIRO)
            || has(self, POCKET_CUCCO)
            || has(self, POCKET_EGG));

    bool second_half = (has(self, EYEDROPS)
        || has(self, EYEBALL_FROG)
        || has(self, PRESCRIPTION)
        || has(self, BROKEN_SWORD));


    return
        (has(self, PROGRESSIVE_STRENGTH_UPGRADE)
            || can_blast_or_smash(self)
            || has(self, BOW))
        && zora_thawed
        && (first_half || second_half);
}

bool has_bottle(state_t *self)
{
    return true; //fixme
}

uint8_t bottle_count(state_t *self)
{
    return 4; //fixme
}

uint8_t heart_count(state_t *self)
{
    return item_count(self, HEART_CONTAINER)
        + (item_count(self, PIECE_OF_HEART) / 4)
        + 3;
}

uint8_t has_hearts(state_t *self, uint8_t count)
{
    return heart_count(self) >= count;
}

bool has_fire_source(state_t *self)
{
    return can_use(self, DINS_FIRE) || can_use(self, FIRE_ARROWS);
}

bool nighttime(state_t *self)
{
    //fixme logic_no_night_tokens_without_suns_song
    return can_play(self, SUNS_SONG);
}

bool had_night_start(state_t *self)
{
    return false;
}

bool can_finish_GerudoFortress(state_t *self)
{
    //fixme
    //world.gerudo_fortress == normal
    //world.gerudo_fortress == 'fast'
    return is_adult(self); 
}

bool guarantee_hint(state_t *self) 
{
    return true; //fixme
}