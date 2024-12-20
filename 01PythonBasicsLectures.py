# Lecture 01: Introduction to Python and Variables

# Print a welcome message
print("Bismillah")

# Initialize variables with different data types
a = 10  # Integer
b = 10.4  # Float
c = "Smas"  # String
d = True  # Boolean

# Check the type of variable 'b' and print it
bKiType = type(b)
print(bKiType)

# Convert the float 'b' to an integer and print its type and value
e = int(b)
print(type(e), e)

# Lecture 02: Multiline Strings and Arithmetic Operations

# Define a multiline string using triple quotes
myrules = '''
snbbndndsndddndbfjbf
fsdjfjd
asdhd
snbbndndsndddndbfjbf
fsdjfjd
asdhd
'''

# Print the multiline string
print(myrules)

# Demonstrate basic arithmetic operations
i = 1  # Initialize variable 'i'
i += 10  # Increment 'i' by 10
i = i + 1  # Further increment 'i' by 1
print(i)  # Print the final value of 'i'

# Lecture 03: Input and Basic Output

# Prompt user to enter their name and age
print("Enter Your Name ")
name = input()  # Get user input for name

print("Enter Your Age ")
age = int(input())  # Get user input for age and convert to integer

# Print the entered name and age
print("Student Name ", name)
print("Student Age ", age)

# Lecture 04: Conditional Statements (if, else, elif)

# Example of multiple if conditions
a = 1
if a == 1:
    print("true value")  # Executes if 'a' equals 1
if a >= 0:
    print("positive")  # Executes if 'a' is non-negative

# Example of if-else condition
if a < 0:
    print("Negative")  # Executes if 'a' is negative
else:
    print("Positive")  # Executes if 'a' is non-negative

# Lecture 05: User Registration and Login System

# Print welcome message and registration prompt
print("Welcome to Aptech Gulshan II")
print("Registration")

# Get user registration details
name = input("Enter your Name: ")
email = input("Enter Your Email: ")
password = input("Enter Your Pass: ")
print("Account Successfully Created")

# Prompt user for login credentials
print("Now You Can Login With Your Credentials")
emailLogin = input("Enter Your Email: ")
passwordLogin = input("Enter Your Pass: ")

# Check if login credentials match the registered details
if (email == emailLogin) and (password == passwordLogin):
    print("Welcome .......")
    
    # Prompt user to enter marks for three subjects
    eng = float(input("Enter Your English Marks: "))
    math = float(input("Enter Your Math Marks: "))
    urdu = float(input("Enter Your Urdu Marks: "))

    # Calculate total marks and percentage
    total = eng + math + urdu
    percentage = (total / 300) * 100

    # Determine the grade based on percentage
    if 80 <= percentage <= 100:
        print("Grade A1")
    elif 70 <= percentage < 80:
        print("Grade A")
    elif 60 <= percentage < 70:
        print("Grade B")
    elif 50 <= percentage < 60:
        print("Grade C")
    elif 40 <= percentage < 50:
        print("Grade D")
    else:
        print("Fail")
else:
    print("Incorrect Email And Password")

# Lecture 06: Odd, Even, and Leap Year Checker

# Define a number and check if it is even or odd
meranum = 2025
if meranum % 2 == 0:
    print("even")  # Executes if 'meranum' is divisible by 2
else:
    print("odd")  # Executes if 'meranum' is not divisible by 2

# Check if the year is a leap year
print("Leap Year") if meranum % 4 == 0 else print("Is not a Leap Year")
