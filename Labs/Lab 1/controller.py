import random
import time
from datetime import datetime
from asteroid import Asteroid

class Controller:
    """this class contains a method to create asteroids to a list"""
    def __init__(self):
        """
        creates 100 asteroids and assigns a random position and velocity
        """
        self.asteroids_list = [None] * 100

        for x in range(100):
            self.asteroids_list[x] = Asteroid(random.randint(1,4),
                                                (random.randint(0,100), random.randint(0, 100), random.randint(0, 100)),
                                                (random.randint(0,5), random.randint(0, 5), random.randint(0, 5)),
                                                time.time())


    def simulate(self, seconds):
        """
        This function will simulate asteroids moving for a certain amount of seconds specified
        :param seconds:
        :return:
        """
        i = 0

        while i < seconds:
            j = 0
            print(self.asteroids_list[0])
            while j < 99:
                self.asteroids_list[j].move()
                j += 1
            time.sleep(1)
            i += 1

def main():
    test = Controller()
    test.simulate(12)


if __name__ == "__main__":
    main()










