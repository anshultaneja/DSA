#Kth Largest Element in an Array
'''
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minheap = []
        
        for item in nums:
            heapq.heappush(minheap, -item)
            
        for _ in range(k-1):
            heapq.heappop(minheap)
        
        return -minheap[0]
