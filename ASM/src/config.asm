;==================================================================================================
; Settings and tables which the front-end may write
;==================================================================================================

; Item override table:
;
; This table changes the meaning of a given item ID within a given scene. It must be terminated with
; four 0x00 bytes (which will happen by default as long as you don't fill the allotted space).
;
; Row format (4 bytes):
; SSTTIINN
; SS = Scene
; TT = Override Type (0x00 = base item, 0x01 = chest, 0x02 = collectable)
; II = Override ID (base item or flag)
; NN = New item ID

.area 0x800, 0
ITEM_OVERRIDES:
.endarea

; Initial Save Data table:
;
; This table describes what extra data should be written when a new save file is created. It must be terminated with
; four 0x00 bytes (which will happen by default as long as you don't fill the allotted space).
;
; Format (4 bytes):
; /* 0x00 */ s16 offset; //offset from the start of the save data
; /* 0x02 */ u8 type; // 0x00 = bitwise OR value with current value, 0x01 = write value
; /* 0x03 */ u8 value;

.area 0x200, 0
INITIAL_SAVE_DATA:
.endarea
INITIAL_SAVE_DATA_END:

PLAYER_ID:
.byte 0x00
COOP_GET_ITEM:
.byte 0x00
PLAYER_NAME_ID:
.byte 0x00

.area 8*32, 0xDF
PLAYER_NAMES:
.endarea

; Special items

.align 0x10