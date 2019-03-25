#ifndef STATE_H
#define STATE_H

#include <stdint.h>
#include <stdbool.h>
#include "item.h"


typedef enum
{
    TRIAL_FOREST,
    TRIAL_FIRE,
    TRIAL_WATER,
    TRIAL_SHADOW,
    TRIAL_SPIRIT,
    TRIAL_LIGHT
} state_trials_e;

typedef enum
{
    AGE_EITHER = 0,
    AGE_ADULT = 1,
    AGE_CHILD = 2,
    AGE_BOTH = 3
} state_age_e;

typedef enum
{
    CAN_REACH_REGION,
    CAN_REACH_LOCATION
} can_reach_e;

typedef struct
{
    uint8_t prog_items[ITEM_E_ANCHOR];
} state_t;

typedef enum
{
    OPTION_OFF,
    OPTION_ON,

    OPTION_CHEST,

    OPTION_OPEN,
    OPTION_VANILLA,
    OPTION_STONES,
    OPTION_TOKENS,
    OPTION_DUNGEONS,
    OPTION_MEDALLIONS,

    OPTION_DUNGEON,

    OPTION_MASK,

    OPTION_QUADRUPLE,
    OPTION_OHKO,
} option_e;

typedef struct
{
    bool keysanity;
    bool open_forest;
    bool open_fountain;
    bool open_kakariko;
    bool open_door_of_time;

    option_e shuffle_smallkeys;
    option_e shuffle_bosskeys;
    bool shuffle_weird_egg;
    bool shuffle_song_items;
    option_e shuffle_scrubs;

    bool bombchus_in_logic;
    bool logic_man_on_roof;
    bool logic_windmill_poh;
    option_e logic_lens;
    item_e logic_earliest_adult_trade;
    item_e logic_latest_adult_trade;
    bool logic_deku_basement_gs;
    bool logic_dmt_bombable;
    bool logic_dc_jump;
    bool logic_dc_staircase;
    bool logic_child_deadhand;
    bool logic_zora_with_cucco;
    bool logic_zora_with_hovers;
    bool logic_forest_well_swim;
    bool logic_forest_vines;
    bool logic_fire_mq_bk_chest;
    bool logic_water_bk_chest;
    bool logic_morpha_with_scale;
    bool logic_adult_kokiri_gs;
    bool logic_crater_bean_poh_with_hovers;
    bool logic_fewer_tunic_requirements;
    bool logic_rusted_switches;
    bool logic_forest_mq_block_puzzle;
    bool logic_spirit_mq_frozen_eye;
    bool logic_gerudo_kitchen;
    bool logic_spirit_child_bombchu;
    bool logic_gtg_mq_with_hookshot;
    bool logic_botw_basement;
    bool unlocked_ganondorf;
    option_e hints;
    option_e damage_multiplier;
    option_e bridge;
    option_e gerudo_fortress;
    uint8_t skipped_trials[6];
    uint8_t big_poe_count;
} options_t;

options_t options;

bool can_reach(state_t *self, int location, can_reach_e reach_type);
bool can_child_attack(state_t *self);
bool has_nuts(state_t *self);
bool can_stun_deku(state_t *self);
bool has_blue_fire(state_t *self);
bool has_ocarina(state_t *self);
bool can_play(state_t *self, item_e song);
bool can_use(state_t *self, item_e item);
bool can_buy_bombchus(state_t *self);
bool has_bombchus_item(state_t *self);
bool can_blast_or_smash(state_t *self);
bool can_see_with_lens(state_t *self);
bool has_projectile(state_t *self, state_age_e age);
bool has_GoronTunic(state_t *self);
bool has_ZoraTunic(state_t *self);
bool can_leave_forest(state_t *self);
bool can_finish_adult_trades(state_t *self);
bool has_bottle(state_t *self);
uint8_t bottle_count(state_t *self);
uint8_t heart_count(state_t *self);
uint8_t has_hearts(state_t *self, uint8_t count);
bool has_fire_source(state_t *self);
bool nighttime(state_t *self);
bool had_night_start(state_t *self);
bool can_finish_GerudoFortress(state_t *self);
bool guarantee_hint(state_t *self);


/* Functions we want to inline aggressively */

inline bool has(state_t *self, item_e item)
{
    return self->prog_items[item] >= 1;
}

inline bool has_c(state_t *self, item_e item, int count)
{
    return self->prog_items[item] >= count;
}

inline uint8_t item_count(state_t *self, item_e item)
{
    return self->prog_items[item];
}

inline bool is_adult(state_t *self)
{
    return has(self, MASTER_SWORD);
}

inline bool has_bow(state_t *self)
{
    return has(self, BOW);
}

inline bool has_slingshot(state_t *self)
{
    return has(self, SLINGSHOT);
}

inline bool has_bombs(state_t *self)
{
    return has(self, BOMB_BAG);
}

inline bool has_sticks(state_t *self)
{
    return has(self, BUY_DEKU_STICK_1)
        || has(self, DEKU_STICK_DROP);
}

inline bool has_bombchus(state_t *self)
{
    return has(self, BOMBCHUS); //fix
}

inline bool can_dive(state_t *self)
{
    return has(self, PROGRESSIVE_SCALE);
}

inline bool has_explosives(state_t *self)
{
    return has_bombs(self) || has_bombchus(self);
}

inline void collect(state_t *self, item_e item)
{
    if (item < ITEM_E_ANCHOR)
    {
        self->prog_items[item]++;
        //clear_cached_unreachable()
    }
}

inline void remove(state_t *self, item_e item)
{
    if (self->prog_items[item] > 0)
        self->prog_items[item]--;
}

#endif // !STATE_H