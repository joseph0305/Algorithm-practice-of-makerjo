import sys

n , M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

k = 3
arr = [0] * k  # [ 0,0,0 ]


ArrOfSum = []


def combi(level, S):
  if level == k:
    #print(arr,sum(arr))
    ArrOfSum.append(sum(arr))
    return
  for i in range(S, n - k + level + 1):
    arr[level] = A[i]
    combi(level + 1, i + 1)


combi(0, 0)
remember = 0
min_dif = 300000
for i in range(len(ArrOfSum)):
  dif = M - ArrOfSum[i]
  if dif >= 0 and dif < min_dif:
    min_dif = dif
    remember = i
   

print(ArrOfSum[remember])

# 반복문 이용해 조합 만들기
#https://www.youtube.com/watch?v=kUBOoogV--U
# 재귀 함수 이용해 조합 만들기
#https://www.youtube.com/watch?v=RfqcJLE2OCE
