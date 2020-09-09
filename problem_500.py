'''
The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2500500 divisors.
Give your answer modulo 500500507.
---
      Getal  = 2^a * 2^b * 2^c * ... 2^x * 2^y * 2^z
# Div(Getal) = (a+1) * (b+1) * (c+1) * ... * (x+1) * (y+1) * (z+1)

==> 16 divs:
32.768 = 2^15 => (15+1) => 16 || 15 Prime Divs
384 = 2^7 * 3^1 => (7+1) * (1+1) => 16 || 7 + 1 => 8 Prime Divs
216‬ = 2^3 * 3*3 => (3+1) * (3+1) => 16 || 3 + 3 => 6 Prime Divs
120 = 2^3 * 3^1 + 5^1 => (3+1) * (1+1) * (1+1) => 16 || 3 + 1 + 1 => 5 Prime Divs

16 = 16 vs 16
16 = 7 * 1 vs 8 + 2 = 10
16 = 3 * 3 vs 4 + 4 = 8
16 = 3 * 1 * 1 vs 4 + 2 + 2 = 8 <- best

2^4 = 2^4
2^4 = 2^3 * 2^1 vs 2^3-1 + 2^1-1
2^4 = 2^2 * 2^2 vs 2^2-1 + 2^2-1
2^4 = 2^2 * 2^1 * 2^1 vs 2^2-1 + 2^2-1 + 2^2-1

2^2^500500 = 2^2^500500
2^2^500500 = 2^2^
'''

squares_minus_one = [(2**x)-1 for x in range(1, 100)]
print(squares_minus_one)