class Vector:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_z(self):
        return self._z

    def set_x(self, z):
        self._z = z

    def add(self, vector):
        self._x += self._x
        self._y += self._y
        self._z += self._z

    def __str__(self):
        return "Asteroid x {0} y {1} and z {2}".format(
                self._x, self._y, self._z)
