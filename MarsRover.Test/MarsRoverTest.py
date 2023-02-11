import unittest

from MarsRover.Planet.Planet import Planet
from MarsRover.Planet.PlanetBuild import PlanetBuild
from MarsRover.Planet.PlanetStatic import PlanetStatic
from MarsRover.Rover.Position import Position
from MarsRover.Rover.Rover import Rover
from MarsRover.Rover.State import State


class MarsRoverTest(unittest.TestCase):
    world: list = PlanetStatic.mapPlanet
    dimension = Planet.dimension
    grid = PlanetBuild.build(dimension, world)

    position_rover: Position = Planet.findRover(dimension, world)
    rover: Rover = Rover()
    rover.state = State()
    rover.state.position = position_rover
    rover.state.orientation = "S"

    def test_orientaton_left_rover_S_E(self):
        rover: Rover = Rover()
        rover.state = State()
        rover.state.orientation = "S"
        rover.turn_left()

        self.assertLessEqual(rover.state.orientation, "E")

    def test_orientaton_left_rover_N_E_S(self):
        rover: Rover = Rover()
        rover.state = State()
        rover.state.orientation = "N"
        rover.turn_left()

        self.assertLessEqual(rover.state.orientation, "E")
        rover.turn_left()
        self.assertLessEqual(rover.state.orientation, "S")

    def test_orientaton_right_rover_W_S_E(self):
        rover: Rover = Rover()
        rover.state = State()
        rover.state.orientation = "W"
        rover.turn_left()

        self.assertLessEqual(rover.state.orientation, "S")
        rover.turn_left()
        self.assertLessEqual(rover.state.orientation, "E")

    def test_advance_rover(self):
        world: list = PlanetStatic.mapPlanet
        dimension = Planet.dimension
        grid = PlanetBuild.build(dimension, world)

        position_rover: Position = Planet.findRover(dimension, world)
        rover: Rover = Rover()
        rover.state = State()
        rover.state.position = position_rover
        rover.state.orientation = "S"

        rover.advance_N(2, dimension, grid)

        position_Next = Position()
        position_Next.x = 0
        position_Next.y = 2

        self.assertLessEqual(rover.state.position.y, position_Next.y)

    def test_backOff_rover(self):
        world: list = PlanetStatic.mapPlanet
        dimension = Planet.dimension
        grid = PlanetBuild.build(dimension, world)

        position_rover: Position = Planet.findRover(dimension, world)
        rover: Rover = Rover()
        rover.state = State()
        rover.state.position = position_rover
        rover.state.orientation = "E"

        rover.backOff_S(2, dimension, grid)

        position_Next = Position()
        position_Next.x = 2
        position_Next.y = 0

        self.assertLessEqual(rover.state.position.y, position_Next.y)


if __name__ == '__main__':
    unittest.main()