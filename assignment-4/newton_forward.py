import math

def newton_forward(x_star: float, x: list[float], y: list[float]) -> float:
	n = len(x)

	h = x[1] - x[0]
	u = (x_star - x[0]) / h

	dy: list[list[float]] = [[y[i] for i in range(n)]]

	for i in range(1, n):
		dyi = []

		for j in range(n - i):
			dyi.append(dy[i - 1][j + 1] - dy[i - 1][j])

		dy.append(dyi)

	y_star = y[0]
	ui = 1

	for i in range(1, n):
		y_star += ((u * ui) / math.factorial(i)) * dy[i][0]
		ui *= (u - i)

	return y_star

if __name__ == "__main__":
	x_star = 2018
	x = [2010, 2015, 2020, 2025]
	y = [16.5, 17.5, 18.7, 20.0]

	print(newton_forward(x_star, x, y))
