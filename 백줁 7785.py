import sys

N = int(input())

name_dic = {}
for _ in range(N):
  name , action = sys.stdin.readline().split()
  if action == "enter":
    name_dic[name] = 0
  elif action == "leave":
    del name_dic[name]
  
name_dic = list(name_dic)
name_dic.sort(reverse=True)

for n in name_dic:
  print(n)
