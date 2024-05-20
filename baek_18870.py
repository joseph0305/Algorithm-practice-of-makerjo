
N = int(input())
nums = list(map(int,input().split()))
di = {}
refine_arr = list(set(nums))
refine_arr.sort()
for i in range(len(refine_arr)):
  di[refine_arr[i]] = i

for n in nums:
  print(di[n],end=" ")