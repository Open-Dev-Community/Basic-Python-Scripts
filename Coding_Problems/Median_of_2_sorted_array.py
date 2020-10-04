'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

'''

class Solution:
    def findMedianSortedArrays(self,A,B) -> float:
        
        # Take the smaller array
        if len(A) <= len(B):
            x = A
            y = B
        else:
            x = B
            y = A

        #Edge case : one array empty
        if len(x) == 0:
            if len(y)%2==0:
                return (y[len(y)//2-1] + y[len(y)//2])/2
            else:
                return y[len(y)//2]
            
        # Set the lower and higher bounds for binary search
        Lx = 0
        Rx = len(x)
        
        # We will partition at this index so x[0..partX] and x[partX...len(x)]
        partX = (Rx + Lx)//2

        # Adjusting partY 
        partY = (len(x)+len(y)+1)//2 - partX

    
        while True:

            # Edge case: x[partX..] or y[..partY] is empty, preventing access error
            if partX == len(x) or partY == 0:
                # The second comparison from (2) i automatically satified
                if x[partX-1] <= y[partY]:
                    if (len(x)+len(y))%2 == 1:
                        # y[..partY] empty
                        if partY == 0:
                            return x[partX-1]
                        else:
                            return max(x[partX-1],y[partY-1]) 
                    else:
                        # x[partX..] and y[..partY] are empty
                        if partY == 0 and partX == len(x):
                            return (x[partX-1] + y[partY])/2
                        # y[..partY] empty
                        elif partY == 0:
                            return (x[partX-1] + min(y[partY],x[partX]))/2
                        #x[partX..] empty
                        else:
                            return (max(x[partX-1],y[partY-1]) + y[partY])/2
                else:
                    #IMPORTANT Rx goes with -1 in binary search!
                    Rx = partX-1

            #Similair edge case
            elif partX == 0 or partY == len(y):
                if x[partX] >= y[partY-1]:
                    if (len(x)+len(y))%2 == 1:
                        if partX == 0:
                            return y[partY-1]
                        else:
                            return max(x[partX-1],y[partY-1]) 
                    else:
                        if partY == len(y) and partX == 0:
                            return (x[partX] + y[partY-1])/2
                        elif partX == 0:
                            return (y[partY-1] + min(y[partY],x[partX]))/2
                        else:
                            return (max(x[partX-1],y[partY-1]) + x[partX])/2

                else:
                    #IMPORTANT Lx goes with +1 in binary search!
                    Lx = partX+1

            # Regural case
            else:
                # We are done
                if (x[partX-1] <= y[partY] and x[partX] >= y[partY-1]):
                    if (len(x)+len(y))%2 == 1:
                        return max(x[partX-1], y[partY-1])
                    else:
                        return (max(x[partX-1], y[partY-1])+min(x[partX], y[partY]))/2
                # We need go to the left
                elif x[partX-1] > y[partY]:
                    Rx = partX-1
                # We need to go to the right
                else:
                    Lx = partX+1
                    
            # Adjust for binary search
            partX = (Rx + Lx)//2
            partY = (len(x)+len(y)+1)//2 - partX
