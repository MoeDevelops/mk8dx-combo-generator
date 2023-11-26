from views.components.sortable_table import SortableTable
import tkinter as tk
from typing import List


class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

    def create_filter(self, name: str, value: str, row: int, column: int):
        label = tk.Label(master=self, text=name)
        label.grid(row=row, column=column, sticky=tk.E)

        entry = tk.Entry(master=self, textvariable=value)
        entry.grid(row=row, column=column + 1, sticky=tk.W)

    def create_table(self, columns: list[str], headings: list[str], data: []):
        label = tk.Label(self)
        label.grid()

        self.table = SortableTable(self, columns, headings, data)
        self.table.grid(columnspan=4)

    def create_button(self, text: str, command):
        button = tk.Button(master=self, text=text, command=command)
        button.grid(columnspan=4)

    def update_table(self, data):
        self.table.update_table(data)
