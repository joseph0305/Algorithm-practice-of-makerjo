# n = 5
# i : 1 to 3
# j : 2 to 4
# k : 3 to 5

# i=1
# j=2 : k  3번
# j=3   k  2
# j=4   k  1
# i=2
# j=3   k  2
# j=4   k  1
# i=3
# j=4   k  1

# n = 6
# i : 1 to 4
# j : 2 to 5
# k : 3 to 6

# i=1
# j=2 : k  4번
# j=3   k  3
# j=4   k  2
# j=5   k  1
# i=2
# j=3   k  3
# j=4   k  2
# j=5   k  1
# i=3
# j=4   k  2
# j=5   k  1
# i=4
# j=5   k  1

#(n-2)! + (n-3)! .. (n-n)!
# S 2:n (n-k)! =
# S 1:n (n-k)

# N! + (N-1)! + (N-2)! + (N-N+1)! (k가 0 to N-1) => K=1 to K=N으로 바꿀수 있나?
# n! = n(n+1) / 2

# N = int(input())
# N = N - 2

# sum = 0
# for n in range(1, N + 1):
#   for i in range(1, n + 1):
#     sum += i

# print(sum)
# print(3)

N = int(input()) - 2

sum = 0
for k in range(1, N + 1):
  sum += (k * (k + 1)) // 2

print(sum)
print(3)

# 시그마 공식 참고
#https://calcproject.tistory.com/663
