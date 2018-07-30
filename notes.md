# 1 two sum

- 最快的算法里对std::sort的使用。

虽然理论上sort是nlogn，但是在实用中sort可以在某些情况下提高速度。尤其当c++的library function对其添加的优化。

# 2 add two numbers

- 想清楚什么时候需要引入dummy node。

常见的原因是为了更简便地处理while loop里面的edge case，比如这里的第一个node的初始化。我们创建新node是依赖while loop的逻辑的，如果为NULL，在loop使用node->next会seg fault。所以通过创建dummy node使得可以直接在loop里使用node->next。然后最后用dummy->next返回整个链的head。

# 3 longest substring without repeating characters

- map<char, int>

优化这个结构的时候，可以考虑bitmap的使用。类似bucketsort的原理。如果是字符则是默认256长度的bitmap，然后对应的位置放置其value。


# 14 longest common prefix

problem: as title.

## ideas

- [me] vertical scanning. time complexity: O(S), where S is the sum of all characters in all string. space complexity: O(1).
- divide and conquer. because LCP satisfies the associative property, that LCP(1,..., n) = LCP(LCP(1,..., n/2), LCP(n/2+1,..., n)). as like in finding min or max. time complexity is O(S), space complexity is O(mlogn), n is the number of string, m is the average length, since divide and conquer requires to store intermediate results.
- binary search. an improvement on the vertical scanning. apply the binary search on the shortest string and do the vertical scanning to validate if it's LCP. time complexity is O(S * log(min string length)), space complexity is O(1).


# 19 Remove Nth Node From End of List

problem: remove the nth node from the linked list. 

## ideas

- two pointers. iterate the linked list in one pass. time complexity O(L), space complexity O(1).


# 21 merge two sorted list

recursion. time complexity: O(n + m). space complexity: O(n + m).

# 22 generate parentheses

problem: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## idea

[me]
- ues a stack to simulate the situation. the left parentheses push in the stack, while the right parentheses pop out the stack.
- how to decide if a combination is well-formed?
when the right parentheses pushes in the stack when the stack is empty, then such combination is not well-formed, such as ())().

```
def print_parenthese(number of pair = n, string s, stack level sl):
    if n == 0:
        results.append(s)
    else:
        print_parenthese(n - 1, s.append('('), sl + 1)
        if sl > 0: // only continue when adding right parentheses will result in well-formed parentheses.
            print_parenthese(n - 1, s.append(')'), sl - 1)

results = []
print_parenthese(3, '', 0)
```

# 23 merge k sorted list

problem: as title.

priority queue. a min heap. assuming there are N elements in total, time complexity: O(k + Nlogk), it takes k to construct a heap, then each time take logk to rearrange the heap.

# 26 remove duplicates from sorted array

problem: given a sorted array, remove the duplicates *in-place*, and return the new length.

two pointer. left pointer points at unique element, and right pointer iterates the array normally, when the its current value is different with its prev value, record the value using left pointer. time complexity O(n), space complexity O(1).

```c++
int remove_duplicates(int[] array) {
    int left = 0, right = 0;
    int prev;
    for(; right < array.length();) {
        if (prev && array[right] == prev) {
            right++;
        }
        if (!prev || array[right] != prev) {
            array[left] = array[right];
            left++;
            right++;
            prev = array[right];
        }
    }

}
```

# 27 remove element

problem: Given an array nums and a value val, remove all instances of that value in-place and return the new length.

- note that here the array is not sorted. still apply two pointer method that having left pointer stop at the first occurence of the target value element, and right pointer keep iterating till reach the first different value element than the target value. then do swap. ends till the right pointer reachs the end. return the new length.

```c++
// this one is the keep-order one.
int remove_element(int[] array, int target) {
    int left = 0, right = 0;
    for(; right < array.length();) {
        while(array[left] != target) {
            left++;
            if(left >= right) right = left;
        }
        while(array[right] == target) right++;
        array[left] = array[right];
        array[right] = target;
    }
    return left;
}
```

