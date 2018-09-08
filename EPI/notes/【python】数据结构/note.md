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
# 当a为str array时，默认排序为alphabetical order。
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