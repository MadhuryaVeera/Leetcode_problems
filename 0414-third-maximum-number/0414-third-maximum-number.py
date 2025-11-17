class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        # First need to pushing elements into a set 
        # so that duplicates can remove 
        # Sotring the array in the decreasing order 
        # Then we get the 3 rd element if existed 
        # If not then return the maximum number of the array

        distinct = list(set(nums))
        distinct.sort(reverse=True)
        if len(distinct) >= 3:
            return distinct[2]
        return distinct[0]
