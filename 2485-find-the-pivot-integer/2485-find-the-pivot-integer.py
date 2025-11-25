class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2  # sum from 1 to n          
        left = 0 
        for x in range(1, n + 1):  
            left += x   
            if left == total - left + x:
                return x
        return -1