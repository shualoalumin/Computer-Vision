import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        # 입력값 가져오기
        unit = unit_entry.get()
        width = float(width_entry.get())
        height = float(height_entry.get())
        
        # 넓이 계산
        area = width * height
        
        # 결과 출력
        result_label.config(text=f"사각형의 넓이는 {area} {unit}²입니다.")
    except ValueError:
        messagebox.showerror("오류", "올바른 숫자를 입력하세요.")

# 메인 창 생성
window = tk.Tk()
window.title("사각형 넓이 계산기")
window.geometry("300x200")

# 색상 및 스타일 변경
window.configure(bg='#f8e5e5')  # 연한 분홍색 배경

title_label = tk.Label(
    window,
    text="사각형 넓이 계산기",
    font=("맑은 고딕", 20, "bold"),
    bg='#f8e5e5',
    fg='#4a4a4a',  # 진한 회색 텍스트
    pady=20
)

# 입력 프레임 스타일
input_frame = tk.Frame(window, bg='#f8e5e5')
input_frame.pack(pady=20)

# 레이블 스타일
unit_label = tk.Label(
    input_frame,
    text="단위 선택:",
    font=("맑은 고딕", 12),
    bg='#f8e5e5',
    fg='#4a4a4a'
)

# 단위 입력
tk.Label(input_frame, text="단위 (예: cm, m, km):").pack()
unit_entry = tk.Entry(input_frame)
unit_entry.pack()

# 가로 길이 입력
tk.Label(input_frame, text="가로 길이:").pack()
width_entry = tk.Entry(input_frame)
width_entry.pack()

# 세로 길이 입력
tk.Label(input_frame, text="세로 길이:").pack()
height_entry = tk.Entry(input_frame)
height_entry.pack()

# 계산 버튼
calculate_button = tk.Button(window, text="계산하기", command=calculate_area)
calculate_button.pack(pady=10)

# 결과 프레임
result_frame = tk.Frame(window, bg='#e8b4b4', pady=20)
result_label = tk.Label(
    result_frame,
    text="넓이: ",
    font=("맑은 고딕", 14, "bold"),
    bg='#e8b4b4',
    fg='#4a4a4a'
)
result_label.pack()

# 프로그램 실행
window.mainloop()