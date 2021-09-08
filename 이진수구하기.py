x = int(input("숫자를 입력하세요"))
result = '' # 이진수가 저장될 문자열
while True: #무한 루프
    if(x%2 == 0): # X가 2로 나눠질때 나머지가 0이면 0을 저장, 아니면 1을 저장
        result += '0'
    else:
        result += '1'
    x= x//2 # 2를 나눈수의 몫만 x에 다시 저장
    if(x == 0 or x == 1): #종결조건
        result += str(x) #숫자를 문자열로 바꿔주어야 함
        print(result[::-1]) #뒷 수부터 하나씩 슬라이싱
        break #탈출


    