# N = M(생성자) + M'1 + M'2 + M'3

# N = 256 2자리거나 3자리
# M = 245
# M이 1자리일때 N은 (0~18)
# M이 2자리일때 N은 (11~117)
# M이 3자리일때 N은 (101~1026)
# M이 4자리일때 N은 (1001~10035)

#N이 0~10 까지 무조건 1개 for로
#N이 11~100 까지 무조건 2개 for로
#N이 101 ~ 1000 3개로

# 256 - X+Y+Z = X*100 + Y*10 + Z
# N = 101X+11Y+2Z
# 256 = 101X+11Y+2Z

# N = 256
# for i in range(0, 10):
#   for j in range(0, 10):
#     for k in range(0, 10):
#       equation = 101 * i + 11 * j + 2 * k
#       if equation == N:
#         print(i, j, k)

# 문제는 3자리인지 4자리인지 변동 못하는게 단점
# ====================================================================================
"""
N = int(input())

def Digitlength( num ):
  len = 0
  while num:
    num //= 10
    len += 1
  return len

final_arr = []
limit = Digitlength(N)

if N in [10, 100, 1000, 10000, 100000, 1000000]:
  limit = limit - 1
arr = [0] * limit


def disassemble(level):
  equation = 0
  len = limit
  if level == limit:  
    #equation = 101 * arr[0] + 11 * arr[1] + 2 * arr[2]
    for i in arr:
      re = ((10 ** (len-1))+1) * i 
      len = len - 1
      equation += re
      
    if equation == N:
      final_arr.append(int("".join(map(str,arr))))
    return
  else:
    for i in range(0, 10):
      arr[level] = i
      disassemble(level + 1)


disassemble(0)

if len(final_arr) == 0:
  print(0)
else:
  print(min(final_arr))
"""
# ====================================================================================

# 자연수 자릿수 구하기
#https://shoark7.github.io/programming/algorithm/3-ways-to-get-length-of-natural-number


# 더 좋은 풀이 (내것으로 체회)
N = int(input())
No_Num = True
for i in range(N):
  if i+ sum(map(int,str(i))) == N:
    No_Num = False
    print(i)
    break # 차피 제일 작음
if No_Num:
  print(0)


# 다른 사람 풀이 1
n=int(input())
print([*[i for i in range(n)if n==i+sum(map(int,str(i)))],0][0])

# 다른 사람 풀이 2

a=int(input())
for i in range(a):
 if i+sum(map(int,str(i)))==a:break
 else:i=0
print(i)


