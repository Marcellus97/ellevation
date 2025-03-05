from elevator import Elevator
from request import Request

class Controller():
    def __init__(self):
        self.time = 0
        # One elevator car with 10 floors
        self.elevator = Elevator(10)
    
    def parse_request(self, request_string) -> Request:
        r :list[str] = request_string.split(' ')
        floor = int(r[0].strip())

        if floor < 0 or floor > self.elevator.size - 1:
            raise Exception(f'{floor} is out of range, max floors is {self.elevator.size}')

        direction = Request.Direction[r[1].strip().upper()]
        return Request(self.time, floor, direction)

    def assign_request(self, request:Request) -> None:
        self.elevator.add_request(request=request)

    def update_elevator(self) -> None:
        self.elevator.move()
        self.elevator.fufill_requests_at_current_floor()
    
    def get_elevator_state(self) -> str:
        return f'time={self.time}, current_floor={self.elevator.currentFloor}, status={self.elevator.status.value}'

    def get_requests_state(self) -> list[tuple[str, str]]:
        requests :list[tuple[int,Request]] = [] + self.elevator.requests_above + self.elevator.requests_below
        requests.sort(key=lambda r:(r[1].time, r[1].floor))
        return [(str(i), str(j)) for i,j in requests]
    
    def tick(self, tick) -> None:
        self.time += tick
    