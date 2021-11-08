# Functions ... continued.

```python
def my_sum(a, b):
    return a + b
```

## Passing variable number of arguments to a function.

```python
# sum_integers_list.py
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))
```

### \*args
\* can receive multiple *positional* arguments.

```python
# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))
```
\* is called the *unpacking operator* and when used in a function definition
it collects/packs the parameters it receives in a *tuple*!


### \*\*kwargs
\*\* can receive multiple *keyword* arguments.

```python
# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
```

\*\* is called the *unpacking operator* and when used in a function definition
it collects/packs the parameters it receives in a *dictionary*!

### Function arguments order.
The function arguments should be in the following order:  
1. Standard arguments.
2. \*args
3. \*\*kwargs

```python
# correct_function_definition.py
def my_function(a, b, *args, **kwargs):
    pass


# wrong_function_definition.py
# def my_function(a, b, **kwargs, *args):
#    pass
```

## Using \* and \*\* as unpacking operators.

Both \* and \*\* can be used to unpack the values from *iterable* objects.
 
Remember how we could unpack composite types.
```python
# tuple unpacking
x = (3,4)
a, b = x
```

We can use \* for unpacking.
```python
# tuple unpacking
x = (3,4)
a, b = *x
```


### Unpacking with \*
```python
# compare
my_list = [1, 2, 3]
print(my_list)

# vs

my_list = [1, 2, 3]
print(*my_list)
```
\* operator used in a function call unpacks the arguments and then they are
passed to the function separately.

For unpacking, the container iterable should have the same number of elements
as the number of function arguments receiving them.  

Multiple \* operators in a function call can be used. They all will do their unpacking and the unpacked elements, combined, will be passed the function separately as *positional* arguments.  

```python
# sum_integers_args_3.py
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))
```
```python
# merging_lists.py
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)
```

When used on LHS of an assignment operator, the unpacking operator \* should
be member of a tuple or a list.
```python
# *a = 1,2,3	# Error: LHS * operator not in a tuple even though RHS is tuple
# *a = (1,2,3)# Error: LHS * operator not in a tuple even though RHS is tuple
# a, = 1,2,3	# Error: LHS only expects 1 value, RHS has 3 to unpack!

# a = 1,2,3		# wrong as a receives a tuple

*a, = 1,2,3
print(a)
b,*a = 1,2,3
print(a)
```

We can use the unpacking operator to split lists or extract its elemetns.  

```python
# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6]

# a, b, c = my_list[0], mylist[1:5], mylist[5] # This is much cumbersome!

a, *b, c = my_list	# Unpacking syntax is much better!

print(a)
print(b)
print(c)


# *a, b, c, d, e = 1, 2, 3	# Error: not enough values for compulsory assmts.

*head, a, b = range(5)			# Unpack and split a generator

# *head, *tail = range(5)		# Error: can't have two starred expr on LHS
```

Above the unpacking should compulsarily supply values for *a* and *c*. *b*
bearing the \* operator can be empty.  

It can also be used to extract values from a generator.
```python
gen = (2 ** x for x in range(10))
print(gen)
*g, = gen
print(g)

# *r = range(10)	# Error: LHS starred element not part of tuple or list.
```

Unpacking also happens in for loops.
```python
for first, *rest in [(1, 2, 3), (4, 5, 6, 7)]:
	print("First:", first)
	print("Rest:", rest)
```

\* can also be used to unpack strings.  
```python
# string_to_list.py
a = [*"Ding dong"]
print(a)
```


### Unpacking with \*\*

\* can be used on any iterable object but \*\* can only be used on dictionaries.

When used in function calls, \*\* will *unpack* its arguments and they will be passed to the function separately, each as a *keyword* arugment.  

```python
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
```

We can also use it to merge dictionaries.  

```python
# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
```

References:  
[\* and \*\* (realpython.com)](https://realpython.com/python-kwargs-and-args/)  
[Link in above article](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#Asterisks_for_unpacking_into_function_call)  
[Some code taken from](https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/)  
