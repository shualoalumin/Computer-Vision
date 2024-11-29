import math
from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operation == 'pow':
            result = math.pow(num1, num2)
        elif operation == 'root':
            if num1 < 0:
                raise ValueError("음수의 제곱근은 계산할 수 없습니다.")
            result = math.pow(num1, 1/num2)
            
        result_label.config(text=f"결과: {result:.2f}")
        
    except ValueError as e:
        if str(e):
            messagebox.showerror("오류", str(e))
        else:
            messagebox.showerror("오류", "올바른 숫자를 입력하세요.")
    except ZeroDivisionError:
        messagebox.showerror("오류", "0으로 나눌 수 없습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"예상치 못한 오류가 발생했습니다: {str(e)}")

# GUI 생성
window = Tk()
window.title("고급 계산기")
window.geometry("300x400")
window.configure(bg='#f0f0f0')

# 입력 필드
Label(window, text="첫 번째 숫자:", bg='#f0f0f0').pack(pady=5)
entry1 = Entry(window)
entry1.pack(pady=5)

Label(window, text="두 번째 숫자:", bg='#f0f0f0').pack(pady=5)
entry2 = Entry(window)
entry2.pack(pady=5)

# 연산 선택
operation_var = StringVar(value='+')
operations = ['+', '-', '*', '/', 'pow', 'root']
Label(window, text="연산 선택:", bg='#f0f0f0').pack(pady=5)

for op in operations:
    Radiobutton(window, 
                text=op, 
                variable=operation_var, 
                value=op,
                bg='#f0f0f0').pack()

# 계산 버튼
Button(window, 
       text="계산하기", 
       command=calculate,
       bg='#4CAF50',
       fg='white',
       padx=20,
       pady=10).pack(pady=20)

# 결과 표시
result_label = Label(window, 
                    text="결과: ", 
                    bg='#f0f0f0',
                    font=('Arial', 12))
result_label.pack(pady=20)

window.mainloop() 