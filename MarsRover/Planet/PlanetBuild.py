from typing import List

from MarsRover.Planet.Dimension import Dimension
from MarsRover.Planet.Obstacle.Box import Box
from MarsRover.Planet.Obstacle.Coline import Coline
from MarsRover.Planet.Obstacle.Obstacle import Obstacle
from MarsRover.Planet.Obstacle.Rock import Rock
from MarsRover.Rover.Position import Position
from MarsRover.Rover.Rover import Rover


class PlanetBuild:

    def build(dimension: Dimension, world: List) -> List:
        listG = []
        for x in range(dimension.width+1):
            listL = []
            for y in range(dimension.height+1):
                builder = {}
                #print(x,y)
                position = Position()
                position.x = x
                position.y = y
                if world[x][y] == Rover:
                    rover = Rover()
                    key, value = position, rover
                    builder[key] = value
                    listL.append(builder)
                elif world[x][y] == Box or world[x][y] == Coline or world[x][y] == Rock:
                    obstacle: Obstacle = world[x][y]
                    key, value = position, obstacle
                    builder[key] = value
                    listL.append(builder)
                elif world[x][y] == None:
                    key, value = position, None
                    builder[key] = value
                    listL.append(builder)
                #print(position.x,position.y,world[x][y])
            listG.append(listL)
        #print("T:", listG)
        return listG
