<<<<<<< HEAD
.n64
.relativeinclude on

.create "../roms/mm/patched.z64", 0
.incbin "../roms/mm/base.z64"

;==================================================================================================
; Constants
;==================================================================================================

;.include "constants.asm"
;.include "addresses.asm"

;==================================================================================================
; Base game editing region
;==================================================================================================

;.include "boot.asm"
.include "hacks.asm"
.include "malon.asm"

;==================================================================================================
; New code region
;==================================================================================================

;.headersize (0x80400000 - 0x03480000)


;.org 0x80400000
;.area 0x1000
;.include "coop_state.asm" ; This should always come first
;.include "init.asm"
;DebugOutput:
;.include "debug.asm"
;.endarea

;.org 0x80401000
;.area 0x1000, 0
;.include "config.asm"
;.endarea

;.org 0x80402000
;.area 0x50, 0
;.include "state.asm"
;.endarea

;.org 0x80402050
;.area 0x2000, 0
;.include "extended_items.asm"
;.include "item_overrides.asm"
;.include "cutscenes.asm"
;.include "shop.asm"
;.include "every_frame.asm"
;.include "menu.asm"
;.include "time_travel.asm"
;.include "song_fix.asm"
;.include "scarecrow.asm"
;.include "initial_save.asm"
;.include "textbox.asm"
;.endarea

;.headersize (0x80405000 - 0x034B3000)

;.org 0x80405000
;.area 0xB000, 0
;.importobj "../build/bundle.o"
;FONT_TEXTURE:
;.incbin("../resources/font.bin")
;.endarea

;==================================================================================================
; ADDED IN v4.0
;==================================================================================================

;.include "empty_bomb_fix.asm"
;.include "fishing.asm"
;.include "bgs_fix.asm"
;.include "chus_in_logic.asm"
;.include "rainbow_bridge.asm"
;.include "gossip_hints.asm"
;.include "potion_shop.asm"
;.include "jabu_elevator.asm"
;.include "dampe.asm"
;.include "dpad.asm"
;.include "chests.asm"
;.align 8
;DPAD_TEXTURE:
;.incbin("../resources/dpad.bin")
;.endarea

.close
