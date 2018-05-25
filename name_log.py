guest_log = []
employee_log = []
name = ''

def why_here():
    you_are = input('Hello! Are you a guest or employee? ')
    refined_you = you_are.lower()
    if refined_you == 'guest':
        log_guest()
    else:
        log_employee()
    return

def log_guest():
    guest_name = input('Welcome to the waiting room. What is your name? ')
    guest_log.append('guest ' + guest_name)
    print()
    print()
    print('Thank you {}! Please have a seat.'.format(guest_name))



def log_employee():
    employee_name = input('Welcome to hell. What is your name? ')
    employee_log.append("Emp ID#: " + str(id(employee_name)) + '  ' + employee_name)
    print()
    print()
    print('{}! Get the fuck to work.'.format(employee_name))


why_here()