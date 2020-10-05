from autopep8 import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        listlength = len(strs)
        if listlength == 0:
            return ""
        elif listlength == 1:
            return strs[0]
        else:
            strs.sort(reverse=False)
            minstringlength = min(len(strs[0]), len(strs[listlength - 1]))
            i = 0
            while i < minstringlength and strs[0][i] == strs[listlength - 1][i]:
                i += 1
            resultantprefix = strs[0][0:i]
            return resultantprefix
