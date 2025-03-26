class Solution {
public:
    int duplicateNumbersXOR(vector<int>& nums) {
        unordered_map<int,int> twice;
        for(int num:nums) twice[num]++;
        
        vector<int> result;
        for(auto a:twice)
        {
            if(a.second==2)
            {
                result.push_back(a.first);
            }
        }
        set<int> s;
        for(auto x:result) s.insert(x);
        int xorresult=0;
        for(const auto& value : s)
        {
            xorresult^=value;
        }  
        return xorresult;
    }
};