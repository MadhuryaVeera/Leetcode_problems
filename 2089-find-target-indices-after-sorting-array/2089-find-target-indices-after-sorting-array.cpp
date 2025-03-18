class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        vector<int>l;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==target) l.push_back(i);
        }
        return l;
    }
};