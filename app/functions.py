import tkinter as tk
from tkinter.simpledialog import askstring
import re
from app.db import save_operation

def get_user_name():
    user_name = askstring("Enter Your Name", "Please enter your name:")
    return user_name

def is_valid_number(input_str):
    # Use regular expressions to check if the input is a valid number
    return re.match(r'^[-+]?[0-9]*\.?[0-9]+$', input_str) is not None

def calculate_and_save(number1, number2, result_label, user_name):
    num1 = number1.get().strip()
    num2 = number2.get().strip()

    if not is_valid_number(num1) or not is_valid_number(num2):
        result_label.config(text="Please enter valid numbers.")
        return

    num1 = float(num1)
    num2 = float(num2)

    # Perform calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    result_text = (
        f"{num1} + {num2} = {addition}\n"
        f"{num1} - {num2} = {subtraction}\n"
        f"{num1} * {num2} = {multiplication}\n"
        f"{num1} / {num2} = {division}"
    )

    result_label.config(text=result_text)

    # Ensure user name is in title case
    user_name = user_name.title()

    # Save the operation to a file named after the user
    operation_text = (
        f"This is {user_name}'s answers:\n"
        f"{num1} + {num2} = {addition}\n"
        f"{num1} - {num2} = {subtraction}\n"
        f"{num1} * {num2} = {multiplication}\n"
        f"{num1} / {num2} = {division}"
    )

    save_operation(f'app/{user_name}.txt', user_name, operation_text)
