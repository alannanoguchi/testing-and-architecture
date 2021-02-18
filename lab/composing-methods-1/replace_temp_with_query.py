# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.
class Employer:    

    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:

    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:

    def __init__(self, students) -> None:
        self.students = students
        

    def process_graduation(self):
        """Find the students in the school who have successfully graduated."""
        passing_student = self.passing_students()

        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in passing_student:
            s.send_congrat_email()
            print(s.name)
        print('****************************')

        
    def passing_students(self):
        '''Return all of the passing students.'''
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
        return passed_students
        
    def find_top_ten(self, passing_student):
        # Find the top 10% of them 
        passing_student.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passing_student))
        return passing_student[index:]
        # return top_10_percent

    def send_employee_referral(self, top_employers, top_10_percent):
        '''Send contact email to top employeers.'''
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

students = [Student(2.1, 'Pinocchio'), Student(2.3, 'goku'), Student(2.7, 'toro'), 
            Student(3.9, 'naruto'), Student(3.2,'kami'), Student(3,'guts')]
school  = School(students)
school.process_graduation()