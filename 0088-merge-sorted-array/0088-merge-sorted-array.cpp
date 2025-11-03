class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        

    vector<int> k;
        k.insert(k.end(), nums1.begin(), nums1.begin() + m);
        k.insert(k.end(), nums2.begin(), nums2.begin() + n);
        nums1 = k;
        sort(nums1.begin(),nums1.end());
        for(auto i :nums1){
        cout<< i <<endl;
        }
    }
    
};