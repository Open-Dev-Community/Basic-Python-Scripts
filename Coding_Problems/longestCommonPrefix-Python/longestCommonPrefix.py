class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        listLength = len(strs)
        if listLength == 0:
            return ""
        elif listLength == 1:
            return strs[0]
        else:
            strs.sort(reverse = False)
            minStringLength = min(len(strs[0]), len(strs[listLength-1]))
            i = 0
            while i < minStringLength and strs[0][i] == strs[listLength-1][i]:
                i +=1
            resultantPrefix = strs[0][0:i]
            return resultantPrefix
        