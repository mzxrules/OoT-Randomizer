.n64
.relativeinclude on

.create "../roms/mm/patched.z64", 0
.incbin "../roms/mm/base.z64"

.include "constants.asm"

; Add dmatable entry for the payload code
.orga 0x205F0
    .word G_PAYLOAD_VROM, (G_PAYLOAD_VROM + G_PAYLOAD_SIZE), G_PAYLOAD_VROM, 0

;==================================================================================================
; Base game editing region
;==================================================================================================

;.include "boot.asm"
.include "code.asm"

;==================================================================================================
; New code region
;==================================================================================================

.headersize (G_PAYLOAD_ADDR - G_PAYLOAD_VROM)


.org G_PAYLOAD_ADDR
.area 0x1000
.include "init.asm"
;DebugOutput:
;.include "debug.asm"
.endarea

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

.close
