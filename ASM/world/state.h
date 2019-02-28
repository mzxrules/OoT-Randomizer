#include <stdint.h>
#include <stdbool.h>
#ifndef STATE_H
#define STATE_H

typedef enum 
{
    MASTER_SWORD,
    BOOMERANG,
    KOKIRI_SWORD,
    DINS_FIRE,
    MAGIC_METER,
    BUY_DEKU_SHIELD,
    BUY_DEKU_NUT_5,
    BUY_DEKU_NUT_10,
    DEKU_NUT_DROP,
    BUY_DEKU_STICK_1,
    DEKU_STICK_DROP,
    BOW,
    SLINGSHOT,
    BOMB_BAG,
    BUY_BLUE_FIRE,
    OCARINA,
    FAIRY_OCARINA,
    OCARINA_OF_TIME,
    FARORES_WIND,
    NAYRUS_LOVE,
    LENS_OF_TRUTH,
    HAMMER,
    MIRROR_SHIELD,
    IRON_BOOTS,
    HOVER_BOOTS,
    MAGIC_BEAN,
    PROGRESSIVE_HOOKSHOT,
    PROGRESSIVE_STRENGTH_UPGRADE,
    BUY_BOMBCHU_5,
    BUY_BOMBCHU_10,
    BUY_BOMBCHU_20,
    BOMBCHUS,
    PROGRESSIVE_WALLET,
    PROGRESSIVE_SCALE,
    GORON_TUNIC,
    BUY_GORON_TUNIC,
    ZORA_TUNIC,
    BUY_ZORA_TUNIC,
    BUY_BOTTLE_BUG,
    EPONA,
    CLAIM_CHECK,
    EYEDROPS,
    EYEBALL_FROG,
    PRESCRIPTION,
    BROKEN_SWORD,
    POACHERS_SAW,
    ODD_MUSHROOM,
    COJIRO,
    POCKET_CUCCO,
    POCKET_EGG,
    HEART_CONTAINER,
    PIECE_OF_HEART,
    FIRE_ARROWS,
    ICE_ARROWS,
    LIGHT_ARROWS,
    ZELDAS_LETTER,

    WEIRD_EGG,
    GERUDO_MEMBERSHIP_CARD,
    CARPENTER_RESCUE,

    KOKIRI_EMERALD,
    GORON_RUBY,
    ZORA_SAPPHIRE,
    FOREST_MEDALLION,
    FIRE_MEDALLION,
    WATER_MEDALLION,
    SHADOW_MEDALLION,
    SPIRIT_MEDALLION,
    LIGHT_MEDALLION,

    GOLD_SKULLTULA_TOKEN,
    STONE_OF_AGONY,

    ZELDAS_LULLABY,
    SARIAS_SONG,
    SUNS_SONG,
    EPONAS_SONG,
    SONG_OF_STORMS,
    SONG_OF_TIME,
    MINUET_OF_FOREST, 
    BOLERO_OF_FIRE,
    SERENADE_OF_WATER,
    NOCTURNE_OF_SHADOW,
    REQUIEM_OF_SPIRIT,
    PRELUDE_OF_LIGHT,

    SMALL_KEY_FOREST_TEMPLE,
    BOSS_KEY_FOREST_TEMPLE,
    SMALL_KEY_FIRE_TEMPLE,
    BOSS_KEY_FIRE_TEMPLE,
    SMALL_KEY_WATER_TEMPLE,
    BOSS_KEY_WATER_TEMPLE,
    SMALL_KEY_SHADOW_TEMPLE, 
    BOSS_KEY_SHADOW_TEMPLE,
    SMALL_KEY_SPIRIT_TEMPLE,
    BOSS_KEY_SPIRIT_TEMPLE,
    SMALL_KEY_BOTTOM_OF_THE_WELL,
    SMALL_KEY_GERUDO_FORTRESS,
    SMALL_KEY_GERUDO_TRAINING_GROUNDS,
    SMALL_KEY_GANONS_CASTLE,
    BOSS_KEY_GANONS_CASTLE,

    FOREST_TRIAL_CLEAR,
    FIRE_TRIAL_CLEAR,
    WATER_TRIAL_CLEAR,
    SHADOW_TRIAL_CLEAR,
    SPIRIT_TRIAL_CLEAR,
    LIGHT_TRIAL_CLEAR,

    //Elements past this point aren't collectible
    ANCHOR,

    //Bottles need to be tracked special as well?
    BOTTLE_WITH_LETTER,
    BOTTLE_WITH_BIG_POE,

    //Items tracked by other means, or are special
    HOOKSHOT,
    LONGSHOT,
    SILVER_GAUNTLETS,
    GOLDEN_GAUNTLETS,
    SCARECROW,
    DISTANT_SCARECROW,
    GANON

} state_items_e;

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

typedef struct
{
    uint8_t prog_items[ANCHOR];
} state_t;

typedef struct
{
    bool keysanity;
    bool open_forest;
    bool open_fountain;
    bool open_kakariko;
    bool open_door_of_time;

    bool shuffle_weird_egg;
    char* shuffle_scrubs;

    bool bombchus_in_logic;
    bool logic_man_on_roof;
    bool logic_windmill_poh;
    bool logic_lens;
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
    char* hints;
    char* damage_multiplier;
    char* bridge;
    char* gerudo_fortress;
    uint8_t skipped_trials[6];
    uint8_t big_poe_count;
} options_t;

extern options_t option;

bool can_reach(state_t *self, void *location);
bool can_child_attack(state_t *self);
bool has_nuts(state_t *self);
bool can_stun_deku(state_t *self);
bool has_blue_fire(state_t *self);
bool has_ocarina(state_t *self);
bool can_play(state_t *self, state_items_e song);
bool can_use(state_t *self, state_items_e item);
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

inline bool has(state_t *self, state_items_e item)
{
    return self->prog_items[item] >= 1;
}

inline bool has_c(state_t *self, state_items_e item, int count)
{
    return self->prog_items[item] >= count;
}

inline uint8_t item_count(state_t *self, state_items_e item)
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
    return true; //fix
}

inline void collect(state_t *self, state_items_e item)
{
    if (item < ANCHOR)
    {
        self->prog_items[item]++;
        //clear_cached_unreachable()
    }
}

inline void remove(state_t *self, state_items_e item)
{
    if (self->prog_items[item] > 0)
        self->prog_items[item]--;
}

#endif // !STATE_H
