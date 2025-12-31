class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # GIVEN
        # strings s and t

        # REQUIRED
        # return true if t is an anagram of s

        # ANALYSIS
        # loop through both strings
        # check if each letter in both strings exist, thus an anagram

        # SOLUTION
        characters = []
        for char in s:
            characters.append(char)
        # print(characters)

        for char in t:
            if char in characters:
                # print(char)
                characters.remove(char)
        # print(characters)
        if characters == [] and len(s) == len(t):
            return True
        return False
        