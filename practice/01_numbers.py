# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
a = input("pick a number, 1 or 2: ")
def is_even(a):
    test = int(a)%2
    if test == 1:
        print("odd")
    else:
        print("even")
#call the function to test it
is_even(a)

def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True

# Ones Digit
# Write a function that returns the ones digit of a number

def ones_digit(num):
    digit_list = list(str(num))
    digit = digit_list.pop(-1)
    print(f'The ones place digit is {digit}.')
#call the function to test it
ones_digit(1352)

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2
#call the boolean test function
test_ones_digit()

# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):
    percentage = (v/max) * 100
    print(f"The percentage is {percentage}%")

#call function to test it
percentage(10, 20)
#use booleans to test known values
def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'
