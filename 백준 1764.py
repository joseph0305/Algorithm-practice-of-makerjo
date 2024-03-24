import sys

N , M = map(int,input().split())

dic = {}
result = []

for _ in range(N):
  dic[sys.stdin.readline().strip()] = 0

for _ in range(M):
  input = sys.stdin.readline().strip()
  if input in dic:
    result.append(input)

result.sort()
print(len(result))
for p in result:
  print(p)
