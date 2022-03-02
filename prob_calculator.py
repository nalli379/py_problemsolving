import random
import copy

class Hat():
    #variable number of arguments for input - unpack dictionary into list
    def __init__(self, **kwargs):
        self.name = type(self).__name__
        self.contents = [k for k, v in kwargs.items() for i in range(v)]
   
    def draw(self, num):
        #if num of balls to draw exceeds the available quantity, return all the balls.
        if num >= len(self.contents):
            return self.contents
        else: 
            #This method accepts argument and remove balls at random if num is less than contents 
            random_draw = []
            for i in range(num):
                random_ball = self.contents.pop(random.randrange(len(self.contents)))
                random_draw.append(random_ball)
            #drawn balls returned as a list of strings
            return random_draw
                 
    def __repr__(self):
        return f"{self.name}: {self.contents}"
    
    def __str__(self):
        return f"{self.name}: {self.contents}"


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    #if number of balls drawn is larger than hat contents, return 0
    if num_balls_drawn > len(hat.contents):
        return 0
    
    #list of expected balls
    expected_balls_list = [k for k, v in expected_balls.items() for i in range(v)]
    
    #if expected balls not in hat return 0
    if not all(ball in hat.contents for ball in expected_balls_list):
        return 0
    
    else:
        #count match between expected balls and draw per loop
        match_count = 0
        #using a copy of hat with draw method
        for i in range(num_experiments):
            hat_copy = copy.deepcopy(hat)
            draw = hat_copy.draw(num_balls_drawn)
            #using set to count ball colour types to compare list counts
            ball_types = set(expected_balls_list)
        
            count = len(ball_types)
            match = 0
            #if the count for number of balls per category is true, then a match count += 1
            for ball in ball_types:
                if expected_balls_list.count(ball) <= draw.count(ball):
                    match += 1
             
            if match == count:
                match_count +=1
                
    return match_count / num_experiments
