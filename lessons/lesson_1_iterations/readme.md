# Iterate using for and while loops
## For loops
For loop iterate over a container like list, set, tuple, dictionary. The length of iteration is fixed and known.  
When iterate over a list, the iteration is in order; when iterate over a tuple, the iteration is in order; when iterate over a set, the iteration is random; when ietrate over a dictionary, we in fcat iterate over its keys, and the order is random.

## While loops
When the length of iteration is unknown and we iterate as long as a condition is true, we use while loop + condition.

**Example**: print the Fibonacci number as long as it is smaller than 100.

```python
a=0
b=1
while a<100:
    print(a)
    c=a+b
    a=b
    b=c
```
