# pfpf - poly fit & peak find 
Fitting a polynomial with the polyfit function combined with peak detection using find_peak results in a precise method for recognizing multiple modals in your dataset
## -input1: 
dataset values (methylation table for example)
## -input2: 
CpG list (choose the rows from the table to work with)
## -input3: 
number of coefficients to fit (the more coefficients the greater resolution, the grater the over_fit too though)

# An example of a use case
## GUI style
### An example of running with plotting results
![GUI style example](https://github.com/noadrow/pfpf/blob/main/20231013000736.gif?raw=true)
### An example of using just for fillteration (CpG filtered list)

## command line style
### An example of running with plotting results
```
python3 log_test.py ./data/GSE87571_normalized_celltype.pickle ./data/GSE87571.no_chrx.no_snp.txt 20 6 "test1" --plot 
```
### An example of using just for fillteration (CpG filtered list)
```
python3 log_test.py ./data/GSE87571_normalized_celltype.pickle ./data/GSE87571.no_chrx.no_snp.txt 20 6 "test1" 
```
### An example of a console output:
![image](https://github.com/noadrow/pfpf/assets/105928017/92074fa0-2870-4ef3-91fb-3f14f8faa368)
### An example of -h\--help use
```
python3 --help
```
#### An example of a console output:
![image](https://github.com/noadrow/pfpf/assets/105928017/4d5fd378-8193-4355-b9ab-518e248f2e19)

## An example of results
### 1 peak:
![image](https://github.com/noadrow/pfpf/blob/main/results_poly/cg00419321_1.png?raw=true)
### 2 peaks:
![image](https://github.com/noadrow/pfpf/blob/main/results_poly/cg00308130_2.png?raw=true)
### 3 peaks:
![image](https://github.com/noadrow/pfpf/blob/main/results_poly/cg01091514_3.png?raw=true)

