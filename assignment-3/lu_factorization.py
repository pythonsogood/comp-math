def lu_factorization(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
	n = len(A)

	L, U = [[0.0] * n for _ in range(n)], [[0.0] * n for _ in range(n)]

	for i in range(n):
		for j in range(i, n):
			U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

		L[i][i] = 1
		for j in range(i+1, n):
			L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

	return L, U

def inverse_lu(A: list[list[float]]) -> list[list[float]]:
	n = len(A)

	L, U = lu_factorization(A)

	Ainv = [[0.0] * n for _ in range(n)]

	for i in range(n):
		b = [0.0] * n
		b[i] = 1

		y = [0.0] * n
		for j in range(n):
			y[j] = b[j] - sum(L[j][k] * y[k] for k in range(j))

		x = [0.0] * n
		for j in range(n - 1, -1, -1):
			if U[j][j] == 0:
				raise ValueError("Singular matrix")

			x[j] = (y[j] - sum(U[j][k] * x[k] for k in range(j + 1, n))) / U[j][j]

		for j in range(n):
			Ainv[j][i] = x[j]

	return Ainv

def main() -> None:
	A1 = [
		[2, 3, 1],
		[4, 7, 2],
		[6, 8, 3],
	]

	A2 = [
		[2, -1, -2],
		[-4, 6, 3],
		[-4, -2, 8],
	]

	print(inverse_lu(A2))

if __name__ == "__main__":
	main()
