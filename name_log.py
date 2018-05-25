guest_log = []
employee_log = []
name = ''

def why_here():
    you_are = input('Hello! Are you a guest or employee? ')
    refined_you = you_are.lower()
    if refined_you == 'guest':
        guest_log.append(refined_you)
    else:
        employee_log.append(refined_you)

def who_you():
    pass

def log_name():
    name = input('Please enter your name: ')
    if name != 'exit'
        guest_log.append(name)
