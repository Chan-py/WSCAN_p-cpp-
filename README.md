# WSCAN
Instruction for experiment

WSCAN is implemented in C++ and compiled via the provided `Makefile`.

After cloning the repository, simply run:
```
make
```

This will generate an executable file named:
```
wscan
```

You can then execute it with the desired parameters.

---

## Parameters for Experiment

- eps : Similarity threshold parameter.

- mu : Minimum number of similar neighbors required.

- gamma : Balance parameter.

- similarity : Name of similarity function to use.

- network : Path of the dataset folder. The folder has to have the file named `network.dat`.

---

### Edge Perturbation Parameters

- edge_p : Percentage of edges to perturb.

- delta_p : Percentage for delta (delta is the parameter for perturbing edge weight).

- weight_method : Method to compute edge weight.  
  Options:
  - "avg"
  - "max"

---

### Parallel Execution

- parallel : Enable parallel mode.  
  (Boolean flag — no value required. Just include `--parallel`.)

- threads : Number of threads to use in parallel mode.s

---

### Synthetic Mode

- synthetic : Enable synthetic dataset mode.  
  (Boolean flag — no value required. Just include `--synthetic`.)

---

### Output

- output_file : Name of the CSV file where results will be stored.

---

## Examples

### Basic Usage
```
./wscan --network karate --similarity WSCAN++ --eps 0.2 --mu 8 --gamma 0.7 --output_file result.csv
```

---

### With Edge Perturbation
```
./wscan --network sociopattern_hospital \
        --similarity WSCAN++ \
        --eps 0.2 --mu 8 --gamma 0.7 \
        --edge_p 0.1 --delta_p 0.05 --weight_method max --output_file result.csv
```

---

### Parallel Execution
```
./wscan --network sociopattern_primaryschool \
        --similarity WSCAN++ \
        --eps 0.2 --mu 8 --gamma 0.7 \
        --parallel --threads 4 --output_file result.csv
```

---

### Synthetic Mode with Custom Output File
```
./wscan --network synthetic_dataset \
        --eps 0.2 --mu 8 --gamma 0.7 \
        --synthetic \
        --output_file synthetic_result.csv
```

---

## Notes

1. Ground-truth Detection  
   The program automatically checks whether the dataset has ground-truth labels by verifying the existence of a `labels.dat` file in the dataset folder (If synthetic, `community.dat`). No additional argument is required.

2. Node Indexing  
   Node indices must start from 1.  
   Although non-consecutive numbering does not cause runtime errors, memory allocation is based on the maximum node ID.  
   Therefore, non-sequential numbering may result in unnecessary memory usage.