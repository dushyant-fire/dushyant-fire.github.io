---
layout:	default
title:	"Approaches"
category:	code
date:	2021-11-10 15:00:00 -0000
permalink:	/code/Python/Data_approaches
---

## Approaches for data analysis using Python

### Finding if two lists have a shared element

- There are at least four ways to approach this problem. More details with respect to time taken for each approach is mentioned in the answer to the <a href="https://stackoverflow.com/questions/3170055/test-if-lists-share-any-items-in-python" target="_blank"> Stackoverflow question</a>

- Using `any()` provides an easy solution and can be impemented by the following `any(i in neglect_strings for i in quad.split('_'))`. In short, the built-in function `any([condition 1, condition 2,..])` behaves like a logical *OR* operator (similar to `|`,`and(A,B)` in MATLAB), and `all()` behaves like a logical *AND* operator (`&`, `and()` in MATLAB)



