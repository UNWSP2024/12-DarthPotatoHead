#Program Written By: Ainsley Bellamy
#Date Written: 04/25/2025
#Program Title: LongDistance_Calls


import tkinter
import tkinter.messagebox
#Initiate GUI class.
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Long Distance Call Rates Per Minute")
#Create frames.
        self.frameTitle = tkinter.Frame(self.main_window)
        self.frameRadios = tkinter.Frame(self.main_window)
        self.frameEnter = tkinter.Frame(self.main_window)
        self.frameButtons = tkinter.Frame(self.main_window)
#Radiobutton IntVar object.
        self.radio_var = tkinter.DoubleVar()
        self.radio_var.set(1)
#Create and pack title label.
        self.title = tkinter.Label(self.frameTitle, text='Long Distance Call Rates Per Minute')
        self.title.pack()
#Create radiobuttons with values equal to the rates so I can perform the math easily later.
        self.rb1 = tkinter.Radiobutton(self.frameRadios, text='Daytime (6:00 A.M. through 5:59 P.M.) --- $0.02', variable=self.radio_var, value=0.02)
        self.rb2 = tkinter.Radiobutton(self.frameRadios, text='Evening (6:00 P.M. through 11:59 P.M.) --- $0.12', variable=self.radio_var, value=0.12)
        self.rb3 = tkinter.Radiobutton(self.frameRadios, text='Off-Peak (midnight through 5:59 P.M.) --- %0.05', variable=self.radio_var, value=0.05)
#Pack radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
#Create proceed and exit buttons.
        self.proceed_button = tkinter.Button(self.frameButtons, text='Proceed', command=self.calculate_cost)
        self.exit_button = tkinter.Button(self.frameButtons, text='Exit', command=self.main_window.destroy)
#Pack proceed and exit buttons.
        self.proceed_button.pack(side='left')
        self.exit_button.pack(side='left')
#Pack frames.
        self.frameTitle.pack()
        self.frameRadios.pack()
        self.frameEnter.pack()
        self.frameButtons.pack()
#Create place for user to enter the number of minutes for their phone call.
        self.prompt = tkinter.Label(self.frameEnter, text='Total Cost')
        self.minutes_Entry = tkinter.Entry(self.frameEnter)
#Pack the prompt and Entry point.
        self.prompt.pack(side='left')
        self.minutes_Entry.pack(side='left')
#Mainloop.
        tkinter.mainloop()
#Define method to calculate the cost for the user's selected rate.
    def calculate_cost(self):
        cost = self.radio_var.get() * float(self.minutes_Entry.get())
        tkinter.messagebox.showinfo('Total Cost', f'The total cost of your call is: ${cost:.2f}')
#Initiate instance of MyGUI class.
if __name__ == "__main__":
    my_gui = MyGUI()