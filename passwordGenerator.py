import random
from tkinter import *
from tkinter.ttk import *

root = Tk()
lengthEntry = IntVar()
passwordType = IntVar()

def copyPasswordToClipboard():
  generatedPassword = passwordOutput.get()
  root.clipboard_clear()
  root.clipboard_append(generatedPassword)

def generate():
  password1 = passwordGeneration()
  passwordOutput.insert(10, password1)

def passwordGeneration():
  passwordOutput.delete(0, END)

  length = int(lengthEntry.get())

  allCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]{}()!@#$%&*,.;:?/-_=+"
  numbers = "0123456789"
  password = ""

  #If the type includes all characters
  if passwordType.get() == 0:
    for i in range(0, length):
      password += random.choice(allCharacters + numbers)
    return password
  
  #If the type is only numbers
  if passwordType.get() == 1:
    for i in range(0, length):
      password += random.choice(numbers)
    return password

# # GUI # #
#Title of GUI window
root.title("Password Generator")

#Create label for length of password
lengthLabel = Label(root, text = "Length")
lengthLabel.grid(row = 0, column = 0)
lengthEntry = Entry(root)
lengthEntry.grid(row = 0, column = 1)
generateButton = Button(root, text = "Generate", command = generate)
generateButton.grid(row = 0, column = 2)

copy_buttons = Button(root, text = "Copy", command = copyPasswordToClipboard)
copy_buttons.grid(row = 1, column = 2)

#Radio buttons to set 
allCharactersButton = Radiobutton(root, text = "All Characters", variable = passwordType, value =0)
allCharactersButton.grid(row = 2, column = 0, sticky = "E")
onlyNumbers = Radiobutton(root, text = "Only Numbers", variable = passwordType, value = 1)
onlyNumbers.grid(row = 2, column = 1, sticky = "E")

#Create label and entry to show
passwordLabel = Label(root, text = "Password")
passwordLabel.grid(row = 1)
passwordOutput = Entry(root)
passwordOutput.grid(row = 1, column = 1)

root.mainloop()