import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

#a1*n + a0 = c * n
# n = - ( a0 / (a1-c))
# a1과 c 비교
# a1 > c 면 계산할 필요 없다 틀린 명제
# a1 < c 면
# n0 =< 교차점 n 봐야함
# a1 = c 면 a0를 봐야함


def TellDefintionIsTrue(a1, a0, c, n0):
  if a1 > c:
    return 0
  elif a1 < c:
    junction = -(a0 / (a1 - c))
    if n0 >= junction:
      return 1
    else:
      return 0
  else:
    if a0 > 0:
      return 0
    else:
      return 1


print(TellDefintionIsTrue(a1, a0, c, n0))
