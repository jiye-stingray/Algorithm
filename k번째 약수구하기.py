# 첫째 줄에 n의 약수들 중 k번째로 작은 수를 출력한다. 
# 만일 n의 약수의 개수가 k개보다 적어서 k번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.
n , k = map(int,input("두개의 수를 입력하세요").split())
c = 0
for i in range(1,n):
    if n%i ==0:
        c += 1
    if c==k:
        print(i)
        break
    else: 
        print(-1) 
        break