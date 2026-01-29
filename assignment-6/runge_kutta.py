from collections.abc import Callable

def runge_kutta_3(f: Callable[[float, float], float], x0: float, y0: float, h: float, xn: float) -> tuple[float, float]:
	n = int((xn - x0) / h)

	x = x0
	y = y0

	for _ in range(n):
		k1 = f(x, y)
		k2 = f(x + h / 2, y + h / 2 * k1)
		k3 = f(x + h, y - h * k1 + 2 * h * k2)

		y += h / 2 * (k1 + 4 * k2 + k3)
		x += h

		if x >= xn:
			break

	return x, y

def runge_kutta_4(f: Callable[[float, float], float], x0: float, y0: float, h: float, xn: float) -> tuple[float, float]:
	n = int((xn - x0) / h)

	x = x0
	y = y0

	for _ in range(n):
		k1 = f(x, y)
		k2 = f(x + h / 2, y + h / 2 * k1)
		k3 = f(x + h / 2, y + h / 2 * k2)
		k4 = f(x + h, y + h * k3)

		y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
		x += h

		if x >= xn:
			break

	return x, y

if __name__ == "__main__":
	print(runge_kutta_3(lambda x, y: y, 0, 1, 0.1, 1))
	print(runge_kutta_4(lambda x, y: x ** 2 + y ** 2, 1, 1.2, 0.05, 1.05))
