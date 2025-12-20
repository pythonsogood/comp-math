import math


def distance(x: list[float]) -> float:
	return math.sqrt(sum(map(lambda i: i ** 2, x)))

def multiply(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
	return [[sum(a * b for a, b in zip(rA, cB)) for cB in zip(*B)] for rA in A]

def relaxation(A: list[list[float]], b: list[float], x0: list[float] | None = None, w: float = 1.1, tol: float = 0.001, nmax: int = 1000) -> tuple[list[float], int]:
	if not (0 < w < 2):
		raise ValueError("w must be in range (0, 2)")

	n = len(A)

	if x0 is None:
		x0 = [0.0] * len(A)

	x = x0.copy()
	k = 0

	while True:
		k += 1

		for i in range(n):
			s = 0.0

			for j in range(n):
				if j == i:
					continue

				s += A[i][j] * x[j]

			x[i] = (1 - w) * x[i] + (w / A[i][i]) * (b[i] - s)

		Ax = multiply(A, [[xi] for xi in x])

		r = [Ax[i][0] - b[i] for i in range(n)]
		r_dist = distance(r)

		if r_dist < tol or k >= nmax:
			break

	return x, k


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

	print(relaxation(A1, b1))

if __name__ == "__main__":
	main()
