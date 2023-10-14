def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]
result1 = is_palindrome(123321)
result2 = is_palindrome(546645)
result3 = is_palindrome(421987)

print(result1) #True
print(result2) #True
print(result3) #False