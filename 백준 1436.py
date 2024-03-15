N = int(input())
num = 1
count = 0
result = 0

while N != count:
  if str(num).find("666") == -1:
    num += 1
  else:
    result = num
    count += 1
    num += 1
  

print(result)
