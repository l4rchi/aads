import random
import typing
import timeit
import functools
import matplotlib.pyplot as plt


def timing_decorator(ndigits: int, number: int, setup: str) -> typing.Callable:
    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                setup=setup,
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator


max_n = 1100001
max_vector = [random.randint(1, 100) for _ in range(max_n)]

n_values = list(range(1, max_n, 1100))
constant_times = []

for n in n_values:
    print(n)
    ndigits = 6
    number_of_runs = 5


    @timing_decorator(ndigits, number_of_runs, f"vector = {max_vector[:n]}")
    def constant_function(vector):
        return 9


    constant_time = constant_function(max_vector[:n])
    constant_times.append(constant_time)

plt.plot(n_values, constant_times, linestyle='-', color='r')
plt.title('Зависимость времени выполнения постоянной функции от n')
plt.xlabel('n')
plt.ylabel('Время выполнения (секунды)')
plt.savefig('constant_time.png')
plt.close()
