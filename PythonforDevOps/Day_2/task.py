numbers = list(map(int, input("Enter a list of numbers:").split()))

if len(numbers) < 2:
    print("Please enter atleast two numbers.")
else:
    smallest = min(numbers)
    numbers.remove(smallest)
    second_smallest = min(numbers)

    print ("Smallest numbers: ", smallest)
    print ("Second Smallest numbers: ", second_smallest)
