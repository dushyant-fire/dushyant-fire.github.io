import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import numpy as np

plot_save_dir = '../../assets/images/Code_blog_pics/'

# Stackoverflow debug - Plotting lineplot for rows
# # One approach is by transposing the columns 
# new_dict = {"Group":[1,2,3],"Week1":[51,20,12],"Week2":[21,87,40],"Week3":[3,10,90]}
# my_new_df = pd.DataFrame(new_dict)
# my_new_df = my_new_df.set_index("Group")
# print(my_new_df)
# transposed = my_new_df.T
# print(transposed)
# lines = itertools.cycle(['-','--','-.'])

# fig,ax = plt.subplots()
# for i in transposed.columns:
# 	print(i)
# 	sns.lineplot(x=transposed.index,y=transposed[i],marker='*',ax = ax,label="Group " + str(i),linestyle=next(lines))
# # transposed.plot(x=transposed.index,y=transposed[1])

# ax.set(ylabel='Group number')

# plt.show()
# fig.savefig(plot_save_dir + "debug_lineplot.png")

## Plotting problem 1.10 chapter 1 heat and MT

x = np.array(range(0,1,0.01))
print(x)

