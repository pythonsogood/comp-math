def jacobi(A: list[list[float]], b: list[float], tol: float = 0.001, nmax: int = 1000) -> list[float] | None:
	n = len(A)
	x = [0.0] * n

	for _ in range(nmax):
		x_new = [0.0] * n

		for i in range(n):
			s = b[i]

			for j in range(n):
				if j == i:
					continue

				s -= A[i][j] * x[j]

			x_new[i] = s / A[i][i]

		if max(abs(x_new[i] - x[i]) for i in range(n)) <= tol:
			return x_new

		x = x_new

def main() -> None:
	A1 = [
		[2, 1, 1],
		[1, 3, -1],
		[-1, 1, 2],
	]

	b1 = [
		6,
		0,
		3,
	]

	print(jacobi(A1, b1))

if __name__ == "__main__":
	main()
