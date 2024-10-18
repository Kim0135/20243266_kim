
# # 첫 번째 입력: 정수의 개수 N
# N = int(input())

# # 두 번째 입력: N개의 정수 리스트
# numbers = list(map(int, input().split()))

# # 최솟값과 최댓값을 구해서 출력
# print(min(numbers), max(numbers))

# def is_perfect(n):
#     divisors = []
    
#     # 약수 구하기 (자기 자신은 제외)
#     for i in range(1, n):
#         if n % i == 0:
#             divisors.append(i)
    
#     # 약수들의 합이 n과 같은지 확인
#     if sum(divisors) == n:
#         # 약수들을 합쳐서 출력 형식에 맞게 반환
#         return f"{n} = {' + '.join(map(str, divisors))}"
#     else:
#         return f"{n} is NOT perfect."

# while True:
#     # 입력 받기
#     n = int(input())
    
#     # 입력이 -1이면 종료
#     if n == -1:
#         break
    
#     # 완전수 여부 판단 및 출력
#     print(is_perfect(n))
import tkinter as tk
from tkinter import Toplevel, messagebox

# 사용자 정보를 저장할 파일
USERS_FILE = "users.txt"

# 회원 정보를 파일에서 불러오는 함수
def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            users = [line.strip().split(",") for line in file]
    except FileNotFoundError:
        users = []
    return users

# 회원 정보를 파일에 저장하는 함수
def save_users(users):
    with open(USERS_FILE, "w") as file:
        for user in users:
            file.write(",".join(user) + "\n")

# 회원 정보 초기화
users = load_users()

# 자리를 나타내는 리스트
seats = ["빈자리" for _ in range(12)]  # 12개의 자리를 초기화

# 자리 상태 업데이트 함수
def update_seat_status():
    for i, button in enumerate(seat_buttons):
        if seats[i] == "빈자리":
            button.config(bg="green", command=lambda i=i: reserve_seat(i))
        else:
            button.config(bg="red", command=lambda i=i: release_seat(i))

# 현재 로그인한 사용자 설정 함수
def set_logged_in_user(username):
    window.logged_in_user = username

# 현재 로그인한 사용자 가져오는 함수
def get_logged_in_user():
    return window.logged_in_user

# 현재 사용자가 로그인했는지 확인하는 함수
def is_user_logged_in():
    return get_logged_in_user() is not None

# 로그인 창 함수
def show_login_window():
    login_window = tk.Toplevel(window)
    login_window.title("로그인")
    
    login_username_label = tk.Label(login_window, text="사용자 이름:")
    login_username_label.grid(row=0, column=0, pady=(10, 5))
    
    login_username_entry = tk.Entry(login_window)
    login_username_entry.grid(row=0, column=1, pady=(10, 5))
    
    login_password_label = tk.Label(login_window, text="비밀번호:")
    login_password_label.grid(row=1, column=0, pady=5)
    
    login_password_entry = tk.Entry(login_window, show="*")
    login_password_entry.grid(row=1, column=1, pady=5)
    
    login_button = tk.Button(login_window, text="로그인", command=lambda: login(login_username_entry.get(), login_password_entry.get()))
    login_button.grid(row=2, column=0, columnspan=2, pady=5)

# 회원가입 창 함수
def show_register_window():
    register_window = tk.Toplevel(window)
    register_window.title("회원가입")
    
    register_username_label = tk.Label(register_window, text="사용자 이름:")
    register_username_label.grid(row=0, column=0, pady=(10, 5))
    
    register_username_entry = tk.Entry(register_window)
    register_username_entry.grid(row=0, column=1, pady=(10, 5))
    
    register_password_label = tk.Label(register_window, text="비밀번호:")
    register_password_label.grid(row=1, column=0, pady=5)
    
    register_password_entry = tk.Entry(register_window, show="*")
    register_password_entry.grid(row=1, column=1, pady=5)
    
    register_button = tk.Button(register_window, text="회원가입", command=lambda: register(register_username_entry.get(), register_password_entry.get()))
    register_button.grid(row=2, column=0, columnspan=2, pady=5)

# 로그인 함수
def login(username, password):
    for user in users:
        if user[0] == username and user[1] == password:
            messagebox.showinfo("로그인 성공", f"{username}님, 환영합니다!")
            set_logged_in_user(username)
            show_seat_reservation_window()
            return
    
    messagebox.showerror("로그인 실패", "사용자 이름 또는 비밀번호가 잘못되었습니다.")

# 로그아웃 함수
def logout():
    set_logged_in_user(None)
    messagebox.showinfo("로그아웃", "로그아웃되었습니다.")

# 회원가입 함수
def register(username, password):
    if not username or not password:
        messagebox.showerror("입력 오류", "모든 필드를 입력해주세요.")
    else:
        users.append([username, password])
        save_users(users)
        messagebox.showinfo("회원가입 성공", f"{username}님, 회원가입이 완료되었습니다!")

# 자리 예약 창 함수
def show_seat_reservation_window():
    seat_window = tk.Toplevel(window)
    seat_window.title("자리 예약")

    # 자리 버튼 생성
    seat_buttons = []
    for i in range(12):
        button = tk.Button(seat_window, text=f"{i+1}번 자리", width=10, height=2, command=lambda i=i: reserve_seat(i))
        button.grid(row=i // 6, column=i % 6, padx=5, pady=5)
        seat_buttons.append(button)

# 자리 예약 함수
def reserve_seat(seat_number):
    if not is_user_logged_in():
        messagebox.showwarning("로그인 필요", "자리를 예약하려면 로그인이 필요합니다.")
        return
    
    user = get_logged_in_user()
    
    if seats[seat_number] == "빈자리":
        seats[seat_number] = user
        messagebox.showinfo("예약 완료", f"{seat_number+1}번 자리가 예약되었습니다.")
    else:
        messagebox.showwarning("예약 불가", f"{seat_number+1}번 자리는 이미 사용 중입니다.")
    
    update_seat_status()

# tkinter 윈도우 생성
window = tk.Tk()
window.title("AI 융합학부 과방 자리 예약 시스템")

# 로그인 버튼
login_button = tk.Button(window, text="로그인", command=show_login_window)
login_button.grid(row=0, column=0, pady=10)

# 회원가입 버튼
register_button = tk.Button(window, text="회원가입", command=show_register_window)
register_button.grid(row=0, column=1, pady=10)

# tkinter 이벤트 루프 시작
window.mainloop()