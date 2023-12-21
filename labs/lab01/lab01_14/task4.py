from labs.lab01.lab01_14.main import get_usage_time,vec
import matplotlib.pyplot as plt


def task4(vec: list): # поиск максимума простым перебором
    max = vec[0]
    for item in vec[1:]:
        if item > max:
            max = item
    return max


N = 6
func_time = get_usage_time(ndigits=5,number=5)(task4)
items = [i for i in range(1, len(vec), 600)]
times = [func_time(vec[:i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Сумма элементов')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()