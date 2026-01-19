class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        box = {} # dicitonary
        for value,weight in items1:
            box[value] = box.get(value,0)+weight
        for value,weight in items2:
            box[value] = box.get(value,0)+weight
        ans=[]
        for value in sorted(box):
            ans.append([value,box[value]])
        return ans      