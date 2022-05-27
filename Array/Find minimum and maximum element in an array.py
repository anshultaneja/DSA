#Find minimum and maximum element in an array
'''
https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
'''
# def getMinMax(a, n):
#     mn = min(a)
#     mx = max(a)
#     return mn,mx
def getMinMax( a, n):
    i=0
    min_num=max_num=a[i]
    while(i<n):
        if a[i]>max_num:
            max_num=a[i]
        if a[i]<min_num:
            min_num=a[i]
        i=i+1
    return min_num,max_num

def main():
  T = int(input())
  while(T>0):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    product = getMinMax(a,n)
    print(product[0] ,end=" ")
    print(product[1])
  T-=1

if __name__ == "__main__":
  main()
