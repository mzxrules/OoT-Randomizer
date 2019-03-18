#ifndef  RANDOM_H
#define  RANDOM_H

#include <stdint.h>

uint64_t    rng_next();
void        rng_set_seed(uint64_t value);
double      rng_next_f64();
float       rng_next_f32();
int32_t     rng_next_s32(int exclusive);
void        rng_shuffle_list(void *list, int element_size, int count);
#endif // ! RANDOM_H