all: jacobi error

jacobi: jacobi.c
	gcc -Wall -O3 --static ${CFLAGS}   jacobi.c -c 
	gcc -Wall -O3 --static ${CFLAGS}   jacobi.o ../../lib/m5op_x86.o ../../lib/m5_mmap.o -o  jacobi -lm
error: error.c
	gcc -Wall -O3 --static  ${CFLAGS}  error.c -o  error -lm

clean:
	rm -f jacobi error *.out 

