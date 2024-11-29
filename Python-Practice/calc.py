from math import pow as p

# 제곱근
def power(x,y):
    return int(p(x,y))   

# 세제곱
def cubic(x):
    return x**3

# 나누기
def divide(x,y):
    if y==0:
        return "Cannot divide by zero"
    quotient=x//y
    remainder=x%y
    decimal=x/y
    return f'몫: {quotient}, 나머지: {remainder}, 소수점: {decimal}'

# 1부터 n까지의 정수를 곱하는 팩토리얼 만들기
from functools import reduce
def factorial(n):
    return reduce(lambda x,y:x*y, range(1,n+1))
