
第一题 easy：反转字符串，字符标表示了一个包含加减乘除和数字的表达式。维持字母的相对顺序，反转运算符号 “20*14” -> “14*20”。

> 先反转整个字符串，然后反转由运算符分割的每个子字符串。

第二题 Medium：一个二维矩阵，找从上到下的最小路径，向下只能向左下，正下和右下走一格。比如[1,2,3],[4,5,6],[7,8,9]最短路径是1+4+7=12

> DP，bottom-up的方式。