"""
Output Format

Print an integer representing the number of distinct triplets.

Sample Input 0

3 2 3
1 3 5
2 3
1 2 3
Sample Output 0

8 

Q: find b[i] >= a[j] and b[i] >= c[k] pair numbers.

Takeaways:
- speed up python!! know how to improve speed, after we get our rough version!
"""

# final accepted version.
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    ai = 0
    bi = 0
    ci = 0
    
    ans = 0
    
    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        
        ans += ai * ci
        bi += 1
    
    return ans

# my version, timeout error
"""
- O(n^2) is not acceptable.
"""
def triplets(a, b, c):
    # recursion on b, for each b's position, find valid a and c area and multiply to obtain number of pairs.
    if not b:
        return 0
    ai = 0
    ci = 0
    while ai < len(a) and a[ai] <= b[0]:
        ai += 1
    while ci < len(c) and c[ci] <= b[0]:
        ci += 1
    bi = 0
    while bi < len(b) and b[bi] == b[0]:
        bi += 1
    return (ai * ci) + triplets(a, b[bi:], c)
        
