all: sobel psnr

CFLAGS?=
LFLAGS?=
sobel: sobel.c
	gcc --static ${CFLAGS} -I../../include/ -Wall -O3   sobel.c -c
	gcc --static ${CFLAGS} -I../../include/ -Wall -O3   sobel.o ../../lib/m5op_x86.o ../../lib/m5_mmap.o -o sobel -lm ${LFLAGS} 

psnr: psnr.c
	gcc -Wall -O3   psnr.c -o  psnr -lm

clean:
	rm -f sobel psnr *.out 

