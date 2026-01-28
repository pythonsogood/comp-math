from collections.abc import Callable

def trapezoid(f: Callable[[float], float], a: float, b: float, n: int) -> float:
	h = (b - a) / n

	return h / 2 * (f(a) + f(b) + 2 * sum(f(a + i * h) for i in range(1, n)))

if __name__ == "__main__":
	print(trapezoid(lambda x: x**3 - 4 * x + 9, -7, 7, 5))
