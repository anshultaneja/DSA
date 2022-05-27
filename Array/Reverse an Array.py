#Reverse an Array
'''
https://practice.geeksforgeeks.org/problems/reverse-an-array/0
'''

t = int(input())
while(t!=0):
  n = int(input())
  arr = list(map(int,input().strip().split()))[:n]
  for i in range(n-1,-1,-1):
    print(arr[i],end=" ")
  t-=1
