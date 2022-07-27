
import time


def mesureTime(func):

    def calculator(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Tiempo de ejecución es: {}".format(time.time() - start))

        return result
    return calculator


@mesureTime
def divicion(a, b):
    time.sleep(1)
    return a/b

print(divicion(8,4))
print(divicion(83344,4443))
print(divicion(843342,435))
