class Car:
    def __init__(self, name, model, release_date, speed=0):
        self.__name = name
        self.__model = model
        self.__release_date = release_date
        self.__speed = speed

    def speed_up(self, up=5):
        self.__speed = self.__speed + up
        return self.__speed

    def speed_down(self, down=5):
        self.__speed = self.__speed - down
        return self.__speed

    def speed_stop(self):
        self.__speed -= self.__speed
        return self.__speed

    def speed_info(self):
        print(self.__speed)

    def speed_reverse(self):
        self.__speed = self.__speed - (self.__speed * 2)
        return self.__speed

Car1 = Car('Ferrari','Berlinetta', 2010)
Car1.speed_up()
Car1.speed_up()
Car1.speed_up()
Car1.speed_up()
Car1.speed_down()
Car1.speed_info()
Car1.speed_reverse()
Car1.speed_info()