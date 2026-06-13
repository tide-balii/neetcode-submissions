class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                tempheight = min(heights[i], heights[j])   
                tempwidth = abs(i - j)
                tempArea = tempheight * tempwidth
                if (tempArea > maxWater) : 
                    maxWater = tempArea 
        return maxWater



        