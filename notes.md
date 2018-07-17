# 14 longest common prefix

## ideas

- [me] vertical scanning. time complexity: O(S), where S is the sum of all characters in all string. space complexity: O(1).
- divide and conquer. because LCP satisfies the associative property, that LCP(1,..., n) = LCP(LCP(1,..., n/2), LCP(n/2+1,..., n)). as like in finding min or max. time complexity is O(S), space complexity is O(mlogn), n is the number of string, m is the average length, since divide and conquer requires to store intermediate results.
- binary search. an improvement on the vertical scanning. apply the binary search on the shortest string and do the vertical scanning to validate if it's LCP. time complexity is O(S * log(min string length)), space complexity is O(1).

## summary 


# 866 prime palindrome

find a prime number that is also a palindromd over N.

## ideas

- find palindrome then check if prime. 

the set of palindrome is smaller, and for each palindrome, we can test whether it is prime in O(N^1/2).

-> find the set of palindrome number over N.

-> how to find the next palindrome number.

from the center move outward, find the critical digit to add 1.

## summary
 
define the palindrome root. say 121 is 12. thus we can use palindrome root to construct palindrome number by increase it by 1 at a time. 

- https://leetcode.com/articles/prime-palindrome/
