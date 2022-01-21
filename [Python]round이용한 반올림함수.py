import math

def my_round(number,n): #n: 반올림 할 소수자리
    integer = int(number)
    if(integer%2==0):#실수number의 정수부분이 짝수라면
        if(number-integer==0.5): #소수부분이 0.5라면
            return round(number)+1
    return round(number,n-1)

x= float(input("반올림 수를 입력하세요."))
n= int(input("반올림 자리 수를 입력하세요."))
Ans=my_round(x,n)
print(Ans)


