#ifndef Z2_H
#define Z2_H
#include <stdint.h>
#include <n64.h>
#include "gu.h"

#define Z64_SCREEN_WIDTH      320
#define Z64_SCREEN_HEIGHT     240

#define Z64_SEG_PHYS          0x00
#define Z64_SEG_TITLE         0x01
#define Z64_SEG_SCENE         0x02
#define Z64_SEG_ROOM          0x03
#define Z64_SEG_KEEP          0x04
#define Z64_SEG_SKEEP         0x05
#define Z64_SEG_OBJ           0x06
#define Z64_SEG_ZIMG          0x0E
#define Z64_SEG_CIMG          0x0F

#define Z64_ETAB_LENGTH       0x0614

typedef struct
{
  int16_t x;
  int16_t y;
  int16_t z;
} z64_xyz_t;

typedef struct
{
  float x;
  float y;
  float z;
} z64_xyzf_t;

typedef uint16_t z64_angle_t;
typedef struct
{
  z64_angle_t x;
  z64_angle_t y;
  z64_angle_t z;
} z64_rot_t;

typedef struct
{
  /* index of z64_col_type in scene file */
  uint16_t    type;
  /* vertex indices, a and b are bitmasked for some reason */
  struct
  {
    uint16_t  unk_00_ : 3;
    uint16_t  va      : 13;
  };
  struct
  {
    uint16_t  unk_01_ : 3;
    uint16_t  vb      : 13;
  };
  uint16_t    vc;
  /* normal vector */
  z64_xyz_t   norm;
  /* plane distance from origin */
  int16_t     dist;
} z64_col_poly_t;

typedef struct
{
  struct
  {
    uint32_t  unk_00_     : 1;
    uint32_t  drop        : 1; /* link drops one unit into the floor */
    uint32_t  special     : 4;
    uint32_t  interaction : 5;
    uint32_t  unk_01_     : 3;
    uint32_t  behavior    : 5;
    uint32_t  exit        : 5;
    uint32_t  camera      : 8;
  } flags_1;                    /* 0x0000 */
  struct
  {
    uint32_t  pad_00_     : 4;
    uint32_t  wall_damage : 1;
    uint32_t  unk_00_     : 6;
    uint32_t  unk_01_     : 3;
    uint32_t  hookshot    : 1;
    uint32_t  echo        : 6;
    uint32_t  unk_02_     : 5;
    uint32_t  terrain     : 2;
    uint32_t  material    : 4;
  } flags_2;                    /* 0x0004 */
} z64_col_type_t;

typedef struct
{
  z64_xyz_t pos;
  z64_xyz_t rot;
  int16_t   fov;
  int16_t   unk_00_;
} z64_camera_params_t;

typedef struct
{
  uint16_t mode;
  uint16_t unk_01_;
  uint32_t seg_params; /* segment address of z64_camera_params_t */
} z64_camera_t;

typedef struct
{
  z64_xyz_t     pos;
  int16_t       width;
  int16_t       depth;
  struct
  {
    uint32_t    unk_00_ : 12;
    uint32_t    active  : 1;
    uint32_t    group   : 6; /* ? */
    uint32_t    unk_01_ : 5;
    uint32_t    camera  : 8;
  } flags;
} z64_col_water_t;

typedef struct
{
  z64_xyz_t         min;
  z64_xyz_t         max;
  uint16_t          n_vtx;
  z64_xyz_t        *vtx;
  uint16_t          n_poly;
  z64_col_poly_t   *poly;
  z64_col_type_t   *type;
  z64_camera_t     *camera;
  uint16_t          n_water;
  z64_col_water_t  *water;
} z64_col_hdr_t;

typedef enum
{
    Z2_ITEM_NULL = -1,
    Z2_ITEM_OCARINA,
    Z2_ITEM_HEROS_BOW,
    Z2_ITEM_FIRE_ARROW,
    Z2_ITEM_ICE_ARROW,
    Z2_ITEM_LIGHT_ARROW,
    Z2_ITEM_FAIRY_OCARINA,
    Z2_ITEM_BOMB,
    Z2_ITEM_BOMBCHU,
    Z2_ITEM_STICK,
    Z2_ITEM_NUT,
    Z2_ITEM_MAGIC_BEAN,
    Z2_ITEM_SLINGSHOT,
    Z2_ITEM_POWDER_KEG,
    Z2_ITEM_PICTOGRAPH_BOX,
    Z2_ITEM_LENS,
    Z2_ITEM_HOOKSHOT,
    Z2_ITEM_GREAT_FAIRY_SWORD,
    Z2_ITEM_OOT_HOOKSHOT,
    Z2_ITEM_BOTTLE,
    Z2_ITEM_RED_POTION,
    Z2_ITEM_GREEN_POTION,
    Z2_ITEM_BLUE_POTION,
    Z2_ITEM_FAIRY,
    Z2_ITEM_DEKU_PRINCESS,
    Z2_ITEM_MILK,
    Z2_ITEM_HALF_MILK,
    Z2_ITEM_FISH,
    Z2_ITEM_BUGS,
    Z2_ITEM_BLUE_FIRE,
    Z2_ITEM_POE,
    Z2_ITEM_BIG_POE,
    Z2_ITEM_SPRING_WATER,
    Z2_ITEM_HOT_SPRING_WATER,
    Z2_ITEM_ZORA_EGG,
    Z2_ITEM_GOLD_DUST,
    Z2_ITEM_MUSHROOM,
    Z2_ITEM_SEAHORSE,
    Z2_ITEM_CHATEAU_ROMANI,
    Z2_ITEM_HYLIAN_LOACH,
    Z2_ITEM_BOTTLE2,
    Z2_ITEM_MOONS_TEAR,
    Z2_ITEM_LAND_DEED,
    Z2_ITEM_SWAP_DEED,
    Z2_ITEM_MOUNTAIN_DEED,
    Z2_ITEM_OCEAN_DEED,
    Z2_ITEM_ROOM_KEY,
    Z2_ITEM_MAMA_LETTER,
    Z2_ITEM_KAFEI_LETTER,
    Z2_ITEM_PENDANT,
    Z2_ITEM_UNK_MAP,
    Z2_ITEM_BOW_FIRE_ARROW,
    Z2_MASK_DEKU = 0x32,
    Z2_MASK_GORON,
    Z2_MASK_ZORA,
    Z2_MASK_FIERCE_DEITY,
    Z2_MASK_MASK_OF_TRUTH,
    Z2_MASK_KAFEI,
    Z2_MASK_ALL_NIGHT,
    Z2_MASK_BUNNY_HOOD,
    Z2_MASK_KEATON,
    Z2_MASK_GARO,
    Z2_MASK_ROMANI,
    Z2_MASK_CIRCUS_LEADER,
    Z2_MASK_POSTMAN,
    Z2_MASK_COUPLE,
    Z2_MASK_GREAT_FAIRY,
    Z2_MASK_GIBDO,
    Z2_MASK_DON_GERO,
    Z2_MASK_KAMARO,
    Z2_MASK_CAPTAINSHAT,
    Z2_MASK_STONE,
    Z2_MASK_BREMEN,
    Z2_MASK_BLAST,
    Z2_MASK_SCENTS,
    Z2_MASK_GIANT,
    Z2_ITEM_BOW_ICE_ARROW,
    Z2_ITEM_BOW_LIGHT_ARROW,
    Z2_ITEM_KOKIRI_SWORD,
    Z2_ITEM_RAZOR_SWORD,
    Z2_ITEM_GILDED_SWORD,
    Z2_ITEM_DEITY_SWORD,
    Z2_ITEM_HERO_SHIELD,
    Z2_ITEM_MIRROR_SHIELD,
    Z2_ITEM_QUIVER_30,
    Z2_ITEM_QUIVER_40,
    Z2_ITEM_QUIVER_50,
    Z2_ITEM_BOMB_BAG_20,
    Z2_ITEM_BOMB_BAG_30,
    Z2_ITEM_BOMB_BAG_40,
    Z2_ITEM_MAGIC,
    Z2_ITEM_ADULTS_WALLET,
    Z2_ITEM_GIANTS_WALLET,
    Z2_ITEM_ODOLWAS_REMAINS,
    Z2_ITEM_GOHTS_REMAINS,
    Z2_ITEM_GYORGS_REMAINS,
    Z2_ITEM_TWINMOLDS_REMAINS,
    Z2_ITEM_BOMBERS_NOTEBOOK = 0x6D
} z2_item_t;

