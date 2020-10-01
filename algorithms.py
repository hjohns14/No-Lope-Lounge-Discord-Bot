import numpy as np
import matplotlib.pyplot as plt
from random import randrange


global t_0, t_1

t_0 = t_1 = 0

def h(x):
    global t_0, t_1
    return t_0 + (t_1 * x)



train_x = [x*10 for x in range(40)]
train_y = [y*randrange(3, 5)+randrange(-25, 25) for y in range(40)]

line = t_0 + t_1 * x

test_x =  test_y = []



def mse(h, alpha, x, y)


plt.plot(train_x, train_y)
plt.show()