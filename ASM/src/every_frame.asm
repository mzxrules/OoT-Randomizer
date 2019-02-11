game_state_update_custom:
    addiu   sp, sp, -0x18
    sw      a0, 0x0018(sp) //Global Context
    sw      ra, 0x0010(sp)

    jal     game_update_start
    lw      a0, 0x0018(sp) //Global Context

    ;after_game_state_update:
    lw      ra, 0x0010 (sp)
    jr      ra
    addiu   sp, sp, 0x18
