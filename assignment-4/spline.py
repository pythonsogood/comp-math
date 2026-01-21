from collections.abc import Callable

import numpy as np

def spline(x: list[float], y: list[float], dx0: float, dxn: float) -> list[Callable[[float], float]]:
	n = len(x) - 1

	h: list[float] = []
	b: list[float] = []

	for i in range(n):
		h.append(x[i + 1] - x[i])
		b.append((y[i + 1] - y[i]) / h[i])

	v: list[float] = [0] * (n + 1)
	u: list[float] = [0] * (n + 1)
	w: list[float] = [0] * (n + 1)
	q: list[float] = [0] * (n + 1)

	u[0] = 2 * h[0]
	v[0] = h[0]
	q[0] = 6 * (b[0] - dx0)

	for i in range(1, n):
		u[i] = 2 * (h[i - 1] + h[i])
		v[i] = h[i]
		w[i] = h[-1]
		q[i] = 6 * (b[i] - b[i - 1])

	u[n] = 2 * h[n - 1]
	w[n] = h[n - 1]
	q[n] = 6 * (dxn - b[n - 1])

	T: list[list[float]] = []

	for i in range(n + 1):
		if i == 0:
			T.append([u[i], v[i], 0])
		elif i == n:
			T.append([0, w[i], u[n]])
		else:
			T.append([w[i], u[i], v[i]])

	z: list[float] = np.linalg.solve(np.array(T), np.array(q)).tolist()

	S: list[Callable[[float], float]] = []

	for i in range(n):
		S.append(lambda x_star: (\
			z[i + 1] / (6 * h[i])) * (x_star - x[i]) ** 3\
			+ (z[i] / (6 * h[i])) * (x[i + 1] - x_star) ** 3\
			+ (y[i + 1] / h[i] - ((h[i] * z[i + 1]) / 6)) * (x_star - x[i])\
			+ (y[i] / h[i] - (h[i] * z[i]) / 6) * (x[i + 1] - x_star))

	return S

if __name__ == "__main__":
	x = [1, 2, 4]
	y = [2, 3, 6]

	s = spline(x, y, 0, 0)

	print(s[0](1))
