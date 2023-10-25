def calculate_sum_in_range(start, end):
    total_sum = 0
    for number in range(start, end + 1):
        total_sum += number
    return total_sum

start = 1
end = 10
result = calculate_sum_in_range(start, end)
print(f"Сума чисел в діапазоні від {start} до {end} дорівнює {result}")
