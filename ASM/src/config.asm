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
; Row format (4 bytes):
; AAAATTVV
; AAAA = Offset from the start of the save data
; TT = Type (0x00 = or value with current value, 0x01 = set the byte to the given value)
; VV = Value to write to the save

.area 0x400, 0
INITIAL_SAVE_DATA:
.endarea

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

