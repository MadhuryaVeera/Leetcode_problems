class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        vector<int> zero;
        for(int i=0;i<arr.size();i++)
        {
            if(arr[i]!=0)
            {
                zero.push_back(arr[i]);
            }
            else
            {
                zero.push_back(0);
                zero.push_back(0);
            }
        }
        zero.resize(arr.size());
        swap(arr,zero);
    }
};