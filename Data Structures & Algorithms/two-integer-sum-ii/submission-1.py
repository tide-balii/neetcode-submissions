class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1 

        while True : 
            temp = numbers[first] + numbers[last] 

            if temp == target :
                return [first + 1, last + 1]

            elif temp < target : 
                first += 1 
            
            else :
                last -= 1 
            
