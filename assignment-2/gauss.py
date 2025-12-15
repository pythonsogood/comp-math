from copy import deepcopy


def gauss(A: list[list[float]], b: list[float]) -> list[float]:
	n = len(A)

	a = deepcopy(A)
	b = deepcopy(b)

	x: list[float] = [0 for _ in range(n)]

	for k in range(n):
		for i in range(k + 1, n):
			cik = a[i][k] = a[k][k]

			for j in range(k + 1, n):
 				a[i][j] -= cik * a[k][j]

			b[i] -= cik * b[k]

	x[n - 1] = b[n - 1] / a[n - 1][n - 1]

	for i in range(n - 2, 1):
		s = 0

		for j in range(i + 1, n):
			s += a[i][j] * x[j]

		x[i] = 1 / a[i][j] * (b[i] - s)

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

	print(gauss(A1, b1))

if __name__ == "__main__":
	main()
