# Sets

**_Sets_** are collections in Python which are:  
- unordered, i.e., the order of elements is not guaranteed and they are
unindexable!  
- have no duplicate elements  
- each element is a _hashable_ type

You can use them to eliminate duplicate entries of a sequence and  
test for _membership_, i.e., whether a member is present in a set or not.  

## Syntax

The following code shows different ways of creating sets:  

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed

print('orange' in basket)  # fast membership testing

print('cabage' in basket)
```

Sets support common mathematical set operations, e.g, _difference, union, intersection, exclusive OR,_ etc.  

```python
# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)               # unique letters in a

print(a - b)           # letters in a but not in b

print(a | b)           # letters in a or b or both

print(a & b)           # letters in both a and b

print(a ^ b)           # letters in a or b but not both

```

Like _list comprehensions_, sets also support _comprehensions_, i.e,, we can
create sets using comprehension syntax:  
```python
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
```

As opposed to _tuples_, _sets_ themselves are mutable but there elements are not.

## Points to ponder:
1. Can we have a list of sets? Why?
2. Can we have a set of lists? Why?
3. What does hashable mean in Python? Where do we need hashable types? Why?

## Links:  
[Unorderliness of sets](https://stackoverflow.com/questions/21701618/why-does-a-set-display-in-same-order-if-sets-are-unordered)
[Why set elements have to be hashable?](https://www.reddit.com/r/learnpython/comments/6zwefw/comment/dmyj8sv/?utm_source=share&utm_medium=web2x&context=3)
