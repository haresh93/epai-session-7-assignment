# EPAI Session 7 Assignment

## Overview of the functions in session7.py

### docstring_check_wrapper

In this function we are keeping closure on docstring_length and hence the inner function can access the docstring_length variable.

This is the outer function which has the docstring_length variable with a value as 50.

This function returns a function which takes in another function as parameter and checks if the docstring length is greater than the 
docstring_length variable if it is greater then we are returning True and if it is less then we are returning False.

### fibonacci_wrapper

This is the outer function which contains a list f which stores the fibonacci numbers that have been generated till now.

This function returns another function which actually generates the fibonacci numbers and appends the numbers to the list f.

The inner function generates the next fibonacci number based on the list f from the outer function which the function can access based on closure. 

It checks if the list is empty, if it is empty appends 0 and if the length of the list is 1 then appends 1 and if it is greater than 1 then
appends the sum of the last 2 numbers in the list and then returns the last element in the list as that is the element wew have generated now.

### global_counter_wrapper

This function takes a function as an argument and returns another function which when called will call the function and returns the result of the function.
    
There is a variable cnt defined in the function which tracks the number of times the function is called and also sets the value in counters dictionary 
with function name as the key in module scope.

### counter_dict_wrapper

This function takes 2 parameters as arguments

fn: The function to track the number of times the function is called
counter_dict: The dict on which the count is stored with the key as the function name

This returns the function which should be called for tracking the count and which inturn executes the function

