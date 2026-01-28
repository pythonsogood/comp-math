import math
from collections.abc import Callable

def weddle(f: Callable[[float], float], a: float, b: float, n: int = 6) -> float:
	assert n % 6 == 0

	h = (b - a) / n

	xs = [a + i * h for i in range(n + 1)]

	s1 = sum(f(xs[i]) for i in range(1, n, 2))
	s2 = sum(f(xs[i]) for i in range(3, n, 6))
	s3 = sum(f(xs[i]) for i in range(2, n, 2))

	return 3 * h / 10 * (f(xs[0]) + f(xs[n]) + 5 * (s1 - s2) + 6 * s2 + s3)

if __name__ == "__main__":
	print(weddle(lambda x: math.log(x), 4, 5.2))
