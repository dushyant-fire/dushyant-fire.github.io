dict={'key1':'value','key2':'value2','key3':'value3'}
# list = ['a','b','c','d']
list = [1,2,3,4]
import pandas as pd
import numpy as np

np_arr = np.array(list)
print(type(np_arr))
print(np_arr[3])

my_dict = {'var1':['A1','A2','A3'], 'var2':[3,4,5]}
my_df = pd.DataFrame(my_dict)
print(my_df)

### inspecting and selecting datatypes
print(my_df.describe())

print(np.logical_or(my_df[['var1']]=='A1',my_df[['var1']]=='A2'))

print(my_df.loc[0,'var1'])

print(dict['key2'])
list2 = list+ [5]
print(list2)

print(my_df[my_df['var2']>3])

select_only = ['A1','A3']
print(my_df[my_df['var1'].isin(select_only)])

print(my_df.sort_values('var1',ascending=False))

### adding columns to dataframes
my_df["var3"]=my_df["var2"]**2
print(my_df)

### Summary statistics
print(my_df[["var2","var3"]].agg([np.mean,np.median]))




