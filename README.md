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