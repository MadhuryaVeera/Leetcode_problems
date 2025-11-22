class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            remainder = num % 3
            # If remainder is 1 or 2, you need (3 - remainder) or remainder ops
            operations += min(remainder, 3 - remainder)
        return operations