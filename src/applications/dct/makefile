all: dct psnr

dct: dct.c
	gcc -Wall -O3   dct.c -o  dct -lm
psnr: psnr.c
	gcc -Wall -O3   psnr.c -o  psnr -lm

clean:
	rm -f dct psnr *.out *.raw 

