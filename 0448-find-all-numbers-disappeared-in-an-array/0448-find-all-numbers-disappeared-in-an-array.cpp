class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        set<int> hari;
        vector<int>mad;
        sort(nums.begin(),nums.end());
        for(auto i: nums){
            hari.insert(i);
        }
        int index=0;
            for (auto it = hari.begin(); it != hari.end(); ++it) {
            if (*it != index + 1) {
             mad.push_back(index+1);
            }
        index++;
        }
        return mad;
    }
};