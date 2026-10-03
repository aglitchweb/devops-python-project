def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Нельзя делить на ноль")
    return a / b


if __name__ == "__main__":
    print("Простой калькулятор")
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("5 * 6 =", multiply(5, 6))
    print("10 / 2 =", divide(10, 2))