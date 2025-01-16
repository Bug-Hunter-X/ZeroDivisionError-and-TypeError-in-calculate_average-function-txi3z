def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [0,1,2,3]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with zero is: {average_zero}")

my_list_with_string = [1,2,"a",4]
average_string = calculate_average(my_list_with_string)
print(f"The average of a list with a string is: {average_string}")
