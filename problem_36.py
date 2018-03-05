# sum of all nrs palindromic in d10 and d2 sub 1m
import cProfile

def b10_palindrome(input_):
    if str(input_)[::-1] == str(input_):
        return True
    else:
        return False

def b2_palindrome(input_):
    tekst = str(bin(input_))[2:]
    if tekst[::-1] == tekst:
        return True
    else:
        return False

def main():
    return sum([x for x in range(1, 1000000, 2) if b10_palindrome(x) and b2_palindrome(x)])

cProfile.run("print(main())")
