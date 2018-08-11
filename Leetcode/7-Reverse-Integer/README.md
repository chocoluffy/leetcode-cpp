# 思路(C++)

重点在implementation.

## idea

- know how many decimal integer in total.
    - use `log` and `pow` to find the total bits. 
    - a while loop to round it by 10.

OR

- how to know the value of first digit without knowing the total digit number.
    - represent integer as string. use more space but intuitive.  
> note that it is not necessary!


## edge cases

- access the direction first, then all following operations use abs value. 

- if the flipped integer overflows, return 0. 

-> check overflow before operation, such as multiply and addition. note that if an positive integer does not overflow, then its negative counterpart will not overflow too. Mainly two methods.
    - use INT_MAX and INT_MIN.
    - use tricks that "if integer overflow occurs, the result will be different with the original if reverse operation applied".

## summary

- `x % n` can give negative number.

## extensions

### flip binary representation

- how does an integer represent in bits?

In binary. 

time O(n), space O(1) solution: 
a pointer scan through the original integer on each bit. and use bit operation to access the value at that bit; and then set value to target position.

## reference

- https://www.geeksforgeeks.org/bits-manipulation-important-tactics/