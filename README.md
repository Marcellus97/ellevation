# Assumptions
* Requests can be entered at the same time
* One elevator car
* 10 floors
* did not need to calculate capacity of passengers
* passengers don't request when elevator is on the same floor

       # current_floor = 3, ignore these requests
       3 up
       3 none
       3 down


# Request definition

Requests are entered as follows:

    {desired_floor} {direction}

To simulate an "outside elevator" request:

    2 up
    8 down


Use direction `none` to simulate an "inside elevator" request:

    4 none

# Algorithm used
After some whiteboarding and some research, I decided to implement the "elevator algorithm", otherwise known as a SCAN, which is commonly used by hard disks.

To store incoming requests to the elevator, I used two priority queues implemented by python's `heapq` module:

* requests for floors above the elevator
* requests for floors below the elevator 

For a `request_floor` and the elevator's `current_floor`, we can calculate the priority like this:

    #above
    abs(request_floor - current_floor) 

    #below
    abs(request_floor - current_floor) * -1


I do this so I can continously sweep up and down the elevator shaft, alternating
using both queues

The standard elevator algorithm confirms my assumptions of
"keep going in the same direction, fufilling requests on the way, until we have to reverse"

https://en.wikipedia.org/wiki/Elevator_algorithm


## Optimization
I have included an optimization in my algorithm:

Imagine the elevator is at floor 0, and we receive these requests:

    time    floor   direction
    --------------------------
    0       2       up
    1       8       up
    2       5       down

The elevator is moving up but runs into a down request. We do "fufill" this request (allow the passeger to board), because it is wasteful in capacity.

My algorithm will fufill the request to floor 8, then sweep back down to pickup the passenger at floor 5 



# Consider other options?
My initial thought was to have a main loop and some priority queue.

I was attempting to create some custom ordering function that handles the up and down requests, even when they are above and below the elevator.

This was far too complicated, and after some more thinking, I decided to use two priority queues. One for above and one for below

# New requirements ideas

## Multiple cars
Multiple cars 
I assume one elevator shaft only has one car
    if many cars can be in one elevator shaft, we must limit each car to a set of floors. Car1 has floors 1-5, Car2 has 6-10

Each tick
    for each request incoming request
        match request with closest car (use direction and current_floor)
        add this to elevator's request queue

## Express elevators
Assuming this means some elevators have altered priority, we will need to modify the priorty calculation for each request.

## Service floors
If a floor 5 is a service floor, and can only be accessed througha priveleged request, then we should define a lookup table (dictionary) to store service floors.

In our `assign_request()` function, we should lookup the desired floor, and ignore requests to a service floor, if the request does not have service floor permissions
