---
layout:	default
title:	Approaches for data analysis using Python
category:	code
date:	2021-11-10 15:00:00 -0000
permalink:	/code/Python/Data_approaches
---

### Finding if two lists have a shared element

- There are at least four ways to approach this problem. More details with respect to time taken for each approach is mentioned in the answer to the <a href="https://stackoverflow.com/questions/3170055/test-if-lists-share-any-items-in-python" target="_blank"> Stackoverflow question</a>

- Using `any()` provides an easy solution and can be impemented by the following `any(i in neglect_strings for i in quad.split('_'))`. In short, the built-in function `any([condition 1, condition 2,..])` behaves like a logical *OR* operator (similar to `|`,`and(A,B)` in MATLAB), and `all()` behaves like a logical *AND* operator (`&`, `and()` in MATLAB)

- Finding location of an element in a list:
```
index = ['A','B','C','D','E'].index('B')
print('index = ' + str(index)')
```
gives, `index = 1`

### Finding if a variable exist in Python
- Local search:
`if 'myVar' in locals():`
- Global search:
`if 'myVar' in globals():`

Remember to include the quotes('') around the variable name.

### Merging DataFrames
- If two DataFrames called `df1` and `df2` exist such that,

```
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)


df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)
```
Then,

```
frames = [df1,df2]
df3 = pd.concat(frames)
print(df3)
```
will give:

```
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
```
### Ways to add multiple legend in the `Matplotlib.pyplot` plot

- Suppose you have a plot with muliple markers denoting set of temperature data and multiple lines denoting the average temperature. If you need to add legend to reflect both the markers and the average lines, multiple legend can be added in the following ways:
1. Collecting the plot/error bars in a `matplotlib.pyplot` container by assigning a variable to the particular plot function, and then calling individual container variables to set it as a legend. This also requires adding an _artist_ which allows manual addition of _art_ on the plots, which is done by `axes/plt/fig.add_artist()` command

```
import matplotlib.pyplot as plt

fig,ax1 = plt.subplots(figsize=(6,4))

# collecting the plot in containers
line1 = ax1.plot([1, 2, 3], label="Line 1", linestyle='--')
line2 = ax1.plot([3, 2, 1], label="Line 2", linewidth=4)

first_legend = ax1.legend(handles=line1, loc='upper right')

ax1.add_artist(first_legend)
ax1.legend(handles=line2, loc='lower right')

plt.show()

```

This gives:

![Container and add_artist multiple legend](/assets/images/Code_blog_pictures/Multiple_legends_container.png "Multiple legend")




