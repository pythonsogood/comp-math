def lagrange_interpolation(x_star: float, x: list[float], y: list[float]) -> float:
	n = len(x)

	s = 0

	for i in range(n):
		prod = 1

		for j in range(n):
			if i == j:
				continue

			prod *= (x_star - x[j]) / (x[i] - x[j])

		s += prod * y[i]

	return s

if __name__ == "__main__":
	x_star = 2
	x = [1, 1.5, 4]
	y = [1, 2/3, 1/4]

	print(lagrange_interpolation(x_star, x, y))
