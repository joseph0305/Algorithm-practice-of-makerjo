import sys

N , num = map(int,input().split())

coins = []
for _ in range(N):
  coins.append(int(sys.stdin.readline()))

count = 0

for i in range(N-1,-1,-1):
  if num == 0:
    break
  quo = num // coins[i]    

  if quo >= 1:
    num = num % coins[i] 
    count += quo


print(count)