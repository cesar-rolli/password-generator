import random
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

import os

from PIL import Image
import pyqrcode

#Image dimensions (this dimensions is capable to read a 150 characters password).
widthImage = 100
lengthImage = 100

root = Tk()
lengthEntry = IntVar()
passwordType = IntVar()

def copyPasswordToClipboard():
  generatedPassword = passwordOutput.get()
  root.clipboard_clear()
  root.clipboard_append(generatedPassword)

def createAction():
  #Create the password.
  password1 = passwordGeneration()
  passwordOutput.insert(10, password1)

  #Create the QR Code.
  qr_data = passwordOutput.get()
  passwordInQRCode = pyqrcode.create(qr_data)
  passwordInQRCode.png('passwordInQRCode.png', scale = 4)

  #Resize the QR Code generated.
  passwordInQRCodeResized = Image.open("passwordInQRCode.png")
  passwordInQRCodeResized = passwordInQRCodeResized.resize((widthImage,lengthImage),Image.ANTIALIAS)
  passwordInQRCodeResized.save(fp="passwordInQRCodeResized.png")

  #Show the password in QR Code.
  qrCodeImage = tk.PhotoImage(file = "passwordInQRCodeResized.png")
  qrImage = tk.Label(root, image = qrCodeImage)
  qrImage.qrCodeImage = qrCodeImage
  qrImage.grid(row = 1, column = 3)

  #Delete created QR Code.
  os.remove("passwordInQRCode.png")
  os.remove("passwordInQRCodeResized.png")

def passwordGeneration():
  passwordOutput.delete(0, END)

  length = int(lengthEntry.get())

  allCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]{}()!@#$%&*,.;:?/-_=+"
  numbers = "0123456789"
  password = ""

  #If the type includes all characters.
  if passwordType.get() == 0:
    for i in range(0, length):
      password += random.choice(allCharacters + numbers)
    return password
  
  #If the type is only numbers.
  if passwordType.get() == 1:
    for i in range(0, length):
      password += random.choice(numbers)
    return password

#Show "Your password's QR Code will appear here." in QR Code format.
qrCodeMessageResized = Image.open("qrCodeMessage.png")
qrCodeMessageResized = qrCodeMessageResized.resize((widthImage, lengthImage),Image.ANTIALIAS)
qrCodeMessageResized.save(fp="qrCodeMessageResized.png")
qrCodeImage = tk.PhotoImage(file = "qrCodeMessageResized.png")
qrImage = tk.Label(root, image = qrCodeImage)
qrImage.qrCodeImage = qrCodeImage
qrImage.grid(row = 1, column = 3)


# # GUI # #
#Title of GUI window.
root.title("Password Generator")
# root.geometry('250x150')

#Create label for length of password.
lengthLabel = Label(root, text = "Length", font = 'Roboto')
lengthLabel.grid(row = 0, column = 0)
lengthEntry = Entry(root, font = 'Roboto')
lengthEntry.grid(row = 0, column = 1)
generateButton = Button(root, text = "Generate", command = createAction)
generateButton.grid(row = 0, column = 4)

#Radio buttons to set.
allCharactersButton = Radiobutton(root, text = "All Characters", variable = passwordType, value =0)
allCharactersButton.grid(row = 0, column = 2, sticky = "E")
onlyNumbers = Radiobutton(root, text = "Only Numbers", variable = passwordType, value = 1)
onlyNumbers.grid(row = 0, column = 3, sticky = "E")

copy_buttons = Button(root, text = "Copy", command = copyPasswordToClipboard)
copy_buttons.grid(row = 1, column = 2)

#Create label and entry to show.
passwordLabel = Label(root, text = "Password", font = 'Roboto')
passwordLabel.grid(row = 1)
passwordOutput = Entry(root, font = 'Roboto')
passwordOutput.grid(row = 1, column = 1)

# root.configure(background = '#111', )
root.resizable(False, False)
root.mainloop()