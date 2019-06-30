# decorator
def my_decorator(my_function):
    def wrapper():
        print("Start decoration")
        my_function()
        print("End decoration")
    return wrapper()


@my_decorator
def bar():
    print("Hello world")
