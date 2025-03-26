class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        // if(nums.size()==1) return ;
        unordered_map<int,int>twice;
        for(auto num:nums) twice[num]++;
         
         vector<int> result;
         for(auto a : twice)
         {
            if(a.second==2)
            {
                result.push_back(a.first);
            }
         }
         return result;
        
        
    }

};