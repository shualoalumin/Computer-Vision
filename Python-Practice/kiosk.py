import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class KioskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("키오스크 프로그램")
        self.root.geometry("800x600")
        
        # 메뉴 데이터
        self.menu_items = {
            "음료": {
                "아메리카노": 3000,
                "카페라떼": 3500,
                "카푸치노": 3500
            },
            "디저트": {
                "치즈케이크": 5000,
                "초코케이크": 5000,
                "크로플": 4000
            }
        }
        
        # 장바구니
        self.cart = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # 스타일 설정
        style = ttk.Style()
        
        # 버튼 스타일
        style.configure("Cursor.TButton",
                       cursor="hand2",
                       font=('Helvetica', 12))  # 버튼 폰트 크기
        
        # 레이블 스타일
        style.configure("Cursor.TLabel",
                       cursor="arrow",
                       font=('Helvetica', 12))  # 기본 레이블 폰트 크기
        
        # 카테고리 레이블용 큰 폰트 스타일
        style.configure("CategoryLabel.TLabel",
                       cursor="arrow",
                       font=('Helvetica', 14, 'bold'))  # 카테고리 폰트 크기
        
        # 총액 표시용 큰 폰트 스타일
        style.configure("Total.TLabel",
                       cursor="arrow",
                       font=('Helvetica', 16, 'bold'))  # 총액 폰트 크기
        
        # 메인 프레임 (padding 제거)
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 메뉴 표시 영역
        self.menu_frame = ttk.LabelFrame(self.main_frame, text="메뉴")
        self.menu_frame.grid(row=0, column=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 장바구니 영역
        self.cart_frame = ttk.LabelFrame(self.main_frame, text="장바구니")
        self.cart_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 총액/결제 영역
        self.payment_frame = ttk.LabelFrame(self.main_frame, text="결제")
        self.payment_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 총액 표시 (내부 위젯의 padding만 유지)
        self.total_label = ttk.Label(
            self.payment_frame, 
            text="총액: 0원", 
            style="Total.TLabel"
        )
        self.total_label.grid(row=0, column=0, pady=5)
        self.checkout_button = ttk.Button(
            self.payment_frame, 
            text="결제하기", 
            command=self.checkout,
            style="Cursor.TButton"
        )
        self.checkout_button.grid(row=1, column=0, pady=5)
        
        self.display_menu()
    
    def display_menu(self):
        row = 0
        for category, items in self.menu_items.items():
            # 카테고리 레이블에 새로운 스타일 적용
            ttk.Label(self.menu_frame, 
                     text=category,
                     style="CategoryLabel.TLabel").grid(row=row, column=0, pady=5)
            row += 1
            
            for item, price in items.items():
                # 메뉴 아이템 레이블에 기본 스타일 적용
                ttk.Label(self.menu_frame, 
                         text=f"{item} - {price}원",
                         style="Cursor.TLabel").grid(row=row, column=0, pady=2)
                # 버튼에 스타일 적용
                ttk.Button(self.menu_frame, 
                          text="추가",
                          style="Cursor.TButton",
                          command=lambda i=item, p=price: self.add_to_cart(i, p)).grid(row=row, column=1)
                row += 1
    
    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        self.update_cart_display()
    
    def update_cart_display(self):
        # 기존 장바구니 표시 내용 삭제
        for widget in self.cart_frame.winfo_children():
            widget.destroy()
            
        # 장바구니 내용 표시
        row = 0
        total = 0
        for item, price in self.cart:
            ttk.Label(self.cart_frame, text=f"{item} - {price}원").grid(row=row, column=0, pady=2)
            row += 1
            total += price
        
        # 총액 업데이트
        self.total_label.config(text=f"총액: {total}원")
    
    def checkout(self):
        # 총액 계산
        total = sum(price for _, price in self.cart)
        
        # 결제 확인 팝업
        if messagebox.askyesno("결제 확인", f"총액: {total}원\n결제하시겠습니까?"):
            # 결제 완료 메시지
            messagebox.showinfo("결제 완료", "결제가 완료되었습니다.")
            # 장바구니 초기화
            self.cart = []
            self.update_cart_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = KioskApp(root)
    root.mainloop() 