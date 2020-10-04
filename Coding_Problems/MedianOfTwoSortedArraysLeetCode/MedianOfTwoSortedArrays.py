import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li = []
        for index in nums1:
            li.append(index)
        for index in nums2:
            li.append(index)

        li.sort(reverse=False)
        listLength = len(li)
        if listLength % 2 == 0:
            mid = math.floor(listLength / 2)
            result = (li[mid - 1] + li[mid]) / 2
            return result
        else:
            mid = math.floor(listLength / 2)
            return li[mid]
