class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        """
        # setup: 1. calculate all left products
        #        2. calculate all right products
        #        3a. store result in answer array
        #        3b. answer array will result in the product of all
        #            numbrers except itself

        answer = [1] * len(nums)
        left_product, right_product = 1, 1
        # iterate from start of the list and calculate left product
        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]        

        # iterate from the end of the list and calculate right product
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
