import math
from typing import overload

import numpy as np

type Vector = list[float]
type Matrix = list[Vector]

def distance(x: Vector) -> float:
	return math.sqrt(sum(map(lambda i: i ** 2, x)))

@overload
def multiply(A: Matrix, B: Matrix) -> Matrix:
	...

@overload
def multiply(A: Matrix, B: Vector) -> Vector | float:
	...

@overload
def multiply(A: Matrix, B: float) -> Matrix:
	...

def multiply(A: Matrix, B: Matrix | Vector | float) -> Matrix | Vector | float:
	if isinstance(B, (float, int)):
		return [[B * A[i][j]] for i in range(len(A)) for j in range(len(A[i]))]
	elif len(B) > 0 and not isinstance(B[0], list):
		vec = extract_column(multiply(A, [[i] for i in B]), 0)

		if len(A) == 1:
			return vec[0]

		return vec

	return [[sum(a * b for a, b in zip(rA, cB)) for cB in zip(*B)] for rA in A]

def normalize(x: Vector) -> Vector:
	dist = distance(x)

	return [i / dist for i in x]

def transpose(x: Matrix | Vector) -> Matrix:  # pyright: ignore[reportRedeclaration]
	n = len(x)

	if n <= 0:
		return x  # pyright: ignore[reportReturnType]

	x: Matrix = [[i] for i in x] if not isinstance(x[0], list) else x

	n = len(x)

	m = len(x[0])

	xT = [[0.0] * m for _ in range(n)]

	for i in range(n):
		for j in range(m):
			xT[i][j] = x[j][i]

	return xT

def inverse(x: Matrix) -> Matrix:
	a = np.array(x)
	return np.linalg.inv(a).tolist()

def divide(a: Matrix, b: Matrix) -> Matrix:
	return multiply(a, inverse(b))

def add(a: Matrix, b: Matrix) -> Matrix:
	c = []

	for i in range(len(a)):
		c.append([])

		for j in range(len(a[i])):
			c[i].append(a[i][j] + b[i][j])

	return c

def extract_column(a: Matrix, n: int) -> Vector:
	x = []

	for i in range(len(a)):
		x.append(a[i][n])

	return x

def subtract(a: Matrix, b: Matrix) -> Matrix:
	c = []

	for i in range(len(a)):
		c.append([])

		for j in range(len(a[i])):
			c[i].append(a[i][j] - b[i][j])

	return c

def power_method(A: Matrix, x0: Vector, tol: float = 0.001, nmax: int = 1000) -> float | None:
	xn = x0
	lambd_prev = None

	for _ in range(nmax):
		xn = multiply(A, xn)
		xn = normalize(xn)

		xnT = transpose(xn)

		Axn = multiply(A, xn)

		lambd_numerator: float = multiply(xnT, Axn)
		lambd_denominator: float = multiply(xnT, xn)
		lambd = lambd_numerator / lambd_denominator

		if lambd_prev is not None:
			pass

		lambd_prev = lambd

	return lambd_prev

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
