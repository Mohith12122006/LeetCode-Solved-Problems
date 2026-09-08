class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        length = len(merged_array)
        mid = length//2
        return float(merged_array[mid] if length % 2 != 0 else (merged_array[mid-1] + merged_array[mid])/2.0)

        