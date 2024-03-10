#
import math

text = input()


def IsPalendrome(text):
  IsPal = 1

  lenth = len(text)
  if lenth == 1:
    return IsPal

  count = math.floor(lenth / 2)
  for i in range(count):
    if text[i] != text[lenth - 1 - i]:
      IsPal = 0
  return IsPal

print(IsPalendrome(text))


# 다른 사람 코딩
# 더 나은 해결책
# 30B 64ms
#a=input();print(+(a[::-1]==a))
