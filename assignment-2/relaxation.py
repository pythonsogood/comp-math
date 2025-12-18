import math


def dist(x: list[float]) -> float:
	return math.sqrt(sum(map(lambda i: i ** 2, x)))

def dist2(x: list[float], y: list[float]) -> float:
	n = min(len(x), len(y))

	dist_square = 0

	for i in range(n):
		dist_square += (y[i] - x[i]) ** 2

	return math.sqrt(dist_square)

def mult(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
	return [[sum(a*b for a, b in zip(rA, cB)) for cB in zip(*B)] for rA in A]

def relaxation(A: list[list[float]], b: list[float], x0: list[float], w: float = 1.5, tol: float = 0.001, nmax: int = 1000) -> tuple[list[float], int]:
	if w <= 1 or w >= 2:
		raise ValueError("w must be in range (1, 2)")

	n = len(A)

	k = 0
	x = x0

	while True:
		k += 1

		for i in range(n):
			o = 0

			for j in range(i):
				o += A[i][j] * x[j]

			for j in range(i + 1, n):
				o += A[i][j] * x[j]

			x[i] = (1 - w) * x[i] + (w / A[i][i]) * (b[i] - o)

		r_dist = dist2(A[i], b)

		if r_dist < tol or k >= nmax:
			break

	return x, k

def main() -> None:
	A1 = [
		[2, 3],
		[4, 1],
	]

	b1 = [
		5,
		11,
	]

	print(relaxation(A1, b1, [1, 2]))

if __name__ == "__main__":
	main()
