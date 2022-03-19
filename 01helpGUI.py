from tkinter import *
from functools import partial


class Convertor:
    def __init__(self):
        # Formatting
        background_color = "light blue"

        # Main Screen
        self.convertor_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.convertor_frame.grid()

        # Temperature Convertor
        self.temp_convertor_label = Label(text="Temperature Convertor",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        self.help_button = Button(self.convertor_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=0)

        def help(self):
            print("You  asked for help")
            get_help = Help()
            get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self):
        background = "orange"

        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()


# Comment
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
