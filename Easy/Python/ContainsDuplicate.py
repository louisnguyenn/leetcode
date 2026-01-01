class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # GIVEN
        # nums: integer array
        
        # REQUIRED
        # if value appears at least twice, return true

        # ANALYSIS
        # map values into a dictionary
        # key: number, value: number of times that number appears

        # SOLUTION
        num_map = {}
        for num in nums:
            if num in num_map:
                num_map[num] += 1
                if num_map[num] >= 2:
                    return True
            else:
                num_map[num] = 1
        return False
