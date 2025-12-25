type Vector = list[float]
type Matrix = list[Vector]

def normalize_inf(x: Vector) -> Vector:
	m = max(abs(i) for i in x)
	return [i / m for i in x]

def multiply(A: Matrix | Vector, B: Matrix | Vector) -> Matrix:
	A = to_matrix(A)
	B = to_matrix(B)

	return [
		[
			sum(
				A[i][k] * B[k][j] if len(A[i]) > k else 0
				for k in range(len(B))
			) for j in range(len(B[i]))
		] for i in range(len(A))
	]

def transpose(x: Matrix | Vector) -> Matrix:
	x = to_matrix(x)

	return [[x[i][j]] for j in range(len(x[0])) for i in range(len(x))]

def extract_column(a: Matrix, n: int) -> Vector:
	return [row[n] for row in a]

def to_matrix(x: Matrix | Vector) -> Matrix:
	if len(x) <= 0 or isinstance(x[0], list):
		return x  # pyright: ignore[reportReturnType]

	return [[i] for i in x] # pyright: ignore[reportReturnType]

def power_method(A: Matrix, x0: Vector, tol: float = 0.001, nmax: int = 1000) -> tuple[float, Vector] | None:
	y_prev = extract_column(multiply(A, x0), 0)
	eigenvalue_prev = None

	for _ in range(nmax):
		xn = normalize_inf(y_prev)
		xnT = extract_column(transpose(xn), 0)

		Axn = extract_column(multiply(A, xn), 0)

		eigenvalue = extract_column(multiply(xnT, Axn), 0)[0] / extract_column(multiply(xnT, xn), 0)[0]

		if eigenvalue_prev is not None:
			if abs(eigenvalue - eigenvalue_prev) < tol:
				return eigenvalue, normalize_inf(xn)

		y_prev = Axn
		eigenvalue_prev = eigenvalue

def main() -> None:
	A1 = [
		[4, 1],
		[2, 3],
	]

	x01 = [
		1,
		1,
	]

	print(power_method(A1, x01))

if __name__ == "__main__":
	main()
