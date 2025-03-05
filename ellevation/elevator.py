from enum import Enum
from request import Request
import heapq
# using a heapq as a priority queueu because we don't need thread saftey
# and we want to have fast inserts and deletes while preserving
# sorted (priority) order

class Elevator():
    class Status(Enum):
        MOVING_UP = 'moving_up'
        MOVING_DOWN = 'moving_down'
        IDLE = 'idle'

    def __init__(self, size) -> None:
        self.size : int = size
        self.currentFloor : int = 0
        self.status = Elevator.Status.IDLE

        # for speedy lookup
        self.requests_above: list[tuple[int, Request]] = list()
        heapq.heapify(self.requests_above)
        self.requests_below: list[tuple[int, Request]] = list()
        heapq.heapify(self.requests_below)

    def add_request(self, request:Request) -> None:
        if request.floor > self.currentFloor:
            #start the elevator if needed
            if self.status == Elevator.Status.IDLE:
                self.status = Elevator.Status.MOVING_UP
            # above should ascending order
            priority = request.floor - self.currentFloor
            prioritized_request = (priority, request)
            heapq.heappush(self.requests_above, prioritized_request)
        elif request.floor < self.currentFloor:
            #start the elevator if needed
            if self.status == Elevator.Status.IDLE:
                self.status = Elevator.Status.MOVING_DOWN
            # below should descending order, so we reverse the sign of the floor priority
            priority = self.currentFloor - request.floor
            prioritized_request = (priority, request)
            heapq.heappush(self.requests_below, prioritized_request)
        else:
            pass # ignore if we are on the same floor
    
    # on update is called after traversing each floor
    def fufill_requests_at_current_floor(self) -> None:
        if self.status == Elevator.Status.MOVING_UP:
           self.fufill_requests_moving_up()
        elif self.status == Elevator.Status.MOVING_DOWN:
           self.fufill_requests_moving_down() 
        # stop if needed
        if len(self.requests_below) == 0 and len(self.requests_above) == 0:
            self.status = Elevator.Status.IDLE

    def fufill_requests_moving_up(self):
        while True:
            #start the elevator if stopped
            if len(self.requests_above) == 0:
                if (len(self.requests_below) == 0):
                    self.status = Elevator.Status.IDLE
                else:
                    self.status = Elevator.Status.MOVING_DOWN
                break
        # we can safely assume this is the smallest in the heap (our list)
            next = self.requests_above[0]
        # are we looking at the current floor? if not, do nothing
            if next[1].floor != self.currentFloor:
                break
            self.pop_request_and_optimize_moving_up()

    def fufill_requests_moving_down(self):
        while True:
            if len(self.requests_below) == 0:
                if (len(self.requests_above) == 0):
                    self.status = Elevator.Status.IDLE
                else:
                    self.status = Elevator.Status.MOVING_UP
                # reverse direction
                break

            next = self.requests_below[0]
            if next[1].floor != self.currentFloor:
                break
            self.pop_request_and_optimize_moving_down()


    def pop_request_and_optimize_moving_up(self):
        removed :tuple[int, Request] = heapq.heappop(self.requests_above)
        #optimization, pick them up on the way down
        if removed[1].direction == Request.Direction.DOWN and len(self.requests_above) > 0:
            # reverse sign for priority
            below_request = (removed[0] * -1, removed[1])
            heapq.heappush(self.requests_below, below_request)
        else:
            print('request fufilled')



    def pop_request_and_optimize_moving_down(self):
        removed :tuple[int, Request] = heapq.heappop(self.requests_below)
        #optimization, pick them up on the way down
        if removed[1].direction == Request.Direction.UP and len(self.requests_below) > 0:
            above_request = (removed[0] * -1, removed[1])
            heapq.heappush(self.requests_above, above_request)
        else:
            print('request fufilled')


    def move(self):
        if self.status == Elevator.Status.IDLE:
            return
        elif self.status == Elevator.Status.MOVING_UP:
            self.currentFloor += 1
        else:
            self.currentFloor -= 1
