class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_map<int,int>ctfreq;
        for(int num:nums) ctfreq[num]++;

        vector<int>res;

        for(auto pair:ctfreq)
        {
            if(pair.second==2) res.push_back(pair.first);
        }
        return res;
    }
};