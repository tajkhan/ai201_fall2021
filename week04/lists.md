

## Zip lists:
Sometimes we'd like to combine data from two separate lists and do something
with them pairwise. One way of doing that may be:

```Python
x = [1935,1940,1945,1950,1955,1960,1965,1970,1975,1980]
y = [32.1,30.5,24.4,23,19.1,15.6,12.4,9.7,8.9,7.2]
print(' Year Population')
for i in range(0,len(x)):
  print('{:5d}    {:>4.1f}'.format(x[i],y[i]))
```

Another way, if we would like to get rid of the indexing and stuff, is to use
the python _zip()_ function which combines two lists to return a list of tuples,
called _zip list_,
whose each element comes from one of the two lists. We can then iterate over
this resultant list of tuples.
```Python
x = [1935,1940,1945,1950,1955,1960,1965,1970,1975,1980]
y = [32.1,30.5,24.4,23,19.1,15.6,12.4,9.7,8.9,7.2]
data = list(zip(x,y))
print(' Year Population')
for year,pop in data:
  print('{:5d}    {:>4.1f}'.format(year,pop))
```

```Python

```

## Points to ponder:
1. What is an _Sequence Type_?
2. What is an _Iterable_?
