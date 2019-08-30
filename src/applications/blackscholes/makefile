all: blackscholes error

blackscholes: blackscholes.c
	gcc -Wall -O3   blackscholes.c -o  blackscholes -lm
error: error.c
	gcc -Wall -O3   error.c -o  error -lm

clean:
	rm -f blackscholes error *.bin 

