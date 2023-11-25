from tkinter import ttk


class SortableTable(ttk.Treeview):
    def __init__(self, master, attributes: list[str], headings: list[str], items: list[any]):
        super().__init__(master, columns=attributes, show="headings")
        self.columns = attributes
        self.sort_column = None
        self.sort_order = False  # False = asc, True = desc

        if len(attributes) != len(headings):
            raise ValueError(
                "Attributes and headings don't have the same length")

        for i in range(len(attributes)):
            column = attributes[i]
            heading = headings[i]
            self.heading(column, text=heading,
                         command=lambda col=column: self.sort_by(col))
            self.column(column, width=100, anchor="center")

        self.update_items(items)

    def update_items(self, items: list[any]):
        self.items = items
        self.update_table()

    def update_table(self):
        if self.sort_column is not None:
            self.items.sort(key=lambda item: getattr(
                item, self.sort_column, None), reverse=self.sort_order)

        self.delete(*self.get_children())

        for item in self.items:
            values = [getattr(item, attribute, None)
                      for attribute in self.columns]
            self.insert("", "end", values=values)

    def sort_by(self, column):
        if self.sort_column == column:
            self.sort_order = not self.sort_order
        else:
            self.sort_order = False

        self.sort_column = column

        self.update_table()
