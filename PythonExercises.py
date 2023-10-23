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

#EX1


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
