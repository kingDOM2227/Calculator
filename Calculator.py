import tkinter as tk

#Text Style Variables
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

#Color Variables
LIGHT_BLUE = "#CCEDFF"
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_GREY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(self):
        #----------GUI Definition------------------
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        # ----------End GUI Definition-------------

       #---------Display Labels--------------------
        self.total_expression = ""
        self.current_expression = ""
       # ---------End Display Labels--------------

#-------------------------------------------------------------------------------------------------------------
                               #FRAME SECTION
#-------------------------------------------------------------------------------------------------------------

        # ------------Creating the frame-------------
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        #----------------Adding the Digits and Operator Buttons-------------
        self.digit = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), ".":(4,1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00d7", "-": "-", "+": "+"}

        #----------------End of Adding the Digits----------------------------

        #---------------Calling Methods--------------------------------------
        self.buttons_frame = self.create_buttons_frame()

        #-------------Expansion of Buttons ------------
        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        #-----------End ofExpansion of Buttons---------
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_botton()
        self.create_sqrt_botton()
        self.bind_keys()
        #-------------End of Calling Methods-----------



#----------//////////////////////////////////////////////////////////////////////////////////------------------

    # ------------------Connecting the keyboard with the Calculator-------------------------

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digit:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
    # ------------------ End of Connecting the keyboard with the Calculator-----------------

    # --------Creating Display Labels------------
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GREY, fg= LABEL_COLOR, padx= 24, font= SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GREY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label, label

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    # ----------End of Creating Display Labels------------

    #----------------Creating the Frame(i.e the designs e.g buttons)--------------------
    def create_display_frame(self):
        frame = tk.Frame(self.window, height= 221, bg= LIGHT_GREY)
        frame.pack(expand=True, fill="both")
        return frame




    #-------------Creating Digit Buttons and Operator Buttons-----------------
    def create_digit_buttons(self):
        for digit, grid_value in self.digit.items():
            button = tk.Button(self.buttons_frame, text = str(digit), bg= WHITE, fg= LABEL_COLOR, font= DIGITS_FONT_STYLE, borderwidth= 0, command= lambda x= digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column =grid_value[1], sticky= tk.NSEW )

    #-------------Operators Functionalities---------------
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    #-----------End of Operators Functionalities----------
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text= symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW, )

            i= i+1

    # -------------Clear Button Functionality---------------

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()


    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    # ----------End of Clear Button Functionality-----------

    # ---------- Square Button Functionality-----------

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()


    def create_square_botton(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    # ----------End of Square Button Functionality-----------

    # ---------- Square Root Button Functionality-----------

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()


    def create_sqrt_botton(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # ----------End of Square Root Button Functionality-----------

    # -------------Equals Button Functionality---------------
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:

            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Math ERROR"
        finally:
            self.update_label()


        # ----------End of Clear Button Functionality-----------

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)


    #---------------End of Creating Digits and Operator Buttons----------------

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    #----------------End of Frame--------------------------------------------

#-----------------------------------FUNCTIONALITIES------------------------------------------------------------

    #--------------------Adding Functionalities------------------------------
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol} ")
        self.total_label.config(text= expression)

    def update_label(self):
        self.label.config(text= self.current_expression[:11])


    # --------------------End of Adding Functionalities----------------------

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
