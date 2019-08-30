all: monte_carlo calc_errors

monte_carlo: monte_carlo.c 
	gcc -Wall -O3 --static ${CFLAGS} -I../../include/ monte_carlo.c -c 
	gcc -Wall -O3 --static ${CFLAGS} -I../../include/ monte_carlo.o ../../lib/m5op_x86.o ../../lib/m5_mmap.o -o  monte_carlo -lm
calc_errors: calc_errors.c
	gcc -Wall -O3 --static  ${CFLAGS} -I../../include/ calc_errors.c -o  calc_errors -lm

clean:
	rm -f monte_carlo calc_errors *.bin

