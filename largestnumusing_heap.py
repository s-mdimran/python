import heapq
nums = list(map(int, input().split()))
print(nums)
print(heapq.nlargest(1, nums)) 
