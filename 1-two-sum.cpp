/**

Given an array of integers, return indices of the two nums such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

 */

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int> &nums, int target)
{
    unordered_map<int, int> map;
	vector<int> result;
	for(int i = 0; i < nums.size(); i++) {
		auto key = map.find(nums[i]);
		if (key != map.end()) {
			// if desired number is in the hash map.
			result.push_back(map[nums[i]]);
			result.push_back(i);
		} else {
			map[target - nums[i]] = i;
		}
	}
	return result;
}

int main() {
    vector<int> input = {1, 2, 3, 8, 4, 9};
    int target = 10;
    vector<int> result = twoSum(input, target);
    cout << result[0] << " " << result[1];
    return 0;
}
