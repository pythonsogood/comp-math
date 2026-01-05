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

def to_matrix(x: Matrix | Vector) -> Matrix:
	if len(x) <= 0 or isinstance(x[0], list):
		return x  # pyright: ignore[reportReturnType]

	return [[i] for i in x] # pyright: ignore[reportReturnType]

def add(a: Matrix, b: Matrix) -> Matrix:
	return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def subtract(a: Matrix, b: Matrix) -> Matrix:
	return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def iterative_method(A: Matrix, B: Matrix, tol: float = 0.001, nmax: int = 1000) -> Matrix | None:
	I = [[1 if i == j else 0 for j in range(len(A[i]))] for i in range(len(A))]

	for _ in range(nmax):
		E = subtract(multiply(A, B), I)

		if max(abs(E[i][j]) for i in range(len(E)) for j in range(len(E[0]))) < tol:
			return B

		B = multiply(B, add(subtract(I, E), multiply(E, E)))

def main() -> None:
	A1 = [
		[4, 2],
		[1, 3],
	]

	B1 = [
		[0.25, -0.2],
		[0.03, 0.25],
	]

	print(iterative_method(A1, B1))

if __name__ == "__main__":
	main()
