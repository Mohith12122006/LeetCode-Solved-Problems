class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: return []

        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(nums[i])
            elif nums[i] < target:
                result.append(nums[i])
                for j in range(i+1,len(nums)):
                    