class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
       for _ in range(k):
        nums_min_idx = nums.index(min(nums))
        nums[nums_min_idx] *= multiplier 
       return nums