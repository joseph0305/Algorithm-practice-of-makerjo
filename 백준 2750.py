import sys

N = int(input())

arr = []

for i in range(N):
  arr.append(int(sys.stdin.readline()))

arr.sort()

for a in arr:
  print(a)


# 정렬 참고 블로그
# 7개 정렬 알고리즘 설명
#https://velog.io/@pppp0722/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-7%EA%B0%9C-%EC%A0%95%EB%A6%AC-Java
# 파이썬 코드로 정렬 알고리즘
#https://velog.io/@supergangho/3-Python-%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%84%A0%ED%83%9D-%EB%B2%84%EB%B8%94-%EC%82%BD%EC%9E%85-%EC%85%B8
#노마드 코더 알고리즘 설명
#https://www.youtube.com/watch?v=Bor_CRWEIXo
