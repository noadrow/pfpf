# pfpf - poly fit & peak find 
poly fit with find peak gives a highly accurate molti-modal recognition 
you can complie it using pyinstaller if you like to
-input1: dataset values (methylation table for example)
-input2: CpG list (choose the rows from the table to work with)
-input3: number of coefficients to fit (the more coefficients the greater resolution, the grater the over_fit too though)

## example of a usecae
### GUI style
![GUI style example](https://github.com/noadrow/pfpf/blob/main/20231013000736.gif?raw=true)

### command line style
```
python3 log_test.py ./data/GSE87571_normalized_celltype.pickle ./data/GSE87571.no_chrx.no_snp.txt 20 6
```

