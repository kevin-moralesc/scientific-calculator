"""Safe math expression evaluator built on Python's ast module."""

import ast
import math
import operator

BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "ln": math.log,
    "log": math.log10,
    "exp": math.exp,
    "abs": abs,
    "factorial": math.factorial,
}

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}

MAX_EXPONENT = 1000


class CalculatorError(Exception):
    """Raised when an expression is invalid or cannot be computed."""


def evaluate(expression):
    """Evaluate a math expression and return the result."""
    try:
        tree = ast.parse(expression.replace("^", "**"), mode="eval")
        return _evaluate_node(tree.body)
    except SyntaxError as error:
        raise CalculatorError("Invalid expression") from error
    except ZeroDivisionError as error:
        raise CalculatorError("Division by zero") from error
    except (ValueError, TypeError, OverflowError) as error:
        raise CalculatorError(f"Math error: {error}") from error


def _evaluate_node(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return node.value

    elif isinstance(node, ast.Name) and node.id in CONSTANTS:
        return CONSTANTS[node.id]

    elif isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPERATORS:
        return UNARY_OPERATORS[type(node.op)](_evaluate_node(node.operand))

    elif isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPERATORS:
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > MAX_EXPONENT:
            raise CalculatorError("Exponent too large")
        return BINARY_OPERATORS[type(node.op)](left, right)

    elif (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in FUNCTIONS
        and not node.keywords
    ):
        arguments = [_evaluate_node(arg) for arg in node.args]
        return FUNCTIONS[node.func.id](*arguments)

    raise CalculatorError("Unsupported expression")