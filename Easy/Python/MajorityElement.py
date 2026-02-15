class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        n = 0

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        for key in count:
            if count[key] > len(nums) / 2:
                n = key

        return n
