def apply_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def my_function():
    print("Original Function Called")

my_function = apply_decorator(my_function)
my_function()
