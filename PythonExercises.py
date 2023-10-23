'''The exercises
Exercise 1: Calculate the Factorial of a Number
Hint: Use a loop to multiply numbers from 1 to the input number to calculate its factorial.

Exercise 2: Check if a Number is a Prime Number
Hint: Use a loop to check if the number is divisible by any number from 2 to its square root. If it's divisible, it's not a prime number.

Exercise 3: Fibonacci Sequence
Hint: Use a loop to generate the Fibonacci sequence up to a specified number of terms. Each term in the sequence is the sum of the two preceding ones.

Exercise 4: Reverse a String
Hint: Use string slicing to reverse the characters of a string. For example, if the string is "hello", the reversed string should be "olleh".

Exercise 5: Calculate the Sum of Digits in a Number
Hint: Use a loop to extract digits one by one from the number and add them to a sum variable.

Exercise 6: Find the Greatest Common Divisor (GCD) of Two Numbers
Hint: Use the Euclidean algorithm to find the GCD of two numbers. The algorithm states that the GCD of two numbers a and b is equal to the GCD of b and a % b (where % represents the modulo operation).

Exercise 7: Count the Number of Words in a Sentence
Hint: Use the split() method to split the sentence into words and then find the length of the resulting list.

Exercise 8: Palindrome Checker
Hint: Use string slicing to compare the input string with its reverse. If they are the same, it's a palindrome.

Exercise 9: Find the Factorial of a Number (Using Recursion)
Hint: Use a recursive function to calculate the factorial of a number. A recursive function is a function that calls itself.

Exercise 10: Convert Decimal to Binary
Hint: Use the division-remainder method to convert a decimal number to binary. Keep dividing the number by 2 and record the remainders until the quotient is 0. The remainders, read in reverse order, form the binary representation of the number.'''

#EX1 : Calculate the Factorial of a Number
n= int(input("Enter the number:\n")) #taking user input to calculate
factorial=1 #declaring the variable factorial as 1. This is because we will later use this variable to do the multiplications taht will reach the factorial.
for i in range (1, n+1): #here we are declaring the variable i inside the range 1 to (n+1). This is because the loop "for... in..." will run iterations a specified number of times. In this case, it will run from number 1 to n (because when we declare a range, the top number will not be counted. So, if we want it to happen 'n' times, we need to declare 'n+1', so n will be the last iteration
    factorial=factorial*i #what happens here: the factorial variable has its value changed for every iteration. ex: iteration 1, factorial is 1 (1(current factorial value)*1 (number of the iteration). In iteration 2, it will be 1*2=2. Iteration 3, it will be 2(current factorial from 2nd iteration)*3(number of the iteration) = 6. Iteration 4 will be 6(current value of factorial from iteration 3) * 4 (4th iteration) = 24 and so on. The result will always be the factorial of n
print (n,"! = ", factorial) #result

#EX2
n=int(input("Enter the number to be checked:\n")) #asking user input of the number to be checked
is_prime=True #is_prime is set to true initially so it will be easier to compare later
for i in range (2, int((n**0.5))+1): #for the considered interval (2 up to nSquareRoot +1), it will consider:
    if n%i==0: #IF there is remainder in the division is zero (which means the division is "perfect", integer numbers
        is_prime=False #IF there is no remainder for the division, is_prime is set to FALSE, which means the number is NOT prime
        break #stop any checking because we already have the answer
if is_prime and n>1: #IMPORTANT - in Python, if we want to check if a condition is TRUE, we do NOT NEED TO write "if xxx == true". Instead, we just write "if xx", it is already inferred true in the code. Only if we want to check for FALSE we would write it (like "if x==FALSE")
    print ("IS prime") #if both conditions are correct (the boolean is_prime is still true AND n is larger than one), it prints "IS prime"
else:
    print ("Is NOT prime")

