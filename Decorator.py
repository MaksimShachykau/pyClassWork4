import time


# декоратор - это способ вызова функции внутри функции
def my_decorator(my_function):
    def wrapper(*args):
        start_working = time.time()
        my_function(*args)
        print("\nworking time = {}".format(str(-start_working+time.time())))
    return wrapper()


@my_decorator
def foo(a=10, b=100):
    item = 0
    for item in range(5000000):
        item += (item * a ** b)
    print(item)
