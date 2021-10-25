# Tuples

Like **_lists_**, **_tuples_** are _sequence data types_ with the difference that they are _imutable_.  

## Syntax

The following code shows different ways of creating tuples:  

```python
# create a tuple with three elements
t = 12345, 54321, 'hello!'
print (t)

# or alternatively:
t2 = ('abc', 123, 44.6)
print (t2)
# output: ('abc', 123, 44.6)

print (t[0])
# output: 12345
```
Notice how a tuple can be created by specifying comma-separated values either
with or without parentheses. They, however, are always displayed with the
parentheses.   

Empty and single-element syntax is slightly peculiar:  
```python
empty = ()
singleton = 'hello',    # <-- note trailing comma
print (len(empty))
# output: 0
print (len(singleton))
# output: 1
print (singleton)
# output: ('hello',)
```

Tuples can be nested:  
```python
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print (u)
# output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
```

Tuples are immutable:  
```python
# Tuples are immutable:
t[0] = 88888
# output: Traceback (most recent call last):
# output: File "<stdin>", line 1, in <module>
# output: TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print (v)
# output: ([1, 2, 3], [3, 2, 1])
```

### Packing and Unpacking
```python
# packing values into a tuple
t = 12345, 54321, 'hello!'

# unpacking tuple values
x, y, z = t
```


#### Disclaimer
Code examples are ~taken~ inspired from various sources including:  
[Python tutorial](https://docs.python.org/3/tutorial/)  
