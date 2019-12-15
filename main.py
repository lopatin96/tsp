from api import *

if __name__ == '__main__':
    # town0 = Town(0, 1, 0)
    # town1 = Town(1, 0, 1)
    # town2 = Town(2, -1, 0)
    # town3 = Town(3, 0, -1)
    #
    # towns0 = [town1, town2, town3]

    town0 = Town(0, 1, 0)
    town1 = Town(1, 0, 1)
    town2 = Town(2, -1, 0)
    town3 = Town(3, -0.5, -1)
    town4 = Town(4, 0.5, -1)

    towns0 = [town1, town2, town3, town4]


    map = Map(town0, [], towns0)
    algo = Algo(map)
    algo.do(0)

