# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18
class Person:
    def __init__(self, my_age):
        self.age = my_age
        
def enter_night_club(individual):
    if individual.age > LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denied.")

# def older_than_18_year_old(age):
#     if age > LEGAL_DRINKING_AGE:
#         return True
#     else: 
#         return False
    
    
person = Person(17.9)
person2 = Person(21)
enter_night_club(person)
enter_night_club(person2)
        
