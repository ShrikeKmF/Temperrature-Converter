from tkinter import *


class Convertor:
    def __init__(self):
        background_color = "light blue"

        self.convertor_frame = Frame(width=300, bg=background_color, pady=10)
        self.convertor_frame.grid()

        self.temp_heading_label = Label(self.convertor_frame,
                                        text="Temperature Convertor",
                                        font="Arial 14 bold",
                                        bg=background_color, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        self.temp_instructions_label = Label(self.convertor_frame,
                                             text="Type in the amount to be"
                                                  "converted and then push"
                                                  "one of the buttons bellow..",
                                             font="Arial 10 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Title goes here")
    something = Convertor()
    root = mainloop()
