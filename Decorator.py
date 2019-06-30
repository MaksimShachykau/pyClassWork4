import time


# декоратор - это способ вызова функции внутри функции
def my_decorator(my_function):
    def wrapper():
        start_working = time.time()
        my_function()
        print("\nworking time = {}".format(str(start_working-time.time())))
    return wrapper()

