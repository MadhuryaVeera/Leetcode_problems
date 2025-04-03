class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int,int> twice;
        for(int num:nums) twice[num]++;

        // vector<int> result;
        for(auto a:twice)
        {
            if(a.second > 1)
            {
                return a.first;
            }
        }
        
        return -1;
    }
};