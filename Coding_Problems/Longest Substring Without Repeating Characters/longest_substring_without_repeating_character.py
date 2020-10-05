def lengthOfLongestSubstring(self, s: str) -> int:
        word_set=set()  # it is a set
        n=len(s) # length of input string
        ans=0    #maximum length of substring
        i=0    # left index
        j=0    # right index
        while i<n and j<n:
                if s[j] not in word_set:
                        word_set.add(s[j]) # adding new character in set
                        j+=1
                        ans=max(ans,j-i)
                else:
                        word_set.remove(s[i]) # removing older character from set
                        i+=1
        return ans


word=input(" Enter a string") # user input 
print(lengthOfLongestSubstring(word))
