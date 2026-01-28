from collections.abc import Callable

def simpson_one_third(f: Callable[[float], float], a: float, b: float, n: int) -> float:
	h = (b - a) / n

	s1 = sum(f(a + i * h) for i in range(2, n, 2))
	s2 = sum(f(a + i * h) for i in range(1, n, 2))

	return h / 3 * (f(a) + f(b) + 2 * s1 + 4 * s2)

def simpson_three_eight(f: Callable[[float], float], a: float, b: float, n: int) -> float:
	h = (b - a) / n

	s1 = sum(f(a + i * h) for i in range(3, n, 3))
	s2 = sum(f(a + i * h) + f(a + (i + 1) * h) for i in range(1, n, 3))

	return 3 * h / 8 * (f(a) + f(b) + 2 * s1 + 3 * s2)

if __name__ == "__main__":
	print(simpson_one_third(lambda x: x ** (1/2), 0, 8, 2))
	print(simpson_three_eight(lambda x: 1 / (1 + x ** 2), 0, 6, 6))
