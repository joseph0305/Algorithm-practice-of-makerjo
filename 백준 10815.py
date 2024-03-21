import sys

a = input()
arr = list(map(int, sys.stdin.readline().split()))
b = input()
compare_arr = list(map(int, sys.stdin.readline().split()))

dict = {}
for ar in arr:
  dict[ar] = 0

for c in compare_arr:
  if c in dict:
    print(1, end=" ")
  else:
    print(0, end=" ")

# 어떤 요소를 찾는 경우 dictionary를 이용하는 것이 탐색속도가 빠른다
# 아님 이진트리 알고리즘 활용
#https://wlstyql.tistory.com/154
