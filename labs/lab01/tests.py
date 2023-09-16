from functions import const_func, draw_graph
from random import random, randint
from decorators import get_usage_time
import timeit
N_ = 20 - 4
step_n = N_ * 10**2
end_n = 10**4 * N_
start_n = 1
x_vec = []
y_vec = []
rand_vec = [randint(1, 100) for _ in range(1, end_n)] # создаем вектор длинной 1:end_n
for step in range(1, end_n,step_n):
    tmp_vec = rand_vec[1:step]
    func = get_usage_time(number=5,ndigits=5)(const_func) # дл каждого вектора 5 раз const_func
    print(tmp_vec)
    x_vec.append(len(tmp_vec))
    y_vec.append(func(tmp_vec))
draw_graph(x_vec,y_vec)
