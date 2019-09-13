import time
from datetime import datetime


class Asteroid:
    """This class embodies the basic functions and attributes of an Asteroid"""

    id = 1

    def __init__(self, radius, position, velocity, timestamp):
        """
        Initialize radius, position, velocity, timestamp
        :param radius: an int
        :param position: an int
        :param velocity: an int
        :param timestamp: an int
        """
        self._meters = radius
        self._position = position
        self._velocity = velocity
        self._timestamp = timestamp
        self._id = Asteroid.id
        Asteroid.id += 1

    # @classmethod
    # def id(cls):
    #     cls.id += 1
    #     return id

    def get_radius(self):
        return self._meters

    def set_radius(self, meters):
        self._meters = meters

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_velocity(self):
        return self._velocity

    def set_velocity(self, velocity):
        self._velocity = velocity

    def get_timestamp(self):
        return self._timestamp

    def set_timestamp(self, timestamp):
        self._timestamp = timestamp

    def set_pos(self, x, y, z):
        self._position = (x, y, z)

    def move(self):
        """
        Modifies position using velocity by adding x,y,z coordinates to initial position
        :return: new position with added velocity
        """
        current_pos = self.get_position()
        current_vel = self.get_velocity()

        self.set_pos(current_pos[0] + current_vel[0], current_pos[1] + current_vel[1],
                     current_pos[2] + current_vel[2])

    def __str__(self):
        return "Asteroid meters: {0}, position: {1} and velocity is: {2} and timestamp: {3}, id: {4}".format(
            self._meters, self._position, self._velocity, self._timestamp, self._id)


def main():
    testAsteroid = Asteroid(12, (80, 0, 0), (1, 1, 1), time.time())
    print(testAsteroid)
    testAsteroid.move()
    print(testAsteroid)


if __name__ == "__main__":
    main()
