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

print(my_df.sort_values('var1',ascending=False))

output:
  var1  var2
2   A3     5
1   A2     4
0   A1     3
```
DataFrames can also be sorted by indexes
- Creating an index: `DataFrame.set_index("Column name")`
- Sorting by index: `DataFrame.sort_index(level="column name")` Can use multiple indices for a DataFrame

### Adding and creating columns

```py
my_df["var3"]=my_df["var2"]**2
print(my_df)

output:
  var1  var2  var3
0   A1     3     9
1   A2     4    16
2   A3     5    25
```

### Summarizing statistics
- You can use several built-in methods such as `
.mean(),.median(),.max(),.min(),.std(),.var(),.cumsum(),.cummin()` for calculating mean, median, max, minimum, standard deviation, variance, cumulative sum, cumulative minimum, respectively.
- An important way of aggregating method calls is by using `.agg()` to compute multipole statistics on multiple columns with one single method call:

```py
print(my_df[["var2","var3"]].agg([np.mean,np.median])) # I am using numpy methods so that I don't have to write function definitions for the built-in methods

gives:

        var2       var3
mean     4.0  16.666667
median   4.0  16.000000

```

- Counting values and proportions using `.value_counts(sort=True,normalize=True)` from a DataFrame which is sorted using `.drop_duplicates(subset="column name")`. DataFrames can be sorted on multiple columns by passing a list to the `subset`.

- Aggregating data using:
1. `.groupby()` method to group the DataFrame based on different variables within a column - such as red,green,blue within the column 'colors'
2. Pivot tables: `.pivot_tables(values="Column to calculate statistics",index="columns to group",columns="second optinoal column to group",fill_value=0,margins=True` where the `fill_value` argument fills all NaNs with whatever value given by the user, margins add a cumulative statistics on the right and bottom.
