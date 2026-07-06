import tkinter as tk

# 버튼 클릭 시 화면에 표시
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# 계산
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# 화면 지우기
def clear():
    entry.delete(0, tk.END)

# 한 글자 삭제
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# 메인 창
window = tk.Tk()
window.title("계산기")
window.geometry("320x450")
window.resizable(True, True)

# 입력창
entry = tk.Entry(window, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# 버튼 배치
buttons = [
    ("C", 1, 0), ("←", 1, 1), ("/", 1, 2), ("*", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
    ("0", 5, 0), (".", 5, 1)
]

for (text, row, col) in buttons:
    if text == "=":
        command = calculate
    elif text == "C":
        command = clear
    elif text == "←":
        command = backspace
    else:
        command = lambda t=text: click(t)

    tk.Button(
        window,
        text=text,
        font=("Arial", 16),
        width=5,
        height=2,
        command=command
    ).grid(row=row, column=col, padx=5, pady=5)

# 0 버튼을 두 칸으로 확장
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

window.mainloop()