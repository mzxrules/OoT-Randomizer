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
.include "config.asm"
.include "init.asm"
;.include "every_frame.asm"
.include "initial_save.asm"
.include "dpad.asm"


.importobj "../build/bundle.o"
.align 8
;FONT_TEXTURE:
;.incbin("../resources/font.bin")
;.endarea
DPAD_TEXTURE:
.incbin("../resources/dpad.bin")

.close