typedef enum
{
    Z2_SLOT_OCARINA,
    Z2_SLOT_BOW,
    Z2_SLOT_FIRE_ARROW,
    Z2_SLOT_ICE_ARROW,
    Z2_SLOT_LIGHT_ARROW,
    Z2_SLOT_QUEST_1,
    Z2_SLOT_BOMB,
    Z2_SLOT_BOMBCHU,
    Z2_SLOT_STICK,
    Z2_SLOT_NUT,
    Z2_SLOT_MAGIC_BEAN,
    Z2_SLOT_QUEST_2,
    Z2_SLOT_POWDER_KEG,
    Z2_SLOT_PICTOGRAPH_BOX,
    Z2_SLOT_LENS,
    Z2_SLOT_HOOKSHOT,
    Z2_SLOT_GREAT_FAIRY_SWORD,
    Z2_SLOT_QUEST_3,
    Z2_SLOT_BOTTLE_1,
    Z2_SLOT_BOTTLE_2,
    Z2_SLOT_BOTTLE_3,
    Z2_SLOT_BOTTLE_4,
    Z2_SLOT_BOTTLE_5,
    Z2_SLOT_BOTTLE_6
} z2_slot_t;

typedef enum {
    Z2_SLOT_POSTMAN,
    Z2_SLOT_ALL_NIGHT,
    Z2_SLOT_BLAST,
    Z2_SLOT_STONE,
    Z2_SLOT_GREAT_FAIRY,
    Z2_SLOT_DEKU,
    Z2_SLOT_KEATON,
    Z2_SLOT_BREMEN,
    Z2_SLOT_BUNNY_HOOD,
    Z2_SLOT_DON_GERO,
    Z2_SLOT_SCENTS,
    Z2_SLOT_GORON,
    Z2_SLOT_ROMANI,
    Z2_SLOT_CIRCUS_LEADER,
    Z2_SLOT_KAFEI,
    Z2_SLOT_COUPLE,
    Z2_SLOT_MASK_OF_TRUTH,
    Z2_SLOT_ZORA,
    Z2_SLOT_KAMARO,
    Z2_SLOT_GIBDO,
    Z2_SLOT_GARO,
    Z2_SLOT_CAPTAIN,
    Z2_SLOT_GIANT,
    Z2_SLOT_FIERCE_DEITY
} z2_mask_slot_t;

typedef enum
{
  Z64_ITEMBTN_B,
  Z64_ITEMBTN_CL,
  Z64_ITEMBTN_CD,
  Z64_ITEMBTN_CR,
} z64_itembtn_t;

typedef struct
{
      char      unk_00_[0x006E];        /* 0x0000 */
      int16_t   run_speed_limit;        /* 0x006E */
      char      unk_01_[0x0004];        /* 0x0070 */
      int16_t   run_speed_max_anim;     /* 0x0074 */
      char      unk_02_[0x0026];        /* 0x0076 */
      int16_t   gravity;                /* 0x009C */
      char      unk_03_[0x0072];        /* 0x009E */
      uint16_t  update_rate;            /* 0x0110 */
      char      unk_04_[0x0022];        /* 0x0112 */
      int16_t   override_aspect;        /* 0x0134 */
      uint16_t  aspect_width;           /* 0x0136 */
      uint16_t  aspect_height;          /* 0x0138 */
      char      unk_05_[0x0050];        /* 0x013A */
      int16_t   game_playing;           /* 0x018A */
      char      unk_06_[0x03B8];        /* 0x018C */
      uint16_t  c_up_icon_x;            /* 0x0544 */
      uint16_t  c_up_icon_y;            /* 0x0546 */
      char      unk_07_[0x021C];        /* 0x0548 */
      uint16_t  game_freeze;            /* 0x0764 */
      char      unk_08_[0x002E];        /* 0x0766 */
      uint16_t  magic_fill_r;           /* 0x0794 */
      uint16_t  magic_fill_g;           /* 0x0796 */
      uint16_t  magic_fill_b;           /* 0x0798 */
      char      unk_09_[0x004A];        /* 0x079A */
      uint16_t  c_button_r;             /* 0x07E4 */
      uint16_t  c_button_g;             /* 0x07E6 */
      uint16_t  c_button_b;             /* 0x07E8 */
      uint16_t  b_button_r;             /* 0x07EA */
      uint16_t  b_button_g;             /* 0x07EC */
      uint16_t  b_button_b;             /* 0x07EE */
      char      unk_0A_[0x0004];        /* 0x07F0 */
      qs510_t   start_icon_dd;          /* 0x07F4 */
      int16_t   start_icon_scale;       /* 0x07F6 */
      char      unk_0B_[0x0006];        /* 0x07F8 */
      uint16_t  start_icon_y;           /* 0x07FE */
      char      unk_0C_[0x0002];        /* 0x0800 */
      uint16_t  start_icon_x;           /* 0x0802 */
      char      unk_0D_[0x000C];        /* 0x0804 */
      uint16_t  c_up_button_x;          /* 0x0810 */
      uint16_t  c_up_button_y;          /* 0x0812 */
      char      unk_0E_[0x0008];        /* 0x0814 */
      uint16_t  start_button_x;         /* 0x081C */
      uint16_t  start_button_y;         /* 0x081E */
      uint16_t  item_button_x[4];       /* 0x0820 */
      uint16_t  item_button_y[4];       /* 0x0828 */
      qs510_t   item_button_dd[4];      /* 0x0830 */
      uint16_t  item_icon_x[4];         /* 0x0838 */
      uint16_t  item_icon_y[4];         /* 0x0840 */
      qs510_t   item_icon_dd[4];        /* 0x0848 */
      char      unk_0F_[0x0264];        /* 0x0850 */
      uint16_t  a_button_y;             /* 0x0AB4 */
      uint16_t  a_button_x;             /* 0x0AB6 */
      char      unk_10_[0x0002];        /* 0x0AB8 */
      uint16_t  a_button_icon_y;        /* 0x0ABA */
      uint16_t  a_button_icon_x;        /* 0x0ABC */
      char      unk_11_[0x0002];        /* 0x0ABE */
      uint16_t  a_button_r;             /* 0x0AC0 */
      uint16_t  a_button_g;             /* 0x0AC2 */
      uint16_t  a_button_b;             /* 0x0AC4 */
      char      unk_12_[0x0030];        /* 0x0AC6 */
      uint16_t  magic_bar_x;            /* 0x0AF6 */
      uint16_t  magic_bar_y;            /* 0x0AF8 */
      uint16_t  magic_fill_x;           /* 0x0AFA */
      char      unk_13_[0x02D6];        /* 0x0AFC */
      int16_t   minimap_disabled;       /* 0x0DD2 */
      char      unk_14_[0x01C0];        /* 0x0DD4 */
      uint16_t  item_ammo_x[4];         /* 0x0F94 */
      uint16_t  item_ammo_y[4];         /* 0x0F9C */
      char      unk_15_[0x0008];        /* 0x0FA4 */
      uint16_t  item_icon_space[4];     /* 0x0FAC */
      uint16_t  item_button_space[4];   /* 0x0FB4 */
                                        /* 0x0FBC */
} z64_gameinfo_t;

