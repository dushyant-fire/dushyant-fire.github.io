---
layout:	default
title:	"Importing data in Python"
category:	code
date:	2022-01-14 08:00:00 -0000
permalink:	/code/Python/ImportData
---

## Importing text files using builtin function 
- Using command `open` 
	- `file = open('data.txt',mode='r')`, `print(file.read())`, remember to close the file (as a good practice) using `file.close()` method call

## Importing flat files (Example .csv, .txt)
   - Can use numpy functions, `np.loadtext('filename.txt',delimiter=',',dtype='float',skiprows=1,usecol=[0,3])`, imports filename.txt, with comma delimiter as string types, skips first header row and imports only first and third column.
   - However, for data with multiple datatypes, loadtext will not work efficiently. `data = np.genfromtext(filename,names=True,dtype=None,delimiter=',')`, which imports the data into structured arrays with header imported as column headers. To get ith row, use `data[i]`, and to get the columns named `header` as `data['header']`.
   - Another method is `np.recfromcsv()`, which has the default `dtype` as `None`, so we don't need to specify it explicitly.

## Importing Excel and pickled files
   - Pickled files are python-specifric files (such as .mat for MATLAB), which stores the array/dict in a .pkl format. This needs a package import `pickle` before importing the pkl file.
   - Excel files can be read using pandas, `file = pd.ExcelFile('filename.xlsx')`. To access sheets, `print(file.sheet_names)` which gives the names of the sheets. Now, to read individual sheets with specific arguments, `file.parse('Sheet_name or index starting from zero',skiprows=[1],names=['Column1'],usecol=[0])`, which then imports data from the specified sheet name or index, skips first row, renames the column to 'Column1', and uses only the first column (specified by `0`).
   - Import Stata data using pandas as `pd.read_stata()`
   - Reading hdf5 (Hierarchical Data Format version 5) file requires importing `h5py` package. hdf5 file has keys associated with it, and respective information within each key. 
   - Reading MATLAB `.mat` file using function `loadmat()` in the `scipy.io` package. This imports the data as dictionary.
 
