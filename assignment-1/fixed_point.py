import math
from collections.abc import Callable


def fixed_point(g: Callable[[float], float], x0: float, tol: float = 0.001, n: int = 0) -> float | None:
	x1 = g(x0)

	if abs(x1 - x0) <= tol:
		print(n)
		return x1

	return fixed_point(g, x1, tol, n + 1)


def main() -> None:
	def func(x: float) -> float:
		return math.cos(x)

	def func2(x: float) -> float:
		print(x)
		return math.exp(x) - (x ** 2)

	def func2_prime(x: float) -> float:
		return math.exp(x) - 2 * x

	def func3(x: float) -> float:
		return -math.sqrt(math.exp(x))

	print(fixed_point(func3, 1, 0.001, 10000))

if __name__ == "__main__":
	main()
