# 10816

N = int(input())
cards = list(map(int,input().split()))
M = int(input())
tests = list(map(int,input().split()))

dic = {}
for c in cards:
  if c in dic:
    dic[c] += 1
  else:
    dic[c] = 1

for t in tests:
  if t in dic:
    print(dic[t],end=" ")
  else:
    print(0,end=" ")

