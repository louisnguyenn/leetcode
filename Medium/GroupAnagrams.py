class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # GIVEN
        # strs: array of strings
        
        # REQUIRED
        # group anagrams together
        # can return the answer in any order
        
        # ANALYSIS
        # data structures: dictionary, lists
        # map characters to find anagrams
        # group anagrams together in an array
        # join the arrays together and return it
        # sort the strings in alphabetical order to match 'idenity'

        # SOLUTION
        strs_map = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s not in strs_map:
                strs_map[s] = []
                strs_map[s].append(string)
            else:
                strs_map[s].append(string)
        # print(strs_map)
        return strs_map.values()
