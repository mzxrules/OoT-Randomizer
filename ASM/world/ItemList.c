#include <stdbool.h>
#include "itemlist.h"

item_info_t item_table[] =
/*
for item in item_table:
     v = item_table[item]
     gi = v[2]
     if gi is None:
         gi = 0
     g = v[1]
     if g is None:
         g = "ITEM_FILL_NORMAL"
     elif g == True:
         g = "ITEM_FILL_ADVANCEMENT"
     elif g == False:
         g = "ITEM_FILL_PRIORITY"
     print("{}\t{}\t{}\t{}\t{}".format(to_c_sym(item),item,v[0],g, gi))
*/
{
    { .k = BOMBS_5, .name = "Bombs (5)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x01},
    { .k = DEKU_NUTS_5, .name = "Deku Nuts (5)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x02},
    { .k = BOMBCHUS_10, .name = "Bombchus (10)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x03},
    { .k = BOOMERANG, .name = "Boomerang", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x06},
    { .k = DEKU_STICK_1, .name = "Deku Stick (1)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x07},
    { .k = LENS_OF_TRUTH, .name = "Lens of Truth", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x0A},
    { .k = HAMMER, .name = "Hammer", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x0D},
    { .k = COJIRO, .name = "Cojiro", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x0E},
    { .k = BOTTLE, .name = "Bottle", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x0F},
    { .k = BOTTLE_WITH_MILK, .name = "Bottle with Milk", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x14},
    { .k = BOTTLE_WITH_LETTER, .name = "Bottle with Letter", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x15},
    { .k = MAGIC_BEAN, .name = "Magic Bean", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x16},
    { .k = SKULL_MASK, .name = "Skull Mask", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x17},
    { .k = SPOOKY_MASK, .name = "Spooky Mask", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x18},
    { .k = KEATON_MASK, .name = "Keaton Mask", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x1A},
    { .k = BUNNY_HOOD, .name = "Bunny Hood", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x1B},
    { .k = MASK_OF_TRUTH, .name = "Mask of Truth", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x1C},
    { .k = POCKET_EGG, .name = "Pocket Egg", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x1D},
    { .k = POCKET_CUCCO, .name = "Pocket Cucco", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x1E},
    { .k = ODD_MUSHROOM, .name = "Odd Mushroom", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x1F},
    { .k = ODD_POTION, .name = "Odd Potion", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x20},
    { .k = POACHERS_SAW, .name = "Poachers Saw", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x21},
    { .k = BROKEN_SWORD, .name = "Broken Sword", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x22},
    { .k = PRESCRIPTION, .name = "Prescription", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x23},
    { .k = EYEBALL_FROG, .name = "Eyeball Frog", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x24},
    { .k = EYEDROPS, .name = "Eyedrops", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x25},
    { .k = CLAIM_CHECK, .name = "Claim Check", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x26},
    { .k = KOKIRI_SWORD, .name = "Kokiri Sword", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x27},
    { .k = DEKU_SHIELD, .name = "Deku Shield", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x29},
    { .k = HYLIAN_SHIELD, .name = "Hylian Shield", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x2A},
    { .k = MIRROR_SHIELD, .name = "Mirror Shield", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x2B},
    { .k = GORON_TUNIC, .name = "Goron Tunic", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x2C},
    { .k = ZORA_TUNIC, .name = "Zora Tunic", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x2D},
    { .k = IRON_BOOTS, .name = "Iron Boots", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x2E},
    { .k = HOVER_BOOTS, .name = "Hover Boots", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x2F},
    { .k = STONE_OF_AGONY, .name = "Stone of Agony", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x39},
    { .k = GERUDO_MEMBERSHIP_CARD, .name = "Gerudo Membership Card", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x3A},
    { .k = HEART_CONTAINER, .name = "Heart Container", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x3D},
    { .k = PIECE_OF_HEART, .name = "Piece of Heart", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x3E},
    { .k = BOSS_KEY, .name = "Boss Key", .type = ITEM_TYPE_BOSSKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x3F},
    { .k = COMPASS, .name = "Compass", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0x40},
    { .k = MAP, .name = "Map", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0x41},
    { .k = SMALL_KEY, .name = "Small Key", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x42},
    { .k = WEIRD_EGG, .name = "Weird Egg", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x47},
    { .k = RECOVERY_HEART, .name = "Recovery Heart", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x48},
    { .k = ARROWS_5, .name = "Arrows (5)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x49},
    { .k = ARROWS_10, .name = "Arrows (10)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x4A},
    { .k = ARROWS_30, .name = "Arrows (30)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x4B},
    { .k = RUPEE_1, .name = "Rupee (1)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x4C},
    { .k = RUPEES_5, .name = "Rupees (5)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x4D},
    { .k = RUPEES_20, .name = "Rupees (20)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x4E},
    { .k = HEART_CONTAINER_BOSS, .name = "Heart Container (Boss)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x4F},
    { .k = GORON_MASK, .name = "Goron Mask", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x51},
    { .k = ZORA_MASK, .name = "Zora Mask", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x52},
    { .k = GERUDO_MASK, .name = "Gerudo Mask", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x53},
    { .k = RUPEES_50, .name = "Rupees (50)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x55},
    { .k = RUPEES_200, .name = "Rupees (200)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x56},
    { .k = BIGGORON_SWORD, .name = "Biggoron Sword", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x57},
    { .k = FIRE_ARROWS, .name = "Fire Arrows", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x58},
    { .k = ICE_ARROWS, .name = "Ice Arrows", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x59},
    { .k = LIGHT_ARROWS, .name = "Light Arrows", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x5A},
    { .k = GOLD_SKULLTULA_TOKEN, .name = "Gold Skulltula Token", .type = ITEM_TYPE_TOKEN, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x5B},
    { .k = DINS_FIRE, .name = "Dins Fire", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x5C},
    { .k = NAYRUS_LOVE, .name = "Nayrus Love", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x5E},
    { .k = FARORES_WIND, .name = "Farores Wind", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x5D},
    { .k = DEKU_NUTS_10, .name = "Deku Nuts (10)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x64},
    { .k = BOMBS_10, .name = "Bombs (10)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x66},
    { .k = BOMBS_20, .name = "Bombs (20)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x67},
    { .k = DEKU_SEEDS_30, .name = "Deku Seeds (30)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x69},
    { .k = BOMBCHUS_5, .name = "Bombchus (5)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x6A},
    { .k = BOMBCHUS_20, .name = "Bombchus (20)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x6B},
    { .k = RUPEE_TREASURE_CHEST_GAME, .name = "Rupee (Treasure Chest Game)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x72},
    { .k = PIECE_OF_HEART_TREASURE_CHEST_GAME, .name = "Piece of Heart (Treasure Chest Game)", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x76},
    { .k = ICE_TRAP, .name = "Ice Trap", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x7C},
    { .k = PROGRESSIVE_HOOKSHOT, .name = "Progressive Hookshot", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x80},
    { .k = PROGRESSIVE_STRENGTH_UPGRADE, .name = "Progressive Strength Upgrade", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x81},
    { .k = BOMB_BAG, .name = "Bomb Bag", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x82},
    { .k = BOW, .name = "Bow", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x83},
    { .k = SLINGSHOT, .name = "Slingshot", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x84},
    { .k = PROGRESSIVE_WALLET, .name = "Progressive Wallet", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x85},
    { .k = PROGRESSIVE_SCALE, .name = "Progressive Scale", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x86},
    { .k = DEKU_NUT_CAPACITY, .name = "Deku Nut Capacity", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x87},
    { .k = DEKU_STICK_CAPACITY, .name = "Deku Stick Capacity", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_NORMAL, .gi = 0x88},
    { .k = BOMBCHUS, .name = "Bombchus", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x89},
    { .k = MAGIC_METER, .name = "Magic Meter", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x8A},
    { .k = OCARINA, .name = "Ocarina", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x8B},
    { .k = BOTTLE_WITH_RED_POTION, .name = "Bottle with Red Potion", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x8C},
    { .k = BOTTLE_WITH_GREEN_POTION, .name = "Bottle with Green Potion", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x8D},
    { .k = BOTTLE_WITH_BLUE_POTION, .name = "Bottle with Blue Potion", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x8E},
    { .k = BOTTLE_WITH_FAIRY, .name = "Bottle with Fairy", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x8F},
    { .k = BOTTLE_WITH_FISH, .name = "Bottle with Fish", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x90},
    { .k = BOTTLE_WITH_BLUE_FIRE, .name = "Bottle with Blue Fire", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x91},
    { .k = BOTTLE_WITH_BUGS, .name = "Bottle with Bugs", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x92},
    { .k = BOTTLE_WITH_BIG_POE, .name = "Bottle with Big Poe", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x93},
    { .k = BOTTLE_WITH_POE, .name = "Bottle with Poe", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x94},
    { .k = BOSS_KEY_FOREST_TEMPLE, .name = "Boss Key (Forest Temple)", .type = ITEM_TYPE_BOSSKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x95},
    { .k = BOSS_KEY_FIRE_TEMPLE, .name = "Boss Key (Fire Temple)", .type = ITEM_TYPE_BOSSKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x96},
    { .k = BOSS_KEY_WATER_TEMPLE, .name = "Boss Key (Water Temple)", .type = ITEM_TYPE_BOSSKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x97},
    { .k = BOSS_KEY_SPIRIT_TEMPLE, .name = "Boss Key (Spirit Temple)", .type = ITEM_TYPE_BOSSKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x98},
    { .k = BOSS_KEY_SHADOW_TEMPLE, .name = "Boss Key (Shadow Temple)", .type = ITEM_TYPE_BOSSKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x99},
    { .k = BOSS_KEY_GANONS_CASTLE, .name = "Boss Key (Ganons Castle)", .type = ITEM_TYPE_BOSSKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x9A},
    { .k = COMPASS_DEKU_TREE, .name = "Compass (Deku Tree)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0x9B},
    { .k = COMPASS_DODONGOS_CAVERN, .name = "Compass (Dodongos Cavern)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0x9C},
    { .k = COMPASS_JABU_JABUS_BELLY, .name = "Compass (Jabu Jabus Belly)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0x9D},
    { .k = COMPASS_FOREST_TEMPLE, .name = "Compass (Forest Temple)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0x9E},
    { .k = COMPASS_FIRE_TEMPLE, .name = "Compass (Fire Temple)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0x9F},
    { .k = COMPASS_WATER_TEMPLE, .name = "Compass (Water Temple)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0xA0},
    { .k = COMPASS_SPIRIT_TEMPLE, .name = "Compass (Spirit Temple)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0xA1},
    { .k = COMPASS_SHADOW_TEMPLE, .name = "Compass (Shadow Temple)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0xA2},
    { .k = COMPASS_BOTTOM_OF_THE_WELL, .name = "Compass (Bottom of the Well)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0xA3},
    { .k = COMPASS_ICE_CAVERN, .name = "Compass (Ice Cavern)", .type = ITEM_TYPE_COMPASS, .fill = ITEM_FILL_NORMAL, .gi = 0xA4},
    { .k = MAP_DEKU_TREE, .name = "Map (Deku Tree)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xA5},
    { .k = MAP_DODONGOS_CAVERN, .name = "Map (Dodongos Cavern)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xA6},
    { .k = MAP_JABU_JABUS_BELLY, .name = "Map (Jabu Jabus Belly)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xA7},
    { .k = MAP_FOREST_TEMPLE, .name = "Map (Forest Temple)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xA8},
    { .k = MAP_FIRE_TEMPLE, .name = "Map (Fire Temple)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xA9},
    { .k = MAP_WATER_TEMPLE, .name = "Map (Water Temple)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xAA},
    { .k = MAP_SPIRIT_TEMPLE, .name = "Map (Spirit Temple)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xAB},
    { .k = MAP_SHADOW_TEMPLE, .name = "Map (Shadow Temple)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xAC},
    { .k = MAP_BOTTOM_OF_THE_WELL, .name = "Map (Bottom of the Well)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xAD},
    { .k = MAP_ICE_CAVERN, .name = "Map (Ice Cavern)", .type = ITEM_TYPE_MAP, .fill = ITEM_FILL_NORMAL, .gi = 0xAE},
    { .k = SMALL_KEY_FOREST_TEMPLE, .name = "Small Key (Forest Temple)", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xAF},
    { .k = SMALL_KEY_FIRE_TEMPLE, .name = "Small Key (Fire Temple)", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB0},
    { .k = SMALL_KEY_WATER_TEMPLE, .name = "Small Key (Water Temple)", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB1},
    { .k = SMALL_KEY_SPIRIT_TEMPLE, .name = "Small Key (Spirit Temple)", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB2},
    { .k = SMALL_KEY_SHADOW_TEMPLE, .name = "Small Key (Shadow Temple)", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB3},
    { .k = SMALL_KEY_BOTTOM_OF_THE_WELL, .name = "Small Key (Bottom of the Well)", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB4},
    { .k = SMALL_KEY_GERUDO_TRAINING_GROUNDS, .name = "Small Key (Gerudo Training Grounds)", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB5},
    { .k = SMALL_KEY_GERUDO_FORTRESS, .name = "Small Key (Gerudo Fortress)", .type = ITEM_TYPE_FORTRESS_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB6},
    { .k = SMALL_KEY_GANONS_CASTLE, .name = "Small Key (Ganons Castle)", .type = ITEM_TYPE_SMALLKEY, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB7},
    { .k = DOUBLE_DEFENSE, .name = "Double Defense", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xB8},
    { .k = ZELDAS_LETTER, .name = "Zeldas Letter", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = MASTER_SWORD, .name = "Master Sword", .type = ITEM_TYPE_ITEM, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = EPONA, .name = "Epona", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = DEKU_STICK_DROP, .name = "Deku Stick Drop", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = DEKU_NUT_DROP, .name = "Deku Nut Drop", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = CARPENTER_RESCUE, .name = "Carpenter Rescue", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = FOREST_TRIAL_CLEAR, .name = "Forest Trial Clear", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = FIRE_TRIAL_CLEAR, .name = "Fire Trial Clear", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = WATER_TRIAL_CLEAR, .name = "Water Trial Clear", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = SHADOW_TRIAL_CLEAR, .name = "Shadow Trial Clear", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = SPIRIT_TRIAL_CLEAR, .name = "Spirit Trial Clear", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = LIGHT_TRIAL_CLEAR, .name = "Light Trial Clear", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = TRIFORCE, .name = "Triforce", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = MINUET_OF_FOREST, .name = "Minuet of Forest", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xBB},
    { .k = BOLERO_OF_FIRE, .name = "Bolero of Fire", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xBC},
    { .k = SERENADE_OF_WATER, .name = "Serenade of Water", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xBD},
    { .k = REQUIEM_OF_SPIRIT, .name = "Requiem of Spirit", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xBE},
    { .k = NOCTURNE_OF_SHADOW, .name = "Nocturne of Shadow", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xBF},
    { .k = PRELUDE_OF_LIGHT, .name = "Prelude of Light", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xC0},
    { .k = ZELDAS_LULLABY, .name = "Zeldas Lullaby", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xC1},
    { .k = EPONAS_SONG, .name = "Eponas Song", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xC2},
    { .k = SARIAS_SONG, .name = "Sarias Song", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xC3},
    { .k = SUNS_SONG, .name = "Suns Song", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xC4},
    { .k = SONG_OF_TIME, .name = "Song of Time", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xC5},
    { .k = SONG_OF_STORMS, .name = "Song of Storms", .type = ITEM_TYPE_SONG, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0xC6},
    { .k = BUY_DEKU_NUT_5, .name = "Buy Deku Nut (5)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = BUY_ARROWS_30, .name = "Buy Arrows (30)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x01},
    { .k = BUY_ARROWS_50, .name = "Buy Arrows (50)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x02},
    { .k = BUY_BOMBS_5_25, .name = "Buy Bombs (5) [25]", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x03},
    { .k = BUY_DEKU_NUT_10, .name = "Buy Deku Nut (10)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x04},
    { .k = BUY_DEKU_STICK_1, .name = "Buy Deku Stick (1)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x05},
    { .k = BUY_BOMBS_10, .name = "Buy Bombs (10)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x06},
    { .k = BUY_FISH, .name = "Buy Fish", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x07},
    { .k = BUY_RED_POTION_30, .name = "Buy Red Potion [30]", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x08},
    { .k = BUY_GREEN_POTION, .name = "Buy Green Potion", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x09},
    { .k = BUY_BLUE_POTION, .name = "Buy Blue Potion", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x0A},
    { .k = BUY_HYLIAN_SHIELD, .name = "Buy Hylian Shield", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x0C},
    { .k = BUY_DEKU_SHIELD, .name = "Buy Deku Shield", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x0D},
    { .k = BUY_GORON_TUNIC, .name = "Buy Goron Tunic", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x0E},
    { .k = BUY_ZORA_TUNIC, .name = "Buy Zora Tunic", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x0F},
    { .k = BUY_HEART, .name = "Buy Heart", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x10},
    { .k = BUY_BOMBCHU_10, .name = "Buy Bombchu (10)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x15},
    { .k = BUY_BOMBCHU_20, .name = "Buy Bombchu (20)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x16},
    { .k = BUY_BOMBCHU_5, .name = "Buy Bombchu (5)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x18},
    { .k = BUY_DEKU_SEEDS_30, .name = "Buy Deku Seeds (30)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x1D},
    { .k = SOLD_OUT, .name = "Sold Out", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x26},
    { .k = BUY_BLUE_FIRE, .name = "Buy Blue Fire", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x27},
    { .k = BUY_BOTTLE_BUG, .name = "Buy Bottle Bug", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x28},
    { .k = BUY_POE, .name = "Buy Poe", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x2A},
    { .k = BUY_FAIRYS_SPIRIT, .name = "Buy Fairy's Spirit", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x2B},
    { .k = BUY_ARROWS_10, .name = "Buy Arrows (10)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x2C},
    { .k = BUY_BOMBS_20, .name = "Buy Bombs (20)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x2D},
    { .k = BUY_BOMBS_30, .name = "Buy Bombs (30)", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x2E},
    { .k = BUY_BOMBS_5_35, .name = "Buy Bombs (5) [35]", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x2F},
    { .k = BUY_RED_POTION_40, .name = "Buy Red Potion [40]", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x30},
    { .k = BUY_RED_POTION_50, .name = "Buy Red Potion [50]", .type = ITEM_TYPE_SHOP, .fill = ITEM_FILL_PRIORITY, .gi = 0x31},
    { .k = KOKIRI_EMERALD, .name = "Kokiri Emerald", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = GORON_RUBY, .name = "Goron Ruby", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = ZORA_SAPPHIRE, .name = "Zora Sapphire", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = FOREST_MEDALLION, .name = "Forest Medallion", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = FIRE_MEDALLION, .name = "Fire Medallion", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = WATER_MEDALLION, .name = "Water Medallion", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = SPIRIT_MEDALLION, .name = "Spirit Medallion", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = SHADOW_MEDALLION, .name = "Shadow Medallion", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
    { .k = LIGHT_MEDALLION, .name = "Light Medallion", .type = ITEM_TYPE_EVENT, .fill = ITEM_FILL_ADVANCEMENT, .gi = 0x00},
};

/*
for item in item_table:
     v = item_table[item]
     if v[0] == 'Song' and v[3] is not None:
         print("{\n    " + ".k = {},".format(to_c_sym(item)))
         s = v[3]
         for k in s:
             print("    .{} = 0x{:02x},".format(k,s[k]))
         print("},")
*/

item_song_t song_items[] = 
{
    {
        .k = MINUET_OF_FOREST,
        .text_id = 0x73,
        .song_id = 0x02,
        .item_id = 0x5a,
    },
    {
        .k = BOLERO_OF_FIRE,
        .text_id = 0x74,
        .song_id = 0x03,
        .item_id = 0x5b,
    },
    {
        .k = SERENADE_OF_WATER,
        .text_id = 0x75,
        .song_id = 0x04,
        .item_id = 0x5c,
    },
    {
        .k = REQUIEM_OF_SPIRIT,
        .text_id = 0x76,
        .song_id = 0x05,
        .item_id = 0x5d,
    },
    {
        .k = NOCTURNE_OF_SHADOW,
        .text_id = 0x77,
        .song_id = 0x06,
        .item_id = 0x5e,
    },
    {
        .k = PRELUDE_OF_LIGHT,
        .text_id = 0x78,
        .song_id = 0x07,
        .item_id = 0x5f,
    },
    {
        .k = ZELDAS_LULLABY,
        .text_id = 0xd4,
        .song_id = 0x0a,
        .item_id = 0x60,
    },
    {
        .k = EPONAS_SONG,
        .text_id = 0xd2,
        .song_id = 0x09,
        .item_id = 0x61,
    },
    {
        .k = SARIAS_SONG,
        .text_id = 0xd1,
        .song_id = 0x08,
        .item_id = 0x62,
    },
    {
        .k = SUNS_SONG,
        .text_id = 0xd3,
        .song_id = 0x0b,
        .item_id = 0x63,
    },
    {
        .k = SONG_OF_TIME,
        .text_id = 0xd5,
        .song_id = 0x0c,
        .item_id = 0x64,
    },
    {
        .k = SONG_OF_STORMS,
        .text_id = 0xd6,
        .song_id = 0x0d,
        .item_id = 0x65,
    },
};

item_event_t event_items[] =
{
    {
        .k = KOKIRI_EMERALD,
        .save_byte = 0xa5,
        .save_bit = 0x04,
        .addr2_data = 0x80,
        .bit_mask = 0x00040000,
        .item_id = 0x6c,
    },
    {
        .k = GORON_RUBY,
        .save_byte = 0xa5,
        .save_bit = 0x08,
        .addr2_data = 0x81,
        .bit_mask = 0x00080000,
        .item_id = 0x6d,
    },
    {
        .k = ZORA_SAPPHIRE,
        .save_byte = 0xa5,
        .save_bit = 0x10,
        .addr2_data = 0x82,
        .bit_mask = 0x00100000,
        .item_id = 0x6e,
    },
    {
        .k = FOREST_MEDALLION,
        .save_byte = 0xa7,
        .save_bit = 0x01,
        .addr2_data = 0x3e,
        .bit_mask = 0x00000001,
        .item_id = 0x66,
    },
    {
        .k = FIRE_MEDALLION,
        .save_byte = 0xa7,
        .save_bit = 0x02,
        .addr2_data = 0x3c,
        .bit_mask = 0x00000002,
        .item_id = 0x67,
    },
    {
        .k = WATER_MEDALLION,
        .save_byte = 0xa7,
        .save_bit = 0x04,
        .addr2_data = 0x3d,
        .bit_mask = 0x00000004,
        .item_id = 0x68,
    },
    {
        .k = SPIRIT_MEDALLION,
        .save_byte = 0xa7,
        .save_bit = 0x08,
        .addr2_data = 0x3f,
        .bit_mask = 0x00000008,
        .item_id = 0x69,
    },
    {
        .k = SHADOW_MEDALLION,
        .save_byte = 0xa7,
        .save_bit = 0x10,
        .addr2_data = 0x41,
        .bit_mask = 0x00000010,
        .item_id = 0x6a,
    },
    {
        .k = LIGHT_MEDALLION,
        .save_byte = 0xa7,
        .save_bit = 0x20,
        .addr2_data = 0x40,
        .bit_mask = 0x00000020,
        .item_id = 0x6b,
    },
};

item_shop_t shop_items[] =
{
    {
        .k = BUY_DEKU_NUT_5,
        .object = 0x00bb,
        .price = 15,
    },
    {
        .k = BUY_ARROWS_30,
        .object = 0x00d8,
        .price = 60,
    },
    {
        .k = BUY_ARROWS_50,
        .object = 0x00d8,
        .price = 90,
    },
    {
        .k = BUY_BOMBS_5_25,
        .object = 0x00ce,
        .price = 25,
    },
    {
        .k = BUY_DEKU_NUT_10,
        .object = 0x00bb,
        .price = 30,
    },
    {
        .k = BUY_DEKU_STICK_1,
        .object = 0x00c7,
        .price = 10,
    },
    {
        .k = BUY_BOMBS_10,
        .object = 0x00ce,
        .price = 50,
    },
    {
        .k = BUY_FISH,
        .object = 0x00f4,
        .price = 200,
    },
    {
        .k = BUY_RED_POTION_30,
        .object = 0x00eb,
        .price = 30,
    },
    {
        .k = BUY_GREEN_POTION,
        .object = 0x00eb,
        .price = 30,
    },
    {
        .k = BUY_BLUE_POTION,
        .object = 0x00eb,
        .price = 100,
    },
    {
        .k = BUY_HYLIAN_SHIELD,
        .object = 0x00dc,
        .price = 80,
    },
    {
        .k = BUY_DEKU_SHIELD,
        .object = 0x00cb,
        .price = 40,
    },
    {
        .k = BUY_GORON_TUNIC,
        .object = 0x00f2,
        .price = 200,
    },
    {
        .k = BUY_ZORA_TUNIC,
        .object = 0x00f2,
        .price = 300,
    },
    {
        .k = BUY_HEART,
        .object = 0x00b7,
        .price = 10,
    },
    {
        .k = BUY_BOMBCHU_10,
        .object = 0x00d9,
        .price = 99,
    },
    {
        .k = BUY_BOMBCHU_20,
        .object = 0x00d9,
        .price = 180,
    },
    {
        .k = BUY_BOMBCHU_5,
        .object = 0x00d9,
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
        .price = 0,
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
        .object = 0x00d8,
        .price = 20,
    },
    {
        .k = BUY_BOMBS_20,
        .object = 0x00ce,
        .price = 80,
    },
    {
        .k = BUY_BOMBS_30,
        .object = 0x00ce,
        .price = 120,
    },
    {
        .k = BUY_BOMBS_5_35,
        .object = 0x00ce,
        .price = 35,
    },
    {
        .k = BUY_RED_POTION_40,
        .object = 0x00eb,
        .price = 40,
    },
    {
        .k = BUY_RED_POTION_50,
        .object = 0x00eb,
        .price = 50,
    },
};
 
bool is_progressive_item(item_e item)
{
    if (item >= SMALL_KEY_FOREST_TEMPLE && item <= SMALL_KEY_GANONS_CASTLE)
        return true;
    return item == SMALL_KEY
        || item == GOLD_SKULLTULA_TOKEN
        || item == PROGRESSIVE_HOOKSHOT
        || item == PROGRESSIVE_STRENGTH_UPGRADE
        || item == PROGRESSIVE_WALLET
        || item == PROGRESSIVE_SCALE;
}

bool display_as_bottle_item(item_e item)
{
    return item >= BOTTLE_WITH_RED_POTION && item <= BOTTLE_WITH_POE;
}