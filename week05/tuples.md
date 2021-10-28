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
# compare with: singleton = 'hello'
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

v[0][1] = 55 
print (v)
# output: ([1, 55, 3], [3, 2, 1])
```

### Packing and Unpacking
```python
# packing values into a tuple
t = 12345, 54321, 'hello!'

# unpacking tuple values
x, y, z = t
```

As opposed to _sets_, _tuples_ themselves are immutable but there elements can be mutable.


## Tuple uses:
Although both _lists_ and _tuples_ are can have heterogenous data, lists are
usually used to process same type of data and tuples for hetergenous data.
Tuples are especially useful in situations where data items belong together and would not make sense by themselves.

Here is an example. The list below shows currency codes for a number of currencies and the exchange rate from US dollars to that currency. The numbers in each case show how many units of the currency one US dollar would buy.

```python
exchange = [('EUR' , 0.869335) , ('JPY' , 113.0005) ,\
('GBP' , 0.760425) , ('AUD' , 1.40553) , ('CAD' , 1.29406) ,\
('CHF' , 0.99148) , ('CNY' , 6.9228) , ('SEK' , 9.09429) ,\
('NZD' , 1.54148) , ('MXN' , 18.99626) , ('SGD' , 1.3809)]
```

Because the list spans multiple lines, I have used the Python continuation character, \, at the end of each line.

Suppose we wanted to write a program that prompts the user to enter a code for a foreign currency and an amount of that currency that the user wants to purchase. The program will compute and print how many US dollars it would take to purchase that many units of the currency. Here some code that will do this.

```python
exchange = [('EUR' , 0.869335) , ('JPY' , 113.0005) ,\
('GBP' , 0.760425) , ('AUD' , 1.40553) , ('CAD' , 1.29406) ,\
('CHF' , 0.99148) , ('CNY' , 6.9228) , ('SEK' , 9.09429) ,\
('NZD' , 1.54148) , ('MXN' , 18.99626) , ('SGD' , 1.3809)]
code = input('Enter a currency code: ')
amount = float(input('How many units do you want to buy? ')

cost = 0
for pair in exchange:
  if pair[0] == code:
    cost = amount/pair[1]

if cost != 0:
  print('Your cost is $'+str(cost))
else:
  print('You did not enter a valid code.')
```

An alternative to using the index notation for tuples in a for loop is to use a form of the for loop that assigns each member of a tuple to a different loop variable:

```python
for c,r in exchange:
  if c == code:
    cost = amount/r
```

## Tuple comprehensions
If we try to use a list comprehension on tuples like this:
```python
tup = (i**2 for i in range (10) if i%5 == 0)
print(tup)
print(type(tup))
```
We see that we get a _Generator Object!!_. Generators (see references below)
is another important concept in Python. However this generator object can be
converted to a tuple:

```python
tup = tuple((i**2 for i in range (10) if i%5 == 0))
print(tup)
```

There are other workarounds as well, e.g., using list comprehension indireclty
to generate a tuple:

```python
tup = tuple([i**2 for i in range (10) if i%5 == 0])
print(tup)
```

Using a trailing comma and an asterisk:
```python
# A trailing comma alone is not sufficient:
tup = (i**2 for i in range (10) if i%5 == 0),
print(type(tup))
print(tup)

# We also need an asterisk:
tup = *(i**2 for i in range (10) if i%5 == 0),
print(type(tup))
print(tup)
```

## Points to ponder:
1. What is a _generator_ in Python? Where and Why is it used?
2. What is the difference between an _iterator_ and a _generator_?

References:
[Some code from here](https://www2.lawrence.edu/fast/GREGGJ/CMSC210/loops/tuples.html)  
[Tuples vs Lists (stackoverflow)](https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples)
[Tuple uses (stackoverflow)](https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each)
[Tuple comprehensions](https://www.pythonpool.com/tuple-comprehension/)  
[Why no tuple comprehension (stackoverflow)](https://stackoverflow.com/questions/16940293/why-is-there-no-tuple-comprehension-in-python)  
[Generators (Python Tips)](https://book.pythontips.com/en/latest/generators.html)  
[Generators (Section.io)](https://www.section.io/engineering-education/python-generators/)  
[Generators vs Iterators (stackoverflow)](https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators)  
[Generators and Iterators (Python practice)](https://anandology.com/python-practice-book/iterators.html)  
[() Generator Expression (python-reference)](https://python-reference.readthedocs.io/en/latest/docs/comprehensions/gen_expression.html)
