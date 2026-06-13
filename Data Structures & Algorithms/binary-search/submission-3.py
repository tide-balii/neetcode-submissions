class Solution:

    def recBinarySearch (self, l : int, r : int, nums: List[int], target: int) -> int:
        midpoint = (l + r) // 2 
        if l > r : 
            return - 1 
        
        elif nums[midpoint] == target : 
            return midpoint 

        elif target < nums[midpoint] :
            r = midpoint - 1 
            return self.recBinarySearch(l, r, nums, target)

        else : 
            l = midpoint + 1 
            return self.recBinarySearch(l, r, nums, target)


    def search(self, nums: List[int], target: int) -> int:
        return self.recBinarySearch(0, len(nums) - 1, nums, target)
        


        