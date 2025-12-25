import math

type Vector = list[float]
type Matrix = list[Vector]

def multiply(A: Matrix | Vector, B: Matrix | Vector) -> Matrix:
	A = to_matrix(A)
	B = to_matrix(B)

	return [
		[
			sum(
				A[i][k] * B[k][j] if len(A[i]) > k else 0
				for k in range(len(B))
			) for j in range(len(B[0]))
		] for i in range(len(A))
	]

def transpose(x: Matrix | Vector) -> Matrix:
	x = to_matrix(x)

	return [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

def extract_column(a: Matrix, n: int) -> Vector:
	return [row[n] for row in a]

def to_matrix(x: Matrix | Vector) -> Matrix:
	if len(x) <= 0 or isinstance(x[0], list):
		return x  # pyright: ignore[reportReturnType]

	return [[i] for i in x] # pyright: ignore[reportReturnType]

def matrix_equals(a: Matrix, b: Matrix) -> bool:
	if len(a) != len(b):
		return False

	for i in range(len(a)):
		if a[i] != b[i]:
			return False

	return True

def largest_off_diagonal(a: Matrix) -> tuple[int, int, float]:
	p, q = 0, 1

	for i in range(len(a)):
		for j in range(len(a)):
			if i == j:
				continue

			if abs(a[i][j]) > abs(a[p][q]):
				p, q = i, j

	return p, q, a[p][q]

def jacobi_method(A: Matrix, tol: float = 0.001, nmax: int = 100000) -> tuple[list[float], list[Vector]] | None:
	if not matrix_equals(A, transpose(A)):
		raise ValueError("A must be symmetric")

	n = len(A)

	V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

	for _ in range(nmax):
		p, q, Apq = largest_off_diagonal(A)

		c = (A[p][p] - A[q][q]) / math.sqrt(((A[p][p] - A[q][q]) ** 2) + 4 * (Apq ** 2))
		s = (2 * Apq) / math.sqrt(((A[p][p] - A[q][q]) ** 2) + 4 * (Apq ** 2))

		G = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
		G[p][p] = c
		G[q][q] = c
		G[p][q] = s
		G[q][p] = -s

		GT = transpose(G)

		A = multiply(multiply(GT, A), G)

		V = multiply(V, G)

		p, q, Apq = largest_off_diagonal(A)

		if abs(Apq) < tol:
			eigenvalues = [A[i][i] for i in range(n)]
			eigenvectors = transpose(V)

			return eigenvalues, eigenvectors

def main() -> None:
	A1 = [
		[4, 1, 2],
		[1, 3, 5],
		[2, 5, 6],
	]

	print(jacobi_method(A1))

if __name__ == "__main__":
	main()
