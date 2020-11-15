class node:
    def __init__(self, x, y, time2reach = -1, tick=-1, reached = False):
        self.x = x
        self.y= y
        self.time2reach = time2reach
        self.path = None
        self.reached = reached # indicate if the cell has already been reached
        self._tick = tick
    def __str__(self):
        return f'Cell x:{self.x} y:{self.y} {"Reached" if self.reached else "Not reached"}'


    
        
    
    
