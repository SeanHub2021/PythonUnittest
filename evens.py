def even_number_of_evens(numbers):
#     Suggested tests;
# 1. Should raise a TypeError if a list is not passed into the function
# 2. If numbers is empty, return False
# 3. If the number of even numbers is odd, return False
# 4. If the number of even numbers is 0, return False
# 5. If the number of even numbers is even, return True

    if isinstance(numbers, list):
            if numbers == []:
                return False
            else:
                evens = 0
                
            for n in numbers:
                if n % 2 == 0:
                    evens += 1
            if evens:
                return evens % 2 == 0
            else:
                return False
    else:
        raise TypeError("A list was not passed into the function")
    return None


if __name__ == '__main__':
    print(even_number_of_evens(5))