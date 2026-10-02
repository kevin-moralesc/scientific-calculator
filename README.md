# Scientific Calculator

A simple scientific calculator with a graphical interface, written in Python.
It uses the `ast` module to parse expressions instead of `eval()`, so arbitrary code can never be executed.

## Features

- Graphical interface built with tkinter (no extra installs needed)
- Operators: `+ - * / // % ^` and parentheses
- Functions: `sin cos tan asin acos atan sqrt ln log exp abs factorial`
- Constants: `pi` and `e`
- Clear error messages (division by zero, invalid input, etc.)
- Use the buttons or type with your keyboard and press Enter

## Requirements

- Python 3.8 or newer (tkinter is included with the Windows installer)

## Usage

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/scientific-calculator.git
cd scientific-calculator
```

Then either double-click `run.pyw`, or run:

```bash
python -m calculator
```

## Examples

| Expression      | Result |
|-----------------|--------|
| `2 + 3 * 4`     | 14     |
| `2 ^ 10`        | 1024   |
| `sqrt(16)`      | 4      |
| `sin(pi / 2)`   | 1      |
| `factorial(5)`  | 120    |

Trigonometric functions use radians.

## Project structure

```
scientific-calculator/
├── calculator/
│   ├── engine.py    # safe expression evaluator
│   ├── gui.py       # tkinter interface
│   └── __main__.py  # entry point for python -m calculator
├── run.pyw          # double-click launcher
├── LICENSE
└── README.md
```

## License

MIT
