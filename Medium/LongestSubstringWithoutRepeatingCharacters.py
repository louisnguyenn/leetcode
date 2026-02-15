class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        longest_substring = 0
        curr_substring = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) # shrink window and remove duplicate
                l += 1
            charSet.add(s[r])
            curr_substring = r - l + 1
            longest_substring = max(curr_substring, longest_substring)

        return longest_substring
                    