# Legacy code to refactor


def calc(left: float, right: float, operator: str) -> float:
    """
    Perform a binary arithmetic operation on two numbers.

    Args:
        left: The first operand.
        right: The second operand.
        operator: One of "+", "-", "*", or "/".

    Returns:
        The result of the operation.

    Raises:
        ValueError: If operator is not one of "+", "-", "*", "/",
            or if operator is "/" and right is zero.
    """
    match operator:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
        case "/":
            if right == 0:
                raise ValueError("Division by zero is not allowed")
            return left / right
        case _:
            raise ValueError(
                f"Invalid operator '{operator}'. "
                "Use one of: '+', '-', '*', '/'"
            )
