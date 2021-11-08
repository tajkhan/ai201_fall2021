# Restricting function arguments

Normally you can pass function arguments as either *positional* or *keyword* methodologies.  

We can, however, restrict certain arguments so that they are always passed using *positional* and others such that they have to be passed in the *keyword* style. For this we use the / and \* operators to separate function arguments when defining a function.    

```python

# Syntax: (pos_only_args, /, pos_or_keyword_args, *, keyworkd_only_args)

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```
