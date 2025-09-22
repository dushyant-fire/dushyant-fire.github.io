---
tags: 
 - work
 - python
draft: false
date: 2021-11-02
modified: 2025-09-21
---

## The Zen of Python, by Tim Peters

Written by Tim Peters. Can be retrieved using `import this`, which gives:

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren't special enough to break the rules.
- Although practicality beats purity.
- Errors should never pass silently.
- Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one-- and preferably only one --obvious way to do it.
- Although that way may not be obvious at first unless you're Dutch.
- Now is better than never.
- Although never is often better than *right* now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea -- let's do more of those!

## Python setup

Python is packaged by many organizations. Most of them are open-source and here are some ways to setup python

- Anaconda
	- Download Anaconda package manager directly from Anaconda
	- **Advantage**: 
		- Easy to install, 
		- GUI setup for installation, 
		- Can use packages only available on conda distribution
	- **Disadvantage**: 
		- Heavy, 
		- Installs unnecessary packages that you would never know of or use
		- Virtual environments can be hard to couple with other programming needs
- Miniconda
	- My favorite if I need packages distributed on conda. 
	- *Highly recommend this over Anaconda distribution for beginners*
	- A lighter version of conda, that can be installed from terminal/PowerShell. Follow Anaconda's miniconda installation guide to the point. 
	- **Advantage**: 
		- Easy to install, 
		- GUI setup for installation, 
		- Can use packages only available on conda distribution
	- **Disadvantage**: 
		- Requires a little bit of experience regarding what to install and how. For example, you will need to install Jupyter separately
		- Virtual environments can be hard to couple with other programming needs
- Python install
	- Install python from python.org
	- Use pyenv for virtual environment creation
	- **Advantage** with this approach is that you can clearly manage virtual environment with much ease than conda distributions
	- **Disadvantage** with this approach is that you need to setup entire environments manually. This gets easier once you know what you want.
