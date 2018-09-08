
第一题 easy：反转字符串，字符标表示了一个包含加减乘除和数字的表达式。维持字母的相对顺序，反转运算符号 “20*14” -> “14*20”。

> 先反转整个字符串，然后反转由运算符分割的每个子字符串。

第二题 Medium：一个二维矩阵，找从上到下的最小路径，向下只能向左下，正下和右下走一格。比如[1,2,3],[4,5,6],[7,8,9]最短路径是1+4+7=12

> DP，bottom-up的方式。

---

1. 给一个字符串s，找出所有Unique的长度为k的substring，并排序。比如caaab，k = 2，返回 aa, ab, ca
- 不重复子串，输入是一个string和一个substr长度，返回所有unique substrs... 留学申请论坛-一亩三分地
返回的是String[]
2. 给一个数组，每一项是学生名字和分数，学生名字可能有重复，找出所有考试平均分最高的分数。比如 [['bob', '88'], ['ted', '100'], ['ted', '20']]，返回88
第二题一开始有个case没过，有点tricky，因为分数可能有负数，然后负数需要取floor，所以不能直接用int作除法，要double做除法，然后取floor以后再转成Int. 比如 -123 / 10 = -12，但应该要-13
- Best Average Grade：input是String[][]，两列，第一列是名字，第二列是分数。要计算每一个人的平均分数，返回最高的分数。注意要用double。. 一亩-三分-地，独家发布
3. 爬楼梯，多了个base，一次可以跳1、2、3步。LC 70，climbing ladder.
4.找一个array中的第二小的数字
5.LC 385 First Unique Char: input是string，找到这个string中第一个unique的cintar，返回string类型，用map做的。
6.isAnagram 可以包含其他符号和空格。
7.给两个数组求点乘（dot product）。
8.求一个数组中和为k的pair的个数（two sum变形）

---

1. reverse the sentence，给一个sentence，应该是string，里面的每个词是用空格隔开的，这个sentence不会在开头或者结尾出现空格，要求返回的结果将每个词里面字母的顺序反过来，但是每个词在句子里的顺序不变，返回结果也要是string，而且和输入一样，每个词之间用空格隔开，开头和结尾不能出现空格。
e.g. input:   hello world
      output:  olleh dlrow. visit 1point3acres for more.
希望能造福后人。