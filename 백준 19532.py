# 772ms
a , b,c,d,e,f = map(int,input().split())
for x in range(-999,1000):
  for y in range(-999,1000):
    if a*x+b*y-c == 0 and d*x+e*y-f == 0 :
      print(x,y)



# 백준 다른 사람 풀이
# 60ms
a,b,x,c,d,y=map(int,input().split())
k=a*d-b*c
print((d*x-b*y)//k,(a*y-c*x)//k)
