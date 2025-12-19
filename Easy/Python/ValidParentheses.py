class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                if stack != []:
                    e = stack.pop()
                    if e == "(" and char == ")" or e == "{" and char == "}" or e == "[" and char == "]":
                        continue
                    else:
                        return False
                else:
                    return False
        if stack != []:
            return False
        return True