typedef struct /* z2_file_t */
{
    int32_t         entrance_index;           /* 0x0000 */
    int8_t          player_mask;              /* 0x0004 */
    int8_t          opening_flag;             /* 0x0005 */
    int8_t          button_mash_timer;        /* 0x0006 */
    char            unk_0x0007;               /* 0x0007 */
    int32_t         cutscene_index;           /* 0x0008 */
    uint16_t        day_time;                 /* 0x000C */
    uint16_t        owl_statue;               /* 0x000E */
    int32_t         night_flag;               /* 0x0010 */
    int32_t         time_passage_rate;        /* 0x0014 */
    int32_t         current_day;              /* 0x0018 */
    int32_t         total_day;                /* 0x001C */
    int8_t          player_character;         /* 0x0020 */
    int8_t          spring_flag;              /* 0x0021 */
    int8_t          tatl_flag;                /* 0x0022 */
    int8_t          owl_save_flag;            /* 0x0023 */
    char            id[6];                    /* 0x0024 */
    int16_t         savect;                   /* 0x002A */
    char            file_name[0x08];          /* 0x002C */
    int16_t         life_max;                 /* 0x0034 */
    int16_t         life;                     /* 0x0036 */
    uint8_t         magic_max;                /* 0x0038 */
    uint8_t         magic;                    /* 0x0039 */
    uint16_t        rupees;                   /* 0x003A */
    uint16_t        unk_0x003C;               /* 0x003C */
    uint16_t        navi_timer;               /* 0x003E */
    uint8_t         magic_acquired;           /* 0x0040 */
    uint8_t         magic_ability;            /* 0x0041 */
    int16_t         life_ability;             /* 0x0042 */
    int16_t         razor_sword_durability;   /* 0x0044 */
    union {
        struct {
            uint16_t hidden_owl         : 1;
            uint16_t                    : 4;
            uint16_t dungeon_entrance   : 1;
            uint16_t stone_tower        : 1;
            uint16_t ikana_canyon;      : 1;
            uint16_t southern_swap      : 1;
            uint16_t woodfall           : 1;
            uint16_t milk_road          : 1;
            uint16_t clock_town         : 1;
            uint16_t mountain_village   : 1;
            uint16_t snowhead           : 1;
            uint16_t zora_cape          : 1;
            uint16_t great_bay          : 1;
        };
        uint16_t    owl_hit_flags;            /* 0x0046 */
    };
    int16_t         unk_0x0048;               /* 0x0048 */
    int16_t         unk_0x004A;               /* 0x004A */
    struct 
    {
        int8_t      b;
        int8_t      c_left;
        int8_t      c_down;
        int8_t      c_right;
    } form_button_items[4];                   /* 0x004C */ //human, goron, zora, deku
    struct
    {
        int8_t      b;
        int8_t      c_left;
        int8_t      c_down;
        int8_t      c_right;
    } form_button_slot[4];                    /* 0x005C */
    union
    {
        uint16_t    equips;                   /* 0x006C */
        struct
        {
            uint16_t    equip_boots : 4;
            uint16_t    equip_tunic : 4;
            uint16_t    equip_shield : 4;
            uint16_t    equip_sword : 4;
        };
    };
    char            unk_0x006E_[0x0002];      /* 0x006E */
    union
    {
        int8_t      items_all[48];
        struct 
        {
            int8_t          items[24];        /* 0x0070 */
            int8_t          masks[24];        /* 0x0088 */
        };
    };
    int8_t          ammo[24];                 /* 0x00A0 */
    union
    {
        struct
        {
            uint32_t                        : 9;    // & 0xFF800000 >> 0x17
            uint32_t nut_upgrade            : 3;    // & 0x00700000 >> 0x14
            uint32_t stick_upgade           : 3;    // & 0x000E0000 >> 0x11
            uint32_t                        : 2;    // & 0x00018000 >> 0x0F
            uint32_t wallet_upgrade         : 3;    // & 0x00007000 >> 0x0C
            uint32_t                        : 6;    // & 0x00000FC0 >> 0x06
            uint32_t bomb_bag               : 3;    // & 0x00000038 >> 0x03
            uint32_t quiver                 : 3;    // & 0x00000007 >> 0x00
        }; //FIXME
        uint32_t    equipment_upgrades;        /* 0x00B8 */
    };
    union
    {
        uint32_t      quest_status;            /* 0x00BC */
        struct
        {
            uint32_t heart_piece            : 4;
            uint32_t                        : 3;
            uint32_t lullaby_intro          : 1;
            uint32_t                        : 5;
            uint32_t bombers_notebook       : 1;
            uint32_t suns_song              : 1;
            uint32_t song_of_storms         : 1;
            uint32_t song_of_soaring        : 1;
            uint32_t eponas_song            : 1;
            uint32_t song_of_healing        : 1;
            uint32_t song_of_time           : 1;
            uint32_t sarias_song            : 1;
            uint32_t oath_to_order          : 1;
            uint32_t elegy_of_emptiness     : 1;
            uint32_t new_wave_bossa_nova    : 1;
            uint32_t goron_lullaby          : 1;
            uint32_t sonata_of_awakening    : 1;
            uint32_t                        : 2;
            uint32_t twinmolds_remains      : 1;
            uint32_t gyorgs_remains         : 1;
            uint32_t gohts_remains          : 1;
            uint32_t odolwas_remains        : 1;
        };
    };
    union
    {
        uint8_t       items;
        struct
        {
            uint8_t : 5;
            uint8_t     map : 1;
            uint8_t     compass : 1;
            uint8_t     boss_key : 1;
        };
    }               dungeon_items[10];        /* 0x00C0 */
    int8_t          dungeon_keys[9];          /* 0x00CA */
    uint8_t         defense_hearts;           /* 0x00D3 */
    uint8_t         stray_fairies[10];        /* 0x00D4 */
    char            form_name[6][3];          /* 0x00DE */
    int16_t         unk_0x00F6;               /* 0x00F6 */
    struct
    {
        uint32_t      chest;
        uint32_t      switch_1;
        uint32_t      switch_2;
        uint32_t      clear;
        uint32_t      collect;
        uint32_t      unk_0x14;
        uint32_t      unk_0x18;
    }               scene_flags[120];         /* 0x00F8 */
    char            unk_0x0E18[0x62];         /* 0x0E18 */
    char            unk_0x0E7A[0x2E26];       /* 0x0E7A */
    
    int32_t         file_index;               /* 0x3CA0 */ 
} z2_file_t;

extern z2_file_t z2_file;
asm(".equ z2_file, 0x801EF670");

typedef struct
{
  uint32_t seg[16];
} z64_stab_t;

typedef struct
{
  uint8_t       scene_index;
  uint8_t       entrance_index;
  union
  {
    uint16_t    variable;
    struct
    {
      uint16_t  transition_out  : 7;
      uint16_t  transition_in   : 7;
      uint16_t  unk_00_         : 1;
      uint16_t  continue_music  : 1;
    };
  };
} z64_entrance_t;

typedef struct
{
  uint32_t scene_vrom_start;
  uint32_t scene_vrom_end;
  uint32_t title_vrom_start;
  uint32_t title_vrom_end;
  char     unk_00_;
  uint8_t  scene_config;
  char     unk_01_;
  char     padding_00_;
} z64_scene_table_t;

typedef struct
{
  uint32_t        size;                 /* 0x0000 */
  Gfx            *buf;                  /* 0x0004 */
  Gfx            *p;                    /* 0x0008 */
  Gfx            *d;                    /* 0x000C */
} z64_disp_buf_t;

typedef struct
{
  Gfx            *poly_opa_w;           /* 0x0000 */
  Gfx            *poly_xlu_w;           /* 0x0004 */
  char            unk_00_[0x0008];      /* 0x0008 */
  Gfx            *overlay_w;            /* 0x0010 */
  char            unk_01_[0x00A4];      /* 0x0014 */
  Gfx            *work_c;               /* 0x00B8 */
  uint32_t        work_c_size;          /* 0x00BC */
  char            unk_02_[0x00E0];      /* 0x00C0 */
  Gfx            *work_w;               /* 0x01A0 */
  z64_disp_buf_t  work;                 /* 0x01A4 */
  char            unk_03_[0x00E4];      /* 0x01B4 */
  z64_disp_buf_t  overlay;              /* 0x0298 */
  z64_disp_buf_t  poly_opa;             /* 0x02A8 */
  z64_disp_buf_t  poly_xlu;             /* 0x02B8 */
  uint32_t        frame_count_1;        /* 0x02C8 */
  void           *frame_buffer;         /* 0x02CC */
  char            unk_04_[0x0008];      /* 0x02D0 */
  uint32_t        frame_count_2;        /* 0x02D8 */
                                        /* 0x02DC */
} z2_gfx_t;

