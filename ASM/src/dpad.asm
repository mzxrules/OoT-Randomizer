dpad_draw:
    sw      ra, 0x0004(sp)
    jal     draw_dpad
    sw      a0, 0x0000(sp)
    lw      a0, 0x0000(sp)
    lw      ra, 0x0004(sp)
    or      a3, a0, r0
    jr      ra
    lw      t6, 0x1CCC(a3)



test_mask_usability_hack:

    lui     t0, hi(SAVE_CONTEXT + 0x4F)
    lui     t1, hi(temp_c_right)
    lb      t2, lo(SAVE_CONTEXT + 0x4F)(t0)
    sb      t2, lo(temp_c_right)(t1)
    li      t3, 0x32
    jal     0x80110038
    sb      t3, lo(SAVE_CONTEXT + 0x4F)(t0)
    lb      t0, (SAVE_CONTEXT + 0x3F1B)
    lui     t4, hi(extern_mask_usability)
    sb      t0, lo(extern_mask_usability)(t4)

    lui     t0, hi(SAVE_CONTEXT + 0x4F)
    lui     t1, hi(temp_c_right)
    lb      t2, lo(temp_c_right)(t1)
    sb      t2, lo(SAVE_CONTEXT + 0x4F)(t0)
    jal     0x80110038
    lw      a0, 0x0038(sp)

    j       return_test_mask_usability_hack
    nop

    
    
temp_c_right:
.byte    0x00
extern_mask_usability:
.byte    0x00
.align 4