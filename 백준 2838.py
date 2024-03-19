N = int(input())
X = 0
Y = 0
result_arr = []

while X*5 <= N:
  Y = 0
  while Y*3 <= N:
    if X*5 + Y*3 == N:
      result_arr.append(X+Y)      
    Y += 1
  X += 1

if len(result_arr) == 0:
  print(-1)
else:
  print(min(result_arr))
