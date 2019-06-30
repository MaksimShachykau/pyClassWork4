import time


# декоратор - это способ вызова функции внутри функции
def my_decorator(my_function):
    def wrapper(*args):
        start_working = time.time()
        my_function(*args)
        print("\nworking time = {}".format(str(-start_working+time.time())))
    return wrapper()


@my_decorator
def foo(a=100):
    for filename in range(a):
        with open(str('file'+ str(filename)), mode='a') as file:
            file.write("String number {}".format(str(filename)))
