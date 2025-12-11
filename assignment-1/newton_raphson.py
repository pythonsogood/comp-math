import math
from collections.abc import Callable


def newton_raphson(f: Callable[[float], float], df: Callable[[float], float], x0: float, tol: float = 0.001, nmax: int = 1000) -> float | None:
	for itr in range(nmax):
		h = f(x0) / df(x0)
		x1 = x0 - h

		if abs(h) < tol:
			print(itr)
			return x1

		x0 = x1


def main() -> None:
	def func(x: float) -> float:
		return (x ** 3) - 2 * x - 5

	def func_prime(x: float) -> float:
		return 3 * (x ** 2) - 2

	def func2(x: float) -> float:
		return math.exp(x) - (x ** 2)

	def func2_prime(x: float) -> float:
		return math.exp(x) - 2 * x

	def func3(x: float) -> float:
		return -math.sqrt(math.exp(x))

	print(newton_raphson(func2, func2_prime, 2, 0.001, 10000))

if __name__ == "__main__":
	main()
