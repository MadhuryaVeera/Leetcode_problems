class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # if original not in nums:
        #      return original
        # else:
        #     for i in range(len(nums)):
        #         if original in nums:
        #             k = original*2
        #     return k

        while original in nums:
            original*=2
        return original

        #   If orgianl not found then return the origianl first , THEN
        #    If original is found in the nums 
        #    then multipy by 2 
        #      again check that multiplied value is there in the nums
        #       then agian mutliply by 2
        #        do same thing untill the number doesnot found in the nums
       
       