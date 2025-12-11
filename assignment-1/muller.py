import math
from collections.abc import Callable
from typing import Literal


def sgn(x: float) -> Literal[-1, 0, 1]:
	"""
		https://ru.wikipedia.org/wiki/Sgn
	"""
	if x > 0:
		return 1

	if x < 0:
		return -1

	return 0

def muller(f: Callable[[float], float], x0: float, x1: float, x2: float, tol: float = 0.001, nmax: int = 1000) -> float | None:
	for n in range(nmax):
		y0 = f(x0)
		y1 = f(x1)
		y2 = f(x2)

		# https://en.wikipedia.org/wiki/Muller%27s_method#Derivation
		h0 = x1 - x0
		h1 = x2 - x1

		d0 = (y1 - y0) / h0
		d1 = (y2 - y1) / h1

		a = (d1 - d0) / (h1 + h0)
		b = a * h1 + d1
		c = y2

		D = math.sqrt(b ** 2 - 4 * a * c)

		x3 = x2 - ((2 * c) / (b + sgn(b) * D))
		y3 = f(x3)

		if abs(y3) < tol:
			return x3

		x0 = x1
		x1 = x2
		x2 = x3


def main() -> None:
	def func(x: float) -> float:
		return math.cos(x) - x * math.exp(x)

	def func2(x: float) -> float:
		return math.exp(x) - (x ** 2)

	def func2_prime(x: float) -> float:
		return math.exp(x) - 2 * x

	def func3(x: float) -> float:
		return -math.sqrt(math.exp(x))

	print(muller(func, -1, 0, 1))

if __name__ == "__main__":
	main()
