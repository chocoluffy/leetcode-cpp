using namespace std;

/**

Question:

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123 Output: 321 

Example 2:

Input: -123 Output: -321 

Example 3:

Input: 120 Output: 21 Note: Assume we are dealing with an environment which
could only store integers within the 32-bit signed integer range: [−2^31,  2^31
− 1]. For the purpose of this problem, assume that your function returns 0 when
the reversed integer overflows.

 */

#include <cmath>

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
     * 17 ms, 96.67%
     */
    int reverse_v1(int x) {
        int direction = x > 0 ? 1 : -1;
        x = abs(x);
        int res = 0;
        int bits = int(log10(x));
        // from high to low digit. 
        for (int i = bits; i >= 0; i--) {
            int bit_v = int(x / pow(10, i));
            x -= bit_v * pow(10, i);
            if (res + bit_v * pow(10, bits - i) > INT_MAX) return 0; // in case overflow happen from addition
            res += bit_v * pow(10, bits - i);
        }
        res = direction * res;
        if (res > pow(2, 31) - 1 || res < (-1 * pow(2, 31))) {
            return 0;
        }
        return res;
    }

    int reverse(int x) {
        int res = 0;
        int tmp;
        while (x) {
            cout << x % 10 << endl;
            tmp = res * 10 + (x % 10);
            if (res != tmp / 10) return 0; // check overflow.
            x /= 10;
            res = tmp;
        }
        return res;
    }
};