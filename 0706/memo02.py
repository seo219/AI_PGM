import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

DATA_FILE = "todo_data.json"


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 스마트 투두 PRO")
        self.root.geometry("900x650")

        self.tasks = []

        self.build_ui()
        self.load_data()
        self.refresh()

        # 자동 저장
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # ---------------- UI ----------------

    def build_ui(self):
        # ===== 상단 입력 =====
        top = ttk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=10)

        self.entry = ttk.Entry(top)
        self.entry.pack(side="left", fill="x", expand=True)

        ttk.Button(top, text="➕ 추가", command=self.add_task).pack(side="left", padx=5)

        self.priority = ttk.Combobox(top, values=["LOW", "MID", "HIGH"], width=8)
        self.priority.set("MID")
        self.priority.pack(side="left")

        self.date_entry = ttk.Entry(top, width=12)
        self.date_entry.insert(0, "YYYY-MM-DD")
        self.date_entry.pack(side="left", padx=5)

        # ===== 검색 =====
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *args: self.refresh())

        search = ttk.Entry(self.root, textvariable=self.search_var)
        search.pack(fill="x", padx=10)
        search.insert(0, "")

        # ===== 리스트 =====
        self.tree = ttk.Treeview(
            self.root,
            columns=("priority", "date", "tag", "status"),
            show="headings"
        )

        self.tree.heading("priority", text="우선순위")
        self.tree.heading("date", text="마감일")
        self.tree.heading("tag", text="태그")
        self.tree.heading("status", text="상태")

        self.tree.column("priority", width=90)
        self.tree.column("date", width=110)
        self.tree.column("tag", width=150)
        self.tree.column("status", width=100)

        self.tree.tag_configure("done", foreground="gray")
        self.tree.tag_configure("high", foreground="red")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree.bind("<Double-1>", self.toggle_done)

        # ===== 하단 =====
        bottom = ttk.Frame(self.root)
        bottom.pack(fill="x")

        ttk.Button(bottom, text="🗑 삭제", command=self.delete_task).pack(side="left")

        self.progress = ttk.Progressbar(bottom, length=200)
        self.progress.pack(side="right", padx=10)

        self.progress_label = ttk.Label(bottom, text="0%")
        self.progress_label.pack(side="right")

    # ---------------- 기능 ----------------

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            return

        task = {
            "text": text,
            "priority": self.priority.get(),
            "date": self.date_entry.get(),
            "tag": self.extract_tag(text),
            "done": False
        }

        self.tasks.append(task)
        self.entry.delete(0, tk.END)

        self.save_data()
        self.refresh()

    def extract_tag(self, text):
        return " ".join([w for w in text.split() if w.startswith("#")])

    def toggle_done(self, event=None):
        selected = self.tree.selection()
        if not selected:
            return

        idx = int(selected[0])
        self.tasks[idx]["done"] = not self.tasks[idx]["done"]

        self.save_data()
        self.refresh()

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            return

        idx = int(selected[0])
        del self.tasks[idx]

        self.save_data()
        self.refresh()

    # ---------------- 필터 + 정렬 ----------------

    def sort_tasks(self):
        order = {"HIGH": 0, "MID": 1, "LOW": 2}

        self.tasks.sort(
            key=lambda x: (
                x["done"],
                order.get(x["priority"], 1),
                x["date"]
            )
        )

    def filter_tasks(self):
        keyword = self.search_var.get().lower()
        if not keyword:
            return self.tasks

        return [
            t for t in self.tasks
            if keyword in t["text"].lower()
            or keyword in t["tag"].lower()
        ]

    # ---------------- 화면 ----------------

    def refresh(self):
        self.tree.delete(*self.tree.get_children())

        self.sort_tasks()
        tasks = self.filter_tasks()

        done_count = 0

        for i, t in enumerate(tasks):
            status = "DONE" if t["done"] else "TODO"

            # 마감일 체크
            try:
                if t["date"] != "YYYY-MM-DD":
                    due = datetime.strptime(t["date"], "%Y-%m-%d")
                    if due < datetime.now() and not t["done"]:
                        status = "⚠ OVERDUE"
            except:
                pass

            tags = []

            if t["done"]:
                tags.append("done")

            if t["priority"] == "HIGH":
                tags.append("high")

            self.tree.insert(
                "",
                "end",
                iid=i,
                values=(t["priority"], t["date"], t["tag"], status),
                tags=tags
            )

            if t["done"]:
                done_count += 1

        self.update_progress(done_count)

    def update_progress(self, done):
        total = len(self.tasks)

        if total == 0:
            self.progress["value"] = 0
            self.progress_label.config(text="0%")
            return

        percent = int((done / total) * 100)

        self.progress["value"] = percent
        self.progress_label.config(text=f"{percent}%")

    # ---------------- 저장 ----------------

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def load_data(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        except:
            self.tasks = []

    def on_close(self):
        self.save_data()
        self.root.destroy()


# ---------------- 실행 ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()