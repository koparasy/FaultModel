#include <worker.h>
#include <benchmark.h>
#include <circle/logger.h>



extern double COS[8*8], C[8];

int my_round(double a) {
    int s = a >= 0.0 ? 1 : -1;
    return (int)(a+s*0.5);
}


const int quant_table[8*8] = {
    16, 11, 10, 16, 24, 40, 51, 61,
    12, 12, 14, 19, 26, 58, 60, 55 ,
    14, 13, 16, 24, 40, 57, 69, 56,
    14, 17, 22, 29, 51, 87, 80, 82,
    18, 22, 37, 56, 68, 109, 103, 77,
    24, 35, 55, 64, 81, 104, 113, 92,
    49, 64, 78, 87, 103, 121, 120, 101,
    72, 92, 95, 98, 112, 100, 103, 99
};

void Worker::calculateWorker(unsigned int index, INPUT_TYPE *input, OUTPUT_TYPE *output)
{
    int r, c, i, j, x, y;
    for (r = 0; r < SIZE; r+=8)
        for (c = 0; c <SIZE; c+=8)
            for (i = 0; i < 8; i++)
                for (j = 0; j < 8; j++) {
                    double sum = 0;
                    for (y = 0; y < 8; y++)
                        for (x = 0; x < 8; x++)
                            sum += (input[(r + y)*SIZE+(c + x)] - 128) * COS[y*8+i] * COS[x*8+j];
                    sum *= C[i] * C[j] * 0.25;
                    // vasiliad: quantization - dequantization
                    sum = my_round(sum/quant_table[i*8+j]) * quant_table[i*8+j];
                    output[(r + i)*SIZE+ (c + j)] = sum;

                }
}


