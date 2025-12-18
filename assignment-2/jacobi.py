def jacobi(A: list[list[float]], b: list[float]) -> list[float]:
	n = len(A)
	m = 1

	x = [0.0 for _ in range(n)]
	c = [0.0 for _ in range(n)]

	def part_a():
		nonlocal m

		for i in range(n):
			x[i] = c[i] / A[i][i]

		m += 1

		if m <= 1:
			return part_b()

	def part_b():
		for i in range(n):
			c[i] = b[i]

			for j in range(n):
				if i == j:
					continue

				c[i] -= A[i][j] * x[j]

		return part_a()

	part_b()

	return x

def main() -> None:
	A1 = [
		[2, 3],
		[4, 1],
	]

	b1 = [
		5,
		11,
	]

	print(jacobi(A1, b1))

if __name__ == "__main__":
	main()
