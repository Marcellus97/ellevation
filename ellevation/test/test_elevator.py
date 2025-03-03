import unittest 
from controller import Controller
from elevator import Elevator

class TestElevator(unittest.TestCase):

    def test_basic_case(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main() 


def test_init(self):
    controller = Controller()
    self.assertEquals(self, 0, controller.elevator.currentFloor)
    self.assertEquals(Elevator.Status.IDLE, controller.elevator.status)
