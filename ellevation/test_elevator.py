import unittest 
from controller import Controller
from elevator import Elevator
from request import Request

class TestElevator(unittest.TestCase):

    def test_init(self):
        controller = Controller()
        self.assertEqual(0, controller.elevator.currentFloor)
        self.assertEqual(Elevator.Status.IDLE, controller.elevator.status)

    def test_move_up(self):
        controller = Controller()
        controller.assign_request(Request(0, 2, Request.Direction.UP))
        self.assertEqual(0, controller.elevator.currentFloor)

        controller.tick(1)
        controller.update_elevator()

        self.assertEqual(1, controller.elevator.currentFloor)
        self.assertEqual(Elevator.Status.MOVING_UP, controller.elevator.status)
        controller.tick(2)
        controller.update_elevator()

        self.assertEqual(2, controller.elevator.currentFloor)
        self.assertEqual(Elevator.Status.IDLE, controller.elevator.status)


    def test_move_up_and_down(self):
        controller = Controller()
        controller.assign_request(Request(0, 8, Request.Direction.UP))
        controller.assign_request(Request(0, 4, Request.Direction.DOWN))

        controller.tick(8)
        for i in range(8):
            controller.update_elevator()

        self.assertEqual(8, controller.elevator.currentFloor)
        self.assertEqual(Elevator.Status.MOVING_DOWN, controller.elevator.status)

        controller.tick(5)
        for i in range(5):
            controller.update_elevator()

        self.assertEqual(4, controller.elevator.currentFloor)
        self.assertEqual(Elevator.Status.IDLE, controller.elevator.status)

if __name__ == '__main__':
    unittest.main() 

