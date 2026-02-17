import math

class BinNode:
    def __init__(self, iniprice, j, n, pup = NotImplemented):
        self.iniprice = iniprice
        self.j = j #upcount
        self.n = n #gen start 0
        self.pup = pup #prob up
    
    def lookup_node(self):
        # n choose j
        coef = math.factorial(self.n) / (math.factorial(self.j) * math.factorial(self.n - self.j))

        pdown = 1 - self.pup
        other = self.n - self.j

        found_chance = coef * (self.pup ** self.j) * (pdown ** other)
        
        return found_chance


node = BinNode(iniprice=100, j=3, n=5, pup=0.7)

print(node.lookup_node())