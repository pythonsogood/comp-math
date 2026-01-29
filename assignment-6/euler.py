from collections.abc import Callable

def euler(f: Callable[[float, float], float], x0: float, y0: float, h: float, xn: float) -> tuple[float, float]:
	n = int((xn - x0) / h)

	x = x0
	y = y0

	for _ in range(n):
		y += h * f(x, y)
		x += h

		if x >= xn:
			break

	return x, y

if __name__ == "__main__":
	print(euler(lambda x, y: y, 0, 1, 0.1, 1))
