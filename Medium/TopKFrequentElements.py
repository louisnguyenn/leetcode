class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums: integer array
        # k: integer

        # return k most frequent elements

        # count mapping, use dictionary
        # compare counts, sort highest count to the top of the dictionary
        # return k most frqeuent elements starting from the top of the dictionary

        nums_map = {}
        elements_list = []
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        # print(nums_map)
        # print(nums_map.values())
        # print(sorted(nums_map.values()))
        # print(nums_map.items())
        # print(nums_map.items()[0])
        # print(nums_map.items()[0][1])

        elements = sorted(nums_map.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            elements_list.append(elements[i][0])
        return elements_list
