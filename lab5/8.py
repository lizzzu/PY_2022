# a
def print_arguments(function):
    def fun(*args, **keywords):
        print(f'Arguments are {args}, {keywords}')
        return function(*args, **keywords)
    return fun

def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

augmented_multiply_by_two = print_arguments(multiply_by_two)
print(augmented_multiply_by_two(10))

augmented_add_numbers = print_arguments(add_numbers)
print(augmented_add_numbers(3, 4))

# b
def multiply_output(function):
    def fun(*args, **keywords):
        return function(*args, **keywords) * 2
    return fun

def multiply_by_three(x):
    return x * 3

augmented_multiply_by_three = multiply_output(multiply_by_three)
print(augmented_multiply_by_three(10))

# c
def augment_function(function, decorators):
    for decorator in decorators:
        function = decorator(function)
    return function

decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
print(decorated_function(3, 4))
