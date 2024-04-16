import math


def test_1(arr):
    return list(set(arr))


def test_2(a, b):
    res = []
    for i in range(a, b + 1):
        k = 0
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                k = k + 1
        if k <= 0:
            res.append(i)
    return res


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.hypot(dx, dy)

    def set_coordinates(self, new_coordinates):
        self.x = new_coordinates[0]
        self.y = new_coordinates[1]

    def __str__(self):
        return f'{self.x}, {self.y}'


def test_4(str_arr):
    str_arr.sort(key=lambda i: len(i))
    print(str_arr)
    str_arr.sort(key=lambda i: len(i), reverse=True)
    print(str_arr)

