#Program Written By: Ainsley Bellamy
#Date Written: 04/09/2025
#Program Title: MPG_Calculator


import tkinter
#Initiate GUI class.
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='#4e0707')
        self.main_window.title("Miles Per Gallon Calculator")
#Create containers.
        self.frameEntryPoint1 = tkinter.Frame()
        self.frameEntryPoint2 = tkinter.Frame()
        self.frameDisplay = tkinter.Frame()
        self.frameButtons = tkinter.Frame()
#Create labels in each frame.
        self.gallons = tkinter.Label(self.frameEntryPoint1, text='Enter the number of gallons '
                                                         'your car can hold:', bg='#4e0707', fg='white')
        self.gallons_entry = tkinter.Entry(self.frameEntryPoint1, width=10, bg='#3a3a3a', fg='white')
        self.miles = tkinter.Label(self.frameEntryPoint2, text='Enter the number of miles your'
                                                       'car can drive with a full tank of gas:', bg='#4e0707', fg='white')
        self.miles_entry = tkinter.Entry(self.frameEntryPoint2, width=10, bg='#3a3a3a', fg='white')
        self.answerBox = tkinter.Label(self.frameDisplay, text='Here are the miles per gallon for your car: ', bg='#4e0707', fg='white')
        self.answer = tkinter.StringVar()
        self.answerDisplay = tkinter.Label(self.frameDisplay, textvariable=self.answer, fg='white', bg='darkred')
        self.answer_button = tkinter.Button(self.frameButtons, text='Calculate', command=self.calculate_answer, borderwidth='8', fg='red', bg='black')
        self.exit_button = tkinter.Button(self.frameButtons, text='Exit Program', command=self.main_window.destroy, borderwidth='8', relief='sunken', fg='red', bg='black')
#Pack labels.
        self.gallons.pack(side='left')
        self.gallons_entry.pack(side='left')
        self.miles.pack(side='left')
        self.miles_entry.pack(side='left')
        self.answerBox.pack(side='left')
        self.answerDisplay.pack(side='left')
        self.answer_button.pack(side='left')
        self.exit_button.pack(side='right')
#Pack frames.
        self.frameEntryPoint1.pack()
        self.frameEntryPoint2.pack()
        self.frameDisplay.pack()
        self.frameButtons.pack()
#Mainloop.
        tkinter.mainloop()
#Define method for calculating the MPG.
    def calculate_answer(self):
        numGallons = float(self.gallons_entry.get())
        numMiles = float(self.miles_entry.get())
        calculated_answer = numMiles / numGallons
        self.answer.set(str(f"{calculated_answer:.2f}"))

#Create instance of myGUI class.
if __name__ == '__main__':
    my_gui = myGUI()