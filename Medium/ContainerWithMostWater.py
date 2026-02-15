class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # A = bh
        # h = height
        # b = indices between l, r pointers in list

        l, r = 0, len(height) - 1
        curr_area = 0
        max_area = 0
        # print(l, r)

        while (l < r):
            if height[l] < height[r]:
                h = height[l]
            else:
                h = height[r]
            b = r - l
            curr_area = b * h
            
            if curr_area > max_area:
                max_area = curr_area

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1 # move either left or right pointer
                       # doesn't matter which bc loop condition will break

        return max_area
