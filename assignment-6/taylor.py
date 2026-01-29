import math
from collections.abc import Callable

from scipy import differentiate

def taylor(f: Callable[[float, float], float], x0: float, y0: float, xt: float, n: int) -> float:
	derivatives: list[float] = [0, f(x0, y0)] + [0] * n

	for k in range(2, n + 1):
		fx: float = differentiate.derivative(lambda x: f(x, y0), x0, order=1).df
		fy: float = differentiate.derivative(lambda y: f(x0, y), y0, order=1).df

		derivatives[k] = fx + fy * derivatives[k - 1]

	dx = xt - x0
	y = y0

	for k in range(1, n + 1):
		y += derivatives[k] * dx**k / math.factorial(k)

	return y

if __name__ == "__main__":
	print(taylor(lambda x, y: x + y, 0, 1, 1, 2))
