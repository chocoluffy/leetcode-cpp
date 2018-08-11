using namespace std;

/**

Question:

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

 */

#include <math.h>

static auto x = []() {
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class Solution {
public:
    /**
     * Fail. Have \0 char inside final string. 
     */
    string convert_v1(string s, int numRows) {
        string* buckets = new string[numRows];
        int block_size = numRows + (numRows - 2);
        if(block_size == 0) {
            // numRows = 1.
            return s;
        }
        for (int i = 0; i < ceil(s.size() / (float)block_size); i++) {
            for (int j = 0; j < numRows; j++) {
                // i: block index, j: element index
                buckets[j].push_back(s[i * block_size + j]);
            }
            for (int k = 0; k < numRows - 2; k++) {
                int bucket_id = numRows - 2 - k;
                buckets[bucket_id].push_back(s[i * block_size + numRows + k]);
            }
        }
        string result;
        for (int n = 0; n < numRows; n++) {
            result.append(buckets[n]);
        }
        delete[] buckets;
        return result;
    }

    string convert(string s, int numRows) {
        string* buckets = new string[numRows];
        int row_id = 0;
        int multiplier = 1;
        for(int i = 0; i < s.size(); i++) {
            // a mapping between cursor index i and row_id.
            buckets[row_id].push_back(s[i]);
            // if row_id < numRows
            if(row_id == numRows - 1) {
                multiplier = -1;
            } else if (row_id == 0) {
                multiplier = 1;
            }
            row_id = row_id + multiplier * 1;
        }
        string result;
        result.reserve(s.size());
        for (int n = 0; n < numRows; n++) {
            result.append(buckets[n]);
        }
        delete[] buckets;
        return result;
    }
};