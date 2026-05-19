class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for num in nums:
            if num not in frequencyMap:
                frequencyMap[num] = 1
            else:
                frequencyMap[num] += 1
        sortedDict = dict(sorted(frequencyMap.items(), key=lambda item: item[1], reverse=True))
        return list(sortedDict.keys())[:k]

        