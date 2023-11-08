def save_operation(filename, user_name, operation):
    try:
        with open(filename, 'a') as file:
            file.write(operation + '\n')
    except FileNotFoundError:
        with open(filename, 'w') as file:
            file.write(operation + '\n')
