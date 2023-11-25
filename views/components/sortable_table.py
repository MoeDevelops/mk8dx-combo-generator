from tkinter import ttk


class SortableTable(ttk.Treeview):
    def __init__(self, master=None, columns=(), data_list=[]):
        super().__init__(master, columns=columns, show="headings")

        self.columns = columns
        self.data_list = data_list

        self.setup_columns()
        self.populate_table()

    def setup_columns(self):
        for col in self.columns:
            self.heading(
                col, text=col, command=lambda c=col: self.sort_column(c, False))
            self.column(col, anchor="center", width=100)

    def sort_column(self, col, reverse):
        data = [(self.set(child, col), child)
                for child in self.get_children("")]
        data.sort(reverse=reverse)

        for index, item in enumerate(data):
            self.move(item[1], "", index)

        self.heading(col, command=lambda: self.sort_column(col, not reverse))

    def populate_table(self):
        for item in self.data_list:
            self.insert("", "end", values=str(item).split(";"))

    def update_table(self, new_data):
        for child in self.get_children(""):
            self.delete(child)

        self.data_list = new_data
        self.populate_table()
