from tkinter import Tk
from controllers.main_controller import MainController
from views.main_view import MainView


if __name__ == "__main__":
    root = Tk()

    root.geometry("1600x800")
    root.title("Mario Kart 8 Deluxe Combo Generator")

    main_view = MainView(root)
    main_controller = MainController(main_view)

    root.mainloop()
