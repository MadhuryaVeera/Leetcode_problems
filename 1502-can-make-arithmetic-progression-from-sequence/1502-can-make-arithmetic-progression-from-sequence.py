class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        common_difference = arr[1] - arr[0]

        for i in range(1,len(arr)-1):
           if arr[i+1]-arr[i]!=common_difference:
            return False

        return True 


        #For above problem why len(arr)-1
        # bcuz while loop has to terminate upto length of the given array only 
        # while usinng the len(arr)
        #  it was going to the out of the range
        #  thats why we use the len(arr)-1


        