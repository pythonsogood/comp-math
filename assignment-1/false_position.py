import math
from collections.abc import Callable


def false_position(f: Callable[[float], float], a: float, b: float, tol: float = 0.001, nmax: int = 1000) -> float | None:
	fa = f(a)
	fb = f(b)

	if fa * fb >= 0:
		raise ValueError("f(a) * f(b) must be less than 0!")

	for n in range(nmax):
		c = (a * fb - b * fa) / (fb - fa)
		fc = f(c)

		if abs(fc) < tol:
			return c

		if fa * fc < 0:
			b = c
			fb = fc
		else:
			a = c
			fa = fc

def main() -> None:
	def func(x: float) -> float:
		return 2 * math.exp(x) * math.sin(x) - 3

	def func2(x: float) -> float:
		return math.exp(x) - (x ** 2)

	def func2_prime(x: float) -> float:
		return math.exp(x) - 2 * x

	def func3(x: float) -> float:
		return -math.sqrt(math.exp(x))

	print(false_position(func, 0, 1))

if __name__ == "__main__":
	main()
