class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashMap = defaultdict(list)
        res = []

        for index, val in enumerate(nums) :
            hashMap[val].append(index) 
        
        for i in range(len(nums)) :
            for j in range(len(nums)) : 
                if j != i :
                    temp = 0 - (nums[j] + nums[i])
                    if temp in hashMap :
                        for k in hashMap[temp] : 
                            if k != j and k != i and sorted([nums[i], nums[j], nums[k]]) not in res:
                                res.append(sorted([nums[i], nums[j], nums[k]]))

        return res



                    
                    
                    
        