typedef struct {
    union {
        struct {
            uint16_t    a   : 1;
            uint16_t    b   : 1;
            uint16_t    z   : 1;
            uint16_t    s   : 1;
            uint16_t    du  : 1;
            uint16_t    dd  : 1;
            uint16_t    dl  : 1;
            uint16_t    dr  : 1;
            uint16_t        : 2;
            uint16_t    l   : 1;
            uint16_t    r   : 1;
            uint16_t    cu  : 1;
            uint16_t    cd  : 1;
            uint16_t    cl  : 1;
            uint16_t    cr  : 1;
        };
        uint16_t        pad;                // 0x00
    };
    int8_t              x;                  // 0x02
    int8_t              y;                  // 0x03
} z64_controller_t;                         // 0x04

typedef struct z2_actor_s z2_actor_t;
struct z2_actor_s
{
  int16_t         id;               /* 0x0000 */
  uint8_t         type;             /* 0x0002 */
  int8_t          room;             /* 0x0003 */
  uint32_t        flags;            /* 0x0004 */
  z64_xyzf_t      pos_1;            /* 0x0008 */
  z64_rot_t       rot_init;         /* 0x0014 */
  char            unk_01_[0x0002];  /* 0x001A */
  uint16_t        variable;         /* 0x001C */
  uint8_t         alloc_index;      /* 0x001E */
  char            unk_02_;          /* 0x001F */
  uint16_t        sound_effect;     /* 0x0020 */
  char            unk_03_[0x0002];  /* 0x0022 */
  z64_xyzf_t      pos_2;            /* 0x0024 */
  z64_rot_t       rot_dir;          /* 0x0030 */
  char            unk_0x36[0x0002]; /* 0x0036 */
  int8_t          unk_0x38;         /* 0x0038 */
  uint8_t         unk_0x39;         /* 0x0039 */
  char            unk_0x3A[0x002];  /* 0x003A */
  z64_xyzf_t      pos_3;            /* 0x003C */ 
  z64_rot_t       rot_1;            /* 0x0048 */ 
  char            unk_06_[0x0002];  /* 0x004E */ //padding?
  uint32_t        unk_0x50;         /* 0x0050 */
  float           unk_0x54;         /* 0x0054 */
  z64_xyzf_t      scale;            /* 0x0058 */
  z64_xyzf_t      vel_1;            /* 0x0064 */
  float           xz_speed;         /* 0x0070 */
  float           gravity;          /* 0x0074 */
  float           min_vel_y;        /* 0x0078 */

  /* struct bgcheck common */
  z64_col_poly_t *wall_poly;                /* 0x007C */
  z64_col_poly_t *floor_poly;               /* 0x0080 */
  uint8_t         wall_poly_source;         /* 0x0084 */
  uint8_t         floor_poly_source;        /* 0x0085 */
  int16_t         wall_rot;                 /* 0x0086 */
  float           floor_height;             /* 0x0088 */ //maybe?
  float           water_surface_dist;       /* 0x008C */
  uint16_t        bgcheck_flags;            /* 0x0090 */
  int16_t         unk_0x92_rot;             /* 0x0092 */
  float           unk_0x94;                 /* 0x0094 */
  float           dist_from_link_xz;        /* 0x0098 */
  float           dist_from_link_y;         /* 0x009C */

  /* struct collision_check common */
  void           *damage_table;     /* 0x00A0 */
  z64_xyzf_t      vel_2;            /* 0x00A4 */
  char            unk_0C_[0x0006];  /* 0x00B0 */
  uint8_t         mass;             /* 0x00B6 */
  uint8_t         health;           /* 0x00B7 */
  uint8_t         damage;           /* 0x00B8 */
  uint8_t         damage_effect;    /* 0x00B9 */
  uint8_t         impact_effect;    /* 0x00BA */
  uint8_t         unk_0xBB;         /* 0x00BB */

  /* struct start */
  z64_rot_t       rot_2;            /* 0x00BC */
  char            unk_0F_[0x0002];  /* 0x00C2 */
  float           unk_0xC4;         /* 0x00C4 */
  void           *draw_drop_shadow; /* 0x00C8 */
  float           unk_0xCC;         /* 0x00CC */
  uint8_t         unk_0xD0;         /* 0x00D0 */
  char            pad_0xD1_[0x0003];/* 0x00D1 */
  /* struct end */

  z64_xyzf_t      unk_0xD4;         /* 0x00D4 */
  z64_xyzf_t      unk_0xE0;         /* 0x00E0 */
  z64_xyzf_t      unk_0xEC;         /* 0x00EC */
  float           unk_0xF8;         /* 0x00F8 */
  float           unk_0xFC;         /* 0x00FC */
  float           unk_0x100;        /* 0x0100 */
  float           unk_0x104;        /* 0x0104 */
  z64_xyzf_t      pos_4;            /* 0x0108 */
  uint16_t        unk_10_;          /* 0x0114 */
  uint16_t        text_id;          /* 0x0116 */
  int16_t         frozen;           /* 0x0118 */
  char            unk_11_[0x0003];  /* 0x011A */
  uint8_t         active;           /* 0x011D */
  char            unk_0x11E;        /* 0x011E */
  uint8_t         tatl_enemy_text_id;/*0x011F */
  z2_actor_t     *attached_a;       /* 0x0120 */
  z2_actor_t     *attached_b;       /* 0x0124 */
  z2_actor_t     *prev;             /* 0x0128 */
  z2_actor_t     *next;             /* 0x012C */
  void           *ctor;             /* 0x0130 */
  void           *dtor;             /* 0x0134 */
  void           *main_proc;        /* 0x0138 */
  void           *draw_proc;        /* 0x013C */
  void           *code_entry;       /* 0x0140 */
                                    /* 0x0144 */
};

typedef struct
{
  z2_actor_t   common;               /* 0x0000 */
  char         unk_00_[0x02E8];      /* 0x013C */
  int8_t       incoming_item_id;     /* 0x0424 */
  char         unk_01_[0x0003];      /* 0x0425 */
  z2_actor_t  *incoming_item_actor;  /* 0x0428 */
  char         unk_02_[0x0008];      /* 0x042C */
  uint8_t      action;               /* 0x0434 */
  char         unk_03_[0x0237];      /* 0x0435 */
  uint32_t     state_flags_1;        /* 0x066C */
  uint32_t     state_flags_2;        /* 0x0670 */
  char         unk_04_[0x01B4];      /* 0x0674 */
  float        linear_vel;           /* 0x0828 */
  char         unk_05_[0x0002];      /* 0x082C */
  uint16_t     target_yaw;           /* 0x082E */
  char         unk_06_[0x0003];      /* 0x0830 */
  int8_t       sword_state;          /* 0x0833 */
  char         unk_07_[0x0050];      /* 0x0834 */
  int16_t      drop_y;               /* 0x0884 */
  int16_t      drop_distance;        /* 0x0886 */
                                     /* 0x0888 */
} z64_link_t;

typedef struct 
{
    z2_actor_t      common;           /* 0x0000 */
} z2_link_t;

typedef struct
{
  z64_controller_t  raw;
  uint16_t          unk_00_;
  z64_controller_t  raw_prev;
  uint16_t          unk_01_;
  uint16_t          pad_pressed;
  int8_t            x_diff;
  int8_t            y_diff;
  char              unk_02_[0x0002];
  uint16_t          pad_released;
  int8_t            adjusted_x;
  int8_t            adjusted_y;
  char              unk_03_[0x0002];
} z64_input_t;

/* context base */
typedef struct
{
  z2_gfx_t       *gfx;                    /* 0x0000 */
  void           *state_main;             /* 0x0004 */
  void           *state_dtor;             /* 0x0008 */
  void           *next_ctor;              /* 0x000C */
  uint32_t        next_size;              /* 0x0010 */
  z64_input_t     input[4];               /* 0x0014 */
  uint32_t        state_heap_size;        /* 0x0074 */
  void           *state_heap;             /* 0x0078 */
  void           *heap_start;             /* 0x007C */
  void           *heap_end;               /* 0x0080 */
  void           *state_heap_node;        /* 0x0084 */
  char            unk_00_[0x0010];        /* 0x0088 */
  int32_t         state_continue;         /* 0x0098 */
  int32_t         state_frames;           /* 0x009C */
  uint32_t        unk_01_;                /* 0x00A0 */
                                          /* 0x00A4 */
} z64_ctxt_t;

