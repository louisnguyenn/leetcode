class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # setup: 1. set up two pointers: one pointer pointing at i and the other at i+1
        #        2. iterate pointer 2 to sum to target. if it is not the target, then iterate
        #           the i pointer
        #        3. if the sum of the two pointers is found, return indices

        i = 0
        j = len(numbers) - 1
        while i < j:
            
            if numbers[i] + numbers[j] == target:
                break
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
        return [i+1, j+1]
