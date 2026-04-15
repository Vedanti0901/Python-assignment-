try:
    #Code that might raise an exception
    numerator = 10
    denominator = int(input("Enter a number: "))
    result = numerator/denominator
except ZeroDivisionError:
    # Handle the specific ZeroDivisionError
    print("Error: Denominator cannot be 0")
except ValueError:
    # Handle the specific ValueError 
    print(" Error: Invalid input. Please enter a valid number.")
else:
    #Code to run if no exception occured
    print(f"The result is {result}")
finally:
    #Code that always rups
    print("Execution finished")