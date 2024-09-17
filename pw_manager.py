# master_pwd = input('What is the master password? ')

def add():
  name = input('Username: ')
  pwd = input('Password: ')

  with open('passwords.txt', 'a') as f:
    f.write(name + ' | ' + pwd + '\n')

def view():
  pass

action = input('Would you like to (add) a new password, (view) existing passwords, or (quit) the program? ').lower()

while True:
  if action == 'quit':
    break

  if action == 'add':
    add()
  elif action == 'view':
    view()
  else:
    print('invalid choice')
    continue