def calculate_product(start,end):
    if start>end:
        start,end = end,start

        product = 1
        for num in range(start,end+1):
            product *= num
            return product
        result = calculate_product(5,25)
        print(result)