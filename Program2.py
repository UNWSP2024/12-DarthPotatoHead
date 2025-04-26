#Program Written By: Ainsley Bellamy
#Date Written: 04/25/2025
#Program Title: Joe_Automotive


import tkinter
#Initiate GUI class.
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='lightgreen')
        self.main_window.title("Joe's Automotive Services")
#Create containers.
        self.frame1 = tkinter.Frame()
        self.frameOptions = tkinter.Frame(bg='lightgreen')
        self.frameDisplay = tkinter.Frame(bg='lightgreen')
        self.frameButtons = tkinter.Frame(bg='lightgreen')
#Create and pack title label.
        self.title = tkinter.Label(text="* * * Joe's Automotive Services * * *\n--------------------------------------------"
                                        "------------------------------------------", bg='lightgreen', fg='black')
        self.title.pack()
#Checkbox objects.
        self.op1_var = tkinter.IntVar()
        self.op2_var = tkinter.IntVar()
        self.op3_var = tkinter.IntVar()
        self.op4_var = tkinter.IntVar()
        self.op5_var = tkinter.IntVar()
        self.op6_var = tkinter.IntVar()
        self.op7_var = tkinter.IntVar()
        self.op8_var = tkinter.IntVar()
#Set checkbox objects to 0.
        self.op1_var.set(0)
        self.op2_var.set(0)
        self.op3_var.set(0)
        self.op4_var.set(0)
        self.op5_var.set(0)
        self.op6_var.set(0)
        self.op7_var.set(0)
#Place checkboxes in correct frame, format, and change their onvalues to equal the proper dollar amounts.
        self.op1 = tkinter.Checkbutton(self.frameOptions, text='Oil Change - $30.00', bg='lightgreen', fg='darkblue', onvalue=30, variable=self.op1_var)
        self.op2 = tkinter.Checkbutton(self.frameOptions, text='Lube Job - $20.00', bg='lightgreen', fg='darkblue', onvalue=20, variable=self.op2_var)
        self.op3 = tkinter.Checkbutton(self.frameOptions, text='Radiator Flush - $40.00', bg='lightgreen', fg='darkblue', onvalue=40, variable=self.op3_var)
        self.op4 = tkinter.Checkbutton(self.frameOptions, text='Transmission Fluid - $100.00', bg='lightgreen', fg='darkblue', onvalue=100, variable=self.op4_var)
        self.op5 = tkinter.Checkbutton(self.frameOptions, text='Inspection - $35.00', bg='lightgreen', fg='darkblue', onvalue=35, variable=self.op5_var)
        self.op6 = tkinter.Checkbutton(self.frameOptions, text='Muffler Replacement - $200.00', bg='lightgreen', fg='darkblue', onvalue=200, variable=self.op6_var)
        self.op7 = tkinter.Checkbutton(self.frameOptions, text='Tire Rotation - $20.00', bg='lightgreen', fg='darkblue', onvalue=20, variable=self.op7_var)
        self.op8 = tkinter.Checkbutton(self.frameOptions, text='Blinker Fluid - $150.00', bg='lightgreen', fg='darkblue', onvalue=150, variable=self.op8_var)
#Pack checkboxes.
        self.op1.pack()
        self.op2.pack()
        self.op3.pack()
        self.op4.pack()
        self.op5.pack()
        self.op6.pack()
        self.op7.pack()
        self.op8.pack()
#Create list of checkbox options so that I can iterate over them later.
        self.checkboxes = [self.op1_var, self.op2_var, self.op3_var, self.op4_var, self.op5_var, self.op6_var, self.op7_var, self.op8_var,]
#Create and pack display labels.
        self.total_display = tkinter.StringVar()
        self.total = tkinter.Label(self.frameDisplay, textvariable=self.total_display, bg='lightgreen', fg='black')
        self.total.pack(side='left')
#Exit and Done buttons.
        self.done_button = tkinter.Button(self.frameButtons, text='Get Total', command=self.get_total, bg='green', fg='white', borderwidth=5)
        self.exit_button = tkinter.Button(self.frameButtons, text='Exit', command=self.main_window.destroy, bg='green', fg='white', relief='sunken', borderwidth=5)
#Pack buttons.
        self.done_button.pack(side='left')
        self.exit_button.pack(side='left')
#Pack frames.
        self.frame1.pack()
        self.frameOptions.pack()
        self.frameDisplay.pack()
        self.frameButtons.pack()
# Mainloop.
        tkinter.mainloop()
#Define method to sum total.
    def get_total(self):
        sumTotal = 0
#Loop through the list and check the onvalues to see if they are greater that 0; if true, add to sumTotal variable.
        for check in self.checkboxes:
            if check.get() > 0:
                value = check.get()
                sumTotal += value
        self.total_display.set(str(f"Total Cost: ${sumTotal:.2f}"))
#Create instance of myGUI class.
if __name__ == '__main__':
    my_gui = myGUI()