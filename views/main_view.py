from views.components.sortable_table import SortableTable
import tkinter as tk
from typing import List


class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def create_table(self, columns: list[str], headings: list[str], data: []):
        self.table = SortableTable(self, columns, headings, data)
        self.table.pack(fill="both", expand=True)

    def update_table(self, data):
        self.update_table(data)
