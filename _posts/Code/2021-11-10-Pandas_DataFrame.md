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
- You can use several built-in methods such as `.mean(),.median(),.max(),.min(),.std(),.var(),.cumsum(),.cummin()` for calculating mean, median, max, minimum, standard deviation, variance, cumulative sum, cumulative minimum, respectively.
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

### Merging dataframes
- Called as a method
- Merging/Joining DataFrames on a common column can be done using `my_df.merge(my_df1,on='common_col')` All other common columns will be written with a suffix of `_x` for `my_df` and `_y` for `my_df1`. To add your own suffixes, include the syntax `suffixes='_suff_x','suff_y'` in the merge call.
- Merging can be done in multiple ways with parameter `how`:
|`how`|Description/Venn equivalence|Application/Caution|
|---|---|---|
|`inner` (default)| Merges only common elements (A\bigcap B)|Can result in loss of data|
|`right`|Merges the left DF on all elements of the right dataframe but only those on the left where the column id matches the right column. Elements not in the other DF becomes `NaN`| Preserves data|
|`left`|Similar to `right`, but the all elements are merged on the left DF| |
|`outer`| Merges all data| Can be used to find not common elements|
- Merging table on itself is also desirable when the data are of some types such as hierarchical, graph data. This helps compare column within a table to same column.
- Merging can be validated in order to force a specific relation to be met by using the parameter `validate=None` (default value) to `validate = 'one_to_many'` or `many_to_one, many_to_many,one_to_one`. 

### Concatenating dataframes
- Called as a function using `pd.concat([list_of_df_to_be_merged],ignore_index=False,join='inner',sort=True,keys=[list_of_keys])`. Default value are listed in the above call. 
- `Ignore_index` set as `False` duplicates index regardless of the dataframes, set as `True` reindexes from 0 to n-1. 
- Default for `join` is `inner` and other options (as per given for `merge` can be selected)
- The parameter `keys` add a label next to the first index of each merged dataframe, and reindexes the columns for each dataframe from 0 to n-1.

### Appending Dataframes
- Called as a method on a dataframe
- Simplified version of concat, done using a similar call `df1.append(df2,ignore_index=False,sort=True)`
-  Does not support `keys` or `join`. By default it is always `join=outer`

### Merge_ordered function
- Similar to `merge`, has similar use of `how`, `on`, `left_on`, and `right_on`, `suffixes`.
- Default merge is `how='outer'`
- Useful for Date/Time series data

### Merge_asof() function
- Can be used when merging two time series or date dataframes such that for any time for the left dataframe, a value in the right dataframe where the time is closest (or less than the time index on the left dataframe) is selected.
- `df1.merge_asof(df2,suffixes=('_s1','_s2'),direction='backward')`, default for direction is 'backward'. Possible values for 'direction' are `forward, backward,nearest`.
- This is amazing!
