; Payload configuration constants
.definelabel G_PAYLOAD_VROM, 0x02EE8000
.definelabel G_PAYLOAD_SIZE, 0x8000
.definelabel G_PAYLOAD_ADDR, (0x80780000 - G_PAYLOAD_SIZE)

; Pointers to game state
.definelabel SAVE_CONTEXT,   0x8011A5D0
.definelabel GLOBAL_CONTEXT, 0x801C84A0
.definelabel PLAYER_ACTOR,   0x801DAA30
.definelabel GET_ITEMTABLE,  0x803A9E7E

; Extended memory map:
; Loaded code files   0x80400000
; ASM working memory  0x80480000
; C working memory    0x80500000

.definelabel DUMMY_ACTOR, 0x80480000
.definelabel C_HEAP,      0x80500000
