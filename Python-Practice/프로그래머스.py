def solution(n):
    if n % 2 == 1:  # n이 홀수인 경우
        answer = 0  # 홀수의 합을 저장할 변수 초기화
        for num in range(1, n + 1, 2):  # 홀수만 반복
            answer += num  # 홀수를 합계에 추가
        return answer  # 최종 홀수의 합 반환
    else:  # n이 짝수인 경우
        answer = 0  # 짝수의 제곱의 합을 저장할 변수 초기화
        for num in range(2, n + 1, 2):  # 짝수만 반복
            answer += num ** 2  # 짝수의 제곱을 합계에 추가
        return answer  # 최종 짝수의 제곱의 합 반환
    
n = int(input("양의정수:"))
print(solution(n))

