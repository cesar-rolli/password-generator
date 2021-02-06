import random
from tkinter import *
import string
from tkinter import messagebox
from tkinter.ttk import *

#Create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

#Function for copying password to clipboard
def copy1():
  random_pswd = entry.get()
  root.clipboard_clear()
  root.clipboard_append(random_pswd)

#Funciton for generation of password
def generate():
  password1 = low()
  entry.insert(10, password1)


def low():
  entry.delete(0, END)

  #Get the length of password
  length = var1.get()
  lower = "abcdefghijklmnopqrstuvwxyz"
  upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "0123456789"
  symbols = "[]{}()!@#$%&*,.;:?/-_=+"
  password=""
    
  #if strength selected is low
  if var.get() == 1:
    for i in range(0, length):
      password = password + random.choice(lower)
    return password 

  #if strength selected is medium
  if var.get() == 0:
    for i in range(0, length):
      password = password + random.choice(lower) + random.choice(lower)
    return password
        
  #if strength selected is strong
  if var.get() == 3:
    for i in range(0, length):
      password = password + random.choice(lower) + random.choice(lower) + random.choice(numbers) + random.choice(symbols)
    return password

  else:
    messagebox.showwarning('Python Says', 'First select any option')



#Title of GUI window
root.title("Password Generator")

#Create label and entry to show
Random_password = Label(root, text = "Password")
Random_password.grid(row = 0)
entry = Entry(root)
entry.grid(row = 0, column = 1)

#Create label for length of password
c_label = Label(root, text = "Length")
c_label.grid(row = 1)

#Create buttons
copy_buttons = Button(root, text = "Copy", command = copy1)
copy_buttons.grid(row = 0, column = 2)
generate_button = Button(root, text = "Generate", command = generate)
generate_button.grid(row = 0, column = 3)
exit_button = Button (root, text = "Exit", command = root.quit)
exit_button.grid(row = 0, column = 4)

#Radio buttons
radio_low = Radiobutton(root, text = "Low", variable = var, value =1)
radio_low.grid(row = 1, column = 2, sticky = "E")
radio_middle = Radiobutton(root, text = "Medium", variable = var, value = 0)
radio_middle.grid(row = 1, column = 3, sticky = "E")
radio_strong = Radiobutton(root, text = "Strong", variable = var, value = 3)
radio_strong.grid(row = 1, column = 3, sticky = "E")
combo = Combobox(root, textvariable = var1)

#Combo box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column = 1, row = 1)
root.mainloop()