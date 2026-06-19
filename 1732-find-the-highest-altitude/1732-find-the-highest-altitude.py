class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Optimal approach which is prefix sum
        current=0
        highest=0
        for g in gain:
            current+=g 
            # current =0 
            # curent =current+g=0+(-5)=-5
            #
            highest=max(highest,current)
            # max(0,-5) =0
            
            # then agaian the loop will contiune and then we got answer of it .
        return highest
            # then finnaly he want to return that element in it 
        