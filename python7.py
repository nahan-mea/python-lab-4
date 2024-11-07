start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

numbers = list(range(start, end + 1))
powers_of_2 = list(map(lambda x: 2 ** x, numbers))

print(powers_of_2)
