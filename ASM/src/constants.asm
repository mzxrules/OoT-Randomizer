; Payload configuration constants
.definelabel G_PAYLOAD_VROM, 0x02EE8000
.definelabel G_PAYLOAD_SIZE, 0x8000
.definelabel G_PAYLOAD_ADDR, (0x80780000 - G_PAYLOAD_SIZE)

; Pointers to game state
.definelabel SAVE_CONTEXT,   0x801EF670
.definelabel GLOBAL_CONTEXT, 0x803E6B20
.definelabel GET_ITEMTABLE,  0x803A9E7E

;.definelabel DUMMY_ACTOR, ?
;.definelabel C_HEAP,      ?
