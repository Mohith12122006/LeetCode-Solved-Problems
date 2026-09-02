class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1
        res = []
        if target not in nums:
            return [-1,-1]
        while left < right:
            if nums[left] == target:
                res.append(left)
                break
            left += 1
        while left < right:
            if nums[right] == target:
                res.append(right)
                break
            right -= 1
        return [left,right]