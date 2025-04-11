class Solution {
public:
    int reverse(int x) {
    
        int orgnum=x;
        long long s=0;
        while(orgnum!=0)
        {
            s=s*10+orgnum%10;
            orgnum/=10;
        }
    
         int n1=pow(-2,31);
         int n2=pow(2,31)-1;
        if(s<n1 || s>n2) 
        {
            return 0;
        }
        return s;    
    }
    
};





