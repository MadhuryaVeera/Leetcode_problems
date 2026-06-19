class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Brute Force approach 
        altitude=[0] # at a point 0 every start elemnt has at 0 index 0 is fix we are taking

        for g in gain:
            altitude.append(altitude[-1]+g)
            #[-5,1,5,0,-7]

            #altitude[-1] =0
            #altitide[-1]+g = 0+(-5) = -5

            #altitude[-1]=-5
            #altitude[-1]+g=-5+1=-4

            #altitude[-1] =-4
            #altitide[-1]+g = -4+(5) = 1

            #altitude[-1]=1
            #altitude[-1]+g = 1+0 =1
            
            #altitude[-1] =1
            #altitide[-1]+g = 1+(-7) = -6

            # then total array we can obtain is [-5,-4,1,1,-6]

            # then we append that to altitude which can give the array is 
            #[0,-5,-4,1,1-6]
            # then  we find the max element in it which is 1.
        return max(altitude)

        