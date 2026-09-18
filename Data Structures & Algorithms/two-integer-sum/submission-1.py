class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targDict = {}
        for i, num in enumerate(nums):
            if targDict.get(num) is not None:
                return [targDict.get(num), i]
            targDict[target - num] = i
