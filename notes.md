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