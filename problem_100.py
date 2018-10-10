## If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random,  it can be seen that the probability of taking two blue discs,P(BB) = (15/21)×(14/20) = 1/2.
## The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
## By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

## R+B > 10^12 where (B/R+B)*(B-1/(R+B-1)) = 1/2
## B / (R+B)  *  (B-1)/(R+B-1)  = 1/ 2
## B * (B-1) / (R+B) * (R+B-1) = 1/2
## (B² - B) / (R² + R*B - R + R*B + B² - B) = 1/2
## (B² - B) / (R² + 2*R*B + B² - B - R) = 1/2
## 2B² - B = R² + 2*R*B + B² - B - R
## 2B² = R² + 2*R*B + B² - R
## B² - R² - 2*R*B + R = 0

## Wolframalpha:
## R = (-)sqrt(2B²+B)-B

from math import sqrt
import math

def chest_check(red, blue):
    if blue**2 - blue - 2*blue*red - red**2 + red == 0:
        return True
    else:
        return False

def value(red, blue):
    return (blue**2 - blue - 2*blue*red - red**2 + red)


def r_value_for_b(blue):
    rt_one = sqrt(2*blue*blue + blue) - blue
    return rt_one

for x in range(7**12, 10**12):
    if chest_check(int(sqrt(2*x**2+x)-x), x):
        print(int(sqrt(2*x**2+x)-x), x)