#EX 3 Fibonacci Sequence
nterms = int(input("How many terms? ")) #asking for the user how many terms of the fibonacci they want
n1, n2 = 0, 1 # first two terms. It's because fibonacci always start with 0 and 1 (then 1,2,3,5,8 and so on), always summing up the last 2 numbers
count = 0 #selecting the count value as zero to store it (will be used in line 62)
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1: 
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms: #creates a loop. While count is smaller than the number of terms (user input), it will execute the following loop:
       print(n1) 
       nth = n1 + n2 #declaring variable nth, which is the sum of both n1 and n2
       n1 = n2 #These lines update the values of n1 and n2 to prepare for the next iteration of the loop. After this step, n1 becomes the old value of n2, and n2 becomes the newly calculated Fibonacci number (nth)
       n2 = nth
       count += 1 #this iteration sums 1 to the count, which will loop again and finish when the count is == the number of terms input


#EX4 - Reverse a string
b = input ("Select the text you want to be reversed:\n")
print(b[::-1]) #string slicing allows to extract portions of the string based on the position of the terms. It also makes possible to revert a string if you use it as 'Variable[::-1]'

#EX5 - Calculate the Sum of Digits in a Number
number = int(input("Enter a number: ")) # Get the number from the user
 
total_sum = 0 # Initialize variables

while number > 0:         # Extract digits and calculate the sum
    digit = number % 10   # Extract the last digit - How? dividing ANY number by 10, the remainder will ALWAYS be the last digit of the number (ex 123/10 is 12 with a remainder of 3, so if we use the operator %, it will give us the last digit always if we divide it by 10)
    total_sum += digit    # Add the digit to the total sum. This line accumulates the sum of all the digits extracted from the number.
    number //= 10         # Remove the last digit from the number. // is an operator that divides a number and doesnt consider values after the comma (so 123//10 is 12, discarding the remaining 3)

# Print the sum of digits
print("Sum of digits:", total_sum)

'''IMPORTANT ABOUT EXERCISE 5
    First Iteration:
        number % 10 gives 3 (the last digit of 123).
        total_sum is updated to 3.
        number //= 10 changes number to 12 (integer division by 10 removes the last digit).

    Second Iteration:
        number % 10 gives 2 (the last digit of 12 after the first iteration).
        total_sum is updated to 3 + 2 = 5.
        number //= 10 changes number to 1.

    Third Iteration:
        number % 10 gives 1 (the last digit of 1 after the first two iterations).
        total_sum is updated to 3 + 2 + 1 = 6.
        number //= 10 changes number to 0.

The reason number //= 10 is crucial is that it effectively moves to the next digit in the number. By performing integer division by 10, you are removing the last digit of the number, and the next iteration of the loop will extract the new last digit.

This process repeats until number becomes 0, effectively extracting and summing all the digits of the original number. The line number //= 10 ensures that the loop progresses through the digits of the number until there are no more digits left to process.'''

#EX 6 - Exercise 6: Find the Greatest Common Divisor (GCD) of Two Numbers
def gcd(a, b): # Function to find the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm
    while b != 0: # Iterate until the second number (b) becomes 0
        temp = b # Store the current value of b in a temporary variable
        b = a % b # Update b with the remainder of a divided by b
        a = temp # Assign the original value of b (stored in the temporary variable) to a
    return a     # When b becomes 0, a holds the GCD of the input numbers

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD using the gcd() function and output the result
result = gcd(num1, num2)
print("The Greatest Common Divisor (GCD) of", num1, "and", num2, "is", result)


#EX 7: Count the Number of Words in a Sentence
# Get a sentence input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words using the split() method
words = sentence.split()

# Initialize a variable to count the words
word_count = 0

# Iterate through the words and count them
for word in words:
    word_count += 1

# Print the number of words in the sentence
print("Number of words in the sentence:", word_count)

'''Explanation of the code:

    sentence.split(): This splits the input sentence into words. By default, split() uses spaces as separators, so it separates the sentence into a list of words.

    for word in words:: This loop iterates through each word in the list of words obtained from the sentence.

    word_count += 1: In each iteration of the loop, the word_count variable is incremented by 1, effectively counting each word.

    Finally, the program prints the number of words in the input sentence.

For example, if the user enters "Hello world, this is a test sentence," the program will output:

javascript

Number of words in the sentence: 7

This code counts the number of words in a sentence by splitting the sentence into words and counting the elements in the resulting list.'''


