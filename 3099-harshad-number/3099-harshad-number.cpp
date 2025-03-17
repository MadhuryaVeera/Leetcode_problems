class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int n) {
     int x=n;
     int sum=0;
     while(x!=0){
        sum+=x%10;
        x/=10;
        }
    //  x=x/10;
     
    
    if(n%sum==0) return sum;
    else return -1;
    }
    
};