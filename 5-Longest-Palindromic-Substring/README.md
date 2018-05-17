# 思路(C++)

重点在algorithm.

- palindrome 的一个惯用技巧，reverse the string.

把问题convert成finding the longest overlapping substring.

> edge case: "abcdasdfghjkldcba" 可以trick这个reverse的方法。需要对max entry做检查：`i + j == s_size + LCSuffix[i][j]`保证为palindrome substring。

## 15 ms, 78%.
- more straightforward idea: for loop each element, and expand from each one to exmain if it is a palindrome string.
- there are two kinds of palindrome pattern: aba and abba, both are valid.
   

## 4ms. 100%.

- compared with the solutions above, only expand at right,
- trick: view repeated elements as one single elements. because repeated elements, no matter how long it is, can still be viewed as valid palindrome. such as: ccbbbbcc, ccbcc.