def display_square(side_length,symbol,filled):
    if filled:
        for i in range(side_length):
            print(symbol * side_length)
        else:
            print(symbol * side_length)
            for i in range(side_length -2):
                print(symbol + ''*(side_length-2)+symbol)
                print(symbol * side_length)

                display_square(5,'*',False)
                display_square(5,'*',True)
