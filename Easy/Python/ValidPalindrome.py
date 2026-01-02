class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s: string

        # if a palindrome, return True, else return False
        
        # use lower() and join() methods to join each word
        # use replace() to remove invalid characters
        # compare each letter by letter starting from the first and last indexes of the string

        s = lower(''.join(char for char in s if char.isalnum()))
        # print(s)
        j = len(s)-1
        for i in range(len(s)):
            if s[i] != s[j]:
                # print(s[i])
                # print(s[j])
                return False
            j -= 1
        return True
