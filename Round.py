def divide_or_square(number):
    if number % 5 == 0:
        return round(number ** 0.5, 2)
    return number % 5