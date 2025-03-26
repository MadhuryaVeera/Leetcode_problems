class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        unordered_map<int,int> once;
        for(auto num : nums) once[num]++;
        vector<int>result;
        for(auto unique:once)
        {
            if(unique.second==1)
            {
                result.push_back(unique.first);
            }
        }
        int sum=0;
        for(auto k :result)
        {
            sum+=k;
        }
        return sum;
    }
};