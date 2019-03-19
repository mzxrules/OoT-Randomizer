/* Generated C code */

#include <stdbool.h>
#include "item.h"

item_info_t item_table[] = {
    [BOMBS_5] = {
        .k = BOMBS_5,
        .name = "Bombs (5)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x01
    },
    [DEKU_NUTS_5] = {
        .k = DEKU_NUTS_5,
        .name = "Deku Nuts (5)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x02
    },
    [BOMBCHUS_10] = {
        .k = BOMBCHUS_10,
        .name = "Bombchus (10)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x03
    },
    [BOOMERANG] = {
        .k = BOOMERANG,
        .name = "Boomerang",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x06
    },
    [DEKU_STICK_1] = {
        .k = DEKU_STICK_1,
        .name = "Deku Stick (1)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x07
    },
    [LENS_OF_TRUTH] = {
        .k = LENS_OF_TRUTH,
        .name = "Lens of Truth",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x0A
    },
    [HAMMER] = {
        .k = HAMMER,
        .name = "Hammer",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x0D
    },
    [COJIRO] = {
        .k = COJIRO,
        .name = "Cojiro",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x0E
    },
    [BOTTLE] = {
        .k = BOTTLE,
        .name = "Bottle",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x0F
    },
    [BOTTLE_WITH_MILK] = {
        .k = BOTTLE_WITH_MILK,
        .name = "Bottle with Milk",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x14
    },
    [BOTTLE_WITH_LETTER] = {
        .k = BOTTLE_WITH_LETTER,
        .name = "Bottle with Letter",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x15
    },
    [MAGIC_BEAN] = {
        .k = MAGIC_BEAN,
        .name = "Magic Bean",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x16
    },
    [SKULL_MASK] = {
        .k = SKULL_MASK,
        .name = "Skull Mask",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x17
    },
    [SPOOKY_MASK] = {
        .k = SPOOKY_MASK,
        .name = "Spooky Mask",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x18
    },
    [KEATON_MASK] = {
        .k = KEATON_MASK,
        .name = "Keaton Mask",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x1A
    },
    [BUNNY_HOOD] = {
        .k = BUNNY_HOOD,
        .name = "Bunny Hood",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x1B
    },
    [MASK_OF_TRUTH] = {
        .k = MASK_OF_TRUTH,
        .name = "Mask of Truth",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x1C
    },
    [POCKET_EGG] = {
        .k = POCKET_EGG,
        .name = "Pocket Egg",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x1D
    },
    [POCKET_CUCCO] = {
        .k = POCKET_CUCCO,
        .name = "Pocket Cucco",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x1E
    },
    [ODD_MUSHROOM] = {
        .k = ODD_MUSHROOM,
        .name = "Odd Mushroom",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x1F
    },
    [ODD_POTION] = {
        .k = ODD_POTION,
        .name = "Odd Potion",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x20
    },
    [POACHERS_SAW] = {
        .k = POACHERS_SAW,
        .name = "Poachers Saw",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x21
    },
    [BROKEN_SWORD] = {
        .k = BROKEN_SWORD,
        .name = "Broken Sword",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x22
    },
    [PRESCRIPTION] = {
        .k = PRESCRIPTION,
        .name = "Prescription",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x23
    },
    [EYEBALL_FROG] = {
        .k = EYEBALL_FROG,
        .name = "Eyeball Frog",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x24
    },
    [EYEDROPS] = {
        .k = EYEDROPS,
        .name = "Eyedrops",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x25
    },
    [CLAIM_CHECK] = {
        .k = CLAIM_CHECK,
        .name = "Claim Check",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x26
    },
    [KOKIRI_SWORD] = {
        .k = KOKIRI_SWORD,
        .name = "Kokiri Sword",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x27
    },
    [DEKU_SHIELD] = {
        .k = DEKU_SHIELD,
        .name = "Deku Shield",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x29
    },
    [HYLIAN_SHIELD] = {
        .k = HYLIAN_SHIELD,
        .name = "Hylian Shield",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x2A
    },
    [MIRROR_SHIELD] = {
        .k = MIRROR_SHIELD,
        .name = "Mirror Shield",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x2B
    },
    [GORON_TUNIC] = {
        .k = GORON_TUNIC,
        .name = "Goron Tunic",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x2C
    },
    [ZORA_TUNIC] = {
        .k = ZORA_TUNIC,
        .name = "Zora Tunic",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x2D
    },
    [IRON_BOOTS] = {
        .k = IRON_BOOTS,
        .name = "Iron Boots",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x2E
    },
    [HOVER_BOOTS] = {
        .k = HOVER_BOOTS,
        .name = "Hover Boots",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x2F
    },
    [STONE_OF_AGONY] = {
        .k = STONE_OF_AGONY,
        .name = "Stone of Agony",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x39
    },
    [GERUDO_MEMBERSHIP_CARD] = {
        .k = GERUDO_MEMBERSHIP_CARD,
        .name = "Gerudo Membership Card",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x3A
    },
    [HEART_CONTAINER] = {
        .k = HEART_CONTAINER,
        .name = "Heart Container",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x3D
    },
    [PIECE_OF_HEART] = {
        .k = PIECE_OF_HEART,
        .name = "Piece of Heart",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x3E
    },
    [BOSS_KEY] = {
        .k = BOSS_KEY,
        .name = "Boss Key",
        .type = ITEM_TYPE_BOSSKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x3F
    },
    [COMPASS] = {
        .k = COMPASS,
        .name = "Compass",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x40
    },
    [MAP] = {
        .k = MAP,
        .name = "Map",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x41
    },
    [SMALL_KEY] = {
        .k = SMALL_KEY,
        .name = "Small Key",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x42
    },
    [WEIRD_EGG] = {
        .k = WEIRD_EGG,
        .name = "Weird Egg",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x47
    },
    [RECOVERY_HEART] = {
        .k = RECOVERY_HEART,
        .name = "Recovery Heart",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x48
    },
    [ARROWS_5] = {
        .k = ARROWS_5,
        .name = "Arrows (5)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x49
    },
    [ARROWS_10] = {
        .k = ARROWS_10,
        .name = "Arrows (10)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x4A
    },
    [ARROWS_30] = {
        .k = ARROWS_30,
        .name = "Arrows (30)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x4B
    },
    [RUPEE_1] = {
        .k = RUPEE_1,
        .name = "Rupee (1)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x4C
    },
    [RUPEES_5] = {
        .k = RUPEES_5,
        .name = "Rupees (5)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x4D
    },
    [RUPEES_20] = {
        .k = RUPEES_20,
        .name = "Rupees (20)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x4E
    },
    [HEART_CONTAINER_BOSS] = {
        .k = HEART_CONTAINER_BOSS,
        .name = "Heart Container (Boss)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x4F
    },
    [GORON_MASK] = {
        .k = GORON_MASK,
        .name = "Goron Mask",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x51
    },
    [ZORA_MASK] = {
        .k = ZORA_MASK,
        .name = "Zora Mask",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x52
    },
    [GERUDO_MASK] = {
        .k = GERUDO_MASK,
        .name = "Gerudo Mask",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x53
    },
    [RUPEES_50] = {
        .k = RUPEES_50,
        .name = "Rupees (50)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x55
    },
    [RUPEES_200] = {
        .k = RUPEES_200,
        .name = "Rupees (200)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x56
    },
    [BIGGORON_SWORD] = {
        .k = BIGGORON_SWORD,
        .name = "Biggoron Sword",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x57
    },
    [FIRE_ARROWS] = {
        .k = FIRE_ARROWS,
        .name = "Fire Arrows",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x58
    },
    [ICE_ARROWS] = {
        .k = ICE_ARROWS,
        .name = "Ice Arrows",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x59
    },
    [LIGHT_ARROWS] = {
        .k = LIGHT_ARROWS,
        .name = "Light Arrows",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x5A
    },
    [GOLD_SKULLTULA_TOKEN] = {
        .k = GOLD_SKULLTULA_TOKEN,
        .name = "Gold Skulltula Token",
        .type = ITEM_TYPE_TOKEN,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x5B
    },
    [DINS_FIRE] = {
        .k = DINS_FIRE,
        .name = "Dins Fire",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x5C
    },
    [NAYRUS_LOVE] = {
        .k = NAYRUS_LOVE,
        .name = "Nayrus Love",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x5E
    },
    [FARORES_WIND] = {
        .k = FARORES_WIND,
        .name = "Farores Wind",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x5D
    },
    [DEKU_NUTS_10] = {
        .k = DEKU_NUTS_10,
        .name = "Deku Nuts (10)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x64
    },
    [BOMBS_10] = {
        .k = BOMBS_10,
        .name = "Bombs (10)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x66
    },
    [BOMBS_20] = {
        .k = BOMBS_20,
        .name = "Bombs (20)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x67
    },
    [DEKU_SEEDS_30] = {
        .k = DEKU_SEEDS_30,
        .name = "Deku Seeds (30)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x69
    },
    [BOMBCHUS_5] = {
        .k = BOMBCHUS_5,
        .name = "Bombchus (5)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x6A
    },
    [BOMBCHUS_20] = {
        .k = BOMBCHUS_20,
        .name = "Bombchus (20)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x6B
    },
    [RUPEE_TREASURE_CHEST_GAME] = {
        .k = RUPEE_TREASURE_CHEST_GAME,
        .name = "Rupee (Treasure Chest Game)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x72
    },
    [PIECE_OF_HEART_TREASURE_CHEST_GAME] = {
        .k = PIECE_OF_HEART_TREASURE_CHEST_GAME,
        .name = "Piece of Heart (Treasure Chest Game)",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x76
    },
    [ICE_TRAP] = {
        .k = ICE_TRAP,
        .name = "Ice Trap",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x7C
    },
    [PROGRESSIVE_HOOKSHOT] = {
        .k = PROGRESSIVE_HOOKSHOT,
        .name = "Progressive Hookshot",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x80
    },
    [PROGRESSIVE_STRENGTH_UPGRADE] = {
        .k = PROGRESSIVE_STRENGTH_UPGRADE,
        .name = "Progressive Strength Upgrade",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x81
    },
    [BOMB_BAG] = {
        .k = BOMB_BAG,
        .name = "Bomb Bag",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x82
    },
    [BOW] = {
        .k = BOW,
        .name = "Bow",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x83
    },
    [SLINGSHOT] = {
        .k = SLINGSHOT,
        .name = "Slingshot",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x84
    },
    [PROGRESSIVE_WALLET] = {
        .k = PROGRESSIVE_WALLET,
        .name = "Progressive Wallet",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x85
    },
    [PROGRESSIVE_SCALE] = {
        .k = PROGRESSIVE_SCALE,
        .name = "Progressive Scale",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x86
    },
    [DEKU_NUT_CAPACITY] = {
        .k = DEKU_NUT_CAPACITY,
        .name = "Deku Nut Capacity",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x87
    },
    [DEKU_STICK_CAPACITY] = {
        .k = DEKU_STICK_CAPACITY,
        .name = "Deku Stick Capacity",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x88
    },
    [BOMBCHUS] = {
        .k = BOMBCHUS,
        .name = "Bombchus",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x89
    },
    [MAGIC_METER] = {
        .k = MAGIC_METER,
        .name = "Magic Meter",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x8A
    },
    [OCARINA] = {
        .k = OCARINA,
        .name = "Ocarina",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x8B
    },
    [BOTTLE_WITH_RED_POTION] = {
        .k = BOTTLE_WITH_RED_POTION,
        .name = "Bottle with Red Potion",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x8C
    },
    [BOTTLE_WITH_GREEN_POTION] = {
        .k = BOTTLE_WITH_GREEN_POTION,
        .name = "Bottle with Green Potion",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x8D
    },
    [BOTTLE_WITH_BLUE_POTION] = {
        .k = BOTTLE_WITH_BLUE_POTION,
        .name = "Bottle with Blue Potion",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x8E
    },
    [BOTTLE_WITH_FAIRY] = {
        .k = BOTTLE_WITH_FAIRY,
        .name = "Bottle with Fairy",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x8F
    },
    [BOTTLE_WITH_FISH] = {
        .k = BOTTLE_WITH_FISH,
        .name = "Bottle with Fish",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x90
    },
    [BOTTLE_WITH_BLUE_FIRE] = {
        .k = BOTTLE_WITH_BLUE_FIRE,
        .name = "Bottle with Blue Fire",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x91
    },
    [BOTTLE_WITH_BUGS] = {
        .k = BOTTLE_WITH_BUGS,
        .name = "Bottle with Bugs",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x92
    },
    [BOTTLE_WITH_BIG_POE] = {
        .k = BOTTLE_WITH_BIG_POE,
        .name = "Bottle with Big Poe",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x93
    },
    [BOTTLE_WITH_POE] = {
        .k = BOTTLE_WITH_POE,
        .name = "Bottle with Poe",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x94
    },
    [BOSS_KEY_FOREST_TEMPLE] = {
        .k = BOSS_KEY_FOREST_TEMPLE,
        .name = "Boss Key (Forest Temple)",
        .type = ITEM_TYPE_BOSSKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x95
    },
    [BOSS_KEY_FIRE_TEMPLE] = {
        .k = BOSS_KEY_FIRE_TEMPLE,
        .name = "Boss Key (Fire Temple)",
        .type = ITEM_TYPE_BOSSKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x96
    },
    [BOSS_KEY_WATER_TEMPLE] = {
        .k = BOSS_KEY_WATER_TEMPLE,
        .name = "Boss Key (Water Temple)",
        .type = ITEM_TYPE_BOSSKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x97
    },
    [BOSS_KEY_SPIRIT_TEMPLE] = {
        .k = BOSS_KEY_SPIRIT_TEMPLE,
        .name = "Boss Key (Spirit Temple)",
        .type = ITEM_TYPE_BOSSKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x98
    },
    [BOSS_KEY_SHADOW_TEMPLE] = {
        .k = BOSS_KEY_SHADOW_TEMPLE,
        .name = "Boss Key (Shadow Temple)",
        .type = ITEM_TYPE_BOSSKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x99
    },
    [BOSS_KEY_GANONS_CASTLE] = {
        .k = BOSS_KEY_GANONS_CASTLE,
        .name = "Boss Key (Ganons Castle)",
        .type = ITEM_TYPE_BOSSKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x9A
    },
    [COMPASS_DEKU_TREE] = {
        .k = COMPASS_DEKU_TREE,
        .name = "Compass (Deku Tree)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x9B
    },
    [COMPASS_DODONGOS_CAVERN] = {
        .k = COMPASS_DODONGOS_CAVERN,
        .name = "Compass (Dodongos Cavern)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x9C
    },
    [COMPASS_JABU_JABUS_BELLY] = {
        .k = COMPASS_JABU_JABUS_BELLY,
        .name = "Compass (Jabu Jabus Belly)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x9D
    },
    [COMPASS_FOREST_TEMPLE] = {
        .k = COMPASS_FOREST_TEMPLE,
        .name = "Compass (Forest Temple)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x9E
    },
    [COMPASS_FIRE_TEMPLE] = {
        .k = COMPASS_FIRE_TEMPLE,
        .name = "Compass (Fire Temple)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0x9F
    },
    [COMPASS_WATER_TEMPLE] = {
        .k = COMPASS_WATER_TEMPLE,
        .name = "Compass (Water Temple)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA0
    },
    [COMPASS_SPIRIT_TEMPLE] = {
        .k = COMPASS_SPIRIT_TEMPLE,
        .name = "Compass (Spirit Temple)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA1
    },
    [COMPASS_SHADOW_TEMPLE] = {
        .k = COMPASS_SHADOW_TEMPLE,
        .name = "Compass (Shadow Temple)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA2
    },
    [COMPASS_BOTTOM_OF_THE_WELL] = {
        .k = COMPASS_BOTTOM_OF_THE_WELL,
        .name = "Compass (Bottom of the Well)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA3
    },
    [COMPASS_ICE_CAVERN] = {
        .k = COMPASS_ICE_CAVERN,
        .name = "Compass (Ice Cavern)",
        .type = ITEM_TYPE_COMPASS,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA4
    },
    [MAP_DEKU_TREE] = {
        .k = MAP_DEKU_TREE,
        .name = "Map (Deku Tree)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA5
    },
    [MAP_DODONGOS_CAVERN] = {
        .k = MAP_DODONGOS_CAVERN,
        .name = "Map (Dodongos Cavern)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA6
    },
    [MAP_JABU_JABUS_BELLY] = {
        .k = MAP_JABU_JABUS_BELLY,
        .name = "Map (Jabu Jabus Belly)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA7
    },
    [MAP_FOREST_TEMPLE] = {
        .k = MAP_FOREST_TEMPLE,
        .name = "Map (Forest Temple)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA8
    },
    [MAP_FIRE_TEMPLE] = {
        .k = MAP_FIRE_TEMPLE,
        .name = "Map (Fire Temple)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xA9
    },
    [MAP_WATER_TEMPLE] = {
        .k = MAP_WATER_TEMPLE,
        .name = "Map (Water Temple)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xAA
    },
    [MAP_SPIRIT_TEMPLE] = {
        .k = MAP_SPIRIT_TEMPLE,
        .name = "Map (Spirit Temple)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xAB
    },
    [MAP_SHADOW_TEMPLE] = {
        .k = MAP_SHADOW_TEMPLE,
        .name = "Map (Shadow Temple)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xAC
    },
    [MAP_BOTTOM_OF_THE_WELL] = {
        .k = MAP_BOTTOM_OF_THE_WELL,
        .name = "Map (Bottom of the Well)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xAD
    },
    [MAP_ICE_CAVERN] = {
        .k = MAP_ICE_CAVERN,
        .name = "Map (Ice Cavern)",
        .type = ITEM_TYPE_MAP,
        .fill = ITEM_FILL_NORMAL,
        .gi = 0xAE
    },
    [SMALL_KEY_FOREST_TEMPLE] = {
        .k = SMALL_KEY_FOREST_TEMPLE,
        .name = "Small Key (Forest Temple)",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xAF
    },
    [SMALL_KEY_FIRE_TEMPLE] = {
        .k = SMALL_KEY_FIRE_TEMPLE,
        .name = "Small Key (Fire Temple)",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB0
    },
    [SMALL_KEY_WATER_TEMPLE] = {
        .k = SMALL_KEY_WATER_TEMPLE,
        .name = "Small Key (Water Temple)",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB1
    },
    [SMALL_KEY_SPIRIT_TEMPLE] = {
        .k = SMALL_KEY_SPIRIT_TEMPLE,
        .name = "Small Key (Spirit Temple)",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB2
    },
    [SMALL_KEY_SHADOW_TEMPLE] = {
        .k = SMALL_KEY_SHADOW_TEMPLE,
        .name = "Small Key (Shadow Temple)",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB3
    },
    [SMALL_KEY_BOTTOM_OF_THE_WELL] = {
        .k = SMALL_KEY_BOTTOM_OF_THE_WELL,
        .name = "Small Key (Bottom of the Well)",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB4
    },
    [SMALL_KEY_GERUDO_TRAINING_GROUNDS] = {
        .k = SMALL_KEY_GERUDO_TRAINING_GROUNDS,
        .name = "Small Key (Gerudo Training Grounds)",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB5
    },
    [SMALL_KEY_GERUDO_FORTRESS] = {
        .k = SMALL_KEY_GERUDO_FORTRESS,
        .name = "Small Key (Gerudo Fortress)",
        .type = ITEM_TYPE_FORTRESS_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB6
    },
    [SMALL_KEY_GANONS_CASTLE] = {
        .k = SMALL_KEY_GANONS_CASTLE,
        .name = "Small Key (Ganons Castle)",
        .type = ITEM_TYPE_SMALLKEY,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB7
    },
    [DOUBLE_DEFENSE] = {
        .k = DOUBLE_DEFENSE,
        .name = "Double Defense",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xB8
    },
    [ZELDAS_LETTER] = {
        .k = ZELDAS_LETTER,
        .name = "Zeldas Letter",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [MASTER_SWORD] = {
        .k = MASTER_SWORD,
        .name = "Master Sword",
        .type = ITEM_TYPE_ITEM,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [EPONA] = {
        .k = EPONA,
        .name = "Epona",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [DEKU_STICK_DROP] = {
        .k = DEKU_STICK_DROP,
        .name = "Deku Stick Drop",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [DEKU_NUT_DROP] = {
        .k = DEKU_NUT_DROP,
        .name = "Deku Nut Drop",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [CARPENTER_RESCUE] = {
        .k = CARPENTER_RESCUE,
        .name = "Carpenter Rescue",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [FOREST_TRIAL_CLEAR] = {
        .k = FOREST_TRIAL_CLEAR,
        .name = "Forest Trial Clear",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [FIRE_TRIAL_CLEAR] = {
        .k = FIRE_TRIAL_CLEAR,
        .name = "Fire Trial Clear",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [WATER_TRIAL_CLEAR] = {
        .k = WATER_TRIAL_CLEAR,
        .name = "Water Trial Clear",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [SHADOW_TRIAL_CLEAR] = {
        .k = SHADOW_TRIAL_CLEAR,
        .name = "Shadow Trial Clear",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [SPIRIT_TRIAL_CLEAR] = {
        .k = SPIRIT_TRIAL_CLEAR,
        .name = "Spirit Trial Clear",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [LIGHT_TRIAL_CLEAR] = {
        .k = LIGHT_TRIAL_CLEAR,
        .name = "Light Trial Clear",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [TRIFORCE] = {
        .k = TRIFORCE,
        .name = "Triforce",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [MINUET_OF_FOREST] = {
        .k = MINUET_OF_FOREST,
        .name = "Minuet of Forest",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xBB
    },
    [BOLERO_OF_FIRE] = {
        .k = BOLERO_OF_FIRE,
        .name = "Bolero of Fire",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xBC
    },
    [SERENADE_OF_WATER] = {
        .k = SERENADE_OF_WATER,
        .name = "Serenade of Water",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xBD
    },
    [REQUIEM_OF_SPIRIT] = {
        .k = REQUIEM_OF_SPIRIT,
        .name = "Requiem of Spirit",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xBE
    },
    [NOCTURNE_OF_SHADOW] = {
        .k = NOCTURNE_OF_SHADOW,
        .name = "Nocturne of Shadow",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xBF
    },
    [PRELUDE_OF_LIGHT] = {
        .k = PRELUDE_OF_LIGHT,
        .name = "Prelude of Light",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xC0
    },
    [ZELDAS_LULLABY] = {
        .k = ZELDAS_LULLABY,
        .name = "Zeldas Lullaby",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xC1
    },
    [EPONAS_SONG] = {
        .k = EPONAS_SONG,
        .name = "Eponas Song",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xC2
    },
    [SARIAS_SONG] = {
        .k = SARIAS_SONG,
        .name = "Sarias Song",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xC3
    },
    [SUNS_SONG] = {
        .k = SUNS_SONG,
        .name = "Suns Song",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xC4
    },
    [SONG_OF_TIME] = {
        .k = SONG_OF_TIME,
        .name = "Song of Time",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xC5
    },
    [SONG_OF_STORMS] = {
        .k = SONG_OF_STORMS,
        .name = "Song of Storms",
        .type = ITEM_TYPE_SONG,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0xC6
    },
    [BUY_DEKU_NUT_5] = {
        .k = BUY_DEKU_NUT_5,
        .name = "Buy Deku Nut (5)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [BUY_ARROWS_30] = {
        .k = BUY_ARROWS_30,
        .name = "Buy Arrows (30)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x01
    },
    [BUY_ARROWS_50] = {
        .k = BUY_ARROWS_50,
        .name = "Buy Arrows (50)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x02
    },
    [BUY_BOMBS_5_25] = {
        .k = BUY_BOMBS_5_25,
        .name = "Buy Bombs (5) [25]",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x03
    },
    [BUY_DEKU_NUT_10] = {
        .k = BUY_DEKU_NUT_10,
        .name = "Buy Deku Nut (10)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x04
    },
    [BUY_DEKU_STICK_1] = {
        .k = BUY_DEKU_STICK_1,
        .name = "Buy Deku Stick (1)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x05
    },
    [BUY_BOMBS_10] = {
        .k = BUY_BOMBS_10,
        .name = "Buy Bombs (10)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x06
    },
    [BUY_FISH] = {
        .k = BUY_FISH,
        .name = "Buy Fish",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x07
    },
    [BUY_RED_POTION_30] = {
        .k = BUY_RED_POTION_30,
        .name = "Buy Red Potion [30]",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x08
    },
    [BUY_GREEN_POTION] = {
        .k = BUY_GREEN_POTION,
        .name = "Buy Green Potion",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x09
    },
    [BUY_BLUE_POTION] = {
        .k = BUY_BLUE_POTION,
        .name = "Buy Blue Potion",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x0A
    },
    [BUY_HYLIAN_SHIELD] = {
        .k = BUY_HYLIAN_SHIELD,
        .name = "Buy Hylian Shield",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x0C
    },
    [BUY_DEKU_SHIELD] = {
        .k = BUY_DEKU_SHIELD,
        .name = "Buy Deku Shield",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x0D
    },
    [BUY_GORON_TUNIC] = {
        .k = BUY_GORON_TUNIC,
        .name = "Buy Goron Tunic",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x0E
    },
    [BUY_ZORA_TUNIC] = {
        .k = BUY_ZORA_TUNIC,
        .name = "Buy Zora Tunic",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x0F
    },
    [BUY_HEART] = {
        .k = BUY_HEART,
        .name = "Buy Heart",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x10
    },
    [BUY_BOMBCHU_10] = {
        .k = BUY_BOMBCHU_10,
        .name = "Buy Bombchu (10)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x15
    },
    [BUY_BOMBCHU_20] = {
        .k = BUY_BOMBCHU_20,
        .name = "Buy Bombchu (20)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x16
    },
    [BUY_BOMBCHU_5] = {
        .k = BUY_BOMBCHU_5,
        .name = "Buy Bombchu (5)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x18
    },
    [BUY_DEKU_SEEDS_30] = {
        .k = BUY_DEKU_SEEDS_30,
        .name = "Buy Deku Seeds (30)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x1D
    },
    [SOLD_OUT] = {
        .k = SOLD_OUT,
        .name = "Sold Out",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x26
    },
    [BUY_BLUE_FIRE] = {
        .k = BUY_BLUE_FIRE,
        .name = "Buy Blue Fire",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x27
    },
    [BUY_BOTTLE_BUG] = {
        .k = BUY_BOTTLE_BUG,
        .name = "Buy Bottle Bug",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x28
    },
    [BUY_POE] = {
        .k = BUY_POE,
        .name = "Buy Poe",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x2A
    },
    [BUY_FAIRYS_SPIRIT] = {
        .k = BUY_FAIRYS_SPIRIT,
        .name = "Buy Fairy's Spirit",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x2B
    },
    [BUY_ARROWS_10] = {
        .k = BUY_ARROWS_10,
        .name = "Buy Arrows (10)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x2C
    },
    [BUY_BOMBS_20] = {
        .k = BUY_BOMBS_20,
        .name = "Buy Bombs (20)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x2D
    },
    [BUY_BOMBS_30] = {
        .k = BUY_BOMBS_30,
        .name = "Buy Bombs (30)",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x2E
    },
    [BUY_BOMBS_5_35] = {
        .k = BUY_BOMBS_5_35,
        .name = "Buy Bombs (5) [35]",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x2F
    },
    [BUY_RED_POTION_40] = {
        .k = BUY_RED_POTION_40,
        .name = "Buy Red Potion [40]",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x30
    },
    [BUY_RED_POTION_50] = {
        .k = BUY_RED_POTION_50,
        .name = "Buy Red Potion [50]",
        .type = ITEM_TYPE_SHOP,
        .fill = ITEM_FILL_PRIORITY,
        .gi = 0x31
    },
    [KOKIRI_EMERALD] = {
        .k = KOKIRI_EMERALD,
        .name = "Kokiri Emerald",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [GORON_RUBY] = {
        .k = GORON_RUBY,
        .name = "Goron Ruby",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [ZORA_SAPPHIRE] = {
        .k = ZORA_SAPPHIRE,
        .name = "Zora Sapphire",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [FOREST_MEDALLION] = {
        .k = FOREST_MEDALLION,
        .name = "Forest Medallion",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [FIRE_MEDALLION] = {
        .k = FIRE_MEDALLION,
        .name = "Fire Medallion",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [WATER_MEDALLION] = {
        .k = WATER_MEDALLION,
        .name = "Water Medallion",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [SPIRIT_MEDALLION] = {
        .k = SPIRIT_MEDALLION,
        .name = "Spirit Medallion",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [SHADOW_MEDALLION] = {
        .k = SHADOW_MEDALLION,
        .name = "Shadow Medallion",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
    [LIGHT_MEDALLION] = {
        .k = LIGHT_MEDALLION,
        .name = "Light Medallion",
        .type = ITEM_TYPE_EVENT,
        .fill = ITEM_FILL_ADVANCEMENT,
        .gi = 0x00
    },
};

item_song_t song_items[] = {
    {
        .k = MINUET_OF_FOREST,
        .text_id = 0x73,
        .song_id = 0x02,
        .item_id = 0x5A,
    },
    {
        .k = BOLERO_OF_FIRE,
        .text_id = 0x74,
        .song_id = 0x03,
        .item_id = 0x5B,
    },
    {
        .k = SERENADE_OF_WATER,
        .text_id = 0x75,
        .song_id = 0x04,
        .item_id = 0x5C,
    },
    {
        .k = REQUIEM_OF_SPIRIT,
        .text_id = 0x76,
        .song_id = 0x05,
        .item_id = 0x5D,
    },
    {
        .k = NOCTURNE_OF_SHADOW,
        .text_id = 0x77,
        .song_id = 0x06,
        .item_id = 0x5E,
    },
    {
        .k = PRELUDE_OF_LIGHT,
        .text_id = 0x78,
        .song_id = 0x07,
        .item_id = 0x5F,
    },
    {
        .k = ZELDAS_LULLABY,
        .text_id = 0xD4,
        .song_id = 0x0A,
        .item_id = 0x60,
    },
    {
        .k = EPONAS_SONG,
        .text_id = 0xD2,
        .song_id = 0x09,
        .item_id = 0x61,
    },
    {
        .k = SARIAS_SONG,
        .text_id = 0xD1,
        .song_id = 0x08,
        .item_id = 0x62,
    },
    {
        .k = SUNS_SONG,
        .text_id = 0xD3,
        .song_id = 0x0B,
        .item_id = 0x63,
    },
    {
        .k = SONG_OF_TIME,
        .text_id = 0xD5,
        .song_id = 0x0C,
        .item_id = 0x64,
    },
    {
        .k = SONG_OF_STORMS,
        .text_id = 0xD6,
        .song_id = 0x0D,
        .item_id = 0x65,
    },
};

item_event_t event_items[] = {
    {
        .k = KOKIRI_EMERALD,
        .save_byte = 0xA5,
        .save_bit = 0x04,
        .addr2_data = 0x80,
        .bit_mask = 0x00040000,
        .item_id = 0x6C,
    },
    {
        .k = GORON_RUBY,
        .save_byte = 0xA5,
        .save_bit = 0x08,
        .addr2_data = 0x81,
        .bit_mask = 0x00080000,
        .item_id = 0x6D,
    },
    {
        .k = ZORA_SAPPHIRE,
        .save_byte = 0xA5,
        .save_bit = 0x10,
        .addr2_data = 0x82,
        .bit_mask = 0x00100000,
        .item_id = 0x6E,
    },
    {
        .k = FOREST_MEDALLION,
        .save_byte = 0xA7,
        .save_bit = 0x01,
        .addr2_data = 0x3E,
        .bit_mask = 0x00000001,
        .item_id = 0x66,
    },
    {
        .k = FIRE_MEDALLION,
        .save_byte = 0xA7,
        .save_bit = 0x02,
        .addr2_data = 0x3C,
        .bit_mask = 0x00000002,
        .item_id = 0x67,
    },
    {
        .k = WATER_MEDALLION,
        .save_byte = 0xA7,
        .save_bit = 0x04,
        .addr2_data = 0x3D,
        .bit_mask = 0x00000004,
        .item_id = 0x68,
    },
    {
        .k = SPIRIT_MEDALLION,
        .save_byte = 0xA7,
        .save_bit = 0x08,
        .addr2_data = 0x3F,
        .bit_mask = 0x00000008,
        .item_id = 0x69,
    },
    {
        .k = SHADOW_MEDALLION,
        .save_byte = 0xA7,
        .save_bit = 0x10,
        .addr2_data = 0x41,
        .bit_mask = 0x00000010,
        .item_id = 0x6A,
    },
    {
        .k = LIGHT_MEDALLION,
        .save_byte = 0xA7,
        .save_bit = 0x20,
        .addr2_data = 0x40,
        .bit_mask = 0x00000020,
        .item_id = 0x6B,
    },
};

item_shop_t shop_items[] = {
    {
        .k = BUY_DEKU_NUT_5,
        .object = 0x00BB,
        .price = 15,
    },
    {
        .k = BUY_ARROWS_30,
        .object = 0x00D8,
        .price = 60,
    },
    {
        .k = BUY_ARROWS_50,
        .object = 0x00D8,
        .price = 90,
    },
    {
        .k = BUY_BOMBS_5_25,
        .object = 0x00CE,
        .price = 25,
    },
    {
        .k = BUY_DEKU_NUT_10,
        .object = 0x00BB,
        .price = 30,
    },
    {
        .k = BUY_DEKU_STICK_1,
        .object = 0x00C7,
        .price = 10,
    },
    {
        .k = BUY_BOMBS_10,
        .object = 0x00CE,
        .price = 50,
    },
    {
        .k = BUY_FISH,
        .object = 0x00F4,
        .price = 200,
    },
    {
        .k = BUY_RED_POTION_30,
        .object = 0x00EB,
        .price = 30,
    },
    {
        .k = BUY_GREEN_POTION,
        .object = 0x00EB,
        .price = 30,
    },
    {
        .k = BUY_BLUE_POTION,
        .object = 0x00EB,
        .price = 100,
    },
    {
        .k = BUY_HYLIAN_SHIELD,
        .object = 0x00DC,
        .price = 80,
    },
    {
        .k = BUY_DEKU_SHIELD,
        .object = 0x00CB,
        .price = 40,
    },
    {
        .k = BUY_GORON_TUNIC,
        .object = 0x00F2,
        .price = 200,
    },
    {
        .k = BUY_ZORA_TUNIC,
        .object = 0x00F2,
        .price = 300,
    },
    {
        .k = BUY_HEART,
        .object = 0x00B7,
        .price = 10,
    },
    {
        .k = BUY_BOMBCHU_10,
        .object = 0x00D9,
        .price = 99,
    },
    {
        .k = BUY_BOMBCHU_20,
        .object = 0x00D9,
        .price = 180,
    },
    {
        .k = BUY_BOMBCHU_5,
        .object = 0x00D9,
        .price = 60,
    },
    {
        .k = BUY_DEKU_SEEDS_30,
        .object = 0x0119,
        .price = 30,
    },
    {
        .k = SOLD_OUT,
        .object = 0x0148,
    },
    {
        .k = BUY_BLUE_FIRE,
        .object = 0x0173,
        .price = 300,
    },
    {
        .k = BUY_BOTTLE_BUG,
        .object = 0x0174,
        .price = 50,
    },
    {
        .k = BUY_POE,
        .object = 0x0176,
        .price = 30,
    },
    {
        .k = BUY_FAIRYS_SPIRIT,
        .object = 0x0177,
        .price = 50,
    },
    {
        .k = BUY_ARROWS_10,
        .object = 0x00D8,
        .price = 20,
    },
    {
        .k = BUY_BOMBS_20,
        .object = 0x00CE,
        .price = 80,
    },
    {
        .k = BUY_BOMBS_30,
        .object = 0x00CE,
        .price = 120,
    },
    {
        .k = BUY_BOMBS_5_35,
        .object = 0x00CE,
        .price = 35,
    },
    {
        .k = BUY_RED_POTION_40,
        .object = 0x00EB,
        .price = 40,
    },
    {
        .k = BUY_RED_POTION_50,
        .object = 0x00EB,
        .price = 50,
    },
};

