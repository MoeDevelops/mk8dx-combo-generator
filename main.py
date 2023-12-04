from tkinter import Tk
from controllers import MainController
from views import MainView
import organiser


def main():
    if not organiser.files_exist():
        organiser.main()

    root = Tk()

    root.geometry("1800x900")
    root.title("Mario Kart 8 Deluxe Combo Generator")

    main_view = MainView(root)
    main_controller = MainController(main_view)

    root.mainloop()


if __name__ == "__main__":
    main()