- OR: using two pointer and the fact that the order can be changed. One start from the left, finding the first target value, the other starts from the end, finding the first non-target element.

- OR: using heuristics, by deciding whether the target value is major. If target value is rare, find it and move it to the end. If the others is rare, find it and move it to the start. 

# 31 next permutation

problem: re-arrange the numbers into the next lexicographically greater permutation.

idea: 

- [mine] use a pointer scanning from the end, keeping the min element, it iterates forward to the find any elements smaller than it. If it cannot find such smaller element, then it will be impossible and return the smallest lexicographical order. If it can find such element, then swap it, and re-arrange the rest using ascending order. 
> construct a min-heap can help. the rest with ascending order can be viewed as a heapsort. time complexity O(nlogn).

- [book] use a heuristic that the while scanning from the end till finding the first descending element to swap, the ascending order is maintianed. thus only requres two pass to solve the problem. The first pass find the first descending element from the end, the second pass will insert that element into the right halve. time complexity O(n).

# 32 longest valid parentheses

problem: return the length of the longest vaild parentheses substring.

idea:

- [mine] similar idea with checking if a string is valid palindrome parenthese string using a queue, and use an extra variable to keep track of the current longest length. If reach non-valid form, then the tracker go clear to 0. time complexity: O(n) because a queue can build up at worst n, space complexity: O(n). 

- [book] use two pointer to replace the queue data structure in my idea, since we are not curious the exact positions of those well-formed paratheses in the string, we only care about the longest length. thus, use one "left" and "right" pointer to record the total "(", ")" it meets during iteration. if they are equal, record the length and update the max len, if right pointer is greater than left pointer, then both clear to 0. Then repeat the procedure by starting from the end, in case of the situation that left pointer is always greater than the right pointer value.
> 🌶️ It also suggest that, data structure always means some trade-off, you can use simpler data structure to do the task by trading some features. like in this question, we use two pointer to replace queue, since we only care about the length of the parathese.

# 42 trapping rain water

problem: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

idea:

- [mine] use a modified stack structure + a extra min variable. push operation stays the same, while pop is different that for any new element aj, pop out all elements ai in the current queue that ai <= aj. and the trapped water: 
$water total = \sigma{ai in the queue}{i}(aj - ai) * (j - i - 1)$, time complexity: O(n), space complexity: O(n). because each element will be touched at most two times(insertion and deletion)。

- [book] brute force: 对于数组里的每一个元素向两边展开，找到两边里最高的值最高的那个元素，那么这个位置可以储存的水是：min(max_left, max_right) - ai. time complexity: O(n^2), space complexity: O(1).

- [book] dp: 上述这个找到两边里最高的值的信息可以被后续利用。我们可以利用两个pass找到对于每个元素的max_left[i]和max_right[i]，那么这个位置可以储存的水是： min(max_left[i], max_right[i]) - ai. time complexity: O(n), space complexity: O(n).

> 🌶️ 关于DP的一种使用场景：遍历数组里的每一个元素时，从中间往两边展开。如果用这种brute force的方法可以解决问题，那么这种做法可以被优化成Dynamic Programming的方式。

> 🌶️ 每次使用stack以及queue的时候，都可以尝试的优化为two pointer的方式。将space complexity从O(n)降为O(1)。

# 866 prime palindrome

problem: find a prime number that is also a palindromd over N.

## ideas

- find palindrome then check if prime. 

the set of palindrome is smaller, and for each palindrome, we can test whether it is prime in O(N^1/2).

-> find the set of palindrome number over N.

-> how to find the next palindrome number.

from the center move outward, find the critical digit to add 1.

## summary
 
define the palindrome root. say 121 is 12. thus we can use palindrome root to construct palindrome number by increase it by 1 at a time. 

- https://leetcode.com/articles/prime-palindrome/
