all: jacobi error

jacobi: jacobi.c
	gcc -Wall -O3   jacobi.c -o  jacobi -lm
error: error.c
	gcc -Wall -O3   error.c -o  error -lm

clean:
	rm -f jacobi error *.out 

