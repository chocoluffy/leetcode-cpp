## `xrange` or `range`
> `xrange`提供的是iterator，对内存比较好。
```python
Python 2：
for i in xrange(0,10,2):
  print(i)
  
Python 3
for i in range(0,10,2):
  print(i)
Note: Use xrange in Python 2 instead of range because it is more efficient as it generates an iterable object, and not the whole list.
```

## `yield` or `return`
yield可以和for loop搭配使用，尤其是当需要返回特别大的占用内存的东西的时候，用yield形成一个generator，每次只有一个对象return。而return必须将所有对象都保存进内存再返回。

## logic
greedy evalution, thus `False and Error(list index out of range)` will still give `False`, but no error.