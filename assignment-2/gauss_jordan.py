from copy import deepcopy


def gauss_jordan(A: list[list[float]], b: list[float]) -> list[float]:
	n = len(A)

	ab = deepcopy(A)
	ab.append(b)

	for k in range(n):
		p = None
		p_max = None

		for i in range(k, n):
			curr_p = abs(A[i][k])

			if p_max is None or p_max < curr_p:
				p = i
				p_max = curr_p

		if p is not None and p != k:
			ab[p], ab[k] = ab[k], ab[p]

		pivot = A[k][k]

		for i in range(len(ab[k])):
			ab[k][i] /= pivot

		for i in range(n):
			if i == k:
				continue

			factor = ab[i][k]

			for j in range(len(ab[i])):
				ab[i][j] /= factor * ab[k][j]

	return ab[len(ab) - 1]

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
