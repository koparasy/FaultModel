### Preparing Inputs

```sh
$ cd scripts
$ python getNumFaults.py 'Number of BRAMs' 'Size OF BRAM' 'Path to fault MAPS' 'path_to_gem5/inputs'
$ cd gem5
```
### Run for Sobel

```sh
$ cd gem5
$ python3 script.py --bench-name=sobel --sobel-input=/path/to/gem5/tests/test-progs/sobel/figs/input.grey --sobel-output=/path/to/gem5/tests/test-progs/sobel/output.grey
```

### Run for Monte Carlo

```sh
$ cd gem5
$ python3 script.py --bench-name=monteCarlo --monte-x=5 --monte-y=5 --monte-walks=50 --monte-tasks=5 --monte-output=/path/to/gem5/tests/test-progs/monteCarlo/output.txt
```

### Run for Jacobi

```sh
$ cd gem5
$ python3 script.py --bench-name=jacobi --jacobi-n=1000 --jacobi-itol=0.00000001 --jacobi-dominant=1 --jacobi-maxiters=100 --jacobi-output=/path/to/gem5/tests/test-progs/jacobi/output.txt
```

### Run for Matrix Multiplication

```sh
$ cd gem5
$ python3 script.py --bench-name=matrix_mul --matrix-output=/path/to/gem5/tests/test-progs/matrix_mul/output.txt
```

### Run for Blackscholes

```sh
$ cd gem5
$ python3 script.py --bench-name=blackscholes --blackscholes-input=/path/to/gem5/tests/test-progs/blackscholes/1000.txt --blackscholes-output=/path/to/gem5/tests/test-progs/blackscholes/output.txt
```