import math
from collections.abc import Callable

def dfdx(f: Callable[[float, float], float], x: float, y: float, eps: float = 0.000001) -> float:
	return (f(x + eps, y) - f(x - eps, y)) / (2 * eps)

def dfdy(f: Callable[[float, float], float], x: float, y: float, eps: float = 0.000001) -> float:
	return (f(x, y + eps) - f(x, y - eps)) / (2 * eps)

def taylor(f: Callable[[float, float], float], x0: float, y0: float, xt: float, n: int) -> float:
	derivatives = [0] * (n + 1)

	derivatives[1] = f(x0, y0)

	for k in range(2, n + 1):
		fx = dfdx(f, x0, y0)
		fy = dfdy(f, y0, x0)

		derivatives[k] = fx + fy * derivatives[k - 1]

	dx = xt - x0
	y = y0

	for k in range(1, n + 1):
		y += derivatives[k] * dx**k / math.factorial(k)

	return y

if __name__ == "__main__":
	print(taylor(lambda x, y: x + y, 0, 1, 1, 2))
