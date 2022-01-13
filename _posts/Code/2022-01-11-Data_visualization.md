---
layout:	default
title:	"Data visualization"
category:	code
date:	2022-01-11 13:00:00 -0000
permalink:	/code/Python/DataVisualization
---

## Plotting libraries

|`matplotlib.pyplot`| `seaborn`| `pandas`
|---|---|---|
|Similar to MATLAB's syntax| Simplified form of pandas and matplotlib.pyplot|
|`plt.plot(data['x'],data['y'],marker='o',color='k') \ ax.set_xlabel('xlabel') \ ax.legend()` | `sns.scatter(x="column header",y="column header",data=df)`|`dataframe.plot(kind='bar',data=dataframe,x="col_name",y="col_name")`|
|Requires elaborate definitions of x, y data, and setting other plot parameters | One line code and reduced form of `matplotlib.pyplot`.| Similar to seaborn but not dedicated for plotting|
| *[More info on `matplotlib.pyplot`](https://matplotlib.org/stable/tutorials/introductory/usage.html)* | *[More info on `seaborn`](https://seaborn.pydata.org/introduction.html)* | *[More info on `pandas` plotting](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)* |


### Seaborn

#### Seaborn methods
- `sns.countplot()`, `sns.boxplot()`, `sns.violinplot()`, `sns.pointplot()`

- Global method, `sns.catplot(kind='box/count/violin/point', x="Col_name_for_x", y="Col_name_for_y", data=dataframe_with_columns, ci=[low_confidence, high_confidence], hue = "Col_name_for_hue_or_subgroups",col="Column_name_for_creating_new_plot_for_each_category",col_wrap="number
_of_columns_in_one_line")`

|Seaborn groups that create FacetGrid()|Seaborn individual equivalents| Use case|
|---|---|---|
|`catplot()`| `countplot()`, `boxplot()`, `violinplot()`, `pointplot()`| Catergorical plots|
|`lmplot()`|`regplot()`| Regression plots|
|`relplot()`| `lineplot()`| Relational plots|

#### Labels and titles
- In seaborn, `catplot` (categorical plot), and `relplot` (relational plot) allows creating subplots (using col, col_wrap, or row, row_wrap parameters). Direct methods create a single axes and only the `AxesSubplot` object, while these two methods create a `FacetGrid` object and `AxesSubplot` objects (these objects are used for labeling/titling of the plots).
- Thus, when the seaborn plots are assigned a variable (for example, `g = sns.catplot()`), `g.fig.suptitle('Title of the figure')` creates a title for the figure.
- Similarly, `g.set(xlabel="label for x",ylabel="new label for y")` sets new x, and y labels
- Setting title for `AxesSubplot` objects require, `g.set_title("Title", y= 1.03)`. Here, y = 1.03 pushes the title a little up (default value is 1). This `y` parameter works for `FacetGrid` object too (`catplot` and `relplot`) 
- Rotating x or y tick labels require calling matplotlib's plt like, `plt.xticks(rotation = 90)`
- `sns.despine(left=True)`

#### Figure color and size
- Tick label sizes changed using `sns.set_context('paper/notebook/talk,poster')`, where the scale size increases with the context from 'paper' to 'poster'.
- Color palettes - can be done by using `sns.set_palette("Purples/RdBu")`, example of continuous palette is "Purples", while "RdBu" is a diverging palette from Red to Blue. Custom palette can be set by passing a list of color values in the `set_palette` method.
- Setting background style using `sns.set_style(white/whitegrid/dark/darkgrid/ticks)`, which change the background to `white` (default), `whitegrid` (white with horizontal grids), `dark` (grey background), `darkgrid`, and `ticks` (ticks on x,y axes)
- Visualizing default color palettes of Seaborn,  `sns.palplot(sns.color_palette('husl',10))` will display 'husl' palette once `plt.show()` is executed. 

Similarly, `sns.palplot(sns.color_palette('coolwarm',6))` will create a diverging palette of 6 shades.

<img class="img_article" src="{{ site.github.url }}/_code_for_blog_/Diverging_palette.jpeg">

<p class="caption">Diverging Palette</p>

