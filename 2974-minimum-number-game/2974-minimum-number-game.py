class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort() # 2,3,4,5
                    # 0 1 2 3
        arr=[]  # empty arr
        for i in range(0,len(nums),2):
            # first bob appends the smallest removed elemnt in the empty array which is 3
            arr.append(nums[i+1]) # i=0 ,i=0+1 =  at 1 index  which is the value of 3 -->appeds into the array 
            # second alice 
            arr.append(nums[i]) # i=0 , which is the value of 2 appends 
        return arr



        