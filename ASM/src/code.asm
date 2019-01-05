.headersize (0x800A5AC0-0xB3C000)

;==================================================================================================
; Set the size of the main heap
;==================================================================================================

.org 0x80174C4C
    lui     t8, hi(G_PAYLOAD_ADDR)
    addiu   t8, lo(G_PAYLOAD_ADDR)
.org 0x80174C5C
    sw      a1, 0x1528(v1)

    
;==================================================================================================
; Custom Code Payload
;==================================================================================================


.org 0x801748A0
    lui     a0, hi(G_PAYLOAD_ADDR)
    addiu   a0, lo(G_PAYLOAD_ADDR)
    lui     a1, hi(G_PAYLOAD_VROM)
    addiu   a1, lo(G_PAYLOAD_VROM)
    lui     a2, hi(G_PAYLOAD_SIZE)
    jal     0x80080C90
    addiu   a2, lo(G_PAYLOAD_SIZE)
    jal     init
    nop


;==================================================================================================
; Prologue Skip
;==================================================================================================

.org 0x80144644
    sw      r0, 0x0004(v0)
    li      t7, 1
    sb      t7, 0x0005(v0) ; Skip Prologue 
    nop

.org 0x801448A4
    addiu   t6, r0, 0x0003 ; Set Default form (Deku). Originally set to 4 (Human)

.org 0x80146AEC
    b   0x80146AFC ; Skip setting the first save file's cutscene number to 0xFFF0

    
;==================================================================================================
; Initial save
;==================================================================================================
.org 0x8014494C
    jal     write_initial_save

;==================================================================================================
; Item Overrides
;==================================================================================================


;==================================================================================================
; Game Class Frame Start Hook
;==================================================================================================

.org 0x80168F64
    game_update_start:

; 80168F64
.org 0x8016A8A8
    lui     t4, hi(game_state_update_custom)
.org 0x8016A8B0
    addiu   t4, lo(game_state_update_custom)

;==================================================================================================
; Special item sources
;==================================================================================================


;==================================================================================================
; Draw Dpad
;==================================================================================================

.org 0x8011F0F0
    jal     dpad_draw
    nop

;==================================================================================================
; Song Fixes
;==================================================================================================


;==================================================================================================
; Enemy Hacks
;==================================================================================================



;==================================================================================================
; Ocarina Song Cutscene Overrides
;==================================================================================================


;==================================================================================================
; Epona Check Override
;==================================================================================================


;==================================================================================================
; Shop Injections
;==================================================================================================
