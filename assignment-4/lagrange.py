from typing import Callable, overload

@overload
def lagrange_interpolation(*, x_star: float, x: list[float], y: list[float]) -> float:
	"""
		Lagrange's interpolation
	"""

@overload
def lagrange_interpolation(*, x_star: float, x: list[float], f: Callable[[float], float]) -> float:
	"""
		Lagrange's interpolation\n
		Uses `f(x)` to calculate `y`
	"""

@overload
def lagrange_interpolation(*, x_star: float, x: list[float], y: list[float], f: Callable[[float], float]) -> float:
	"""
		Lagrange's interpolation\n
		If size of `y` values are less than size of `x`, it fills `y` by calculating values from `f(x)`
	"""

def lagrange_interpolation(*, x_star: float, x: list[float], y: list[float] | None = None, f: Callable[[float], float] | None = None) -> float:
	n = len(x)

	if y is not None:
		m = len(y)

		if m < n:
			if f is not None:
				y += [f(x[i]) for i in range(m, n)]
			else:
				raise ValueError(f"y does not have enough values for {n=} and f is not defined to automatically fill it up")
	elif f is not None:
		y = [f(i) for i in x]
	else:
		raise ValueError("f or y must be defined!")

	s = 0

	for i in range(n):
		prod = 1

		for j in range(n):
			if i == j:
				continue

			prod *= (x_star - x[j]) / (x[i] - x[j])

		s += prod * y[i]

	return s

if __name__ == "__main__":
	x_star = 2
	x = [1, 1.5, 4]
	y = [1, 2/3, 1/4]

	print(lagrange_interpolation(x_star=x_star, x=x, f=lambda x: 1/x))
