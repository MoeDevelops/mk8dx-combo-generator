from tkinter import Tk
from controllers import MainController
from views import MainView


if __name__ == "__main__":
    root = Tk()

    root.geometry("1800x900")
    root.title("Mario Kart 8 Deluxe Combo Generator")

    main_view = MainView(root)
    main_controller = MainController(main_view)

    root.mainloop()
