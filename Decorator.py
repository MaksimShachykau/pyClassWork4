

# декоратор - это способ вызова функции внутри функции
def my_decorator(my_function):
    def wrapper():
        print("Start decoration - start function")
        my_function()
        print("End decoration - end function")
    return wrapper()


@my_decorator
def bar():
    print("Hello world")
