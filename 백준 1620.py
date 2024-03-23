import sys

M , N = map(int, input().split())

po_dic = {}
po_dic_re = {}

for i in range(1,M+1):
  input = sys.stdin.readline().strip()
  po_dic[i] = input
  po_dic_re[input] = i
  
result_arr = []
for _ in range(N):
  test = sys.stdin.readline().strip()
  if test.isdigit():
    result_arr.append(po_dic[int(test)])
  else:
    result_arr.append(po_dic_re[test])


for p in result_arr:
  print(p)
