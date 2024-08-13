#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

# Create some visitors and parks
visitor1 = Visitor("Alice")
visitor2 = Visitor("Bob")

park1 = NationalPark("Yellowstone")
park2 = NationalPark("Yosemite")

# Create some trips
trip1 = Trip(visitor1, park1, "2023-08-01", "2023-08-05")
trip2 = Trip(visitor1, park2, "2023-09-10", "2023-09-15")
trip3 = Trip(visitor2, park1, "2023-07-20", "2023-07-25")  

 

# # Test trips method
# print(visitor1.trips())  # Should print a list with trip1 and trip2
# print(visitor2.trips())  # Should print a list with trip3

# # Test national_parks method
# print(visitor1.national_parks())  # Should print a list with park1 and park2
# print(visitor2.national_parks())  # Should print a list with only park1

ipdb.set_trace()
