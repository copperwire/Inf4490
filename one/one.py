import numpy as np 
import seaborn

import io
import matplotlib.pyplot as plt

N = 1e4

func = lambda x: - x **4  + 2*x**3 + 2*x**2 -x

d_func = lambda x: - 4*x**3 + 6*x**2 + 4 * x - 1

x = np.linspace(-2, 3, N)
gamma = x[1] - x[2]

a = np.zeros(N)
a[0] = x[0]
endp = 0
eps = 1e-4

if len(a) == len(x): 


	for i in range(int(N-1)):
		if abs(d_func(a[i])) ** 2 > eps:
			a[i+1] = a[i] - gamma*d_func(a[i])
		else:
			endp = i
			break

	plt.plot(x, func(x))
	plt.plot(a[:endp], func(a[:endp]))
	plt.title(r"N = {}, $\gamma = $ {}".format(N, np.round(gamma, 2))) 
	plt.show()

else:
	print(len(g_asc), len(x))