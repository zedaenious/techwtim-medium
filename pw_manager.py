# master_pwd = input('What is the master password? ')

def add():
  name = input('Username: ')
  pwd = input('Password: ')

  #a = append mode
  with open('pw.txt', 'a') as f:
    f.write(name + ' | ' + pwd + '\n')

def view():
  # r = read mode
  with open('pw.txt', 'r') as f:
    for line in f.readlines():
      data = line.rstrip()
      name, pwd = data.split(" | ")
      print('Username:', name, '\nPassword:', pwd + '\n')

while True:
  action = input('Would you like to (add) a new password, (view) existing passwords, or (quit) the program? ').lower()

  if action == 'quit':
    break

  if action == 'add':
    add()
    continue
  elif action == 'view':
    view()
    continue
  else:
    print('invalid choice')
    continue