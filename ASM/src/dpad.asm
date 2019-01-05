dpad_draw:
    sw      ra, 0x0004(sp)
    jal     draw_dpad
    sw      a0, 0x0000(sp)
    lw      a0, 0x0000(sp)
    lw      ra, 0x0004(sp)
    or      a3, a0, r0
    jr      ra
    lw      t6, 0x1CCC(a3)
