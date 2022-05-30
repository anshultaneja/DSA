#Sort an array of 0s, 1s and 2s

'''
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1#
'''

class Solution:
    def sort012(self,arr,n):
        # code here
        l = 0 # index for 0's
        m = 0 # index for 1's
        h = n-1 # index for 2's
        
        while(m<=h):
            if arr[m] == 1:
                m+=1
            elif arr[m] == 0:
                arr[m],arr[l] = arr[l],arr[m]
                m+=1
                l+=1
            elif arr[m] == 2:
                arr[m],arr[h] = arr[h],arr[m]
                h-=1
        
## Time Complexity = O(n)
## Space Complexity = o(1)
