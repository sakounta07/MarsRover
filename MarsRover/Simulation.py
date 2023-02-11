from typing import List

from MarsRover.Planet.Planet import Planet
from MarsRover.Planet.PlanetBuild import PlanetBuild
from MarsRover.Planet.PlanetStatic import PlanetStatic
from MarsRover.Rover.Position import Position
from MarsRover.Rover.Rover import Rover
from MarsRover.Rover.State import State


class Simulation:
    world: List = PlanetStatic.mapPlanet
    dimension = Planet.dimension
    grid: List = PlanetBuild.build(dimension, world)

    position_rover: Position = Planet.findRover(dimension, world)
    rover: Rover = Rover()
    rover.state = State()
    rover.state.position = position_rover
    rover.state.orientation = "N"
    #rover.turn_left()
    print("H: ", dimension.height)
    rover.advance_N(1, dimension,grid)
    print("** Orientation Rover: ", rover.state.orientation)
    print("*** Position Rover: (", rover.state.position.x, ",", rover.state.position.y, ")")
    rover.turn_right()
    rover.advance_N(1, dimension,grid)
    print("** Orientation Rover: ", rover.state.orientation)
    print("*** Position Rover: (", rover.state.position.x, ",", rover.state.position.y, ")")
    rover.turn_left()
    rover.turn_right()
    rover.advance_N(1, dimension, grid)
    print("** Orientation Rover: ", rover.state.orientation)
    print("*** Position Rover: (", rover.state.position.x, ",", rover.state.position.y, ")")
    rover.advance_N(1, dimension, grid)
    print("** Orientation Rover: ", rover.state.orientation)
    print("*** Position Rover: (", rover.state.position.x, ",", rover.state.position.y, ")")
    rover.turn_right()
    rover.advance_N(1, dimension, grid)
    rover.turn_right()
    rover.advance_N(1, dimension, grid)
    print("** Orientation Rover: ", rover.state.orientation)
    print("*** Position Rover: (", rover.state.position.x, ",", rover.state.position.y, ")")


    rover.advance_N(1, dimension,grid)
    rover.advance_N(0, dimension,grid)
    #rover.backOff_S(2)
    print("** Orientation Rover: ", rover.state.orientation)
    print("*** Position Rover: (", rover.state.position.x,",", rover.state.position.y, ")")
