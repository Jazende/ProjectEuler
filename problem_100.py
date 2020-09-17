from math import sqrt

class ProbabilityBox:
    def __init__(self, blue=None, red=None):
        self.blue = blue if blue else 1
        self.red = red if red else 1
    
    @property
    def total(self):
        return self.blue + self.red
    
    @property
    def chance(self):
        top = self.blue * (self.blue-1)
        bot = self.total * (self.total-1)
        return (top*2) - bot

    def find_next_combination(self):
        self.red += 1
        while True:
            c = self.chance
            if c == 0:
                break
            elif c > 0:
                self.red += 1
            elif c < 0:
                self.blue += 1
            # print(self.total, self.blue, self.red, self.chance)
        return self


two = sqrt(2) + 1
zero = sqrt(2) - 1
calc = lambda x: round(1+sqrt(2) * x + 0.5, 1)

if __name__ == '__main__':
    box = ProbabilityBox()

    # red = 292893218813
    red = 3
    while True:
        x = calc(red)
        if int(x) == x:
            print(x, red)
            box.red = red
            box.blue = red+int(x)-1
            if box.chance == 0:
                print(box.red+box.blue, box.blue, box.red, box.chance)
                # break
        red += 1
        if red > 40:
            break

