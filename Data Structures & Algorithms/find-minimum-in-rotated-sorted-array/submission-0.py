class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        
        l, r = 0, len(nums) - 1

        while l <= r :
            mid = (l + r) // 2 

            if nums[mid] > nums[r] :
                l = mid + 1 
            
            elif nums[l] > nums[mid] :
                r = mid
            
            elif nums[l] <= nums[mid] and nums[l] <= nums[r] :
                return nums[l]

        return nums[l]

             
      
          


        