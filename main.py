from api import *

if __name__ == '__main__':
    # town0 = Town(0, 1, 0)
    # town1 = Town(1, 0, 1)
    # town2 = Town(2, -1, 0)
    # town3 = Town(3, 0, -1)
    #
    # towns = [town1, town2, town3]

    # town0 = Town(0, 1, 0)
    # town1 = Town(1, 0, 1)
    # town2 = Town(2, -1, 0)
    # town3 = Town(3, -0.5, -1)
    # town4 = Town(4, 0.5, -1)
    #
    # towns = [town1, town2, town3, town4]

    town0 = Town(0, 1, 0)
    town1 = Town(1, 1, 1)
    town2 = Town(2, -1, 1)
    town3 = Town(3, -1.5, 1.5)
    town4 = Town(4, -2, 1)
    town5 = Town(5, -1.5, -1)
    town6 = Town(6, 0.5, -1)

    towns = [town1, town2, town3, town4, town5, town6]

    map = Map(town0, [], towns)
    algo = Algo(map)
    algo.do(0)

