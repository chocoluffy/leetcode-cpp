# 思路(C++)

重点在algorithm.

- palindrome 的一个惯用技巧，reverse the string.

把问题convert成finding the longest overlapping substring.

> edge case: "abcdasdfghjkldcba" 可以trick这个reverse的方法。需要对max entry做检查：`i + j == s_size + LCSuffix[i][j]`保证为palindrome substring。