typedef struct
{
    int16_t           poly_idx;                 /* 0x0000 */
    uint16_t          list_next;                /* 0x0002 */
                                                /* 0x0004 */
} z64_col_list_t;


typedef struct
{
    uint16_t          floor_list_idx;           /* 0x0000 */
    uint16_t          wall_list_idx;            /* 0x0002 */
    uint16_t          ceil_list_idx;            /* 0x0004 */
                                                /* 0x0006 */
} z64_col_lut_t;

typedef struct 
{
    z2_actor_t       *actor;                    /* 0x0000 */
    z64_col_hdr_t    *col_hdr;                  /* 0x0004 */
    uint16_t          unk_0x08;                 /* 0x0008 */
    uint16_t          unk_0x0A;                 /* 0x000A */
    uint16_t          unk_0x0C;                 /* 0x000C */
    int16_t           unk_0x0E;                 /* 0x000E */ //number of polys?
    int16_t           unk_0x10;                 /* 0x0010 */
    z64_xyzf_t        scale_1;                  /* 0x0014 */
    z64_rot_t         rot_1;                    /* 0x0020 */
    z64_xyzf_t        pos_1;                    /* 0x0028 */
    z64_xyzf_t        scale_2;                  /* 0x0034 */
    z64_rot_t         rot_2;                    /* 0x0040 */
    z64_xyzf_t        pos_2;                    /* 0x0048 */
    int16_t           unk_0x54;                 /* 0x0054 */
    int16_t           unk_0x56;                 /* 0x0056 */
    int16_t           unk_0x58;                 /* 0x0058 */
    int16_t           unk_0x5A;                 /* 0x005A */
    char              unk_0x5C[0x8];            /* 0x005C */
                                                /* 0x0064 */
} z2_col_chk_actor_t;

typedef struct /* z64_col_ctxt_t */
{
    /* static collision stuff */
    z64_col_hdr_t      *col_hdr;                  /* 0x0000 */
    z64_xyzf_t          bbox_min;                 /* 0x0004 */
    z64_xyzf_t          bbox_max;                 /* 0x0010 */
    int32_t             n_sect_x;                 /* 0x001C */
    int32_t             n_sect_y;                 /* 0x0020 */
    int32_t             n_sect_z;                 /* 0x0024 */
    z64_xyzf_t          sect_size;                /* 0x0028 */
    z64_xyzf_t          sect_inv;                 /* 0x0034 */
    z64_col_lut_t      *stc_lut;                  /* 0x0040 */
    uint16_t            stc_list_max;             /* 0x0044 */
    uint16_t            stc_list_pos;             /* 0x0046 */
    z64_col_list_t     *stc_list;                 /* 0x0048 */
    uint8_t            *stc_check;                /* 0x004C */

    /* bg actor collision struct start */
    int8_t              unk_0x0050;               /* 0x0050 */
    z2_col_chk_actor_t  actors[50];               /* 0x0054 */
    uint16_t            actor_loaded[50];         /* 0x13DC */
    /* dynamic collision stuff */
    z64_col_poly_t     *dyn_poly;                 /* 0x1440 */
    z64_xyz_t          *dyn_vtx;                  /* 0x1444 */
    int32_t             unk_0x1448;               /* 0x1448 */
    void               *unk_0x144C;               /* 0x144C */
    /* struct */
    struct
    {
        z64_col_list_t   *list;                 /* 0x1450 */
        int32_t           count;                /* 0x1454 */
        int32_t           max;                  /* 0x1458 */
    } dyn;
    /* bg actor collision struct end */
    uint32_t            dyn_list_max;             /* 0x145C */
    uint32_t            dyn_poly_max;             /* 0x1460 */
    uint32_t            dyn_vtx_max;              /* 0x1464 */
    uint32_t            mem_size;                 /* 0x1468 */
    uint32_t            unk_0x146C;               /* 0x146C */
                                                  /* 0x1470 */
} z2_col_ctxt_t;



typedef struct
{
  /* file loading params */
  uint32_t      vrom_addr;
  void         *dram_addr;
  uint32_t      size;
  /* unknown, seem to be unused */
  void         *unk_00_;
  uint32_t      unk_01_;
  uint32_t      unk_02_;
  /* completion notification params */
  OSMesgQueue  *notify_queue;
  OSMesg        notify_message;
} z64_getfile_t;

/* object structs */
typedef struct
{
  int16_t       id;
  void         *data;
  z64_getfile_t getfile;
  OSMesgQueue   load_mq;
  OSMesg        load_m;
} z64_mem_obj_t;

typedef struct
{
  void         *obj_space_start;
  void         *obj_space_end;
  uint8_t       n_objects;
  char          unk_00_;
  uint8_t       keep_index;
  uint8_t       skeep_index;
  z64_mem_obj_t objects[19];
} z64_obj_ctxt_t;

typedef struct
{
    char              unk_00_[0x0128];          /* 0x0000 */
    void             *icon_item;                /* 0x0128 */
    void             *icon_item_24;             /* 0x012C */
    void             *icon_item_s;              /* 0x0130 */
    void             *icon_item_lang;           /* 0x0134 */
    void             *name_texture;             /* 0x0138 */
    void             *p13C;                     /* 0x013C */
    char              unk_01_[0x0094];          /* 0x0140 */
    uint16_t          state;                    /* 0x01D4 */
    char              unk_02_[0x000E];          /* 0x01D6 */
    uint16_t          changing;                 /* 0x01E4 */
    uint16_t          screen_prev_idx;          /* 0x01E6 */
    uint16_t          screen_idx;               /* 0x01E8 */
    char              unk_03_[0x002E];          /* 0x01EA */
    int16_t           item_cursor;              /* 0x0218 */
    char              unk_04_[0x0002];          /* 0x021A */
    int16_t           quest_cursor;             /* 0x021C */
    int16_t           equip_cursor;             /* 0x021E */
    int16_t           map_cursor;               /* 0x0220 */
    int16_t           item_x;                   /* 0x0222 */
    char              unk_05_[0x0004];          /* 0x0224 */
    int16_t           equipment_x;              /* 0x0228 */
    char              unk_06_[0x0002];          /* 0x022A */
    int16_t           item_y;                   /* 0x022C */
    char              unk_07_[0x0004];          /* 0x022E */
    int16_t           equipment_y;              /* 0x0232 */
    char              unk_08_[0x0004];          /* 0x0234 */
    int16_t           cursor_pos;               /* 0x0238 */
    char              unk_09_[0x0002];          /* 0x023A */
    int16_t           item_id;                  /* 0x023C */
    int16_t           item_item;                /* 0x023E */
    int16_t           map_item;                 /* 0x0240 */
    int16_t           quest_item;               /* 0x0242 */
    int16_t           equip_item;               /* 0x0244 */
    char              unk_0A_[0x0004];          /* 0x0246 */
    int16_t           quest_hilite;             /* 0x024A */
    char              unk_0B_[0x0018];          /* 0x024C */
    int16_t           quest_song;               /* 0x0264 */
    char              unk_0C_[0x0016];          /* 0x0266 */
                                                /* unknown structure */
    char              s27C[0x0038];             /* 0x027C */
                                                /* 0x02B4 */
} z64_pause_ctxt_t;

typedef struct
{
  uint32_t vrom_start;
  uint32_t vrom_end;
} z64_object_table_t;

/* lighting structs */
typedef struct
{
  int8_t  dir[3];
  uint8_t col[3];
} z64_light1_t;

typedef struct
{
  int16_t x;
  int16_t y;
  int16_t z;
  uint8_t col[3];
  int16_t intensity;
} z64_light2_t;

typedef union
{
  z64_light1_t  light1;
  z64_light2_t  light2;
} z64_lightn_t;

typedef struct
{
  uint8_t       type;
  z64_lightn_t  lightn;
} z64_light_t;

typedef struct z64_light_node_s z64_light_node_t;
struct z64_light_node_s
{
  z64_light_t      *light;
  z64_light_node_t *prev;
  z64_light_node_t *next;
};

typedef struct
{
  z64_light_node_t *light_list;
  uint8_t           ambient[3];
  uint8_t           fog[3];
  int16_t           fog_position;
  int16_t           draw_distance;
} z64_lighting_t;

