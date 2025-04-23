import tkinter as tk
from tkinter import ttk, messagebox
import ast
from vol2.Task34 import Task34_vol2


# Dictionary of available tasks
TASKS = {
    'Task34 Vol2': Task34_vol2(),
    # Add more tasks here as needed, e.g.
    # 'Task35_example': Task35_example(),
}

class TaskTesterUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Tester")

        # Заголовок задачи
        self.title_label = ttk.Label(root, text="", font=(None, 14, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='w')

        # Условие задачи
        self.condition_label = ttk.Label(root, text="", wraplength=500, justify='left')
        self.condition_label.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 5), sticky='w')

        # Описание входных данных
        ttk.Label(root, text="Input Data:").grid(row=2, column=0, padx=5, pady=(0, 2), sticky='nw')
        self.input_info_label = ttk.Label(root, text="", wraplength=500, justify='left')
        self.input_info_label.grid(row=2, column=1, padx=5, pady=(0, 2), sticky='w')

        # Описание выходных данных
        ttk.Label(root, text="Output Data:").grid(row=3, column=0, padx=5, pady=(0, 10), sticky='nw')
        self.output_info_label = ttk.Label(root, text="", wraplength=500, justify='left')
        self.output_info_label.grid(row=3, column=1, padx=5, pady=(0, 10), sticky='w')

        # Dropdown для выбора задачи
        ttk.Label(root, text="Select Task:").grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.task_var = tk.StringVar()
        self.task_combo = ttk.Combobox(root, textvariable=self.task_var, values=list(TASKS.keys()), state='readonly')
        self.task_combo.grid(row=4, column=1, padx=5, pady=5, sticky='ew')
        self.task_combo.current(0)
        self.task_combo.bind("<<ComboboxSelected>>", lambda e: self.update_task_info())

        # Поле для ввода параметров
        ttk.Label(root, text="Input Parameters (Python literal):").grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.input_text = tk.Text(root, height=8, width=60)
        self.input_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Кнопка Execute
        self.exec_button = ttk.Button(root, text="Execute", command=self.execute_task)
        self.exec_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # Окно вывода
        ttk.Label(root, text="Output:").grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.output_text = tk.Text(root, height=4, width=60, state='disabled')
        self.output_text.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        root.grid_columnconfigure(1, weight=1)

        # Инициализировать отображение информации для первой задачи
        self.update_task_info()

    def update_task_info(self):
        """
        Обновляет заголовок, условие, описание входных и выходных данных для выбранной задачи.
        """
        task = TASKS.get(self.task_var.get())
        try:
            info = task.get_info()
            self.title_label.config(text=info.get('title', ''))
            self.condition_label.config(text=info.get('condition', ''))
            self.input_info_label.config(text=info.get('input', ''))
            self.output_info_label.config(text=info.get('output', ''))
        except Exception as e:
            self.title_label.config(text="Error loading info")
            self.condition_label.config(text=str(e))
            self.input_info_label.config(text="")
            self.output_info_label.config(text="")

    def execute_task(self):
        task_name = self.task_var.get()
        task = TASKS.get(task_name)
        user_input = self.input_text.get("1.0", tk.END).strip()

        try:
            # Parse the user input into a Python literal
            params = ast.literal_eval(user_input)
            # If single parameter not in tuple/list, wrap into tuple
            if not isinstance(params, tuple) and not isinstance(params, list):
                params = (params,)

            # Call the task's execute method
            result = task.execute(*params) if isinstance(params, tuple) else task.execute(params)

            # Display the result
            self.output_text.configure(state='normal')
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, str(result))
            self.output_text.configure(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = TaskTesterUI(root)
    root.mainloop()
