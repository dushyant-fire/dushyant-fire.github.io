dict={'key1':'value','key2':'value2','key3':'value3'}
# list = ['a','b','c','d']
list = [1,2,3,4]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fig_save_dir = '../assets/images/Code_blog_pics/'

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
extra_cols = {'var1':'A1','var2':3}
my_df=my_df.append(extra_cols,ignore_index =True)
my_df["var3"]=my_df["var2"]**2
print(my_df)
row_data = my_df[my_df["var1"]=="A3"]
print(row_data)

exit()

### Summary statistics
print(my_df[["var2","var3"]].agg([np.mean,np.median]))

pivoted = pd.pivot_table(my_df,values=['var2','var3'],index='var1',aggfunc=['mean','sum'])

print(pivoted)

melted = my_df.melt(id_vars='var1',value_vars='var2')
print(melted)

def func1():
	x=1
	print(x)

func1()

def func2(x,n=1): # creates a variable n with default parameter 1
	sq = x**n
	return sq
print(func2(4,3))

def func3(*args): # Function with variable non-keyworded input parameters
	sum_all=0

	for i in args:
		sum_all = sum_all + i

	print(sum_all)

func3(2,3,4)

def func4(**kwargs): # Function with variable kew-worded input parameters, by default it creates a dictionary of all niput parameters to be looped over later
	
	print("\n New Person")
	for key, value in kwargs.items():
		print(key + ':' + value)

	print("\n Entry Completed")

func4(Name='Daniel',Occupation='Carpenter',Salary='100000')

func_lambda = lambda x,y:x**y
output = func_lambda(2,3) 
print(output)

def errors_func_sqrt(x):
	# if x<0:
	# 	raise ValueError('x must be non-negative')
	try: # will try to execute this
		sq = x** -0.5
	except TypeError: # Excluding only TypeErrors
		print('x must be int or float')

errors_func_sqrt('hi')

enum_obj = enumerate(range(4))
# print(*enum_obj)
for x1,x2 in enum_obj:
	print(x1,x2)

arms = [1,1.04,0.9]
heights = [arm_length*1.8 for arm_length in arms]
print(heights)

arms = [1,1.04,0.9]
heights=[]
for arm_length in arms:
	heights.append(arm_length*1.8)
print(heights)

sns.palplot(sns.color_palette('coolwarm',6))

# plt.savefig(fig_save_dir+'Diverging_palette.jpeg')

# plt.show()

## Datetime objects
import datetime as dt
date = dt.datetime(2022,1,25,15,53,43)
print(date.isoformat())
print(dt.datetime.today())

time_diff = dt.timedelta(hours = 10)
date_new = date + time_diff
print(date_new)

ET = dt.timezone(dt.timedelta(hours=-5)) # Eastern standard time, timezone object
#adding timezone to date info
dt_with_tz = date.astimezone(ET)
print(dt_with_tz)

dt_string = "2022-01-22 1:00:01"
dt_format = "%Y-%m-%d %H:%M:%S"
print(dt.datetime.strptime(dt_string,dt_format))
print(date.strftime("The person was seen on %Y/%m/%d at %H hours, %M minutes on the street of D.C."))
print(time_diff.total_seconds())
exit()
## Analyzing FIFA dataset for fun visualizations

import matplotlib.pyplot as plt
import seaborn as sns

fifa_dir = 'FIFA22 Dataset/'

players = pd.read_csv(fifa_dir + 'players_fifa22.csv')
teams = pd.read_csv(fifa_dir + 'teams_fifa22.csv')

print(players.columns)
print(teams.columns)

print(teams.iloc[0])

top_10_teams = teams.nlargest(10,'IntPrestige')
print(top_10_teams)

# plt.scatter(players['Height'],players['HeadingAccuracy'])
# plt.show()
