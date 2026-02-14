class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest_length = 0
        for num in numSet:
            if (num - 1) not in numSet:
                curr_length = 0
                while (num + curr_length) in numSet:
                    curr_length += 1
                longest_length = max(curr_length, longest_length)
        return longest_length
