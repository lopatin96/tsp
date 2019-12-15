import math
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np


class Town:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.position = (x, y)

    def __str__(self):
        return f'id: {self.idx}: x: {self.position[0]}, y: {self.position[1]};'

    def distance(self, other_town):
        return math.sqrt(
            math.pow((other_town.position[0] - self.position[0]), 2) + math.pow(
                (other_town.position[1] - self.position[1]), 2))


class Map:
    def __init__(self, start_town, current_path, towns):
        self.start_town = start_town
        self.current_path = current_path
        self.towns = towns

    def __str__(self):
        result = 'current path:\n'
        result += str(self.start_town) + '\n'
        for town in self.current_path:
            result += str(town) + '\n'
        result += '\nOther maps:\n'
        for town in self.towns:
            result += str(town) + '\n'
        return result

    def add_town_to_current(self, town):
        self.towns.remove(town)
        self.current_path.append(town)

    def calculate_current_path(self):
        x = 0
        for idx in range(len(self.current_path)):
            if idx == 0:
                x = self.start_town.distance(self.current_path[0])
            else:
                x += self.current_path[idx - 1].distance(self.current_path[idx])
        return x

    def find_minimum_spanning_tree(self):
        towns = list()
        towns.append(self.start_town)
        for town in self.towns:
            towns.append(town)
        x = np.zeros((len(towns), len(towns)))
        for i, town1 in enumerate(towns):
            for j, town2 in enumerate(towns):
                x[i][j] = town1.distance(town2)
        tcsr = minimum_spanning_tree(x)
        return np.sum(tcsr.toarray().astype('double'))

    def branch_and_bound(self):
        return self.calculate_current_path() + self.find_minimum_spanning_tree()

    def path(self):
        result = ''
        for town in self.current_path:
            result += str(town.idx) + ' -> '
        return result[:-4]


class Algo:
    def __init__(self, map):
        self.init(map)

    def init(self, map):
        self.maps = [Map(map.start_town, map.current_path[:], map.towns[:]) for _ in map.towns]

    def do(self, level):
        # print('level', level)
        # print(self.maps)

        if len(self.maps) == 1:  # results
            print('sd', self.maps[0].current_path)
            print(self.maps[0].path())

        score = 100000000
        for idx, map in enumerate(self.maps):
            map.add_town_to_current(map.towns[idx])

        maps_to_delete = []
        for map in self.maps:
            if score >= map.branch_and_bound():
                # print(map.branch_and_bound())
                score = map.branch_and_bound()
            else:
                maps_to_delete.append(map)

        maps = [m for m in self.maps if m not in maps_to_delete]

        for map in maps:
            algo = Algo(map)
            algo.do(level+1)

