

def docstring_check_wrapper():
    """
    This is the outer function which has the docstring_length variable with a value as 50.
    This function returns a function which takes in another function as parameter and checks if the docstring length is greater than the 
    docstring_length variable
    """
    docstring_length = 50
    def inner(fn: "The Function for which we need to check the length of the docstring"):
        """
        This function takes a function as a parameter and uses docstring_length variable from the outer function by closure and 
        compares the length of the docstring of the function with the docstring_length variable and returns true if it is more than in else return False. 
        """
        nonlocal docstring_length
        if fn.__doc__ and len(fn.__doc__) > docstring_length:
            return True
        else:
            return False
    
    return inner


def fibonacci_wrapper():
    """
    This is the outer function which contains a list f which stores the fibonacci numbers that have been generated till now.

    This function returns another function which actually generates the fibonacci numbers and appends the numbers to the list f.
    """
    f = []
    def fibonacci():
        """
        This function generates the next fibonacci number based on the list f from the outer function which the function can access based on closure. 

        It checks if the list is empty, if it is empty appends 0 and if the length of the list is 1 then appends 1 and if it is greater than 1 then
        appends the sum of the last 2 numbers in the list and then returns the last element in the list as that is the element wew have generated now.
        """
        nonlocal f
        if not len(f):
            f.append(0)
        elif len(f) == 1:
            f.append(1)
        else:
            f.append(f[-1] + f[-2])

        return f[-1]
    
    return fibonacci


counters = dict()

def global_counter_wrapper(fn = lambda *args, **kwargs: print("Dummy")):
    """
    This function takes a function as an argument and returns another function which when called will call the function and returns the result of the function.
    
    There is a variable cnt defined in the function which tracks the number of times the function is called and also sets the value in counters dictionary 
    with function name as the key in module scope.
    """
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    
    return inner


def counter_dict_wrapper(fn = lambda *args, **kwargs: print("Dummy"), counter_dict = dict()):
    """
    This function takes 2 parameters as arguments

    fn: The function to track the number of times the function is called
    counter_dict: The dict on which the count is stored with the key as the function name

    This returns the function which should be called for tracking the count and which inturn executes the function
    """
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        nonlocal counter_dict
        cnt += 1
        counter_dict[fn.__name__] = cnt
        return fn(*args, **kwargs)
    
    return inner
