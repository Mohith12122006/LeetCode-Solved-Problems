class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first = -1
        last = -1
        for i in range(n):
            if nums[i] != target:
                continue
            
            if first == -1:
                first = i
            
            last = i
        return [first,last]