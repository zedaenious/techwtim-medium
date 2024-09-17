pwd = input('What is the master password? ')

def add():
  pass

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