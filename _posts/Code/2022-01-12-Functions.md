---
layout:	default
title:	"Functions"
category:	code
date:	2022-01-12 13:00:00 -0000
permalink:	/code/Python/Functions
---

## Scopes

|Local| Global| Built-ins| Non-local|
|---|---|---|---|
|No specific arguyment needed| preceeding argument `global varioable_name` needed to initialize the variable value from a global parameter | such as `sum(), tuple(), abs()`| Requires a keyword `nonlocal` to emphasize that the variable is not local in a nested function.|

### Function with multiple and variable inputs using `def` keyword

```
def func1():
	x=1
	print(x)

func1() # prints 1

def func2(x,n=1): # creates a variable n with default parameter 1
	sq = x**n
	return sq
print(func2(4,3)) # Prints 64

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

## This will print:
#  New Person
# Name:Daniel
# Occupation:Carpenter
# Salary:100000
#
# Entry Completed
```

### `lambda` functions - For oneline functions

Example: 

```
func_lambda = lambda x,y:x**y
output = func_lambda(2,3)
print(output)
``` 
Prints 8, which is 2 raised to 3.

### Error messages and exceptions
- Can be done using `try, except` and `raise` inside the function

For Example:

```
def errors_func_sqrt(x):
	# if x<0:
	#	raise ValueError('x must be non-negative')
	try: # will try to execute this
		sq = x** -0.5
	except TypeErrror: # Excluding only TypeErrors
		print('x must be int or float')
```

Now, if we pass `errors_func_sqrt(-9)` when the if statement line is uncommented, it will raise the `ValueError`, is we pass `errors_func_sqrt('hi')`, it will raise the `TypeError` and print the statement which we asked for.

### Using `docstrings`
- `docstrings` are function information written between ''' and ''' using standard formats
- Google style or Numpy docstring standard can be accessed using `function.__doc__` or using the package `inspect` which can be called by `inspect.getdoc(function)`

### Using context manager
- A *compound* statement such as `with` is used to open a context_manager
```
with open("file.txt") as myf:
	text = myf.read() 

n = 0
for word in text.split():
	if word.lower() == ['bubblegum']
		n = 0

print(n) # Prints out number of times bubblegum word appears in the read file.
```
- Writing context manager using either *classes* or a *function* using the keyword `yield` and using the `@contextlib.contextmanager` decorator (which is a text that goes before the context manager function definition)

```
@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())
```

The above code will open a file as a read_only, as specified within the content manager function

- In order to make sure some part of the code runs (such as closing a file) regardless of some error in coding, use `try`, `except`, and `finally` statements:
```
try:
    # code that may cause exceptions
except:
    # code that handle exceptions
finally:
    # code that runs regardless of the other two statements
```
