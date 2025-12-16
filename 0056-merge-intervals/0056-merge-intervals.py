class Solution:
    def merge(self, intervals):
        # First, sort intervals by their start value
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # If merged is empty or no overlap, just add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap: merge by updating the end value
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged