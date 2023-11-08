import tkinter as tk
from app.functions import calculate_and_save, get_user_name


def main():
    app = tk.Tk()
    app.title("Number Operations")

    user_name_var = tk.StringVar()
    user_name_var.set("")

    user_name_label = tk.Label(app, text="User Name:", font=('Arial', 12))
    user_name_label.grid(row=0, column=0)

    user_name_entry = tk.Entry(app, textvariable=user_name_var, font=('Arial', 12))
    user_name_entry.grid(row=0, column=1)

    number1_label = tk.Label(app, text="Number 1:", font=('Arial', 12))
    number1_label.grid(row=1, column=0)
    number1 = tk.Entry(app, font=('Arial', 24))
    number1.grid(row=1, column=1)

    number2_label = tk.Label(app, text="Number 2:", font=('Arial', 12))
    number2_label.grid(row=2, column=0)
    number2 = tk.Entry(app, font=('Arial', 24))
    number2.grid(row=2, column=1)

    result_label = tk.Label(app, text="", font=('Arial', 12))
    result_label.grid(row=3, column=0, columnspan=2)

    def calculate_and_save_wrapper():
        user_name = user_name_var.get()
        calculate_and_save(number1, number2, result_label, user_name)

    calculate_button = tk.Button(app, text="Calculate", font=('Arial', 18),
                                 command=calculate_and_save_wrapper)
    calculate_button.grid(row=4, column=0, columnspan=2)

    app.mainloop()


if __name__ == '__main__':
    main()
