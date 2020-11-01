import datetime


class University:

    def __init__(self, name, students, teachers):
        self.__name = name
        self.__students = students
        self.__teachers = teachers
        print(f'In {name} {students} students and {teachers} teachers')

    def setname(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print('Error')

    def getname(self):
        return self.__name

    def setteachers(self, teachers):
        if isinstance(teachers, int):
            self.__teachers = teachers
        else:
            print('Error')

    def getteachers(self):
        return self.__teachers

    def gender_of_students(self):
        girls = round(self.__students * 0.63)
        boys = self.__students - girls
        print(f'Girls in university about: {girls}')
        print(f'Boys in university about: {boys}')

    def professors_in_teachers(self):
        professors = round(self.__teachers * 0.32)
        docents = round(self.__teachers * 0.45)
        methodists = self.__teachers - (professors + docents)
        print(f'Methodists in university: {methodists}')

# U1 = University('MSLU', 7653, 1010)
# U1.gender_of_students()
# U1.professors_in_teachers()


class Smartphone:
    def __init__(self, name, release_year, price):
        self.__name = name
        self.release_year = release_year
        self.__price = price
        print(f'{name} was released in {release_year} for {price} USD')

    def setname(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print('Error')

    def getname(self):
        return self.__name

    def setprice(self, price):
        if isinstance(price, int):
            self.__price = price
        else:
            print('Error')

    def getprice(self):
        return self.__price

    def black_friday(self):
        new_price = self.__price * 0.30
        print(f'Акция: {self.__name} за {new_price} USD!')

    def years_old(self):
        years_old = datetime.date.today() - self.release_year
        print(f'{years_old} in sold')

# S1 = Smartphone('Samsung', datetime.date(2020,10,10), 45)
# S1.years_old()
# S1.setname(123)
# print(S1.getname())
# S1.setprice(100.5)
# print(S1.getprice())
# S1.black_friday()


class Earth:
    def __init__(self, population, total_of_countries, world_wars_old):
        self.__population = population * 1000000000
        self.__total_of_countries = total_of_countries
        self.__world_wars_old = world_wars_old
        print(f'Our planet has about {self.__population} peoples and {self.__total_of_countries} countries.\n'
              f'Second World War was beginning in {self.__world_wars_old}')

    def set_population(self, population):
        if isinstance(population, int) or isinstance(population, float):
            self.__population = population
        else:
            print('Error! Population mast be "int"')

    def get_population(self):
        return self.__population

    def set_world_wars_old(self, date):
        if isinstance(date, datetime.date) and date <= datetime.date.today():
            self.__world_wars_old = date
        else:
            print('Error! Wrong date')

    def get_world_wars_old(self):
        return self.__world_wars_old

    def world_wars_old(self):
        how_old = datetime.date.today() - self.__world_wars_old
        print(f'С момента начала войны прошло: {how_old}')

    def population_gender(self):
        woman = self.__population * 0.54
        man = self.__population - woman
        print(f'Population is about{woman} woman and about{man} man')

# E1 = Earth(9.653, 192, datetime.date(1939,9,1))
# E1.world_wars_old()
# E1.set_world_wars_old(datetime.date(2021,11,2))
# print(E1.get_world_wars_old())
# E1.world_wars_old()
