#include "random.h"

static uint64_t seed;

uint64_t rng_next()
{
    seed = seed * 0x5851F42D4C957F2DULL + 0x14057B7EF767814FULL;
    return seed;
}

void rng_set_seed(uint64_t value)
{
    seed = value;
    
}

typedef union double_bin {
    double d;
    uint64_t u;
} double_bin_t;

typedef union float_bin {
    float f;
    uint32_t u;
} float_bin_t;

double rng_next_f64()
{
    uint64_t next = rng_next();
    next >>= 64 - 52;
    double_bin_t result;
    
    result.d = 1.0;
    result.u |= next;
    return result.d - 1;
}

float rng_next_f32()
{
    uint64_t next = rng_next();
    next >>= 64 - 23;
    float_bin_t result;
    result.f = 1.0f;
    result.u |= next;
    return result.f - 1;
}

int32_t rng_next_s32(int exclusive)
{
    return (int)((double)rng_next_f64() * exclusive);
}

void rng_shuffle_list(void *list, int element_size, int count)
{
    //Fisher-Yates "inside-out" shuffle
    for (int i = 0; i < count; i++)
    {
        int j = rng_next_s32(i + 1);
        if (j != i)
        {
            char *e_i = ((char *)list) + i * element_size;
            char *e_j = ((char *)list) + j * element_size;
            
            for (int iter = 0; iter < element_size; iter++)
            {
                char temp = e_i[iter];
                e_i[iter] = e_j[iter];
                e_j[iter] = temp;
            }
        }
    }
}