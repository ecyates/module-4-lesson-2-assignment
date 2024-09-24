# Event Management System Enhancement
# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and 
# a method get_participant_count to retrieve the current count.
import random

class Event:
    '''Each event has a name, date, and a participant count (default=0).'''
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
        
    def add_participant(self):
        '''This function adds a participant to the count'''
        self.participant_count += 1
        return self.participant_count
    
    def get_participant_count(self):
        '''This function retrieves the participant count.'''
        return self.participant_count
    
# Let's create two events
event1 = Event("Townhall", "10/15/2024")
event2 = Event("Mary and Bobby's Wedding", "9/30/2024")
# Let's generate a random number of participants for both events
for i in range(random.randint(0, 500)):
    event1.add_participant()
for j in range(random.randint(0, 500)):
    event2.add_participant()
# Let's capture the new participant counts
e1_participants = event1.get_participant_count()
e2_participants = event2.get_participant_count()
# And report the randomly generated participant counts
print(f"{event1.name} on {event1.date} will have {e1_participants} participants!")
print(f"{event2.name} on {event2.date} will have {e2_participants} participants!")
# We can also compare these and alert the user.
if e1_participants > e2_participants:
    print(f"{event1.name} has more participants than {event2.name}!")
elif e2_participants > e1_participants:
    print(f"{event2.name} has more participants than {event1.name}!")
else: 
    print(f"{event1.name} and {event2.name} have the same number of participants!")
    
