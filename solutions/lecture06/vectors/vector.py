class Vec2D:
    
    # Konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, vec):
        return Vec2D(self.x + vec.x, self.y + vec.y)
    
    def mag(self):
        return ((self.x**2) + self.y**2)**0.5
    
    def __repr__(self):
        return f'({self.x}, {self.y})'