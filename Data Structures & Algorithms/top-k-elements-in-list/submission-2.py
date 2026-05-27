class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # establish the count of each number in a dict
        count = {} 
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # populate array where each index represents count 
        # and the values are the numbers with that count
        # max size of array should be the size of the nums + 1 (b/c zero index)
        freq = [[] for i in range(len(nums) + 1)] 
        for num, ct in count.items():
            freq[ct].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
            


            
        
        