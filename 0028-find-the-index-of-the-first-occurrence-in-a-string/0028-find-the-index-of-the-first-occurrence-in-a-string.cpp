class Solution {
public:
    int strStr(string haystack, string needle) {
        int m=haystack.size(),n= needle.size();
        for(int i=0;i< m-n;++i)   // condition reason ("sad" occurs at index 0 and 6.)
        {
            if(haystack.substr(i,n)==needle)
            {
                return i;
            }
        }
        return -1;
    }
};