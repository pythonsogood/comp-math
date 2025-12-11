import math
from collections.abc import Callable


def secant(f: Callable[[float], float], x0: float, x1: float, tol: float = 0.001, nmax: int = 1000) -> float | None:
	xn_prev = x0
	xn = x1

	fn_prev = f(xn_prev)
	fn = f(xn)

	for n in range(nmax):
		xn_next = xn - fn * ((xn - xn_prev) / (fn - fn_prev))
		fn_next = f(xn_next)

		if abs(fn_next) < tol:
			return xn_next

		xn_prev = xn
		fn_prev = fn

		xn = xn_next
		fn = fn_next


def main() -> None:
	def func(x: float) -> float:
		return x ** 3 - 2 * x - 5

	def func2(x: float) -> float:
		return math.exp(x) - (x ** 2)

	def func2_prime(x: float) -> float:
		return math.exp(x) - 2 * x

	def func3(x: float) -> float:
		return -math.sqrt(math.exp(x))

	print(secant(func, 2, 3, 10 ** (-5)))

if __name__ == "__main__":
	main()
