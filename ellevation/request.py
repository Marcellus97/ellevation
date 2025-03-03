from enum import Enum

class Request():

    class Direction(Enum):
        UP = 'up'
        DOWN = 'down'
        NONE = 'none'
    
        def __str__(self):
            return str(self.value)


    def __init__(self, time: int, floor :int, direction :Direction):
        self.time: int = time
        self.floor: int = floor
        self.direction: Request.Direction = direction
    
    def __str__(self):
        return f'time={self.time}, destination_floor={self.floor}, direction={self.direction}'

