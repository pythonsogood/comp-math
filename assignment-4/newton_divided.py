import math

def newton_divided(x_star: float, x: list[float], y: list[float]) -> float:
	n = len(x)

	dy: list[list[float]] = [[y[i] for i in range(n)]]

	for i in range(1, n):
		dyi = [0.0] * i

		for j in range(i, n):
			dyi.append((dy[i - 1][j] - dy[i - 1][j - 1]) / (x[j] - x[j - 1]))

		dy.append(dyi)

	y_star = y[0]
	p = 1

	for i in range(1, n):
		p *= x_star - x[i - 1]
		y_star += dy[i][i] * p

	return y_star

if __name__ == "__main__":
	x_star = 301
	x = [300, 304, 305, 307]
	y = [2.4771, 2.4829, 2.4843, 2.4871]

	print(newton_divided(x_star, x, y))
