class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr = []
        # build the integer
        integer = 0
        for i in range(len(digits)):
            e = digits.pop()
            integer += e*(10**i)
            # print(integer)
        # add one
        integer += 1

        # rebuild list
        while integer > 0:
            arr.insert(0, integer % 10)
            integer /= 10
        return arr