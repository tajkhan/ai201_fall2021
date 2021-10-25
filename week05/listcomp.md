# Lists

## List comprehensions contd...

Below is how we would create nested lists, i.e., lists of lists, using list
comprehensions. A 2D matrix shown below:   

matrix = [
  [1, 2, 3, 4],  
  [5, 6, 7, 8],  
  [9, 10, 11, 12],  
  ]

```python
matrix = [[row[i] for row in matrix] for i in range(4)]
print(matrix)
```
