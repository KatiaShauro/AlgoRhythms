from gui.main_window import TaskTesterUI
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    app = TaskTesterUI(root)
    root.mainloop()