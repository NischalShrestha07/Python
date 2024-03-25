# WAP for filter() to filter  only even numbers from a given list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers from the list:", even_numbers)
