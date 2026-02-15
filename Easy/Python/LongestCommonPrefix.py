class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for s in strs:
                if char != s[i]:
                    return shortest[:i]

        return shortest
