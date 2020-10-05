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
        mid = math.floor(listLength / 2)
        if listLength % 2 == 0:
            return (li[mid - 1] + li[mid]) / 2
        else:
            return li[mid]
