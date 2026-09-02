class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(nums)
        n = len(nums[0])
        for i in range(m):
            for j in range(i + 1, n):
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
        for i in range(m):
            nums[i].reverse()