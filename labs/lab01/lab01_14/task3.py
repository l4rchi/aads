from labs.lab01.lab01_14.main import get_usage_time,vec
import matplotlib.pyplot as plt


def task3(vec: list,x:float = 6 * 1.5):
    result = 0
    for i in range(len(vec), 0, -1):
        result = result * x + vec[i - 1]
    return result

N = 6
func_time = get_usage_time(ndigits=5,number=5)(task3)
items = [i for i in range(1, len(vec), 600)]
times = [func_time(vec[:i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Сумма элементов')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()