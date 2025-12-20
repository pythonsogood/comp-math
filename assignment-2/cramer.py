from copy import deepcopy

import numpy as np


def determinant(m: list[list[float]]) -> float:
	"""
		https://www.geeksforgeeks.org/python/how-to-calculate-the-determinant-of-a-matrix-using-numpy/

		"For large matrices, numpy.linalg.slogdet() is a numerically stable method.
		It computes the sign and the logarithm of the determinant separately,
		which helps prevent numerical overflow or underflow when dealing with very large or very small values."
	"""

	mn = np.array(m)
	sign, logdet = np.linalg.slogdet(mn)

	return (sign * np.exp(logdet)).item()

def cramer(A: list[list[float]], b: list[float]) -> list[float]:
	D = determinant(A)

	if D == 0:
		raise ValueError("det(A) == 0")

	n = len(A)

	x = [0.0] * n

	for i in range(n):
		Ai = deepcopy(A)
		for j in range(n):
			Ai[j][i] = b[j]

		Di = determinant(Ai)

		x[i] = Di / D

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

	print(cramer(A1, b1))

if __name__ == "__main__":
	main()
