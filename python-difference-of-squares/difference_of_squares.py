def difference(number):
    square = square_of_sum(number)
    sum = sum_of_squares(number)
    total = square - sum
    return total


def square_of_sum(number):
    total = 0
    for i in range(1, number+1):
        total += i
    return total**2


def sum_of_squares(number):
    total = 0
    for i in range(1, number+1):
        total += i**2
    return total



