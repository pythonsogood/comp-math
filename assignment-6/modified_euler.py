from collections.abc import Callable

def modified_euler(f: Callable[[float, float], float], x0: float, y0: float, h: float, xn: float) -> float:
	n = int((xn - x0) / h)

	x = x0
	y = y0

	for _ in range(n):
		d = f(x, y)

		y += h / 2 * (d + f(x + h, y + h * d))
		x += h

	if x < xn:
		d = f(x, y)

		hf = xn - x
		y += hf / 2 * (d + f(x + hf, y + hf * d))

	return y

if __name__ == "__main__":
	print(modified_euler(lambda x, y: y, 0, 1, 0.1, 1))
