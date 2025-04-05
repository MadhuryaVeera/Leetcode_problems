class Solution {
public:
    int findLucky(vector<int>& arr) {

        unordered_map<int,int> c;
        for(auto arra :arr) c[arra]++;     

        int maxLucky = -1;            
        
        for (const auto& pair : c) {
            if (pair.first == pair.second) {
                maxLucky = max(maxLucky, pair.first);
            }
        }
        return maxLucky;
    }
};