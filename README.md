# yololist
hashable lists

## Usage
```python
>>> mylist = [1, 2, 3]
>>> mydict = {}
>>> mydict[mylist] = 'fail'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

That's frustrating.  Let's try it again...

```python
>>> from yololist import Yololist as list
>>> mylist = [1, 2, 3]
>>> my_yololist = list(mylist)
>>> mydict = {}
>>> mydict[my_yololist] = 'pass'
>>> # Let's get crazy.
... 
>>> print(mydict)
{[1, 2, 3]: 'pass'}
>>> my_yololist.append(9)
>>> my_yololist[0] = 9
>>> print(mydict)
{[9, 2, 3, 9]: 'pass'}
```

## Warning
This should never be used, under any circumstance.