typedef struct
{
  int8_t  numlights;
  Lightsn lites;
} z64_gbi_lights_t;

typedef void (*z64_light_handler_t)(z64_gbi_lights_t*, z64_lightn_t*,
                                    z2_actor_t*);

typedef struct /* z2_view_t */
{
    char            view_magic[4];          /* 0x0000 */
    z2_gfx_t       *gfx;                    /* 0x0004 */
    struct
    {
        uint32_t        top;                /* 0x0008 */
        uint32_t        bottom;             /* 0x000C */
        uint32_t        left;               /* 0x0010 */
        uint32_t        right;              /* 0x0014 */
    } screen;
    float           camera_distance;        /* 0x0018 */
    float           fog_distance;           /* 0x001C */
    float           z_distance;             /* 0x0020 */
    char            unk_0x24[0x004];        /* 0x0024 */
    z64_xyzf_t      unk_0x28;               /* 0x0028 */
    z64_xyzf_t      unk_0x34;
    z64_xyzf_t      unk_0x40;
    Vp              viewport_movemem;       /* 0x0050 */
    Mtx             unk_mtx_0x60;
    Mtx             unk_mtx_0xA0;
    char            unk_0x00E0[0x40];       /* 0x00E0 */
    Mtx            *unk_mtx_0x60_task;      /* 0x0120 */
    Mtx            *unk_mtx_0xA0_task;      /* 0x0124 */
    float           unk_0x128;          
    float           unk_0x12C;          
    float           unk_0x130;          
    float           unk_0x134;          
    float           unk_0x138;          
    float           unk_0x13C;          
    float           unk_0x140;      
    float           unk_0x144;
    float           unk_0x148;
    char            unk_0x14C[0x10];

    uint16_t        perspnorm_scale;        /* 0x015C */
    uint32_t        unk_0x160;
    uint32_t        unk_0x164;
                                            /* 0x0168 */
} z2_view_t;

typedef struct /* z2_camera_t */
{
    union
    {
        struct 
        {
            z64_xyzf_t unk_0x00;
            struct /* 0x24 */
            {
                float       unk_0x00;
                float       unk_0x04; 
                int16_t     unk_0x08;
                int16_t     unk_0x0A; 
                int16_t     unk_0x0C;
                float       unk_0x10;
            };

        } t1;
        struct
        {
            uint16_t unk_0x00;
        } t2;
        char    unk_0x00[0x50];
    };
        /* 0x0000 */

    z64_xyzf_t      unk_0x50;
    z64_xyzf_t      unk_0x5C;
    z64_xyzf_t      unk_0x68;

    char            unk_0x74[0x0C];

    z64_xyzf_t      unk_0x80;
    z64_ctxt_t     *game;                   /* 0x008C */
    z2_actor_t     *focus;                  /* 0x0090 */
    z64_xyzf_t      focus_pos;              /* 0x0094 */
    uint32_t        unk_0xA0;
    uint32_t        unk_0xA4;
    uint32_t        unk_0xA8;
    char            unk_0xAC[0xCC];
                                            /* 0x0178 */
} z2_camera_t;

typedef struct /* z2_actor_ctxt_t */
{
    /* game_t 0x1CA0 */
    uint8_t         unk_0x0000;             /* 0x0000 */
    uint8_t         unk_0x0001;             /* 0x0001 */
    uint8_t         unk_0x0002;             /* 0x0002 */
    uint8_t         unk_0x0003;             /* 0x0003 */
    int8_t          unk_0x0004;             /* 0x0004 */
    uint8_t         unk_0x0005;             /* 0x0005 */
    char            unk_0x0006[5];          /* 0x0006 */
    int8_t          unk_0x000B;             /* 0x000B */
    char            unk_0x000C[2];          /* 0x000C */
    uint8_t         n_actors_loaded;        /* 0x000E */
    uint8_t         unk_0x000F;             /* 0x000F */
    struct
    {
        int32_t     count;                  /* 0x0000 */
        z2_actor_t *first;                  /* 0x0004 */
        int32_t     unk;                    /* 0x0008 */
                                            /* 0x000C */

    }               actor_list[16];         /* 0x0010 */
    char            unk_0x00D0[0x50];       /* 0x00D0 */
    struct
    {
        MtxF            unk_0x0120;             /* 0x0120 */
        float           unk_0x0160;             /* 0x0160 */
        float           unk_0x0164;             /* 0x0164 */
        int16_t         unk_0x0168;             /* 0x0168 */
        uint8_t         unk_0x016A;             /* 0x016A */
        uint8_t         unk_0x016B;             /* 0x016B */
        int8_t          unk_0x016C;             /* 0x016C */
        struct
        {
            float           unk_0x00;             
            float           unk_0x04;
            float           unk_0x08;
            float           unk_0x0C;
            int32_t         unk_0x10;
                                            /* 0x0014 */

        }               unk_0x0170[3];      /* 0x0170 */
        int32_t         unk_0x01AC;         /* 0x01AC */
        int32_t         unk_0x01B0;         /* 0x01B0 */
        int32_t         unk_0x01B4;         /* 0x01B4 */
    };
    int32_t         switch_1;           /* 0x01B8 */ //perm
    int32_t         switch_2;           /* 0x01BC */ //perm
    int32_t         switch_3;           /* 0x01C0 */
    int32_t         switch_4;           /* 0x01C4 */
    int32_t         chest;              /* 0x01C8 */
    int32_t         clear;              /* 0x01CC */
    int32_t         unk_0x01D0;         /* 0x01D0 */
    int32_t         collectible_1;      /* 0x01D4 */ //Perm
    int32_t         collectible_2;      /* 0x01D8 */
    int32_t         collectible_3;      /* 0x01DC */
    int32_t         collectible_4;      /* 0x01E0 */
    struct
    {
        char        unk_0x00[0x0A];
        int8_t      unk_0x0A;
        int8_t      unk_0x0B;
        int16_t     unk_0x0C;
        int16_t     unk_0x0E;
    }   unk_0x01E4;                     /* 0x01E4 */
    int8_t          unk_0x01F4;
    uint8_t         unk_0x01F5;
    float           unk_0x01F8;
    char            unk_0x01FC[0x54];

    int32_t         unk_0x0250;
    char            unk_0x0254[0x14];
    uint8_t         unk_0x0268;         /* 0x0268 */
    char            unk_0x0269[3];
    char            unk_0x026C[0x18];   /* 0x026C */
                                        /* 0x0284 */

} z2_actor_ctxt_t;

typedef struct /* z2_dialog_t */
{
    z2_view_t       view;                   /* 0x00000 */ //168
    char            unk_0x00168[0x10000];   /* 0x00168 */
    struct
    {
        char        unk_0x0000[0x1D80];
        //uint8_t   unk_0x1880;
        int32_t     offset;                 /* 0x1D80 */
        int32_t     length;                 /* 0x1D84 */
        uint16_t    id;                     /* 0x1D9C */
        char        unk_0x1D9E[0x0E];       /* 0x1D9E */

    }  message;                             /* 0x10168 */
    char            dialog[3];              /* 0x11F24 */ //todo length
    int16_t         unk_0x11FEC;
    int16_t         unk_0x11FEE;
    int16_t         unk_0x11FF0;

} z2_dialog_t;

