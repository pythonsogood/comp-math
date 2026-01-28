from collections.abc import Callable

from scipy import integrate

def lagrange_basis_polynomial(xs: list[float], i: int) -> Callable[[float], float]:
	def L(x: float) -> float:
		prod = 1

		for j in range(len(xs)):
			if j == i:
				continue

			prod *= (x - xs[j]) / (xs[i] - xs[j])

		return prod

	return L

def newton_cotes(f: Callable[[float], float], a: float, b: float, n: int) -> float:
	h = (b - a) / n

	xs = [a + i * h for i in range(n + 1)]
	w = [integrate.quad(lagrange_basis_polynomial(xs, i), a, b)[0] for i in range(n + 1)]

	return sum(w[i] * f(xs[i]) for i in range(n + 1))

if __name__ == "__main__":
	print(newton_cotes(lambda x: x**3 - 4 * x + 9, -7, 7, 5))
