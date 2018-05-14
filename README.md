# leetcode-cpp

## usage

- `template.sh <NO.> <new folder name>` to scaffold a new folder and creates templates files such as main.cpp, run.sh, README.md and solution.h.

- inside each different folder, use `make run` to auto compile and run the script; use `make debug` to generate debuggable executable.

- record different versions of implementation as `_v1`, `_v2` and so on. and record time and precentile. try to improve algorithm to be all above 90%.

- put ideas on README.md under each question. mark if its emphasis is on "Algorithm" or on "Implementation".

## milestone

| # | Title | Solution | Speed & Percentile |
|---| ----- | -------- | ---------- |
|1| Two Sum | hashmap with early stop. | 7ms, 98% |
|2| Add Two Numbers in Linked List | dummy node for linked list. | 41ms, 98% | 
|3| Longest Substring Without Repeating Characters | bitmap in replace of <char, int> hashmap recording most recent position. | 19ms, 98% |
|4| Median of Two Sorted Arrays | do binary search on the shorter array between nums1 and nums2, compare the max\min number of left\right hand side. | 42 ms. 98% | 