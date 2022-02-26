
class Rectangle:
    def __init__(self, width, height):
        self.name = type(self).__name__
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.width = new_width
        return self.width
    
    def set_height(self, new_height):
        self.height = new_height
        return self.height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    
    def get_diagonal(self):
        return ((self.width**2 + self.height**2)** 0.5)
    
    def get_picture(self):
        #Returns a string that represents the shape using lines of "*".
        p_string = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                p_string = p_string + '*'*self.width + '\n'
        return p_string

    def get_amount_inside(self, shape):
        #returns how many times the passed in shape can fit inside the object (with no rotations)
        if shape.width > self.width or shape.height > self.height:
            return 0
        else:
            return (self.width//shape.width) * (self.height//shape.height)
        
        
    def __repr__(self):
        return f"This object is a {self.name}"
    
    def __str__(self):
        return f"{self.name}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_len):
        self.name = type(self).__name__
        self.width = side_len
        self.height = side_len
    
    def set_width(self, new_width):
        return self.set_side(new_width)
    
    def set_height(self, new_height):
        return self.set_side(new_height)
    
    def set_side(self, new_side_len):
        self.width = new_side_len
        self.height = new_side_len
        return self.width, self.height
    
    def __str__(self):
        return f"{self.name}(side={self.width})"