/* game context */
typedef struct
{
  z64_ctxt_t       common;                 /* 0x00000 */
  uint16_t         scene_index;            /* 0x000A4 */
  char             unk_00_[0x001A];        /* 0x000A6 */
  uint32_t         screen_top;             /* 0x000C0 */
  uint32_t         screen_bottom;          /* 0x000C4 */
  uint32_t         screen_left;            /* 0x000C8 */
  uint32_t         screen_right;           /* 0x000CC */
  float            camera_distance;        /* 0x000D0 */
  float            fog_distance;           /* 0x000D4 */
  float            z_distance;             /* 0x000D8 */
  float            unk_01_;                /* 0x000DC */
  char             unk_02_[0x0190];        /* 0x000E0 */
  z2_actor_t      *camera_focus;           /* 0x00270 */
  char             unk_03_[0x00AE];        /* 0x00274 */
  uint16_t         camera_mode;            /* 0x00322 */
  char             unk_04_[0x001A];        /* 0x00324 */
  uint16_t         camera_flag_1;          /* 0x0033E */
  char             unk_05_[0x016C];        /* 0x00340 */
  int16_t          event_flag;             /* 0x004AC */
  char             unk_06_[0x02E6];        /* 0x004AE */
  uint32_t         camera_2;               /* 0x00794 */
  char             unk_07_[0x0010];        /* 0x00798 */
  z64_lighting_t   lighting;               /* 0x007A8 */
  char             unk_08_[0x0008];        /* 0x007B8 */
  z64_col_hdr_t   *col_hdr;                /* 0x007C0 */
  char             unk_09_[0x1460];        /* 0x007C4 */
  char             actor_ctxt[0x0008];     /* 0x01C24 */
  uint8_t          n_actors_loaded;        /* 0x01C2C */
  char             unk_0A_[0x0003];        /* 0x01C2D */
  struct
  {
    uint32_t       length;
    z2_actor_t    *first;
  }                actor_list[12];         /* 0x01C30 */
  char             unk_0B_[0x0038];        /* 0x01C90 */
  z2_actor_t      *arrow_actor;            /* 0x01CC8 */
  z2_actor_t      *target_actor;           /* 0x01CCC */
  char             unk_0C_[0x0058];        /* 0x01CD0 */
  uint32_t         swch_flags;             /* 0x01D28 */
  uint32_t         temp_swch_flags;        /* 0x01D2C */
  uint32_t         unk_flags_0;            /* 0x01D30 */
  uint32_t         unk_flags_1;            /* 0x01D34 */
  uint32_t         chest_flags;            /* 0x01D38 */
  uint32_t         clear_flags;            /* 0x01D3C */
  uint32_t         temp_clear_flags;       /* 0x01D40 */
  uint32_t         collect_flags;          /* 0x01D44 */
  uint32_t         temp_collect_flags;     /* 0x01D48 */
  void            *title_card_texture;     /* 0x01D4C */
  char             unk_0D_[0x0007];        /* 0x01D50 */
  uint8_t          title_card_delay;       /* 0x01D57 */
  char             unk_0E_[0x0010];        /* 0x01D58 */
  void            *cutscene_ptr;           /* 0x01D68 */
  int8_t           cutscene_state;         /* 0x01D6C */
  char             unk_0F_[0xE66F];        /* 0x01D6D */
  uint8_t          textbox_state_1;        /* 0x103DC */
  char             unk_10_[0x00DF];        /* 0x103DD */
  uint8_t          textbox_state_2;        /* 0x104BC */
  char             unk_11_[0x0002];        /* 0x104BD */
  uint8_t          textbox_state_3;        /* 0x104BF */
  char             unk_12_[0x0272];        /* 0x104C0 */
  struct {
    uint16_t       unk_00_;
    uint16_t       fadeout;
    uint16_t       a_button_carots;
    uint16_t       b_button;
    uint16_t       cl_button;
    uint16_t       cd_button;
    uint16_t       cr_button;
    uint16_t       hearts_navi;
    uint16_t       rupees_keys_magic;
    uint16_t       minimap;
  }                hud_alpha_channels;    /* 0x10732 */
  char             unk_13_[0x000C];       /* 0x10746 */
  struct
  {
    uint8_t        unk_00_;
    uint8_t        b_button;
    uint8_t        unk_01_;
    uint8_t        bottles;
    uint8_t        trade_items;
    uint8_t        hookshot;
    uint8_t        ocarina;
    uint8_t        warp_songs;
    uint8_t        suns_song;
    uint8_t        farores_wind;
    uint8_t        dfnl;
    uint8_t        all;
  }                restriction_flags;      /* 0x10752 */
  char             unk_14_[0x0002];        /* 0x1075E */
  z64_pause_ctxt_t pause_ctxt;             /* 0x10760 */
  char             unk_15_[0x0D90];        /* 0x10A14 */
  z64_obj_ctxt_t   obj_ctxt;               /* 0x117A4 */
  int8_t           room_index;             /* 0x11CBC */
  char             unk_16_[0x000B];        /* 0x11CBD */
  void            *room_ptr;               /* 0x11CC8 */
  char             unk_17_[0x0118];        /* 0x11CCC */
  uint32_t         gameplay_frames;        /* 0x11DE4 */
  uint8_t          link_age;               /* 0x11DE8 */
  char             unk_18_;                /* 0x11DE9 */
  uint8_t          spawn_index;            /* 0x11DEA */
  uint8_t          n_map_actors;           /* 0x11DEB */
  uint8_t          n_rooms;                /* 0x11DEC */
  char             unk_19_[0x000B];        /* 0x11DED */
  void            *map_actor_list;         /* 0x11DF8 */
  char             unk_20_[0x0008];        /* 0x11DFC */
  void            *scene_exit_list;        /* 0x11E04 */
  char             unk_21_[0x000C];        /* 0x11E08 */
  uint8_t          skybox_type;            /* 0x11E14 */
  int8_t           scene_load_flag;        /* 0x11E15 */
  char             unk_22_[0x0004];        /* 0x11E16 */
  int16_t          entrance_index;         /* 0x11E1A */
  char             unk_23_[0x0042];        /* 0x11E1C */
  uint8_t          fadeout_transition;     /* 0x11E5E */
                                           /* 0x11E5F */
} z64_game_t;

/* mm game context */
typedef struct /* z2_game_t */
{
    z64_ctxt_t      common;                 /* 0x00000 */
    uint16_t        scene_index;            /* 0x000A4 */
    uint8_t         scene_draw_id;          /* 0x000A6 */
    char            unk_0x000A7[9];         /* 0x000A7 */
    void*           scene_addr;             /* 0x000B0 */
    char            unk_0x00B4[4];          /* 0x000B4 */
    z2_view_t       view_scene;             /* 0x000B8 */
    z2_camera_t     cameras[4];             /* 0x00220 */
    z2_camera_t    *active_cameras[4];      /* 0x00800 */
    int16_t         camera_cur;             /* 0x00810 */
    int16_t         camera_next;            /* 0x00812 */
    char            unk_0x814[0x1C];        /* 0x00814 */
    z2_col_ctxt_t   col_ctxt;               /* 0x00830 */
    z2_actor_ctxt_t actor_ctxt;             /* 0x01CA0 */
    //uint16_t       *test;                   /* 0x01F24 */

} z2_game_t;

extern z2_game_t z2_game;
asm(".equ z2_game, 0x803E6B20");

typedef struct
{
  void             *ptr;                      /* 0x0000 */
  uint32_t          vrom_start;               /* 0x0004 */
  uint32_t          vrom_end;                 /* 0x0008 */
  uint32_t          vram_start;               /* 0x000C */
  uint32_t          vram_end;                 /* 0x0010 */
  char              unk_00_[0x0004];          /* 0x0014 */
  uint32_t          vram_ctor;                /* 0x0018 */
  uint32_t          vram_dtor;                /* 0x001C */
  char              unk_01_[0x000C];          /* 0x0020 */
  char              ctxt_size;                /* 0x002C */
                                              /* 0x0030 */
} z64_state_ovl_t;

