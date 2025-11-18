class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True) 
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0  

        #  nums.sort() --> ascending order[1,2,3..]
        #   nums.sort(reverese=True) -->descending order[3,2,1,0....]
        #   len(num)-2 only why?  [2,2,1]  -> len(num)=3 - 2 = 1  --> so loop i run only one time from i=0,1,2...
        #   then it can check the triangle condition which is a<(b+c) & b<(a+c) & c<(a+b) 
        #   if it obey all teh conditions then it can make a triangle 
        #
        #
        #
