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
                                             font="Arial 10 italic", wrap=290,
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
                                  bg="Khaki", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="to Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
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

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"

        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert,
                                                               fahrenheit)
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert,
                                                               celsius)

            else:
                answer = "Too Cold"
                has_errors = "yes"

            if has_errors == "no":
                self.convertor_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.convertor_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg="error")

        except ValueError:
            self.convertor_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        return rounded


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Title goes here")
    something = Convertor()
    root.mainloop()
