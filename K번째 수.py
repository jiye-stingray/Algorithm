# n개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열 중에서 
# s번째부터 e번째 까지의 수를 오름 차순으로 정렬했을 때 
# K 번째로 나타나는 숫자를 출력하는 프로그램을 작성하시오.

##첫 번째 줄에 테스트 케이스 t가 주어집니다.
##첫 번째 줄은 자연수 n, s, e, k 가 차례로 주어집니다.
##두 번 째 줄에 n개의 숫자가 차례로 주어진다.

t = int(input("몇번 테스트 할까요?"))
for i in range(t):
    print("4가지 조건을 차레대로 입력하세요")
    n,s,e,k = map(int,input().split())
    # 배열 받은뒤, list 화
    print(n,"만큼 수를 입력하세요")
    arr = list(map(int, input().split()))
    arr = arr[s-1:e]
    arr.sort()
    print(arr[k-1])
    


