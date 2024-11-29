#구구단 전체
for dan in range(2, 10):
    for num in range(1, 10):
        print(f"{dan} x {num} = {dan * num}")
    print()

#원하는 구구단 입력하기
n = int(input("원하는 단수를 입력하세요:"))
for x in range(1, 10):
    print(f"{n} x {x} = {n * x}")
