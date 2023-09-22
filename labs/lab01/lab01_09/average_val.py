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


max_n = 900001
max_vector = [random.randint(1, 100) for _ in range(max_n)]

n_values = list(range(1, max_n, 900))
average_times = []

for n in n_values:
    print(n)
    ndigits = 6
    number_of_runs = 5


    @timing_decorator(ndigits, number_of_runs, f"vector = {max_vector[:n]}")
    def calculate_average(vector):
        return sum(vector) / len(vector)


    average_time = calculate_average(max_vector[:n])
    average_times.append(average_time)

plt.plot(n_values, average_times, linestyle='-', color='b')
plt.title('Зависимость среднего времени выполнения от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')

plt.savefig('average_value.png')
