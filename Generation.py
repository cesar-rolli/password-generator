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