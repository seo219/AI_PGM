import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import os

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")

        self.filename = None
        self.modified = False
        self.dark = False

        self.font_size = 12

        self.make_menu()
        self.make_text()
        self.make_status()

        self.bind_shortcuts()

        self.update_title()

    # ---------------- 메뉴 ----------------

    def make_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="파일", menu=file)
        file.add_command(label="새 파일\tCtrl+N", command=self.new_file)
        file.add_command(label="열기\tCtrl+O", command=self.open_file)
        file.add_command(label="저장\tCtrl+S", command=self.save_file)
        file.add_command(label="다른 이름으로 저장", command=self.save_as)
        file.add_separator()
        file.add_command(label="종료", command=self.exit_program)

        edit = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="편집", menu=edit)
        edit.add_command(label="실행 취소", command=lambda:self.text.event_generate("<<Undo>>"))
        edit.add_command(label="다시 실행", command=lambda:self.text.event_generate("<<Redo>>"))
        edit.add_separator()
        edit.add_command(label="잘라내기", command=lambda:self.text.event_generate("<<Cut>>"))
        edit.add_command(label="복사", command=lambda:self.text.event_generate("<<Copy>>"))
        edit.add_command(label="붙여넣기", command=lambda:self.text.event_generate("<<Paste>>"))
        edit.add_separator()
        edit.add_command(label="찾기 (Ctrl+F)", command=self.find_text)

        view = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="보기", menu=view)
        view.add_command(label="다크모드", command=self.toggle_dark)
        view.add_command(label="글자 크게", command=self.font_up)
        view.add_command(label="글자 작게", command=self.font_down)
        view.add_command(label="자동 줄바꿈", command=self.toggle_wrap)

    # ---------------- 텍스트 ----------------

    def make_text(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True)

        scroll = ttk.Scrollbar(frame)
        scroll.pack(side="right", fill="y")

        self.text = tk.Text(
            frame,
            undo=True,
            font=("Consolas", self.font_size),
            wrap="word",
            yscrollcommand=scroll.set
        )

        self.text.pack(fill="both", expand=True)

        scroll.config(command=self.text.yview)

        self.text.bind("<<Modified>>", self.on_modified)
        self.text.bind("<KeyRelease>", self.update_status)

    # ---------------- 상태바 ----------------

    def make_status(self):
        self.status = ttk.Label(self.root, anchor="w")
        self.status.pack(fill="x")
        self.update_status()

    # ---------------- 기능 ----------------

    def update_title(self):
        name = "새 파일"

        if self.filename:
            name = os.path.basename(self.filename)

        star = "*" if self.modified else ""
        self.root.title(f"{star}{name} - Python Notepad")

    def on_modified(self, event=None):
        self.modified = True
        self.update_title()
        self.update_status()
        self.text.edit_modified(False)

    def update_status(self, event=None):
        row, col = self.text.index("insert").split(".")
        self.status.config(text=f"줄 {row}   열 {int(col)+1}")

    def new_file(self):
        if not self.ask_save():
            return

        self.text.delete("1.0", tk.END)
        self.filename = None
        self.modified = False
        self.update_title()

    def open_file(self):
        if not self.ask_save():
            return

        file = filedialog.askopenfilename()

        if file:
            with open(file, "r", encoding="utf-8") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", f.read())

            self.filename = file
            self.modified = False
            self.update_title()

    def save_file(self):
        if self.filename is None:
            return self.save_as()

        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(self.text.get("1.0", tk.END))

        self.modified = False
        self.update_title()

    def save_as(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text",".txt"),("Python",".py"),("All","*.*")]
        )

        if file:
            self.filename = file
            self.save_file()

    def ask_save(self):
        if not self.modified:
            return True

        result = messagebox.askyesnocancel("저장", "변경사항을 저장하시겠습니까?")

        if result is None:
            return False

        if result:
            self.save_file()

        return True

    def exit_program(self):
        if self.ask_save():
            self.root.destroy()

    # ---------------- 찾기 ----------------

    def find_text(self):
        word = simpledialog.askstring("찾기", "찾을 내용을 입력하세요")

        if not word:
            return

        self.text.tag_remove("find", "1.0", tk.END)

        pos = "1.0"

        while True:
            pos = self.text.search(word, pos, stopindex=tk.END)

            if not pos:
                break

            end = f"{pos}+{len(word)}c"

            self.text.tag_add("find", pos, end)

            pos = end

        self.text.tag_config("find", background="yellow")

    # ---------------- 다크모드 ----------------

    def toggle_dark(self):

        self.dark = not self.dark

        if self.dark:
            self.text.config(
                bg="#1E1E1E",
                fg="white",
                insertbackground="white"
            )
        else:
            self.text.config(
                bg="white",
                fg="black",
                insertbackground="black"
            )

    # ---------------- 글꼴 ----------------

    def font_up(self):
        self.font_size += 1
        self.text.config(font=("Consolas", self.font_size))

    def font_down(self):
        if self.font_size > 8:
            self.font_size -= 1
            self.text.config(font=("Consolas", self.font_size))

    # ---------------- 줄바꿈 ----------------

    def toggle_wrap(self):
        if self.text["wrap"] == "none":
            self.text.config(wrap="word")
        else:
            self.text.config(wrap="none")

    # ---------------- 단축키 ----------------

    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e:self.new_file())
        self.root.bind("<Control-o>", lambda e:self.open_file())
        self.root.bind("<Control-s>", lambda e:self.save_file())
        self.root.bind("<Control-f>", lambda e:self.find_text())

        self.root.protocol("WM_DELETE_WINDOW", self.exit_program)

root = tk.Tk()
Notepad(root)
root.mainloop()