class Solution {
public:
    int distinctAverages(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        set<float> avg;
        int n= nums.size();
        for(int i=0;i<=n/2;i++)
        {
            int k = (nums[i]+nums[n-i-1])/2.0;
            avg.insert(k);
        }
        return avg.size();
    }
};