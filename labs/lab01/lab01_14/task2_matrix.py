import numpy as np
import random
from labs.lab01.lab01_14.main import get_usage_time
import matplotlib.pyplot as plt


def create(n: int) -> np.array:
    result = np.array([[random.randint(0, 1000) for j in range(n)] for i in range(n)])
    return result


def matrix_multi(A, B):
    return np.dot(A, B)


N = 6
count = range(1, 250 * N, 10 * N)
matrix_A = create(250*N)
matrix_B = create(250*N)
func = get_usage_time(ndigits=5)(matrix_multi)
items = [i for i in count]
times = [func(matrix_A[:i, :i], matrix_B[:i, :i]) for i in items]

fig = plt.plot(items, times, 'bo-')
plt.title('Сумма элементов')
ax = plt.gca()
ax.set_xlabel('Число элементов')
ax.set_ylabel('Время, сек')
plt.show()