# Emmanuel Cruz 

# Nov 19, 2024

# Problem 1

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


L = [57, 83]

counter = 0

while counter <= 10:
 
    L.append  (counter)
    counter += 1
    
print("The list has," ,len(L), "elements")
print("The third element in the list is," ,L[0],)