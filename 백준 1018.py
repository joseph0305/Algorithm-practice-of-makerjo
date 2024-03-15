import sys

M, N = map(int, input().split())
chess_plate = []

for i in range(M):
  chess_plate.append(sys.stdin.readline().strip())

def HowmanyNeeded(str, start):
  count = 0
  arr = ['W', 'B']
  compare = start

  for s in str:
    if arr[compare] != s:
      count += 1
    compare = not compare

  return count

resultW = 0
resultB = 0
exeeded_N = N - 8 + 1
exeeded_M = M - 8 + 1
count_arr = []
startW = 0
startB = 1

for i in range(0, exeeded_N):
  for j in range(0, exeeded_M):
    for k in range(0 + j, 8 + j):
      st = chess_plate[k][i:8 + i]
      resultW += HowmanyNeeded(st, startW)
      resultB += HowmanyNeeded(st, startB)
      #print(st,result)
      startW = not startW
      startB = not startB
    #print()
    count_arr.append(resultW)
    count_arr.append(resultB)
    resultW = 0
    resultB = 0
    
#print(count_arr)
print(min(count_arr))
