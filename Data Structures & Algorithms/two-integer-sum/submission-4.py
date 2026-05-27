class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSeen = {} # num: idx 
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prevSeen:
                return [prevSeen[diff], idx]
            else: 
                prevSeen[num] = idx

        