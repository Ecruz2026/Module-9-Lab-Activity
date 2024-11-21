# Emmanuel Cruz 

# Nov 19, 2024


# Write an infinite loop that prints “Infinite”. An infinite loop never ends. The
# condition is always true. After you prove to yourself that this works, comment out the code that
# produces the infinite loop. To break a loop in progress you should be able to do ctrl-C or
# command-C (depending on your platform).



# i = 1
# while True:
# print("Infinite")

# This will print out Infinite until I do ctrl-C and break the loop.



# Create a list called L that starts with the numbers 57 and 83 in it. Then build a while
# loop, starting with a counter assigned to the value 0. On each iteration, the loop should append
# the current value of a counter variable to the list and then increase the counter by 1. The while
# loop should stop once the counter variable is greater than 10. Finish by printing a statement
# that tells us a) how many elements are in the list, and b) what the third element in the list is.


# L = [57, 83]

# counter = 0

# while counter <= 10:
 
    # L.append  (counter)
    # counter += 1
    
# print("The list has," ,len(L), "elements")
# print("The third element in the list is," ,L[0],)

# After the loop, L will contain [57, 83, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], giving it a total of 13 elements (2 starting values plus 11 from the loop).



# Using a while loop, ask the user to enter a number. Append each entered number
# to a list and add them together. Continue asking for a number until the sum of the list of
# numbers is greater than 100.


#numbers = []

#total_sum = 0

#while total_sum <= 100:

    #user_input = input("Please enter a number: ")

    #number = float(user_input)

    #numbers.append(number)

    #total_sum += number

#print("The total sum of the numbers is:", total_sum)
#print("The numbers entered were:", numbers)

# Once the total sum exceeds 100, the loop exits, and the program prints the total sum of all the numbers that have been entered, as well as the list of those individual numbers.
