
# Program Name: Assignment3.py
# Course: IT3883 / Section XXX
# Student Name: [Enter your name]
# Assignment Number: Lab 3
# Due Date: [Enter due date]
# Purpose: Convert miles per gallon (MPG) into kilometers per liter (km/L).
#          The answer updates automatically whenever the user changes the MPG
#          value.
# Resources: Python tkinter documentation (docs.python.org/3/library/tkinter.html);

import math
import tkinter as tk


MPG_TO_KM_PER_LITER = 0.425143707


def build_window():
    """Create the window and its live MPG-to-km/L converter."""
    window = tk.Tk()
    window.title("MPG to km/L Converter")
    window.geometry("490x335")
    window.resizable(False, False)
    window.configure(bg="#f3f6fb")

    # StringVar connects the text field to our conversion function.
    mpg_text = tk.StringVar()
    result_text = tk.StringVar(value="—")
    message_text = tk.StringVar(value="Enter an MPG value to begin.")

    # Calculate a new result every time the text inside the entry changes.
    def update_result(*unused_arguments):
        typed_value = mpg_text.get().strip()

        if typed_value == "":
            result_text.set("—")
            message_text.set("Enter an MPG value to begin.")
            return

        try:
            mpg_number = float(typed_value)
        except ValueError:
            result_text.set("—")
            message_text.set("Please enter a number, not letters or symbols.")
            return

        # Negative MPG and non-finite numbers are not valid fuel-economy values.
        if not math.isfinite(mpg_number) or mpg_number < 0:
            result_text.set("—")
            message_text.set("Enter a non-negative, finite MPG value.")
            return

        converted_number = mpg_number * MPG_TO_KM_PER_LITER
        if not math.isfinite(converted_number):
            result_text.set("—")
            message_text.set("This MPG value is too large to convert.")
            return

        result_text.set(f"{converted_number:.4f} km/L")

    # The input is tracked, so there is no need for a Convert button.
    mpg_text.trace_add("write", update_result)

    # Build the application header.
    tk.Label(
        window,
        text="Fuel Economy Converter",
        font=("Arial", 20, "bold"),
        fg="#182b49",
        bg="#f3f6fb",
    ).pack(pady=(24, 6))

    tk.Label(
        window,
        text="Miles per gallon  →  Kilometers per liter",
        font=("Arial", 11),
        fg="#52627a",
        bg="#f3f6fb",
    ).pack(pady=(0, 20))

    # The user types MPG into a single input box.
    tk.Label(
        window,
        text="Miles per gallon (MPG)",
        font=("Arial", 11, "bold"),
        fg="#182b49",
        bg="#f3f6fb",
    ).pack(anchor="w", padx=45)

    mpg_entry = tk.Entry(
        window,
        textvariable=mpg_text,
        font=("Arial", 17),
        justify="center",
        bg="white",
        fg="#182b49",
        relief="solid",
        bd=1,
    )
    mpg_entry.pack(fill="x", padx=45, ipady=7, pady=(7, 21))

    # The output label changes automatically after each keystroke.
    tk.Label(
        window,
        text="Kilometers per liter (km/L)",
        font=("Arial", 11, "bold"),
        fg="#182b49",
        bg="#f3f6fb",
    ).pack(anchor="w", padx=45)

    tk.Label(
        window,
        textvariable=result_text,
        font=("Arial", 22, "bold"),
        fg="#126b54",
        bg="#f3f6fb",
        anchor="center",
    ).pack(fill="x", pady=(7, 4))

    tk.Label(
        window,
        textvariable=message_text,
        font=("Arial", 10),
        fg="#52627a",
        bg="#f3f6fb",
    ).pack(pady=(3, 9))

    tk.Label(
        window,
        text="Conversion: 1 MPG = 0.425143707 km/L",
        font=("Arial", 9),
        fg="#687589",
        bg="#f3f6fb",
    ).pack()

    mpg_entry.focus_set()
    return window, mpg_text, result_text, message_text


if __name__ == "__main__":
    app_window, mpg_text, result_text, message_text = build_window()
    app_window.mainloop()
