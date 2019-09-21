## Building
```sh
$ git clone https://github.com/koparasy/FaultModel.git
$ cd FaultModel
$ git submodule init
$ git submodule update
$ cd gem5
$ scons build/X86/gem5.opt -j9
```

j is the number of cores you have + 1

### Preparing Inputs

```sh
$ cd scripts
$ python getNumFaults.py 'Number of BRAMs' 'Size OF BRAM' 'Path to fault MAPS' 'path_to_gem5/inputs'
$ cd gem5
```

## Deterministic Run

### Run for Sobel

```sh
$ cd gem5
$ python3 run.py --bench-name=sobel --sobel-input=/path/to/gem5/tests/test-progs/sobel/figs/input.grey --sobel-output=/path/to/gem5/tests/test-progs/sobel/golden.bin
```

### Run for Monte Carlo

```sh
$ cd gem5
$ python3 run.py --bench-name=monteCarlo --monte-x=5 --monte-y=5 --monte-walks=50 --monte-tasks=5 --monte-output=/path/to/gem5/tests/test-progs/monteCarlo/golden.bin
```

### Run for Jacobi

```sh
$ cd gem5
$ python3 run.py --bench-name=jacobi --jacobi-n=1000 --jacobi-itol=0.00000001 --jacobi-dominant=1 --jacobi-maxiters=100 --jacobi-output=/path/to/gem5/tests/test-progs/jacobi/golden.bin
```

### Run for Matrix Multiplication

```sh
$ cd gem5
$ python3 run.py --bench-name=matrix_mul --matrix-output=/path/to/gem5/tests/test-progs/matrix_mul/golden.bin
```

### Run for Blackscholes

```sh
$ cd gem5
$ python3 run.py --bench-name=blackscholes --blackscholes-input=/path/to/gem5/tests/test-progs/blackscholes/1000.txt --blackscholes-output=/path/to/gem5/tests/test-progs/blackscholes/golden.bin
```

## Random Run

### Run for Sobel

```sh
$ cd gem5
$ python3 random_injection.py --random --bench-name=sobel --sobel-input=/path/to/gem5/tests/test-progs/sobel/figs/input.grey --sobel-output=/path/to/gem5/tests/test-progs/sobel/golden.bin
```

### Run for Monte Carlo

```sh
$ cd gem5
$ python3 random_injection.py --random --bench-name=monteCarlo --monte-x=5 --monte-y=5 --monte-walks=50 --monte-tasks=5 --monte-output=/path/to/gem5/tests/test-progs/monteCarlo/golden.bin
```

### Run for Jacobi

```sh
$ cd gem5
$ python3 random_injection.py --random --bench-name=jacobi --jacobi-n=1000 --jacobi-itol=0.00000001 --jacobi-dominant=1 --jacobi-maxiters=100 --jacobi-output=/path/to/gem5/tests/test-progs/jacobi/golden.bin
```

### Run for Matrix Multiplication

```sh
$ cd gem5
$ python3 random_injection.py --random --bench-name=matrix_mul --matrix-output=/path/to/gem5/tests/test-progs/matrix_mul/golden.bin
```

### Run for Blackscholes

```sh
$ cd gem5
$ python3 random_injection.py --random --bench-name=blackscholes --blackscholes-input=/path/to/gem5/tests/test-progs/blackscholes/1000.txt --blackscholes-output=/path/to/gem5/tests/test-progs/blackscholes/golden.bin