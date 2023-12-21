import numpy as np
import matplotlib.pyplot as plt
from labs.lab01.lab01_14.main import get_usage_time,vec


def task2(vec: list):  #Произведение элементов
    return np.prod(vec)


N = 6
func_time = get_usage_time(ndigits=5,number=5)(task2)
items = [i for i in range(1, len(vec), 600)]
times = [func_time(vec[:i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Сумма элементов')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()