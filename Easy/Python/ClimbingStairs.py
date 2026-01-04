class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n number of steps
        # can climb 1 or 2 steps
        # n-1, n-2 steps

        # how many distinct ways
        # return: integer

        # dynamic programming: tabulation approach

        # base case
        if n <= 2:
            return n
        
        arr = [0] * (n+1)
        arr[1] = 1 # 1 way to reach step 1
        arr[2] = 2 # 2 ways to reach step 2

        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        
        return arr[n]
