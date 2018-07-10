# 思路(C++)

重点在implementation.

## ideas

- how to check if an integer is out of range of a valid? (-2^31, 2^31-1)?
Still, because we scanning the digits sequentially, we can perform safety check before each addition and multiply to see if it exceeds the INT_MAX.
-> so basically, as we are adding one digit at a time, we will test the current value with (INT_MAX / 10 - digit) to see if it is overflow.

- character to integer
after confirming the character is an valid integer char. 
```
while(str[i] >= '0' && str[i] <= '9') {
    int digit = str[i] - '0';
}
```

## summary

重点还是放在思考那些重算法的题上。这些简单但是重实现细节的题目可以比较快的过一过。

## reference
