class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        mid = -1

        while mid != r and mid != l:
            mid = (r + l) // 2
            # print(mid)
            if nums[mid] != target:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                return mid
        
        return -1
