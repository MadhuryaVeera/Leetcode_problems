class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        
        # Counter is an dictionalry used to count the frequency of a character 

        return min(
            c['b'],
            c['a'],
            c['l']//2,
            c['o']//2,
            c['n']
        )

        