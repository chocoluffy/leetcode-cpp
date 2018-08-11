# 思路(C++)

重点在implementation。

- deque

- map<char, int>
优化这个结构的时候，可以考虑bitmap的使用。类似bucketsort的原理。如果是字符则是默认256长度的bitmap，然后对应的位置放置其value。

- vector