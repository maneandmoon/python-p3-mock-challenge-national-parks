class NationalPark:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if(not hasattr(self, 'name') and isinstance(new_name, str) and len (new_name) >= 3):
            self._name= new_name
        # else:
        #     raise ValueError('name has already been created') 


    def trips(self):
        # matching_trips = []
        # for trip in Trip.all:
        #     if(trip.national_park == self):
        #         matching_trips.append(trip)
        #     return matching_trips    
        return [trip for trip in Trip.all if trip.national_park == self]
    
    #appending trips that match current national_park aka self
    #     return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set(trip.visitor for trip in self.trips()))
    
    #find all relevant trips and extract spec. the visitor trips
    # we have relevant trips from the def trips(self) so we can iterate over it 
    #by accessing the instance method
    # for trip in self.trips() leave trip.visitor
    #want it to be unique so use set then list
    
    def total_visits(self):
        #find all trips for current natl park (self)
        # return len(self.trips())
        if(len(self.trips()) == 0):
            return 0
        else:
            return len(self.trips())
    
    def best_visitor(self):
        greatest_visitor= None
        greatest_visitor_count = 0

        for cur_visitor in self.visitors():
            cur_count = 0
            for trip in self.trips():
                if trip.visitor == cur_visitor:
                    cur_count += 1
                if(cur_count > greatest_visitor_count):
                    greatest_visitor_count = cur_count
                    greatest_visitor = cur_visitor
        return greatest_visitor

     
        # visits = {}
        # for trip in self.trips():
        #     if trip.visitor not in visits:
        #         visits[trip.visitor] = 0
        #     visits[trip.visitor] += 1
        # if not visits:
        #     return None    
        # return max(visits, key=visits.get)

#get all trips to current park (self.trips())
#get all unique visitors to park (self.visitors())
#could use a dictionary but instance can't be instance of class


    def __repr__(self):
        return f"NationalPark(name={self._name})"

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    #   Trip.all.append(self)

    # # Property getters and setters for start_date and end_date
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value
        # else: 
        #     raise ValueError("Start date must be a string with at least 7 characters.")

    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
           self._end_date = value    
        # else:
        #      raise ValueError("End date must be a string with at least 7 characters.")   
    
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, new_visitor):
        if(isinstance(new_visitor, Visitor)):
            self._visitor = new_visitor

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, new_national_park):
        if(isinstance(new_national_park, NationalPark)):
            self._national_park = new_national_park

    def __repr__(self):
        return f'<Trip start={self.start_date} end={self.end_date} park={self.national_park.name} visitor={self.visitor.name} />'

class Visitor:
    def __init__(self, name):
        self.name = name

    def trips(self):
        #look through all the trips (Trip.all)
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        # parks = [trip.national_park for trip in self.trips()]
        # return list(set(parks))
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        # pass
        if not isinstance(park, NationalPark):
            raise TypeError("Argument must be a NationalPark.")
        return sum(1 for trip in self.trips() if trip.national_park == park)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if(isinstance(new_name, str) and 1 <= len(new_name) <= 15):
            self._name = new_name
        # else:
        #     raise ValueError("Name must be string of length 1-15")

    def __repr__(self):
        return f'<Visitor name={self.name} />'        
        
