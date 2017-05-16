a, b, c = map(int,input().split())

maiorab = (a+b+abs(a-b))/2
maiorab = (maiorab+c+abs(maiorab-c))/2

print('%d eh o maior'%maiorab)
