class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
         set<int>v;
        for(int i=0;i<nums1.size();i++)
        {
            for(int j=0;j<nums2.size();j++)
            {
                if(nums1[i]==nums2[j])
                {
                    v.insert(nums1[i]);
                }
            }
        }
        return vector<int>(v.begin(),v.end());


    }
};