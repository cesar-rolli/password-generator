#Function for copying password to clipboard
def copy1():
    random_pswd = entry.get()
    root.clipboard_clear()
    root.clipboard_append(random_pswd)

#Funciton for generation of password
def generate():
    password1 = low()
    entry.insert(10, password1)