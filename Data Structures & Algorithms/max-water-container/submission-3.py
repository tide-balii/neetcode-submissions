class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights)
        
        l, r, area = 0, len(heights) - 1, 0  


        for i in range(len(heights)) :
            tempArea = min(heights[l], heights[r]) * (r - l)
            area = max(tempArea, area)
            if (heights[l] <= heights[r]) :
                l += 1 
            else :
                r -= 1

        
        return area

        