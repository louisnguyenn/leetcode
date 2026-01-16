class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        prices: array
        prices[i]: price of given stock on ith day
        i: day

        loop through array
        'slide the window' through each iteration of the array
        compare profit on each day
        return highest profit

        make window of size 2
        buy price will always be on the left of the window
        'buy first before sell'
        when the lowest buy price is found, increase the window and calculate profit of other prices
        if lowest buy price has not been found yet, shift the window one index

        window size = n = 2
        FOR i, j=i+1 IN RANGE len(prices)
            IF j > len(prices)
                return 0 # no profit found
            IF i < j
                WHILE j <= len(prices)
                    buy = i // save day
                    new_profit = prices[buy] - prices[j]
                    IF profit < new_profit
                        profit = new_profit
                    ELSE
                        j += 1
            ELSE
                ITERATE WINDOW
                i += 1
                j += 1
        """
        #
        # this solution takes too long, should be O(n)
        #
        # max_profit, profit = 0, 0
        # for i in range(len(prices)-1):
        #     for j in range(len(prices)):
        #         # print(i)
        #         # print(j)
        #         if j > i:
        #             profit = prices[j] - prices[i]
        #             if profit > max_profit:
        #                 max_profit = profit

        i, j = 0, 1
        profit, max_profit = 0, 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            else:
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
            j += 1
            
        if max_profit <= 0:
            return 0
        return max_profit
