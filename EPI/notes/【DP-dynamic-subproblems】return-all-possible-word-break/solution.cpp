// compared to normal dp problem, each case is associated with all prev subproblems! thus need to cache the result.
// following is the dynamic programming version.
for(int i = 0; i < s.size(); i++) {
  vector<string> res;
  for(int j = 0; j < size(); j++) {
    if (dp[j].size() > 0 && dict.find(s.substring(j+1, i)) != dict.cend()) {
      vector<string> curr_list = merge(dp[j], s.substring(j+1, i));
      res.insert(res.end(), curr_list.start(), curr_list.end());
    }
  }
  dp[i] = res;
}
return dp[s.size() - 1];

// following is the recursion version.
class Solution {
    unordered_map<string, vector<string>> m;

    vector<string> combine(string word, vector<string> prev){
        for(int i=0;i<prev.size();++i){
            prev[i]+=" "+word;
        }
        return prev;
    }

    public:
    vector<string> wordBreak(string s, unordered_set<string>& dict) {
        if(m.count(s)) return m[s]; //take from memory
        vector<string> result;
        if(dict.count(s)){ //a whole string is a word
            result.push_back(s);
        }
        for(int i=1;i<s.size();++i){
            string word=s.substr(i);
            if(dict.count(word)){
                string rem=s.substr(0,i);
                vector<string> prev=combine(word,wordBreak(rem,dict));
                result.insert(result.end(),prev.begin(), prev.end());
            }
        }
        m[s]=result; //memorize
        return result;
    }
};