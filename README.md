# leetcode-cpp

## usage

- `template.sh <NO.> <new folder name>` to scaffold a new folder and creates templates files such as main.cpp, run.sh, README.md and solution.h.

- inside each different folder, use `make run` to auto compile and run the script; use `make debug` to generate debuggable executable.

- record different versions of implementation as `_v1`, `_v2` and so on. and record time and precentile. try to improve algorithm to be all above 90%.

- put ideas on README.md under each question. mark if its emphasis is on "Algorithm" or on "Implementation".

## todo

- summarize common modular operations and helpful util functions, with their time complexity, such as "longest common substring\subsequence", "check if integer overflow".

- also recording each solution's time & space complexity. 

- check "Discussion" tab for smart tricks.

## milestone

| Title | Solution | Speed & Percentile |
| ----- | -------- | ---------- |
|1. Two Sum | hashmap with early stop. | 7ms, 98% |
|2. Add Two Numbers in Linked List | dummy node for linked list. | 41ms, 98% | 
|3. Longest Substring Without Repeating Characters | bitmap in replace of <char, int> hashmap recording most recent position. | 19ms, 98% |
|4. Median of Two Sorted Arrays | do binary search on the shorter array between nums1 and nums2, compare the max\min number of left\right hand side. | 42 ms. 98% | 
|5. Longest Palindromic Substring | straightforward: for loop each element and expand at both side; best: only expand at right and jump through repeated elements as repeated one no matter how long it is will definitely be a valid palindrome string | 4ms, 100% |
|6. ZigZag Conversion| create zigzag moving iterator that follows the pattern of the normal for loop iterator. Essentially, to have a direction indicator that will change the zigzag iterator's moving direction. | 21 ms, 98.44%|
|7. Reverse Integer| check integer overflow before potential operations, trick is to check if applying reverse operation can yield original result. | 16 ms, 99.17%|
|8. String to Integer (atoi)| convert each character to integer, check if overflow before any further operations. | 4ms, 100%|