#EX 8: Palindrome Checker
a = input ("Select the text you want to check:\n") #asking for user input
b=(a[::-1]) #declaring variable b, which is the exact opposite of a (using the string inversion)
if b==a: #if b is the same as a, it means it is a palindrome
    print ("Text IS a palindrome")
else:
    print ("Text is NOT a palindrome")


#EX 9 : Find the Factorial of a Number (Using Recursion)
#In a recursive function, the function calls itself with a modified argument until it reaches a base case where the function returns a specific value. For finding the factorial of a number, the recursive definition is as follows:
# Recursive function to calculate factorial
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Get user input
num = int(input("Enter a number: "))

# Call the recursive function and print the result
print("Factorial using recursion:", factorial_recursive(num))

'''The user input is stored in the variable num. This variable is then passed as an argument to the factorial_recursive function when the function is called using factorial_recursive(num).

The function definition is def factorial_recursive(n):, which means the function expects an argument n when it is called. In this case, when you call factorial_recursive(num), the value of num (which was captured from user input) is passed as the argument n to the function.

Inside the function, the variable n (the function parameter) is used in the recursive calls and calculations. So, even though the function is defined with factorial_recursive(n), the n inside the function corresponds to the value passed when the function is called, in this case, num.

In summary, the variable num holds the user input, and this value is passed as the argument to the factorial_recursive function, where it is referred to as n within the function for calculations. The name n inside the function doesn't have to match the name of the variable used when calling the function. The connection is established through the function call (factorial_recursive(num)) where the value of num is passed as n.'''

#EX10 Convert Decimal to Binary

# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    binary_num = ""  # Initialize an empty string to store the binary representation
    
    # Continue the loop until the decimal number becomes 0
    while decimal_num > 0:
        remainder = decimal_num % 2  # Get the remainder of the division by 2
        binary_num = str(remainder) + binary_num  # Add the remainder to the beginning of the binary representation
        decimal_num //= 2  # Update the decimal number by integer division by 2
    
    # If the input decimal number was 0, the binary representation is also 0
    if binary_num == "":
        binary_num = "0"
    
    return binary_num

# Get user input for the decimal number
decimal_num = int(input("Enter a decimal number: "))

# Call the function and print the binary representation
print("Binary representation:", decimal_to_binary(decimal_num))

'''Explanation of the code:

    while decimal_num > 0:: This loop continues until the decimal number becomes 0.
    remainder = decimal_num % 2: This line calculates the remainder when the decimal number is divided by 2.
    binary_num = str(remainder) + binary_num: The remainder is added to the beginning of the binary_num string. This step records the remainders in reverse order.
    decimal_num //= 2: The decimal number is updated by integer division by 2, effectively moving to the next bit for the binary representation.
    If the input decimal number was 0, the binary representation is set to "0".

This code captures a decimal number from the user and converts it to binary using the division-remainder method. It then prints the binary representation of the input decimal number.

Binary numbers might seem unfamiliar at first, but they follow a strict logical pattern based on the powers of 2. Let's break it down:

Binary is a base-2 number system, meaning it only uses two digits: 0 and 1. Each digit in a binary number represents a power of 2. Starting from the rightmost digit (or the least significant bit), the first digit represents 2^0 (which is 1), the second digit represents 2^1 (which is 2), the third digit represents 2^2 (which is 4), and so on.

For example, the binary number 1011 can be calculated as follows:

    1 * 2^3 (the leftmost digit, which is 1, represents 2^3 = 8)
    0 * 2^2 (the second digit from the left is 0, so it doesn't contribute to the total)
    1 * 2^1 (the third digit from the left, which is 1, represents 2^1 = 2)
    1 * 2^0 (the rightmost digit, which is 1, represents 2^0 = 1)

Adding these together (8 + 0 + 2 + 1) gives us the decimal equivalent: 11.

In the context of the division-remainder method used in the Python code I provided earlier, we are essentially breaking down a decimal number into a sum of powers of 2, which results in its binary representation.

Understanding this logic helps when working with binary numbers, especially in computer science and digital electronics, where binary is commonly used to represent data and perform calculations inside computers.
'''

