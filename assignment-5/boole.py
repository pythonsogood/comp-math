from collections.abc import Callable

def boole(f: Callable[[float], float], a: float, b: float, n: int = 4) -> float:
	assert n % 4 == 0

	h = (b - a) / n

	xs = [a + i * h for i in range(n + 1)]

	s1 = sum(f(xs[i]) for i in range(1, n, 2))
	s2 = sum(f(xs[i]) for i in range(2, n - 1, 2))
	s3 = sum(f(xs[i]) for i in range(4, n + 1, 4))

	return 2 * h / 45 * (7 * (f(a) + f(b)) + 32 * s1 + 12 * s2 + 14 * s3)

if __name__ == "__main__":
	print(boole(lambda x: 1 / (1 + x ** 2), 0, 6))
