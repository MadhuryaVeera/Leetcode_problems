class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert each number to string
        nums_str = list(map(str, nums))
        # Sort using a custom key: repeat each string to make sure it compares correctly
        nums_str.sort(key=lambda x: x*10, reverse=True)
        # If the largest number is '0', the whole number is zero
        if nums_str[0] == '0':
            return '0'
        return ''.join(nums_str)