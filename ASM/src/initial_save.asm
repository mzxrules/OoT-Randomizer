;===========================================
; Writes extra data to the initial save file
;===========================================
write_initial_save:
    addi    sp, sp, -0x10
    sw      ra, 0x00(sp)
    jal     0x80144684
    nop

    li      a0, SAVE_CONTEXT

	; loop over the save data table
    li      a1, INITIAL_SAVE_DATA

@@save_data_loop:
    lh      t2, 0x00 (a1) ; t2 = override entry save data offset
    beqz    t2, @@return  ; Reached end of save data table
    nop
    add     t7, a0, t2      ; t7 = save data address
    lb      t8, 0x02(a1)    ; t8 = write type
    bnez    t8, @@overwrite_type ; if type is 0, use 'or' type (set bits) otherwise use overwrite type (set byte)
    lb      t9, 0x03(a1)    ; t9 = value to write
    lb      t2, 0x00(t7)    ; t2 = current saved value
    or      t9, t9, t2      ; t9 = given value | current saved value

@@overwrite_type:
    sb      t9, 0x00 (t7)   ; write the value into the save data
    b       @@save_data_loop
    addiu   a1, a1, 0x04

@@return:
    lw      ra, 0x00(sp)
    jr      ra
    addiu   sp, sp, 0x10