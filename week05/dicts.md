# Dictionaries

**_Dictionaries_** are _assosciative collections_, i.e., they store pairs
of assosciated values, usually termed as _key:value_ pairs. They may have
different names in other contexts - in C++ they are called _maps_.  

The values in a dictionary can be accessed by using its _key_ as index.  

They _keys_ in a dictionary have to be:  
- immutable, i.e., numbers, strings, tuples (if they don't contain mutable)
elements, etc.  
- unique in a dictionary, i.e., can't be repeated.  

## Syntax

The following code shows different ways of creating dictionaries:  

```python
# curly braces with key:value pairs
tel = {'jack': 4098, 'sape': 4139}	# compare with creating a set!!

#The dict() constructor builds dictionaries directly from sequences of
key-value pairs:
tel2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel2)
# output: {'sape': 4139, 'guido': 4127, 'jack': 4098}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
tel3 = dict(sape=4139, guido=4127, jack=4098)
print (tel3)
# output: {'sape': 4139, 'guido': 4127, 'jack': 4098}


# dict comprehensions can also be used to construct dictionaries
tel4 = {x: x**2 for x in (2, 4, 6)}
print(tel4)
# output: {2: 4, 4: 16, 6: 36}
```

## Basic usage
```python
# values can be accessed by using their keys as indices!
print (tel['jack'])		# access a value
# output: 4098

# what if you index a key that does not exist?
tel['guido'] = 4127		# warning: this will add a new element!!
print (tel)
# output: {'jack': 4098, 'sape': 4139, 'guido': 4127}

# you can remove a key:value pair using the built-in 'del' command
del tel['sape']
tel['irv'] = 4127
print (tel)
# output: {'jack': 4098, 'guido': 4127, 'irv': 4127}

print (list(tel))		# list() operation on a dict returns a copy of keys!
# output: ['jack', 'guido', 'irv']

print (sorted(tel))
# output: ['guido', 'irv', 'jack']

# you can check for the existance of a key
print ('guido' in tel)
# output: True
print ('jack' not in tel)
# output: False
```

## Looping over a dictionary  
The _dict.items()_ method can be used to retrieve _key:value_ paris:
```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

# output: gallahad the pure
#         robin the brave
```


Links:  
[Dictionary View Objects](https://johnlekberg.com/blog/2020-09-19-dict-view.html)

```python
```


