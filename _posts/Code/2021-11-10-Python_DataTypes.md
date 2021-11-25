---
layout:	default
title:	Python built-in and package DataTypes 
category:	code
date:	2021-11-24 12:30:00 -0000
permalink:	/code/Python/DataTypes
---

### List, Dictionaries, pandas' DataFrame, and numpy's array

| | List | Dictionaries| Array(numpy)|DataFrame(pandas)|
|:---|:---:|:---:|:---:|:---:|
|Syntax| `list = ['a','b','c','d']`|`dict={'key1':'value1','key2':'value2','key3':'value3'}`|  After `import numpy as np`, `np_array = np.array(list)` will create `[1 2 3 4]` which has a type `<class 'numpy.ndarray'>`|If `my_dict = {'var1':['A1','A2','A3'], 'var2':['B1','B2','B3']}`, after `import pandas as pd`, `my_df = pd.DataFrame(my_dict)`|
|How to select, add, or delete?|`list_subset = list[:3]` gives `['a','b','c']` | `dict_subset=dict['key1']` gives `value1`  unique keys required| Select using `np_arr[row, column]`, e.g. `selected_np_arr = np_array[3]` will return `3`| Simple two square brackets (`my_df[['var1']]`) for column access, and slicing `[:3]` for row access. More versatile: Using either `loc` for label basedd access or `iloc` for index based access. Adding double brackets in loc returns a dataframe and not a series - `my_df.loc[['var1'],'2']`| 
|Remember| 0-indexing, reverse indexing: `list[-1]` will give 'd', Built-in functions like `min(list),max(list)`, delete using `del(list[2])`| Unique keys required to access dict info, but can be accessed with []| Numpy allows only single type of object in an array, if a list contains float and strings, all types will be converted to strings| | 
|Use| When dealing with collection of values, order of data matters, or selecting sub-set is required| When dealing with look-up tables| | |

### Logical operators in packages

| List/Data | Numpy|DataFrame(pandas)|
|---|---|---|
|`x=2`, `x>0 and x<1` returns `False` | `np_arr = np.array([1,2,3,4])`, `np_arr>3` returns a numpy array `([False,False,False,True])`, but `np_arr>3 and np_arr<=4` throws an error. Numpy requires `logical_and(condition1,condition2)`, or `logical_or()`, or `logical_not()` for multiple conditions| Uses numpy `logical_and()` etc operators on series objects (`df[]`) or DataFrames(`df[[]]`) extracted from the DataFrame|

### For loops

| On Lists| On Dictionaries| On Numpy array| on DataFrames|
|---|:---:|:---:|:---:|
|Again, if `list = ['a','b',c',d']`, `for i,j in enumerate(list): print('index=' +str(i)+'value='+str(list(j)))`| Error if looping through Dict like list. To loop through keys, `for key,value in dict.items():`| If iterated over 2D numpy array, entire array will be printed. Instead `for i in np.nditer(np_arr):print(i)` will print the first row individually and then the second and so on.| Providing only name of the DataFrame loops it through the headings, iterating through each rows require a `iterrows()` method. e.g. `for labl,row in my_df.iterrows(): print(labl + ':' row)` prints row label follows by all row column values|



