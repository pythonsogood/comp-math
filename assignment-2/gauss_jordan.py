from copy import deepcopy


def augment(A: list[list[float]], b: list[float]) -> list[list[float]]:
	return [row + [b[i]] for i, row in enumerate(deepcopy(A))]

def gauss_jordan(A: list[list[float]], b: list[float]) -> list[float]:
	n = len(A)

	Ab = augment(A, b)

	for k in range(n):
		p = None
		p_max = None

		for i in range(k, n):
			curr_p = abs(Ab[i][k])

			if p_max is None or p_max < curr_p:
				p = i
				p_max = curr_p

		if p is not None and p != k:
			Ab[p], Ab[k] = Ab[k], Ab[p]

		pivot = Ab[k][k]

		for i in range(len(Ab[k])):
			Ab[k][i] /= pivot

		for i in range(n):
			if i == k:
				continue

			factor = Ab[i][k]

			for j in range(len(Ab[i])):
				Ab[i][j] -= factor * Ab[k][j]

	return [Ab[i][-1] for i in range(n)]

def main() -> None:
	A1 = [
		[2, 3],
		[4, 1],
	]

	b1 = [
		5,
		11,
	]

	print(gauss_jordan(A1, b1))

if __name__ == "__main__":
	main()
