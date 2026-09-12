class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            firstValIdx = numDict.get(target - nums[i])
            if firstValIdx is not None:
                return [firstValIdx, i]
            numDict[nums[i]] = i