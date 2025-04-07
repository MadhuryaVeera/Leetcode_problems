class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<int,int>  once;
        for(auto ss : s) once[ss]++;

        for(int i=0;i<s.size();i++){
            if(once[s[i]] ==1)
                return i;
          }
          return -1;
     }
};