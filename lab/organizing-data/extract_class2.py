# by Kami Bigdely
# Extract class

class Person:
    def __init__(self, full_name, birth_year, email, movies=[]):
        self.full_name = full_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email)

full_names = ['Elizabeth Debicki', 'Jim Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
email = ['deb@makeschool.com', 'jim@makeschool.com']
    
for i, value in enumerate(email):
    person = Person(full_names[i], birth_year[i], email[i], movies[i])

    if birth_year[i] > 1985:
        print(full_names[i])
        print('Movies Played: ', end='')
        for m in person.movies:
            print(m, end=', ')
        print()
        person.send_hiring_email()