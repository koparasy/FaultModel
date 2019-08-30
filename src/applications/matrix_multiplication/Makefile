all: matrix_mul

matrix_mul: matrix_mul.c
	gcc -Wall -O3 -static matrix_mul.c ${CFLAGS} -c
	gcc -Wall -O3 -static matrix_mul.o ../../lib/m5op_x86.o ../../lib/m5_mmap.o -o matrix_mul -lm

clean:
	rm -f *.o matrix_mul
