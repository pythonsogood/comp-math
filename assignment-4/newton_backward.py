import math

def newton_backward(x_star: float, x: list[float], y: list[float]) -> float:
	n = len(x)

	h = x[1] - x[0]
	v = (x_star - x[-1]) / h

	dy: list[list[float]] = [[y[i] for i in range(n)]]

	for i in range(1, n):
		dyi = [0.0] * i

		for j in range(i, n):
			dyi.append(dy[i - 1][j] - dy[i - 1][j - 1])

		dy.append(dyi)

	y_star = y[-1]
	vi = 1

	for i in range(1, n):
		y_star += ((v * vi) / math.factorial(i)) * dy[i][n - 1]
		vi *= v + 1

	return y_star

if __name__ == "__main__":
	x_star = 2023
	x = [2010, 2015, 2020, 2025]
	y = [16.5, 17.5, 18.7, 20.0]

	print(newton_backward(x_star, x, y))
