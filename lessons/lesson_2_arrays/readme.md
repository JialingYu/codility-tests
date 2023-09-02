# Arrays
**Example**: return the reverse of a list

```python
def reverse(a):
    """
    Parameters
    ----------
    a : list
        input a list

    Returns
    -------
    a : list
        the reverse of a 
    """
    k = len(a)
    # iterate over the first half of the list
    for i in range(k//2):
        # swap two positions
        a[i], a[k-i-1] = a[k-i-1], a[i]
    return a
```
