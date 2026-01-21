from collections.abc import Callable

import numpy as np

def spline(x: list[float], y: list[float], dx0: float, dxn: float) -> list[Callable[[float], float]]:
	n = len(x) - 1

	h: list[float] = [x[i + 1] - x[i] for i in range(n)]
	b: list[float] = [(y[i + 1] - y[i]) / h[i] for i in range(n)]

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
		w[i] = h[i - 1]
		q[i] = 6 * (b[i] - b[i - 1])

	u[n] = 2 * h[n - 1]
	w[n] = h[n - 1]
	q[n] = 6 * (dxn - b[n - 1])

	T: list[list[float]] = [[0] * (n + 1) for _ in range(n + 1)]

	for i in range(n + 1):
		T[i][i] = u[i]
		if i < n:
			T[i][i + 1] = v[i]

		if i > 0:
			T[i][i - 1] = w[i]

	z: list[float] = np.linalg.solve(np.array(T), np.array(q)).tolist()

	S: list[Callable[[float], float]] = []

	for i in range(n):
		xi, xi1 = x[i], x[i + 1]
		yi, yi1 = y[i], y[i + 1]
		hi = h[i]
		zi, zi1 = z[i], z[i + 1]

		S.append(lambda x_star: (\
			zi1 / (6 * hi)) * (x_star - xi) ** 3\
			+ (zi / (6 * hi)) * (xi1 - x_star) ** 3\
			+ (yi1 / hi - ((hi * zi1) / 6)) * (x_star - xi)\
			+ (yi / hi - (hi * zi) / 6) * (xi1 - x_star))

	return S

if __name__ == "__main__":
	x = [1, 2, 4]
	y = [2, 3, 6]

	s = spline(x, y, 0, 0)

	print(s[1](4))
