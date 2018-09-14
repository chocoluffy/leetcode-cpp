## OJ里用python的解法
在遇到runtime error的时候需要注意的地方：
- recursion function stack mem. 尽量少引入可能尺寸过大的全局变量。如果能够直接改动数据首选直接改动用作flag。
- 尽量避免O(n^2)复杂度的算法，在hackerrank上容易runtime error。
- 多使用python built-in的操作比如，set(), sorted()等等来加速，以及保持算法简洁。

# String
### 将string的all chars转换为list
`lst = list('hello') # return ['h', 'e'....]`

### string reverse
`s[::-1]`可以获得s的反转。
```
def is_palindrome(s):
	return s == s[::-1]
```

# Dictionary
### dictionary return value防止key not found
`a = {}, b = a.get('s', 0)`, 当's'不存在a里面的时候，返回0。

### .iteritems() 遍历dictionary
```python
for k, v in d.iteritems():
	print k, v
```

### 使用defaultdict()
```python
from collections import defaultdict
a = defaultdict(int)
a = defaultdict(list)
a = defaltdict(lambda: 3) # set default value.
```

# Array
### enumerate: 重组array获得元素的index
`s = {s: i for i, s in enumerate(str_lst)}`

