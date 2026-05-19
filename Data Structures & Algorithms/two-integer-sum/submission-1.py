class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedMap = {}
        for index, num in enumerate(nums):
            diff = target - num 
            if diff in visitedMap:
                return [visitedMap[diff], index]
            else:
                visitedMap[num] = index
            
            
        