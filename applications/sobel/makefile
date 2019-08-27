all: sobel psnr

sobel: sobel.c
	gcc -Wall -O3   sobel.c -o  sobel -lm
psnr: psnr.c
	gcc -Wall -O3   psnr.c -o  psnr -lm

clean:
	rm -f sobel psnr *.out 

