from elevator import Elevator
from request import Request
from controller import Controller

# Create our list of elevators
# lets define one with ten floors as defined in the problem

# One car with 10 floors

command_string = """
    --- Commands ---
    "commands" to show command list
    "stop" to stop polling
    "state" to show current elevator state
    "reqstate" to begin a request sequence
    "format" 'floor' 'direction'
    "begin" to begin a request sequence
    "done" to end a request sequence
"""

#init our elevator controller
controller = Controller()

def main():

    print('Starting elevator service... \n')
    print(controller.get_elevator_state())
    while True:

        command = input()
        if command == 'commands':
            print(command_string)
        elif command == 'stop':
            print('Stopping elevator service... \n')
            break
        elif command == 'state':
            print(controller.get_elevator_state())
        elif command == 'reqstate':
            for state in controller.get_requests_state():
                print(state)
        elif command == 'begin':
            request_poll()
            print(controller.get_elevator_state())
        elif command == '':
            controller.tick(1)
            controller.update_elevator()
            print(controller.get_elevator_state())


def request_poll():
    print('starting request...')
    while True:
        user_input = input()
        if user_input == 'done':
            break
        try:
            new_request = controller.parse_request(user_input)
            controller.assign_request(new_request)
        except (Exception) as error:
            print(f'--- Error! Request could not be parsed --- {error.args}') 

if __name__ == '__main__':
    main()