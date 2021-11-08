# Lambda Functions

In Python, Lambdas are functions but:  
1. they are anonymous functions
2. they can only contain expressions and can’t include statements in its body.
3. they are written as a single line of execution

## Functions vs Lambdas
Consider the following functions:  
```python
# sum two numbers
def sum (a, b):
	return a+b

# find min of two numbers
def min (a, b):
	if a<b:
		return a
	else:
		return b
```

The equivalent lambda will be:  
```python
lambda a, b: a+b

lambda a, b: a if a<b else b
```
Lambda functions are defined using the keyword *lambad*. We can make a few
observations about the lambda functions:  
1. they do not have names (anonymous)
2. they do not use parentheses for function arguments
3. their body only contains a single *expression*
4. they do not have a *return* statement. The lambda function automatically
returns the result of the expression comprising its body.

Each lambda function returns a *callable* object (a function object).  

Although we can assign names to these nameless functions and call them but that is not the purpose!  
```python
mysum = lambda a, b: a+b

print(mysum(3,5))

# we can even direclty call them when defined!!
print( (lambda a, b: a if a<b else b)(345, 298) )
```

## Passing function objects
Lambdas are really handy when we need to pass function objects as arguments
to other functions. Consider the following code.
```python
def makeeven (arg):
  if arg%2==0:
    return arg
  else:
    return arg+1

def apply_function(fn, lst):
  lr = []
  for x in lst:
    lr.append(fn(x))

  return lr

print(apply_function(makeeven, [1,3,4,6,9,0]))
```

This small function can be constructed on the fly using a lambda instead of
declaring it separately.
```python
def apply_function(fn, lst):
  lr = []
  for x in lst:
    lr.append(fn(x))

  return lr

print(apply_function(lambda x: x if x%2==0 else x+1, [1,3,4,6,9,0]))
```

There are many functions in python that take function objects are their
arguments. Foremost among them are the so-called *key functions*.
```python
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids)) # Lexicographic sort

sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
print(sorted_ids)
```

Similarly there are map() and filter().
```python
list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))

list(filter(lambda x: x%2==0, range(11)))
```


# References:
[How to use Python Lambda functions.](https://realpython.com/python-lambda/)
