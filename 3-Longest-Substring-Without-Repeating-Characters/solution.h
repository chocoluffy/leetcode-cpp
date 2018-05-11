using namespace std;

/**

Question:

Given a string, find the length of the longest substring without repeating
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.

 */

#include <set>
#include <unordered_map>
#include <vector>

static auto x = []() {
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class Solution
{
  public:
    /**
     * 338 ms. 9%.
     * - maintain a queue by inserting and removing elements.
     */
    int lengthOfLongestSubstring_v1(string s)
    {
        set<char> pool;
        int maxlen = 0;
        int head = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (pool.insert(s[i]).second)
            {
                // if insert succeeds.
                maxlen = pool.size() > maxlen ? pool.size() : maxlen;
            }
            else
            {
                // if insert fails.
                pool.clear();
                while (head < i)
                {
                    if (s[head] == s[i])
                    {
                        // find the conflicted position.
                        head++;
                        break;
                    }
                    head++;
                }
                for (int j = head; j < i + 1; j++)
                {
                    // insert [head, i] char to set.
                    pool.insert(s[j]);
                }
            }
        }
        return maxlen;
    }

    /**
     * - 37 ms. 61%
     * - Use map to record the most recent position of each character. 
     */
    int lengthOfLongestSubstring_v2(string s)
    {
        unordered_map<char, int> map;
        int max = 0;
        int ls_head = 0;
        for (int i = 0; i < s.size(); i++) {
            auto key = map.find(s[i]);
            if (key == map.end()) {
                // if current char not in the map.
                // calculate current longest substring's length and compare with max.
                max = max > (i - ls_head + 1) ? max : (i - ls_head + 1);
            } else {
                // if current char in the map.
                // [1] validate if its index > ls_head(longest substring head)
                if (map[s[i]] >= ls_head) {
                    // conflicted char within current longest substring.
                    ls_head = map[s[i]] + 1;
                } else {
                    // not within.
                    max = max > (i - ls_head + 1) ? max : (i - ls_head + 1);
                }
            }
            map[s[i]] = i;
        }
        return max;
    }

    /**
     * 19 ms. 98%
     * - use bitmap in replace of <char, int> hashmap.
     */
    int lengthOfLongestSubstring(string s) {
        vector<float> map(256);
        int max = 0;
        int ls_head = 0;
        for (int i = 0; i < s.size(); i++) {
            if (map[s[i]] == 0) {
                // if current char not in the map.
                // calculate current longest substring's length and compare with max.
                max = max > (i - ls_head + 1) ? max : (i - ls_head + 1);
            } else {
                int actual_val = round(map[s[i]]);
                // if current char in the map.
                // [1] validate if its index > ls_head(longest substring head)
                if (actual_val >= ls_head) {
                    // conflicted char within current longest substring.
                    ls_head = actual_val + 1;
                } else {
                    // not within.
                    max = max > (i - ls_head + 1) ? max : (i - ls_head + 1);
                }
            }
            map[s[i]] = i + 0.1;
        }
        return max;
    }
};