from typing import List

from MarsRover.Planet.Dimension import Dimension
from MarsRover.Planet.Obstacle.Box import Box
from MarsRover.Planet.Obstacle.Coline import Coline
from MarsRover.Planet.Obstacle.Rock import Rock
from MarsRover.Rover.Orientation import Orientation
from MarsRover.Rover.Position import Position
from MarsRover.Rover.State import State


class Rover:
    def __int__(self, s: State):
        self.state = s

    def canMove(self, grid: List, dimension: Dimension) -> bool:
        if self.state.orientation == Orientation.N:
            position_Next = Position()
            position_Next.x = self.state.position.x
            position_Next.y = self.state.position.y + 1
            if position_Next.y <= dimension.height:
                if next(iter(grid[position_Next.x][position_Next.y].values())) == Box or next(iter(grid[position_Next.x][position_Next.y].values())) == Coline or next(iter(grid[position_Next.x][position_Next.y].values())) == Rock:
                    print("Obstacle in front")
                    return False
        if self.state.orientation == Orientation.S:
            position_Next = Position()
            position_Next.x = self.state.position.x
            position_Next.y = self.state.position.y - 1
            if position_Next.y >= 0:
                if next(iter(grid[position_Next.x][position_Next.y].values())) == Box or next(iter(grid[position_Next.x][position_Next.y].values())) == Coline or next(iter(grid[position_Next.x][position_Next.y].values())) == Rock:
                    print("Obstacle in front")
                    return False
        if self.state.orientation == Orientation.E:
            position_Next = Position()
            position_Next.x = self.state.position.x - 1
            position_Next.y = self.state.position.y
            if position_Next.x >= 0:
                if next(iter(grid[position_Next.x][position_Next.y].values())) == Box or next(iter(grid[position_Next.x][position_Next.y].values())) == Coline or next(iter(grid[position_Next.x][position_Next.y].values())) == Rock:
                    print("Obstacle in front")
                    return False
        if self.state.orientation == Orientation.W:
            position_Next = Position()
            position_Next.x = self.state.position.x + 1
            position_Next.y = self.state.position.y
            if position_Next.x <= dimension.width:
                if next(iter(grid[position_Next.x][position_Next.y].values())) == Box or next(iter(grid[position_Next.x][position_Next.y].values())) == Coline or next(iter(grid[position_Next.x][position_Next.y].values())) == Rock:
                    print("Obstacle in front")
                    return False
        return True

    def canMove_Back(self, grid: List, dimension: Dimension) -> bool:
        if self.state.orientation == Orientation.N:
            position_Next = Position()
            position_Next.x = self.state.position.x
            position_Next.y = self.state.position.y - 1
            if position_Next.y >= 0:
                if next(iter(grid[position_Next.x][position_Next.y].values())) == Box or next(iter(grid[position_Next.x][position_Next.y].values())) == Coline or next(iter(grid[position_Next.x][position_Next.y].values())) == Rock:
                    print("Obstacle in front")
                    return False
        if self.state.orientation == Orientation.S:
            position_Next = Position()
            position_Next.x = self.state.position.x
            position_Next.y = self.state.position.y + 1
            if position_Next.y <= dimension.height:
                if next(iter(grid[position_Next.x][position_Next.y].values())) == Box or next(iter(grid[position_Next.x][position_Next.y].values())) == Coline or next(iter(grid[position_Next.x][position_Next.y].values())) == Rock:
                    print("Obstacle in front")
                    return False
        if self.state.orientation == Orientation.E:
            position_Next = Position()
            position_Next.x = self.state.position.x + 1
            position_Next.y = self.state.position.y
            if position_Next.x <= dimension.width:
                if next(iter(grid[position_Next.x][position_Next.y].values())) == Box or next(iter(grid[position_Next.x][position_Next.y].values())) == Coline or next(iter(grid[position_Next.x][position_Next.y].values())) == Rock:
                    print("Obstacle in front")
                    return False
        if self.state.orientation == Orientation.W:
            position_Next = Position()
            position_Next.x = self.state.position.x - 1
            position_Next.y = self.state.position.y
            if position_Next.x >= 0:
                if next(iter(grid[position_Next.x][position_Next.y].values())) == Box or next(iter(grid[position_Next.x][position_Next.y].values())) == Coline or next(iter(grid[position_Next.x][position_Next.y].values())) == Rock:
                    print("Obstacle in front")
                    return False
        return True

    def advance_N(self, delta: int, dimension_planet: Dimension, grid: List) -> State:

            # move forward while being on the edge of the toroidal planet
            if delta > 0 and self.canMove(grid, dimension_planet):
                if self.state.orientation == "N":
                    if self.state.position.y == dimension_planet.height or (self.state.position.y + delta) > dimension_planet.height:
                        self.state.position.y = 0
                    elif (self.state.position.y + delta) <= dimension_planet.height:
                        self.state.position.y = self.state.position.y + delta

                if self.state.orientation == "S":
                    if self.state.position.y == 0 or (self.state.position.y - delta) < 0:
                        self.state.position.y = dimension_planet.height
                    elif (self.state.position.y - delta) >= 0:
                        self.state.position.y = self.state.position.y - delta

                if self.state.orientation == "E":
                    if self.state.position.x == 0 or (self.state.position.x - delta) < 0:
                        self.state.position.x = dimension_planet.width
                    elif (self.state.position.x - delta) >= 0:
                        self.state.position.x = self.state.position.x - delta

                if self.state.orientation == "W":
                    if self.state.position.y == dimension_planet.width or (self.state.position.x + delta) > dimension_planet.width:
                        self.state.position.x = 0
                    elif (self.state.position.x + delta) <= dimension_planet.width:
                        self.state.position.x = self.state.position.x + delta
            return self.state

    def backOff_S(self, delta: int, dimension_planet: Dimension, grid: List) -> State:
        # move backwards while on the edge of the toroidal planet
        if delta > 0 and self.canMove_Back(grid, dimension_planet):
            if self.state.orientation == "S":
                if self.state.position.y == dimension_planet.height or (self.state.position.y + delta) > dimension_planet.height:
                    self.state.position.y = 0
                elif (self.state.position.y + delta) <= dimension_planet.height:
                    self.state.position.y = self.state.position.y + delta

            if self.state.orientation == "N":
                if self.state.position.y == 0 or (self.state.position.y - delta) < 0:
                    self.state.position.y = dimension_planet.height
                elif (self.state.position.y - delta) >= 0:
                    self.state.position.y = self.state.position.y - delta

            if self.state.orientation == "W":
                if self.state.position.x == 0 or (self.state.position.x - delta) < 0:
                    self.state.position.x = dimension_planet.width
                elif (self.state.position.x - delta) >= 0:
                    self.state.position.x = self.state.position.x - delta

            if self.state.orientation == "E":
                if self.state.position.y == dimension_planet.width or (self.state.position.x + delta) > dimension_planet.width:
                    self.state.position.x = 0
                elif (self.state.position.x + delta) <= dimension_planet.width:
                    self.state.position.x = self.state.position.x + delta
        return self.state

    def turn_left(self) -> State:
        if self.state.orientation == "N":
            self.state.orientation = "E"
            return self.state
        if self.state.orientation == "S":
            self.state.orientation = "E"
            return self.state
        if self.state.orientation == "E":
            self.state.orientation = "S"
            return self.state
        if self.state.orientation == "W":
            self.state.orientation = "N"
            return self.state

    def turn_right(self) -> State:
        if self.state.orientation == "N":
            self.state.orientation = "W"
            return self.state
        if self.state.orientation == "S":
            self.state.orientation = "W"
            return self.state
        if self.state.orientation == "E":
            self.state.orientation = "N"
            return self.state
        if self.state.orientation == "W":
            self.state.orientation = "S"
            return self.state



