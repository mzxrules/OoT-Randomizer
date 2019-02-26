#include <stdint.h>
#include <stdbool.h>
#include <n64.h>
#include "world.h"

uint8_t big_poe_count = 10;


//self.keysanity = self.shuffle_smallkeys != 'dungeon'
//self.check_beatable_only = not self.all_reachable

uint8_t skipped_trials[6];


uint8_t dungeon_mq[6];

//         self.can_take_damage = True
