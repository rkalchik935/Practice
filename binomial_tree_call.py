import math

class BinNode:
    def __init__(self, price, j, n, up, down, pup):
        self.price = price #intial
        self.j = j #upcount
        self.n = n #gens, start 0
        self.k = n - j #downcount
        self.up = up
        self.down = down
        self.pup = pup #prob up
    
    def lookup_node(self):
        # n choose j
        coef = math.factorial(self.n) / (math.factorial(self.j) * math.factorial(self.k))
        pdown = 1 - self.pup

        found_chance = coef * (self.pup ** self.j) * (pdown ** self.k)
        
        return found_chance
    
    def get_price(self):
        total_ups = self.up ** self.j
        total_downs = self.down ** (self.k)
        
        return self.price * total_downs * total_ups
        




node = BinNode(price=100, j=3, n=5, up=1.5, down=0.5, pup=0.7)

print(node.lookup_node())

print(node.get_price())