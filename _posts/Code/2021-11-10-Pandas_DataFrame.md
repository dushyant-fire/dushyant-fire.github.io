---
layout:	default
title:	"Pandas DataFrame"
category:	code
date:	2021-11-24 18:00:00 -0000
permalink:	/code/Python/DataFrame
---

### Inspecting a DataFrame
- If you have a DataFrame like this:

```py
my_dict = {'var1':['A1','A2','A3'], 'var2':[3,4,5]}
my_df = pd.DataFrame(my_dict)
print(my_df)

  var1  var2
0   A1     3
1   A2     4
2   A3     5
```

- `df.head()` - Returns first few rows on the DataFrame
- `df.info()` - Info on each column, its datatyps, and missing values
- `df.shape` - returns rows and columns for the DataFrame
- `.describe()` - calculates few summary statistics of each column 

```py
print(df.describe())

       var2
count   3.0
mean    4.0
std     1.0
min     3.0
25%     3.5
50%     4.0
75%     4.5
max     5.0
```
### Subsetting and sorting DataFrames

```py
----
print(my_df[my_df['var2']>3])

output:
  var1  var2
1   A2     4
2   A3     5

----
select_only = ['A1','A3']
print(my_df[my_df['var1'].isin(select_only)])

output:
  var1  var2
0   A1     3
2   A3     5
```
