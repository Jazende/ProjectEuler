import re

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @property
    def c_val(self):
        try:
            return int(self.value)
        except:
            if self.value == 'T':
                return 10
            elif self.value == 'J':
                return 11
            elif self.value == 'Q':
                return 12
            elif self.value == 'K':
                return 13
            elif self.value == 'A':
                return 14
    
    def __repr__(self):
        return f'{self.value}{self.suit}'

    def __lt__(self, other):
        if self.c_val < other.c_val:
            return True
        return False

class Hand(list):
    def __init__(self, cards):
        self._score = 0
        for card in cards:
            self.append(card)
        self.sort()
        self._suits = {suit: len([card for card in self if card.suit == suit]) for suit in ['C', 'D', 'S', 'H']}
        self._values = {val: len([card for card in self if card.c_val == val]) for val in range(2, 15)}

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = max(self._score, value)

    @property
    def flush(self):
        if any([self._suits[suit] == 5 for suit in self._suits]):
            return True
        return False
    
    @property
    def royal(self):
        if all([self._values[val] == 1 for val in range(10, 15)]):
            return True
        return False

    @property
    def four(self):
        if any([self._values[val] == 4 for val in range(2, 15)]):
            return True
        return False

    @property
    def three(self):
        if any([self._values[val] == 3 for val in range(2, 15)]):
            return True
        return False

    @property
    def pair(self):
        if any([self._values[val] == 2 for val in range(2, 15)]):
            return True
        return False

    @property
    def full(self):
        if self.three and self.pair:
            return True
        return False
    
    @property
    def two_pair(self):
        c_vals = [self._values[val] for val in range(2, 15)]
        c_vals.sort()
        if c_vals == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2]:
            return True
        return False

    @property
    def straight(self):
        v = [card.c_val for card in self]
        v.sort()
        v = [x-min(v) for x in v]
        if v == [0, 1, 2, 3, 4]:
            return True
        return False

    @property
    def high_card(self):
        return max([card.c_val for card in self]) / 100

    @property
    def pair_value(self):
        for card in self:
            for other_card in [c for c in self if not c == card]:
                if card.c_val == other_card.c_val:
                    return card.c_val

with open(r'p054_poker.txt', 'r') as f:
    raw_input = f.read()

inputs = raw_input.strip().split('\n')

left_win = 0
right_win = 0

for hand in inputs:
    left_hand  = Hand([Card(x[0], x[1]) for x in hand[:14].split(' ')])

    right_hand = Hand([Card(x[0], x[1]) for x in hand[15:].split(' ')])

    for hand in [left_hand, right_hand]:
        if hand.flush and hand.royal:
            hand.score = 900

        elif hand.flush and hand.straight:
            hand.score = 800
        
        elif hand.four:
            hand.score = 700
        
        elif hand.full:
            hand.score = 600

        elif hand.full:
            hand.score = 500
        
        elif hand.straight:
            hand.score = 400

        elif hand.three:
            hand.score = 300
        
        elif hand.two_pair:
            hand.score = 200
        
        elif hand.pair:
            hand.score = (100 + hand.pair_value + (hand.high_card / 100) )

        else:
            hand.score = (hand.high_card / 100)
  
    if left_hand.score > right_hand.score:
        left_win += 1
    if left_hand.score < right_hand.score:
        right_win += 1
    if left_hand.score == right_hand.score:
        print(left_hand, left_hand.pair_value, " vs ", right_hand, right_hand.pair_value, "\t", left_hand.score, )

print(left_win)