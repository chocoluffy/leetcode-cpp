## set
去掉duplicates的操作：
```python
s = set([])
s.add()

# or
s = list(set(a)) # 转换为list
```

## sorted
返回一个新的list，来实现排序。
```python
a = sorted(a) # 从小到大
a = sorted(a, reverse = True) # 从大到小
a = sorted(a, key = a[1], reverse = True) # 以a[1]作为排序的根据
# 当a为str array时，默认排序为alphabetical order从小到大。

#当需要根据多个属性来排序的时候，首先按照第一个属性排序，当第一个属性持平的时候根据第二个属性来排序：
# 例一
a = [('Al', 2),('Bill', 1),('Carol', 2), ('Abel', 3), ('Zeke', 2), ('Chris', 1)] 
b = sorted(a, key = lambda x: (-x[1], x[0])) # 先根据数据从大到小，打平的时候根据字母顺序。

# 例二
d = ["ale","apple","monkey","plea", "alea"]
sorted(d, key = lambda x: (-len(x), x)) # 先按长度从大到小，打平的时候按照字母顺序。
['monkey', 'apple', 'alea', 'plea', 'ale']
```

## in-place operations
一些操作是直接修改原有数据的，因此也会返回None，特别注意不能用于返回赋值。
```python
lst.reverse()
lst.sort()
```

## bisect获得rightmost插入位置
返回插入该元素以保持ordered顺序的rightmost位置(index)。
```python
import bisect
a = [1, 2, 4, 4, 5]
print bisect.bisect(a, 6) # 5
```

## stack using list
```python
# stack using list
stack.append("Iqbal")
print(stack.pop())
```

## queue using deque
```python
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
queue.append("Akbar")
print(queue.popleft())                 
print(queue)
```