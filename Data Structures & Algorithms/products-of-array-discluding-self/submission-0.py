class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Populating an array with all the products previous to the current index
        preProducts = [None] * len(nums)
        preProducts[0] = 1
        runningProduct = nums[0]
        for i in range(1, len(nums)):
            preProducts[i] = runningProduct
            runningProduct *= nums[i]

        # Populating an array with all the products after current index
        postProducts = [None] * len(nums)
        postProducts[-1] = 1
        runningProduct2 = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postProducts[i] = runningProduct2
            runningProduct2 *= nums[i]

        # Multiply Pre & Post array to find final array
        output = [preProducts[i]*postProducts[i] for i in range(len(nums))]
        return output

             
            