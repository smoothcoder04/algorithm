def remove_even(list):
    return [num for num in list if num % 2 != 0]


result = remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"The list after removing even numbers are: {result}")
