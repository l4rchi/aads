from random import randint
from decorators import get_usage_time
import functools
import timeit
import typing
import matplotlib.pyplot as plt


def const_func(rand_vec):
    tries_ = 5
    sum_ = 0
    for i in rand_vec:
        sum_ += i
   # print(sum_/len(rand_vec))


def draw_graph(items, times):
    fig = plt.plot(items, times, 'bo-')
    plt.title('The execution time of the sorting algorithm')
    ax = plt.gca()
    ax.set_xlabel('Number of elements, $10^n$ pieces')
    ax.set_ylabel('Time, sec')
    plt.show()



