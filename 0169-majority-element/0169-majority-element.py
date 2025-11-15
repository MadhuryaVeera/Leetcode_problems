class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    # nums= [3,2,3]
    # After sort =[2,3,3]
    #              0 1 2  --> length =3
    # return nums[length]//2     --> nums[3]//2 = nums[1] = 3 element return chestam . 
    #  Difference between // and /.
    #  // --> Integer division
    #  /  --> Float division
   