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

        self.to_convert_entry = Entry(self.convertor_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        self.conversion_buttons_frame = Frame(self.convertor_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="to Centigrade", font="Arial 10 bold",
                                  bg="Khaki", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="to Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        self.convertor_label = Label(self.convertor_frame,
                                     font="Arial 14 bold",
                                     fg="Purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.convertor_label.grid(row=4)

        self.hist_help_frame = Frame(self.convertor_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame,
                                       font="Arial 12 bold",
                                       text="Calculation History",
                                       width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Title goes here")
    something = Convertor()
    root = mainloop()
