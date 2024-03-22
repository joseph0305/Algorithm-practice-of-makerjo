import sys


N , M = map(int,sys.stdin.readline().split())

S = []
count = 0

for _ in range(N):
  S.append(sys.stdin.readline())

for _ in range(M):
  if sys.stdin.readline() in S:
    count += 1


print(count)
