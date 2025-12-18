def gauss_seidel(A: list[list[float]], b: list[float]) -> list[float]:
	n = len(A)

	x = [0.0 for _ in range(n)]
	y = [0.0 for _ in range(n)]

	itr = 0

	def part_a():
		for k in range(n):
			if abs(x[k] - y[k]) > 0.0001:
				print(itr)

				for i in range(n):
					y[i] = x[i]

					print(x[i])

				part_b()

	def part_b():
		nonlocal itr

		itr += 1

		for i in range(n):
			x[i] = A[i][n - 1]

			for j in range(n):
				if j == i:
					continue

				x[i] -= A[i][j] * x[j]

			x[i] /= A[i][i]

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

	print(gauss_seidel(A1, b1))

if __name__ == "__main__":
	main()
