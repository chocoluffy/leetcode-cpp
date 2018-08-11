# 思路(C++)

重点algorithm. 

- two pointer. 

## ideas

- we can always reshape and reposition that container(Trapezoid) into a triangle. thus the question is equivalent to finding two indexes m, n in order to maximize min(an, am) * abs(n - m).

-> two pointer.

> essentially, all two pointers tricks is related to exploring the uncertainty while keeping the optimal structure. 

Say there are two pointers i and j, pointing at the start and end of the array, and we assume that ai < aj. we can prove that moving the longer line inward is always worse than the current result. Thus we move the shorter line inward. 

## reference

- https://leetcode.com/problems/container-with-most-water/solution/