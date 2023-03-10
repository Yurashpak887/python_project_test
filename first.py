import time

import math as m
def base_decorator(number):
    def iteration(func):
        def wrapper(x,y,z):
            print(number)
            start = time.time()
            print("----------")
            func(x,y,z)
            print("Chas", time.time() - start)
        return wrapper
    return iteration


@base_decorator(2)
def suma(x,y,z):
    print(m.sqrt(x+y+z/y**2))

suma(4,5,5)


@base_decorator(5)
def minus(x,y,z):
    print(print(m.sqrt(x-y-z/y**2)))
minus(6,1,3)


class A:
    @staticmethod
    def hello():
        print("Hello")

