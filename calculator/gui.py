"""Graphical interface for the calculator, built with tkinter."""

import tkinter as tk

from calculator.engine import CalculatorError, evaluate

WINDOW_TITLE = "Scientific Calculator"
DISPLAY_FONT = ("Consolas", 22)
BUTTON_FONT = ("Segoe UI", 12)
COLUMNS = 5

BUTTON_ROWS = [
    ["sin(", "cos(", "tan(", "sqrt(", "C"],
    ["ln(", "log(", "exp(", "factorial(", "⌫"],
    ["pi", "e", "(", ")", "^"],
    ["7", "8", "9", "/", "%"],
    ["4", "5", "6", "*", "-"],
    ["1", "2", "3", "+", "//"],
    ["0", ".", "="],
]


def format_result(value):
    """Show integers as-is and floats without trailing noise."""
    return str(value) if isinstance(value, int) else f"{value:.12g}"


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.resizable(False, False)

        self.display = tk.Entry(self, font=DISPLAY_FONT, justify="right", bd=8)
        self.display.grid(row=0, column=0, columnspan=COLUMNS, sticky="nsew")
        self.display.bind("<Return>", lambda _event: self.calculate())
        self.display.focus()

        self.status = tk.Label(self, fg="red", anchor="e")
        self.status.grid(row=1, column=0, columnspan=COLUMNS, sticky="nsew")

        self._create_buttons()

    def _create_buttons(self):
        for row_index, labels in enumerate(BUTTON_ROWS, start=2):
            for column, label in enumerate(labels):
                span = COLUMNS - column if label == "=" else 1
                tk.Button(
                    self,
                    text=label,
                    font=BUTTON_FONT,
                    width=6,
                    height=2,
                    command=lambda text=label: self.press(text),
                ).grid(row=row_index, column=column, columnspan=span, sticky="nsew")

    def press(self, label):
        self.status.config(text="")
        if label == "C":
            self.display.delete(0, tk.END)
        elif label == "⌫":
            self.display.delete(len(self.display.get()) - 1, tk.END)
        elif label == "=":
            self.calculate()
        else:
            self.display.insert(tk.END, label)

    def calculate(self):
        expression = self.display.get().strip()
        if not expression:
            return
        try:
            result = format_result(evaluate(expression))
        except CalculatorError as error:
            self.status.config(text=str(error))
            return
        self.status.config(text="")
        self.display.delete(0, tk.END)
        self.display.insert(0, result)


def main():
    CalculatorApp().mainloop()


if __name__ == "__main__":
    main()