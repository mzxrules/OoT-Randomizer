.n64
.relativeinclude on

.create "../roms/mm/patched.z64", 0
.incbin "../roms/mm/base.z64"

.include "constants.asm"

.orga 0x10
    .word 0xDDF7E3E7, 0x4774416C

; Add dmatable entry for the payload code
.orga 0x205F0
    .word G_PAYLOAD_VROM, (G_PAYLOAD_VROM + G_PAYLOAD_SIZE), G_PAYLOAD_VROM, 0

;==================================================================================================
; Base game editing region
;==================================================================================================

;.include "boot.asm"
.include "code.asm"
.include "link.asm"

;==================================================================================================
; New code region
;==================================================================================================

.headersize (G_PAYLOAD_ADDR - G_PAYLOAD_VROM)
.org G_PAYLOAD_ADDR
.area G_PAYLOAD_SIZE

.include "config.asm"
.include "init.asm"
;.include "every_frame.asm"
.include "initial_save.asm"
.include "dpad.asm"

.importobj "../build/bundle.o"

.align 0x08
DPAD_TEXTURE:
.incbin("../resources/dpad.bin")

.endarea  //payload size
.close
