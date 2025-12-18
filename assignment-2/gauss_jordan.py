from copy import deepcopy


def gauss_jordan(A: list[list[float]], b: list[float]) -> list[float]:
	n = len(A)

	ab = deepcopy(A)
	ab.append(b)

	a = deepcopy(A)
	b = deepcopy(b)

	x: list[float] = [0 for _ in range(n)]

	for k in range(n):
		p = None

		for i in range(k, n):
			pass

		if p is not None and p != k:
			ab[p], ab[k] = ab[k], ab[p]

		pivot = a[k][k]


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

	print(gauss_jordan(A1, b1))

if __name__ == "__main__":
	main()
