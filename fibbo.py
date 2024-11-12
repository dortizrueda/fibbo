import argparse

from functools import cache

def fibbo(n: int) -> int:
    """
    Computes the n-th Fibonacci number.
    :param n: n-th Fibonacci number.
    :return: solucion of the n-th Fibonacci number.
    """
    f0, f1 = 0, 1
    if n < 0:
        raise ValueError("n is negative")
    if (n == 0) or (n == 1):
        return n
    else:
        return fibbo(n - 1) + fibbo(n - 2)


##cache={}

##def fibbo_recursive(n: int) -> int:
##  """..."""
##if n<0
##  raise ValueError("n is negative")
##if n<2
##  return n
##if n in cache:
##  return cache[n]

@cache
def fibonacci_recursive_memoization(n:int)->int:
    if n<0:
        raise ValueError("n must be greater than or equal to zero.")
    if n<2:
        return n
    return fibonacci_recursive_memoization(n-1) + fibonacci_recursive_memoization(n-2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help="Fibonnaci n-th number")  # positional argument
    args = parser.parse_args()
    print(fibbo(args.n))
