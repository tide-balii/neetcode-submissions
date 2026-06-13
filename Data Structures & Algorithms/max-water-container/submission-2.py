class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        pointer1 = 0
        pointer2 = len(heights) - 1 
        for i in range(len(heights)):
            tempWidth = abs(pointer1 - pointer2)
            tempHeight = min(heights[pointer1], heights[pointer2])
            tempArea = tempWidth * tempHeight 
            if (tempArea > maxWater):
                maxWater = tempArea

            if (heights[pointer2] == heights[pointer1]): 
                pointer2 -= 1 

            elif (heights[pointer1] > heights[pointer2]):
                pointer2 -= 1

            elif (heights[pointer2] > heights[pointer1]):
                pointer1 += 1 
 

        return maxWater



           



        