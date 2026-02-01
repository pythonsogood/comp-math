from collections.abc import Callable

from scipy import integrate

def picard(f: Callable[[float, float], float], x0: float, y0: float, n: int) -> Callable[[float], float]:
	phi: list[Callable[[float], float]] = [lambda x: y0]

	for _ in range(n):
		phi.append(lambda x, p=phi[-1]: y0 + integrate.quad(lambda t: f(t, p(t)), x0, x)[0])

	return phi[-1]

if __name__ == "__main__":
	print(picard(lambda x, y: x + y, 0, 1, 3)(1))
