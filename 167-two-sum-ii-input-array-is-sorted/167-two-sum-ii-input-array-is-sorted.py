class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # loop through the list, for each element, find if target-element is in the list
        res = []
        for i in range(len(numbers)):
            x = target - numbers[i]
            if x in numbers[i+1:]:
                print(x, i+1)
                res.append(i + 1)
                res.append(numbers[i+1:].index(x) + i + 2)
                return res
                