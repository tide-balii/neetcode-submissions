class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            for y, num2 in enumerate(numbers):
                comb = num + num2
                if comb == target and i != y:
                    return [i + 1, y + 1]

                



        