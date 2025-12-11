import math
from collections.abc import Callable


def bisection(f: Callable[[float], float], a: float, b: float, tol: float = 0.001, nmax: int = 1000, i: int = 1) -> float | None:
	c = (a + b) / 2
	fc = f(c)

	if abs(fc) < tol or i > nmax:
		return c

	fa = f(a)
	if fa * fc <= 0:
		return bisection(f, a, c, tol, nmax, i + 1)

	fb = f(b)
	if fc * fb <= 0:
		return bisection(f, c, b, tol, nmax, i + 1)


def main() -> None:
	def func(x: float) -> float:
		return x ** 3 - x - 2

	def func2(x: float) -> float:
		return math.exp(x) - (x ** 2)

	def func2_prime(x: float) -> float:
		return math.exp(x) - 2 * x

	def func3(x: float) -> float:
		return -math.sqrt(math.exp(x))

	print(bisection(func, 1, 2, 0.001, 10000))

if __name__ == "__main__":
	main()
