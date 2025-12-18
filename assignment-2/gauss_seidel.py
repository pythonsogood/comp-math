def gauss_seidel(A: list[list[float]], b: list[float], tol: float = 0.001, nmax: int = 1000) -> list[float] | None:
	n = len(A)
	x = [0.0] * n

	for _ in range(nmax):
		x_old = x.copy()

		for i in range(n):
			s = b[i]

			for j in range(n):
				if j == i:
					continue

				s -= A[i][j] * x[j]

			x[i] = s / A[i][i]

		if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
			return x

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

	print(gauss_seidel(A1, b1))

if __name__ == "__main__":
	main()
