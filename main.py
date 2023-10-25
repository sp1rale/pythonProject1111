def is_lucky_number(number):
    if len(str(number)) != 6:
        return False

    first_half = number // 1000
    second_half = number % 1000

    sum_first_half = sum(map(int, str(first_half)))
    sum_second_half = sum(map(int, str(second_half)))

    return sum_first_half == sum_second_half

num = 123420
if is_lucky_number(num):
    print(f"{num} є щасливим числом.")
else:
    print(f"{num} не є щасливим числом.")
