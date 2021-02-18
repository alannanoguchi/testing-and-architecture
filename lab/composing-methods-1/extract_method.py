# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

# def print_stat():
#     grade_list = []
#     # Get the inputs from the user
#     n_student = 5
#     for _ in range(0, n_student):
#         grade_list.append(int(input('Enter a number: ')))

#     # Calculate the mean and standard deviation of the grades
#     sum = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
#     for grade in grade_list:
#         sum = sum + grade
#     mean = sum / len(grade_list)
#     sd = 0 # standard deviation
#     sum_of_sqrs = 0
#     for grade in grade_list:
#         sum_of_sqrs += (grade - mean) ** 2
#     sd = math.sqrt(sum_of_sqrs / len(grade_list))
#     # print out the mean and standard deviation in a nice format.
#     print('****** Grade Statistics ******')
#     print("The grades's mean is:", mean)
#     print('The population standard deviation of grades is: ', round(sd, 3))
#     print('****** END ******')

# print_stat()

class Grades:
    def __init__(self, student_grades = []):
        self.grade_list = []

        for grade in student_grades:
            self.grade_list.append(grade)

    def user_grades(self):
        """Get the inputs from the user."""
        n_students = 5
        for _ in range(0, n_students):
            grade = int(input('Enter a number: '))
            self.grade_list.append(grade)
        return self.print_stat()

    def calc_mean(self):
        """Calculate the mean of the grades. """
        total = 0

        for grade in self.grade_list:
            total += grade

        return total / len(self.grade_list)

    def calc_sd(self, mean):
        """Calculate the standard deviation of the grades."""
        sum_of_sqrs = 0

        for grade in self.grade_list:
            sum_of_sqrs += (grade - mean) ** 2

        return math.sqrt(sum_of_sqrs / len(self.grade_list))

    def print_stat(self):
        """Print out the mean and standard deviation in a nice format."""
        mean = self.calc_mean()
        sd = self.calc_sd(mean)

        print('****** Grade Statistics ******')
        print("The grades's mean is:", mean)
        print('The population standard deviation of grades is: ', round(sd, 3))
        print('****** END ******')

Grades().user_grades()





