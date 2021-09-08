
#시그마 공식: n*n(+1)/2
s = 0
n = 100
x = n*(n+1)/2
print(x)

# for문
s1 = 0
for i in range(1,101):
    s1 += i
print(s1)

#재귀함수
n1 = 100
def Hap(n):
    if n <= 1:
        return 1
    else:
        return n + Hap(n-1)

n1 = Hap(n1)
print(n1)