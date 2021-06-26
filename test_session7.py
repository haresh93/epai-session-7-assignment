import session7


############ Test cases for the docstring_check_wrapper function ##############

def test_docstring_check_wrapper_with_no_docstring():

    def foo_bar():
        pass

    docstring_checker = session7.docstring_check_wrapper()

    assert docstring_checker(foo_bar) == False, "For the function without any docstring the docstring_checker is not returning an expected response"

def test_docstring_check_wrapper_with_global_docstring_length():

    def foo_bar():
        """
        This is the docstring
        """
        pass

    global docstring_length
    docstring_length = 5

    docstring_checker = session7.docstring_check_wrapper()

    assert docstring_checker(foo_bar) == False, "When a global docstring_length variable is set to a value 5 docstring_checker is not returning an expected response"

def test_docstring_check_wrapper_with_length_less_than_50():
    
    def foo_bar():
        """
        This is the docstring
        """
        pass

    docstring_checker = session7.docstring_check_wrapper()

    assert docstring_checker(foo_bar) == False, "For the function with a docstring length less than 50 the docstring_checker is not returning an expected response"

def test_docstring_check_wrapper_with_length_more_than_50():

    def foo_bar():
        """
        This is the docstring for the foo_bar function with length greater than 50 to test the docstring_checker if it returns True
        """
        pass

    docstring_checker = session7.docstring_check_wrapper()

    assert docstring_checker(foo_bar) == True, "For the function with a docstring length less than 50 the docstring_checker is not returning an expected response"


########## Test cases for the Fibonacci Wrapper ##############

def test_fibonacci_wrapper():

    fibonacci_nos = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
    next_fibonacci = session7.fibonacci_wrapper()

    for i in range(10):
        fib_no = next_fibonacci()

        assert fib_no == fibonacci_nos[i], "The Generated Fibonacci num is not a valid fibonacci num"

def test_fibonacci_wrapper_manipulating_the_closure_list():

    global f
    fibonacci_nos = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
    next_fibonacci = session7.fibonacci_wrapper()

    for i in range(10):
        f = fibonacci_nos
        fib_no = next_fibonacci()

        assert fib_no == fibonacci_nos[i], "The Generated Fibonacci num is not a valid fibonacci num"

########## Test cases for the global_counter_wrapper ##########


def mul(a, b, c):
    return a * b * c


def add(a, b):
    return a + b

def div(a, b):
    return a / b


def test_global_counter_wrapper():
    pass