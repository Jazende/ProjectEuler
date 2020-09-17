# from functools import lru_cache

# def fib_range():
#     fib = [1, 1]
#     while len(fib) < 90:
#         fib.append(fib[-1]+fib[-2])
#     return fib

# smallest_cache = {}
# def smallest_digit_sum(n):
#     if n in smallest_cache:
#         return smallest_cache[n]
#     x = 1
#     while True:


# def digit_sum(n):
#     return sum(int(x) for x in str(n))

# def range_smallest_digit_sum(from_=1, to=20):
#     return sum(smallest_digit_sum(x) for x in range(1, to))

# print(digit_sum(10))
