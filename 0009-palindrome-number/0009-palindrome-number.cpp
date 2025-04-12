class Solution {
public:
    bool isPalindrome(int num) {
        int orig_num=num;
       long long rev_num=0;
       while(num>0)
       {
        // int temp=num%10;
        rev_num=rev_num*10+num%10;
        num/=10;
       }
    //    return rev_num;
       if(orig_num==rev_num)
       {
        return true;
       }
       else{
        return false;
       }

    }
};