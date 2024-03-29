# leetcode-cpp

## usage

- `template.sh <NO.> <new folder name>` to scaffold a new folder and creates templates files such as main.cpp, run.sh, README.md and solution.h.

- inside each different folder, use `make run` to auto compile and run the script; use `make debug` to generate debuggable executable.

- record different versions of implementation as `_v1`, `_v2` and so on. and record time and precentile. try to improve algorithm to be all above 90%.

- put ideas on README.md under each question. mark if its emphasis is on "Algorithm" or on "Implementation".

## todo

- summarize common modular operations and helpful util functions, with their time complexity, such as "longest common substring\subsequence", "check if integer overflow".

- summarize common data structure implementation, such as trie tree.

- also recording each solution's time & space complexity. 

- check "Discussion" tab for smart tricks.

## milestone

| Title | Description | Solution | Speed & Percentile |
| ----- | ----- | -------- | ---------- |
|1. Two Sum | find a pair summing to target value. | hashmap with early stop. | 7ms, 98% |
|2. Add Two Numbers in Linked List | doing addition and curry. | dummy node for linked list. | 41ms, 98% | 
|3. Longest Substring Without Repeating Characters | as title. | bitmap in replace of <char, int> hashmap recording most recent position. if there is a collision then found a repeated character. | 19ms, 98% |
|4. Median of Two Sorted Arrays | find median number from two sorted arrays. | do binary search on the shorter array between nums1 and nums2, compare the max\min number of left\right hand side. Median is a position that the number of elements at two sides are equal. | 42 ms. 98% | 
|5. Longest Palindromic Substring | as title. | straightforward: for loop each element and expand at both side; best: only expand at right and jump through repeated elements as repeated one no matter how long it is will definitely be a valid palindrome string | 4ms, 100% |
|6. ZigZag Conversion | given a string, and place it in a zigzag way, then collect them row by row to form a new string. | create zigzag moving iterator that follows the pattern of the normal for loop iterator. Essentially, to have a direction indicator that will change the zigzag iterator's moving direction. | 21 ms, 98.44%|
|7. Reverse Integer | as title. |  check integer overflow before potential operations, trick is to check if applying reverse operation can yield original result. | 16 ms, 99.17%|
|8. String to Integer (atoi) | as title, with some edge cases. | convert each character to integer, check if overflow before any further operations. | 4ms, 100%|
|11. Container With Most Water | an array of integer, as vertical lines on coordinates, together with x-axis forms a container, find the one holds most water. | two pointer at two ends moving inwards. we can prove that moving the longer line inward is always worse than the current result. Thus we move the shorter line inward.  | 4ms, 100%|

## algorithm summary

### median

A position that the number of elements at two sides is the same.

Problems: NO.4


### two pointer

Essentially a way of searching. find the direction of keeping the sub-structure optimality. keep the optimality and explore\compare.

Problems: NO.11

### first descending element

useful in finding the next lexicographically greater permutation. 

## data structure summary

### trie(prefix tree)

Compared to hashmap.

```c++
// trie node
struct TrieNode
{
    struct TrieNode *children[ALPHABET_SIZE];

    // isEndOfWord is true if the node represents
    // end of a word
    bool isEndOfWord;
};

// Returns new trie node (initialized to NULLs)
struct TrieNode *getNode(void){
    struct TrieNode *pNode =  new TrieNode;
    pNode->isEndOfWord = false;

    for (int i = 0; i < ALPHABET_SIZE; i++)
        pNode->children[i] = NULL;

    return pNode;
}

// If not present, inserts key into trie
// If the key is prefix of trie node, just
// marks leaf node
void insert(struct TrieNode *root, string key)
{
    struct TrieNode *pCrawl = root;

    for (int i = 0; i < key.length(); i++)
    {
        int index = key[i] - 'a';
        if (!pCrawl->children[index])
            pCrawl->children[index] = getNode();

        pCrawl = pCrawl->children[index];
    }

    // mark last node as leaf
    pCrawl->isEndOfWord = true;
}
```
> Note the coding way in method `insert()`, we use a new variable `struct TrieNode *pCrawl` to iterate through the `key`, so that it doesn't change the position of `*root`.

- https://www.geeksforgeeks.org/trie-insert-and-search/

### priority queue

- [Why is Binary Heap Preferred over BST for Priority Queue? - GeeksforGeeks](https://www.geeksforgeeks.org/why-is-binary-heap-preferred-over-bst-for-priority-queue/)