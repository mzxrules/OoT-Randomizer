;==================================================================================================
; Item upgrade functions
;==================================================================================================

no_upgrade:
    jr      ra
    ori     v0, a1, 0

;==================================================================================================

hookshot_upgrade:
    lbu     t0, 0x7D (a0) ; Load hookshot from inventory

    beq     t0, 0xFF, @@return
    li      v0, 0x08 ; Hookshot

    li      v0, 0x09 ; Longshot

@@return:
    jr      ra
    nop

;==================================================================================================

strength_upgrade:
    lbu     t0, 0xA3 (a0) ; Load strength from inventory
    andi    t0, t0, 0xC0 ; Mask bits to isolate strength

    beqz    t0, @@return
    li      v0, 0x54 ; Goron Bracelet

    beq     t0, 0x40, @@return
    li      v0, 0x35 ; Silver Gauntlets

    li      v0, 0x36 ; Gold Gauntlets

@@return:
    jr      ra
    nop

;==================================================================================================

bomb_bag_upgrade:
    lbu     t0, 0xA3 (a0) ; Load bomb bag from inventory
    andi    t0, t0, 0x18 ; Mask bits to isolate bomb bag

    beqz    t0, @@return
    li      v0, 0x32 ; Bomb Bag

    beq     t0, 0x08, @@return
    li      v0, 0x33 ; Bigger Bomb Bag

    li      v0, 0x34 ; Biggest Bomb Bag

@@return:
    jr      ra
    nop

;==================================================================================================

bow_upgrade:
    lbu     t0, 0xA3 (a0) ; Load quiver from inventory
    andi    t0, t0, 0x03 ; Mask bits to isolate quiver

    beqz    t0, @@return
    li      v0, 0x04 ; Bow

    beq     t0, 0x01, @@return
    li      v0, 0x30 ; Big Quiver

    li      v0, 0x31 ; Biggest Quiver

@@return:
    jr      ra
    nop

;==================================================================================================

slingshot_upgrade:
    lbu     t0, 0xA2 (a0) ; Load bullet bag from inventory
    andi    t0, t0, 0xC0 ; Mask bits to isolate bullet bag

    beqz    t0, @@return
    li      v0, 0x05 ; Slingshot

    beq     t0, 0x40, @@return
    li      v0, 0x60 ; Bullet Bag (40)

    li      v0, 0x7B ; Bullet Bag (50)

@@return:
    jr      ra
    nop

;==================================================================================================

wallet_upgrade:
    lbu     t0, 0xA2 (a0) ; Load wallet from inventory
    andi    t0, t0, 0x30 ; Mask bits to isolate wallet

    beqz    t0, @@return
    li      v0, 0x45 ; Adult's Wallet

    li      t1, 0x10
    beq     t0, t1, @@return
    li      v0, 0x46 ; Giant's Wallet

    ori     v0, a1, 0   ; Tycoon's Wallet (unchanged)

@@return:
    jr      ra
    nop

tycoon_wallet:
    ; a0 = save context
    lbu     t0, 0xA2 (a0) ; Load wallet from inventory
    ori     t0, t0, 0x30  ; Give lvl 3 wallet
    sb      t0, 0xA2 (a0) ; Store wallet to inventory
    jr      ra
    nop

;==================================================================================================

scale_upgrade:
    lbu     t0, 0xA2 (a0) ; Load scale from inventory
    andi    t0, t0, 0x06 ; # Mask bits to isolate scale

    beqz    t0, @@return
    li      v0, 0x37 ; Silver Scale

    li      v0, 0x38 ; Gold Scale

@@return:
    jr      ra
    nop

;==================================================================================================

nut_upgrade:
    lbu     t0, 0xA1 (a0) ; Load nut limit from inventory
    andi    t0, t0, 0x20 ; Mask bits to isolate nut limit, upper bit only

    beqz    t0, @@return
    li      v0, 0x79 ; 30 Nuts

    li      v0, 0x7A ; 40 Nuts

@@return:
    jr      ra
    nop

;==================================================================================================

stick_upgrade:
    lbu     t0, 0xA1 (a0) ; Load stick limit from inventory
    andi    t0, t0, 0x04 ; Mask bits to isolate stick limit, upper bit only

    beqz    t0, @@return
    li      v0, 0x77 ; 20 Sticks

    li      v0, 0x78 ; 30 Sticks

@@return:
    jr      ra
    nop

;==================================================================================================

magic_upgrade:
    lbu     t0, 0x32 (a0) ; Load magic level from inventory

    beqz    t0, @@return
    li      v0, 0xC0 ; Single Magic

    li      v0, 0xC1 ; Double Magic

@@return:
    jr      ra
    nop

;==================================================================================================

arrows_to_rupee:
    lbu     t0, 0xA3 (a0) ; Load quiver from inventory
    andi    t0, t0, 0x03 ; Mask bits to isolate quiver

    beqz    t0, @@return
    li      v0, 0x4D ; Blue Rupee

    ori     v0, a1, 0

