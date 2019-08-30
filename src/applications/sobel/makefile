all: sobel psnr

CFLAGS?=
LFLAGS?=
sobel: sobel.c
	gcc --static ${CFLAGS} -Wall -O3   sobel.c -o  sobel -lm ${LFLAGS} 

psnr: psnr.c
	gcc -Wall -O3   psnr.c -o  psnr -lm

clean:
	rm -f sobel psnr *.out 

