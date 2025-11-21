class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the last row
        dp = triangle[-1][:]
        # Move upwards to the top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update dp with min path sum for current cell
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        # Top cell holds the answer
        return dp[0]