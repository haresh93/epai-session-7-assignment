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

    session7.docstring_length = 5

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

    fibonacci_nos = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
    next_fibonacci = session7.fibonacci_wrapper()

    for i in range(10):
        session7.f = fibonacci_nos
        fib_no = next_fibonacci()

        assert fib_no == fibonacci_nos[i], "The Generated Fibonacci num is not a valid fibonacci num"

########## Test cases for the global_counter_wrapper ##########


def mul(a, b):
    return a * b


def add(a, b):
    return a + b

def div(a, b):
    return a / b


def test_global_counter_wrapper_returned_func_same_as_passed():

    wrapped_add = session7.global_counter_wrapper(add)
    wrapped_mul = session7.global_counter_wrapper(mul)
    wrapped_div = session7.global_counter_wrapper(div)
    assert add(10, 20) == wrapped_add(10, 20), "The wrapped function which is returned is not behaving same as the one passed to global_counter_wrapper "
    assert mul(10, 20) == wrapped_mul(10, 20), "The wrapped function which is returned is not behaving same as the one passed to global_counter_wrapper "
    assert div(10, 20) == wrapped_div(10, 20), "The wrapped function which is returned is not behaving same as the one passed to global_counter_wrapper "

def test_global_counter_wrapper_verifying_counter():
    counters = session7.counters

    wrapped_add = session7.global_counter_wrapper(add)
    wrapped_mul = session7.global_counter_wrapper(mul)
    wrapped_div = session7.global_counter_wrapper(div)

    for i in range(10):
        wrapped_add(i * 4, i * 5)
    
    for i in range(20):
        wrapped_mul(i * 10, i * 20)
    
    for i in range(30):
        wrapped_div(i + 10, i + 30)
    
    assert counters["add"] == 10, "The counter is not right for the add function"
    assert counters["mul"] == 20, "The counter is not right for the mul function"
    assert counters["div"] == 30, "The counter is not right for the div function"

def test_global_counter_wrapper_manipulating_the_global_counters():
    counters = session7.counters

    wrapped_add = session7.global_counter_wrapper(add)
    wrapped_mul = session7.global_counter_wrapper(mul)
    wrapped_div = session7.global_counter_wrapper(div)

    for i in range(10):
        counters["add"] = 0
        wrapped_add(i * 4, i * 5)
    
    for i in range(20):
        counters["mul"] = 0
        wrapped_mul(i * 10, i * 20)
    
    for i in range(30):
        counters["div"] = 0
        wrapped_div(i + 10, i + 30)
    
    assert counters["add"] == 10, "The counter is not right for the add function"
    assert counters["mul"] == 20, "The counter is not right for the mul function"
    assert counters["div"] == 30, "The counter is not right for the div function"

def test_global_counter_wrapper_changing_reference_of_the_global_counters():
    wrapped_add = session7.global_counter_wrapper(add)
    wrapped_mul = session7.global_counter_wrapper(mul)
    wrapped_div = session7.global_counter_wrapper(div)

    session7.counters = {
        "add": 0,
        "mul": 0,
        "div": 0
    }
    
    counters = session7.counters

    for i in range(10):
        wrapped_add(i * 4, i * 5)
    
    for i in range(20):
        wrapped_mul(i * 10, i * 20)
    
    for i in range(30):
        wrapped_div(i + 10, i + 30)
    
    assert counters["add"] == 10, "The counter is not right for the add function"
    assert counters["mul"] == 20, "The counter is not right for the mul function"
    assert counters["div"] == 30, "The counter is not right for the div function"

####### Test cases for the counter_dict_wrapper #######

def test_counter_dict_wrapper_returned_func_same_as_passed():
    counters = {}
    wrapped_add = session7.counter_dict_wrapper(add, counters)
    wrapped_mul = session7.counter_dict_wrapper(mul, counters)
    wrapped_div = session7.counter_dict_wrapper(div, counters)
    assert add(10, 20) == wrapped_add(10, 20), "The wrapped function which is returned is not behaving same as the one passed to counter_dict_wrapper "
    assert mul(10, 20) == wrapped_mul(10, 20), "The wrapped function which is returned is not behaving same as the one passed to counter_dict_wrapper "
    assert div(10, 20) == wrapped_div(10, 20), "The wrapped function which is returned is not behaving same as the one passed to counter_dict_wrapper "

def test_counter_dict_wrapper_verifying_counter():
    counters = {}

    wrapped_add = session7.counter_dict_wrapper(add, counters)
    wrapped_mul = session7.counter_dict_wrapper(mul, counters)
    wrapped_div = session7.counter_dict_wrapper(div, counters)

    for i in range(10):
        wrapped_add(i * 4, i * 5)
    
    for i in range(20):
        wrapped_mul(i * 10, i * 20)
    
    for i in range(30):
        wrapped_div(i + 10, i + 30)
    
    assert counters["add"] == 10, "The counter is not right for the add function"
    assert counters["mul"] == 20, "The counter is not right for the mul function"
    assert counters["div"] == 30, "The counter is not right for the div function"

def test_counter_dict_wrapper_manipulating_counters_object():
    counters = {}

    wrapped_add = session7.counter_dict_wrapper(add, counters)
    wrapped_mul = session7.counter_dict_wrapper(mul, counters)
    wrapped_div = session7.counter_dict_wrapper(div, counters)

    for i in range(10):
        counters["add"] = 0
        wrapped_add(i * 4, i * 5)
    
    for i in range(20):
        counters["mul"] = 0
        wrapped_mul(i * 10, i * 20)
    
    for i in range(30):
        counters["div"] = 0
        wrapped_div(i + 10, i + 30)
    
    assert counters["add"] == 10, "The counter is not right for the add function"
    assert counters["mul"] == 20, "The counter is not right for the mul function"
    assert counters["div"] == 30, "The counter is not right for the div function"

def test_global_counter_wrapper_changing_reference_of_the_counters_dict():
    counters = {}

    wrapped_add = session7.counter_dict_wrapper(add, counters)
    wrapped_mul = session7.counter_dict_wrapper(mul, counters)
    wrapped_div = session7.counter_dict_wrapper(div, counters)

    counters = {
        "add": 0,
        "mul": 0,
        "div": 0
    }

    for i in range(10):
        wrapped_add(i * 4, i * 5)
    
    for i in range(20):
        wrapped_mul(i * 10, i * 20)
    
    for i in range(30):
        wrapped_div(i + 10, i + 30)
    
    assert counters["add"] == 0, "The counter is not right for the add function"
    assert counters["mul"] == 0, "The counter is not right for the mul function"
    assert counters["div"] == 0, "The counter is not right for the div function"