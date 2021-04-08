import tkinter
from tkinter import Button, Label, Entry, END, StringVar
from tkinter.messagebox import showinfo

class KilometerConverterGUI:
   def __init__(self):
 # create window
       self.main_window = tkinter.Tk()
       self.main_window.geometry('380x290+100+20')
       self.main_window.title("Kilometers to Miles Converter")
 # Create widgets
       self.entry_km = Entry(self.main_window, width=12,font=('Tahoma', 12))
       self.label_km = Label(self.main_window, text="kilometers",
                           font=('MV Boli', 12, 'italic'))
       self.label_equal = Label(self.main_window, text = "is equal to",
                                font=('MV Boli', 12, 'italic'))
       self.ml = StringVar()
       self.label_ml = Label(self.main_window, textvariable = self.ml,
                             font=('Tahoma', 12))
       self.label_mle = Label(self.main_window, text = "miles", width=20,
                             height=8,font=('MV Boli', 12, 'italic'))
 #buttons
       self.button_convert = Button(self.main_window, text='Convert',
                   font=('Times New Roman',12, 'italic'),command=self.convert)
       self.button_quit = Button(self.main_window, text="   Quit   ", font=(
              'Times New Roman',12, 'italic'),command=self.main_window.destroy)
#lay out widgets
       self.entry_km.grid(row=0, column=3, padx=8, pady=8)
       self.label_km.grid(row=0, column= 4, padx=5, pady=8)
       self.label_equal.grid(row=2, column=1, padx=5, pady=8)
       self.label_ml.grid(row=2, column=3, padx=8, pady=8)
       self.label_mle.grid(row=2, column=4, padx=8, pady=8)
       self.button_convert.grid(row=4, column=1, columnspan=1,
                    padx=8, pady=8)
       self.button_quit.grid (row=4, column=4, columnspan=3,
                    padx=3, pady=3)
       self.main_window.mainloop()

# method for validation of input
   def is_number(self,s):
       try:
           float(s)
           return True
       except ValueError:
           return False

 # method for convert button
   def convert(self):
       km = self.entry_km.get()
       if self.is_number(km):
           ml = round((float(km) /1.60934),3)
           self.ml.set(ml)
       else:
           self.entry_km.delete(0, END)
           showinfo(message="Incorrect input")

my_gui=KilometerConverterGUI()
