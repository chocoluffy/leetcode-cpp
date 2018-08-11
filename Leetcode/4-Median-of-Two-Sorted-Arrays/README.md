# 思路(C++)

重点在Algorithm。

## intuition: 

- tree structure of (m+n) elements. 

- binary search at both array at same time. and adjust by comparing each own middle in order that there will be half element at each side.

> final submission idea: do binary search on the shorter array between nums1 and nums2. note that "median" means find an element splitting the array such that two side have same length and the maximum number of one side is always smaller than the minimum number of the other side.

## analysis

- binary search in c++.

```
while(min <= max) {
    target = array[(min + max) / 2]; 
    if (target < guess) {
        min = target;
    } else {
        max = target;
    }
}
```

## hard part

edge case analysis. 

- when index will overflow the array or underflow. use `max(index + 1, array_size)` and `min(index - 1, array_size)` to ensure no seg fault.

- array splitting problem, need to pay attention to two specific positions. [1] split at index -1, meaning taking none from this array for left hand side, and taking all elements for right hand side. [2] split at index `array_size`.
