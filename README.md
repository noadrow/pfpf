# pfpf - poly fit & peak find 
Fitting a polynomial with the polyfit function combined with peak detection using find_peak results in a precise method for recognizing multiple modes in your data
## -input1: 
dataset values (methylation table for example)
## -input2: 
CpG list (choose the rows from the table to work with)
## -input3: 
number of coefficients to fit (the more coefficients the greater resolution, the grater the over_fit too though)

# example of a usecae
## GUI style
![GUI style example](https://github.com/noadrow/pfpf/blob/main/20231013000736.gif?raw=true)

## command line style
```
python3 log_test.py ./data/GSE87571_normalized_celltype.pickle ./data/GSE87571.no_chrx.no_snp.txt 20 6
```
example of console output:
![image](https://github.com/noadrow/pfpf/assets/105928017/92074fa0-2870-4ef3-91fb-3f14f8faa368)

## result examples
### 1 peak:
![image](https://github.com/noadrow/pfpf/blob/main/results_poly/cg00419321_1.png?raw=true)
### 2 peaks:
![image](https://github.com/noadrow/pfpf/blob/main/results_poly/cg00308130_2.png?raw=true)
### 3 peaks:
![image](https://github.com/noadrow/pfpf/blob/main/results_poly/cg01091514_3.png?raw=true)

