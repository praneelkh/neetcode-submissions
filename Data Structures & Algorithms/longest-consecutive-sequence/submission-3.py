class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequenceLength = 0

        for num in nums:
            # check if start of sequence
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longestSequenceLength = max(length, longestSequenceLength)
        return longestSequenceLength
