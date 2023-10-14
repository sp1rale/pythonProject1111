def display_even_numbers(start,end):
    for num in range (start,end+1):
        if num % 2 == 0:
            print(num)
            display_even_numbers(5, 15)
