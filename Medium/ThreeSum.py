class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i, x, in enumerate(nums):
            # check for duplicates by skipping over them
            if i > 0 and x == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                triplet = x + nums[l] + nums[r] # compute
                if triplet < 0:
                    l += 1
                elif triplet > 0:
                    r -= 1
                else:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    # move left pointer 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
