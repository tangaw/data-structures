# Import lru_cache as decoractor to cache previously calculated results for recursive function
from functools import lru_cache

@lru_cache(maxsize=5)
def fib(n):
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2)


def main():
  for i in range(400):
    print(f"{i}: {fib(i)}")
  print("done")


if __name__ == "__main__":
  main()