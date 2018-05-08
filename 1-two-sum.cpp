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

/**
 * 10ms.
 */
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

/**
 * 7 ms.
 */
vector<int> twoSum_v2(vector<int> &nums, int target)
{
    unordered_map<int, int> map;
	vector<int> result;
	for(int i = 0; i < nums.size(); i++) {
		auto key = map.find(nums[i]);
		if (key != map.end()) {
			// if desired number is in the hash map.
			result.push_back(map[nums[i]]);
			result.push_back(i);
			return result;
		} else {
			map[target - nums[i]] = i;
		}
	}
}

/**
 * 6ms. 
 */
// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();


/**
 * 4ms.
 * - std::sort is almost impossible to beat. even it is o(nlogn) in conception.
 */
vector<int> twoSum_v3(vector<int>& nums, int target) {
	vector<int> indices;
	int lenOfVectors = nums.size();
	bool found=false;
	vector< pair<int, int> > new_nums;
	for(int i=0; i<lenOfVectors; ++i){
		new_nums.push_back(make_pair(nums[i], i));
	}
	sort(new_nums.begin(), new_nums.end());
	int j=0, k=lenOfVectors-1;
	while(j<k){
		if(new_nums[j].first+new_nums[k].first==target){
			indices.push_back(new_nums[j].second);
			indices.push_back(new_nums[k].second);
			break;
		}
		else if(new_nums[j].first+new_nums[k].first<target){
			j++;
		}
		else{
			k--;
		}
	}
	return indices;
}

int main() {
    vector<int> input = {1, 2, 3, 8, 4, 9};
    int target = 10;
    vector<int> result = twoSum_v2(input, target);
    cout << result[0] << " " << result[1];
    return 0;
}
