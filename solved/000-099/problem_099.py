from math import log10

with open(r'p099_base_exp.txt', 'r') as f:
    inputs_ = f.read()

numbers = [[int(i) for i in x.split(',')] for x in inputs_.split('\n')]
print(numbers.index(max(numbers, key=lambda x: x[1] * log10(x[0])))+1)

# class BigExp:
#     def __init__(self, base, exponent):
#         self.base = base
#         self.exponent = exponent
#         self.value = self.exponent * log10(self.base)

#     def __gt__(self, other):
#         if self.value > other.value:
#             return True

#     def __repr__(self):
#         return f'{self.base}**{self.exponent} = {self.value}'

# numbers = [BigExp(x[0], x[1]) for x in numbers]
# print(numbers.index(max(numbers))+1)