@@return:
    jr      ra
    nop

;==================================================================================================

bombs_to_rupee:
    lbu     t0, 0xA3 (a0) ; Load bomb bag from inventory
    andi    t0, t0, 0x18 ; Mask bits to isolate bomb bag

    beqz    t0, @@return
    li      v0, 0x4D ; Blue Rupee

    ori     v0, a1, 0

@@return:
    jr      ra
    nop

;==================================================================================================

seeds_to_rupee:
    lbu     t0, 0xA2 (a0) ; Load seed bag from inventory
    andi    t0, t0, 0xC0 ; Mask bits to isolate seed bag

    beqz    t0, @@return
    li      v0, 0x4D ; Blue Rupee

    ori     v0, a1, 0

@@return:
    jr      ra
    nop

;==================================================================================================
; Item effect functions
;==================================================================================================

no_effect:
    jr      ra
    nop

;==================================================================================================

give_bottle:
    ; a0 = save context
    ; a1 = item code to store
    addiu   t0, a0, 0x86 ; t0 = First bottle slot
    li      t1, -1 ; t1 = Bottle slot offset

@@loop:
    addiu   t1, t1, 1
    bgt     t1, 3, @@return ; No free bottle slots
    nop

    ; Check whether slot is full
    addu    t2, t0, t1
    lbu     t3, 0x00 (t2)
    bne     t3, 0xFF, @@loop
    nop

    ; Found an open slot
    sb      a1, 0x00 (t2)

@@return:
    jr      ra
    nop

;==================================================================================================

give_dungeon_item:
    ; a0 = save context
    ; a1 = mask (0x01 = boss key, 0x02 = compass, 0x04 = map)
    ; a2 = dungeon index
    addiu   t0, a0, 0xA8
    addu    t0, t0, a2 ; t0 = address of this dungeon's items
    lbu     t1, 0x00 (t0)
    or      t1, t1, a1
    sb      t1, 0x00 (t0)
    jr      ra
    nop

;==================================================================================================

give_small_key:
    ; a0 = save context
    ; a1 = dungeon index
    addiu   t0, a0, 0xBC
    addu    t0, t0, a1 ; t0 = address of this dungeon's key count
    lb      t1, 0x00 (t0)
    bgez    t1, @not_negative
    nop
    li      t1, 0x00
@not_negative:
    addiu   t1, t1, 1
    sb      t1, 0x00 (t0)
    jr      ra
    nop

;==================================================================================================

give_defense:
    ; a0 = save context
    li      t0, 0x01
    sb      t0, 0x3D (a0) ; Set double defense flag
    li      t0, 0x14
    sb      t0, 0xCF (a0) ; Set number of hearts to display as double defense
    li      t0, 0x0140
    sh      t0, 0x1424 (a0) ; Give health refill
    jr      ra
    nop

give_magic:
    ; a0 = save context
    li      t0, 1
    sb      t0, 0x32 (a0) ; Set meter level
    sb      t0, 0x3A (a0) ; Required for meter to persist on save load
    li      t0, 0x30
    sh      t0, 0x13F4 (a0) ; Set meter size
    sb      t0, 0x33 (a0) ; Fill meter
    jr      ra
    nop

double_magic:
    ; a0 = save context
    li      t0, 2
    sb      t0, 0x32 (a0) ; Set meter level
    li      t0, 1
    sb      t0, 0x3A (a0) ; Required for meter to persist on save load
    sb      t0, 0x3C (a0) ; Required for meter to persist on save load
    li      t0, 0x60
    sh      t0, 0x13F4 (a0) ; Set meter size
    sb      t0, 0x33 (a0) ; Fill meter
    jr      ra
    nop

;==================================================================================================

bombchu_upgrade:
    lbu     t0, 0x7C (a0) ; Load bomchu from inventory
    beq     t0, 0xFF, @@return
    li      v0, 0x6B ; Bombchu 20 pack

    lbu     t0, 0x94 (a0) ; Load bombchu count from inventory
    sltiu   t0, t0, 0x06
    beqz    t0, @@return  ; if 
    li      v0, 0x6A ; Bombchu 5 Pack

    li      v0, 0x03 ; Bombchu 10 Pack

@@return:
    jr      ra
    nop

;==================================================================================================

ocarina_upgrade:
    lbu     t0, 0x7B (a0) ; Load ocarina from inventory

    beq     t0, 0xFF, @@return
    ori     v0, a1, 0 ; Fairy Ocarina (unchanged)

    li      v0, 0x0C ; Ocarina of Time

@@return:
    jr      ra
    nop

give_fairy_ocarina:
    ; a0 = save context
    li      t0, 0x07
    sb      t0, 0x7B (a0)
    jr      ra
    nop

;==================================================================================================

give_song:
    ; a0 = save context
    ; a1 = quest bit
    li      t0, 1
    sllv    t0, t0, a1
    lw      t1, 0xA4(a0)
    or      t1, t1, t0
    sw      t1, 0xA4(a0)
    jr      ra
    nop
