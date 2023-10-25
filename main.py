def display_odd_numbers_between(start, end):
    for number in range(start + 1, end):
        if number % 2 != 0:
            print(number)

display_odd_numbers_between(1, 10)
