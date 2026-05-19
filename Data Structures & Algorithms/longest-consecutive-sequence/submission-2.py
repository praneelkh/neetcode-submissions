class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        ml_count = 0
        cl_count = 1

        for num in numSet:
            n = num
            while (n-1) in numSet:
                cl_count += 1
                n -= 1
            ml_count = max(cl_count, ml_count)
            cl_count = 1
        return ml_count
        