/* dram addresses */
//#define z64_osSendMesg_addr                     0x80001E20
//#define z64_osRecvMesg_addr                     0x80002030
//#define z64_osCreateMesgQueue_addr              0x80004220
//#define z64_file_mq_addr                        0x80007D40
//#define z64_vi_counter_addr                     0x80009E8C
//#define z64_DrawActors_addr                     0x80024AB4
//#define z64_DeleteActor_addr                    0x80024FE0
//#define z64_SpawnActor_addr                     0x80025110
//#define z64_minimap_disable_1_addr              0x8006CD50
//#define z64_minimap_disable_2_addr              0x8006D4E4
//#define z64_SwitchAgeEquips_addr                0x8006F804
//#define z64_UpdateItemButton_addr               0x8006FB50
//#define z64_GiveItem_addr                       0x8006FDCC
//#define z64_UpdateEquipment_addr                0x80079764
//#define z64_LoadRoom_addr                       0x80080A3C
//#define z64_UnloadRoom_addr                     0x80080C98
//#define z64_Io_addr                             0x80091474
//#define z64_entrance_offset_hook_addr           0x8009AA44
//#define z64_frame_update_func_addr              0x8009AF1C
//#define z64_frame_update_call_addr              0x8009CAE8
//#define z64_disp_swap_1_addr                    0x800A1198
//#define z64_disp_swap_2_addr                    0x800A11B0
//#define z64_disp_swap_3_addr                    0x800A11C8
//#define z64_disp_swap_4_addr                    0x800A11E4
//#define z64_frame_input_func_addr               0x800A0BA0
//#define z64_main_hook_addr                      0x800A0C3C
//#define z64_frame_input_call_addr               0x800A16AC
//#define z64_DisplayTextbox_addr                 0x800DCE14
//#define gspF3DEX2_NoN_fifoTextStart             0x800E3F70
//#define z64_day_speed_addr                      0x800F1650
//#define z64_light_handlers_addr                 0x800F1B40
//#define z64_object_table_addr                   0x800F8FF8
//#define z64_entrance_table_addr                 0x800F9C90
//#define z64_scene_table_addr                    0x800FB4E0
//#define z64_scene_config_table_addr             0x800FBD18
//#define z64_seq_pos_addr                        0x801043B0
//#define gspF3DEX2_NoN_fifoDataStart             0x801145C0
//#define z64_file_addr                           0x8011A5D0
//#define z64_input_direct_addr                   0x8011D730
//#define z64_stab_addr                           0x80120C38
//#define z64_seq_buf_addr                        0x80124800
//#define z64_ctxt_addr                           0x801C84A0
//#define z64_link_addr                           0x801DAA30
//#define z64_state_ovl_tab_addr                  0x800F1340
//#define z64_event_state_1_addr                  0x800EF1B0
//#define z64_LinkInvincibility_addr              0x8038E578
//#define z64_LinkDamage_addr                     0x8038E6A8
//
///* rom addresses */
//#define z64_icon_item_static_vaddr              0x007BD000
//#define z64_icon_item_static_vsize              0x000888A0
//#define z64_icon_item_24_static_vaddr           0x00846000
//#define z64_icon_item_24_static_vsize           0x0000B400
//#define z64_nes_font_static_vaddr               0x00928000
//#define z64_nes_font_static_vsize               0x00004580
//#define z64_file_select_static_vaddr            0x01A02000
//#define z64_file_select_static_vsize            0x000395C0
//#define z64_parameter_static_vaddr              0x01A3C000
//#define z64_parameter_static_vsize              0x00003B00
//
///* context info */
//#define z64_ctxt_filemenu_ctor                  0x80812394
//#define z64_ctxt_filemenu_size                  0x0001CAD0
//#define z64_ctxt_game_ctor                      0x8009A750
//#define z64_ctxt_game_size                      0x00012518
//
///* function prototypes */
//typedef void (*z64_DrawActors_proc)       (z64_game_t *game, void *actor_ctxt);
//typedef void (*z64_DeleteActor_proc)      (z64_game_t *game, void *actor_ctxt,
//                                           z2_actor_t *actor);
//typedef void (*z64_SpawnActor_proc)       (void *actor_ctxt, z64_game_t *game,
//                                           int actor_id, float x, float y,
//                                           float z, uint16_t rx, uint16_t ry,
//                                           uint16_t rz, uint16_t variable);
//typedef void (*z64_SwitchAgeEquips_proc)  (void);
//typedef void (*z64_UpdateItemButton_proc) (z64_game_t *game, int button_index);
//typedef void (*z64_UpdateEquipment_proc)  (z64_game_t *game, z64_link_t *link);
//typedef void (*z64_LoadRoom_proc)         (z64_game_t *game,
//                                           void *p_ctxt_room_index,
//                                           uint8_t room_index);
//typedef void (*z64_UnloadRoom_proc)       (z64_game_t *game,
//                                           void *p_ctxt_room_index);
//typedef void (*z64_Io_proc)               (uint32_t dev_addr, void *dram_addr,
//                                           uint32_t size, int32_t direction);
//typedef void (*z64_SceneConfig_proc)      (z64_game_t *game);
//typedef void (*z64_DisplayTextbox_proc)   (z64_game_t *game, uint16_t text_id,
//                                           int unknown_);
//typedef void (*z64_GiveItem_proc)         (z64_game_t *game, uint8_t item);
//
//typedef void(*z64_LinkDamage_proc)        (z64_game_t *ctxt, z64_link_t *link,
//                                           uint8_t damage_type, float unk_00, uint32_t unk_01,
//                                           uint16_t unk_02);
//typedef void(*z64_LinkInvincibility_proc) (z64_link_t *link, uint8_t frames);
//
///* data */
//#define z64_file_mq             (*(OSMesgQueue*)      z64_file_mq_addr)
//#define z64_vi_counter          (*(uint32_t*)         z64_vi_counter_addr)
//#define z64_stab                (*(z64_stab_t*)       z64_stab_addr)
//#define z64_scene_table         ( (z64_scene_table_t*)z64_scene_table_addr)
//#define z64_day_speed           (*(uint16_t*)         z64_day_speed_addr)
//#define z64_light_handlers      ( (z64_light_handler_t*)                      \
//                                                      z64_light_handlers_addr)
//#define z64_object_table        ( (z64_object_table_t*)                      \
//                                                      z64_object_table_addr)
//#define z64_entrance_table      ( (z64_entrance_t*)                     \
//                                   z64_entrance_table_addr)
//#define z64_scene_config_table  ( (z64_SceneConfig_proc*)                     \
//                                   z64_scene_config_table_addr)
//#define z64_file                (*(z64_file_t*)       z64_file_addr)
//#define z64_input_direct        (*(z64_input_t*)      z64_input_direct_addr)
//#define z64_gameinfo            (*                    z64_file.gameinfo)
//#define z64_ctxt                (*(z64_ctxt_t*)       z64_ctxt_addr)
//#define z64_game                (*(z64_game_t*)      &z64_ctxt)
////#define z64_link                (*(z64_link_t*)       z64_link_addr)
//#define z64_state_ovl_tab       (*(z64_state_ovl_t(*)[6])                     \
//                                                      z64_state_ovl_tab_addr)
//#define z64_event_state_1       (*(uint32_t*)         z64_event_state_1_addr)
//
//
///* functions */
//#define z64_osSendMesg          ((osSendMesg_t)       z64_osSendMesg_addr)
//#define z64_osRecvMesg          ((osRecvMesg_t)       z64_osRecvMesg_addr)
//#define z64_osCreateMesgQueue   ((osCreateMesgQueue_t)                        \
//                                 z64_osCreateMesgQueue_addr)
//#define z64_DrawActors          ((z64_DrawActors_proc)z64_DrawActors_addr)
//#define z64_DeleteActor         ((z64_DeleteActor_proc)                       \
//                                 z64_DeleteActor_addr)
//#define z64_SpawnActor          ((z64_SpawnActor_proc)z64_SpawnActor_addr)
//#define z64_SwitchAgeEquips     ((z64_SwitchAgeEquips_proc)                   \
//                                                      z64_SwitchAgeEquips_addr)
//#define z64_UpdateItemButton    ((z64_UpdateItemButton_proc)                  \
//                                                      z64_UpdateItemButton_addr)
//#define z64_UpdateEquipment     ((z64_UpdateEquipment_proc)                   \
//                                                      z64_UpdateEquipment_addr)
//#define z64_LoadRoom            ((z64_LoadRoom_proc)  z64_LoadRoom_addr)
//#define z64_UnloadRoom          ((z64_UnloadRoom_proc)                        \
//                                                      z64_UnloadRoom_addr)
//#define z64_Io                  ((z64_Io_proc)        z64_Io_addr)
//#define z64_DisplayTextbox      ((z64_DisplayTextbox_proc)                    \
//                                                      z64_DisplayTextbox_addr)
//#define z64_GiveItem            ((z64_GiveItem_proc)  z64_GiveItem_addr)
//
//#define z64_LinkDamage          ((z64_LinkDamage_proc)z64_LinkDamage_addr)
//#define z64_LinkInvincibility   ((z64_LinkInvincibility_proc)                 \
//                                                      z64_LinkInvincibility_addr)

#endif
