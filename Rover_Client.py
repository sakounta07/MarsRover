import random
import socket

from MarsRover.Planet.Planet import Planet
from MarsRover.Planet.PlanetBuild import PlanetBuild
from MarsRover.Planet.PlanetStatic import PlanetStatic
from MarsRover.Rover.Position import Position
from MarsRover.Rover.Rover import Rover
from MarsRover.Rover.State import State


Host = "127.0.0.1"
Port = 2208

# Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))

# Config Rover #
world: list = PlanetStatic.mapPlanet
dimension = Planet.dimension
grid = PlanetBuild.build(dimension, world)
position_rover: Position = Planet.findRover(dimension, world)
rover = Rover()
rover.state = State()
rover.state.position = position_rover
rover.state.orientation = "N"


def avance():
    rover.advance_N(1, dimension, grid)
    return str("### After Advancing : (" + str(rover.state.position.x) + "," + str(rover.state.position.y) + ") ****> " + rover.state.orientation)


def reculer():
    rover.backOff_S(1, dimension, grid)
    return str("### After Retreating : (" + str(rover.state.position.x) + "," + str(rover.state.position.y) + ") ****> " + rover.state.orientation)


def turnR():
    rover.turn_right()
    return str("### After Turning Right : ("+str(rover.state.position.x)+","+str(rover.state.position.y)+") ****> "+rover.state.orientation)


def turnL():
    rover.turn_left()
    return str("### After Turning Left : ("+str(rover.state.position.x)+","+str(rover.state.position.y)+") ****> "+rover.state.orientation)


msg = "\n ### Bonjour c'est le Rover, j'attends vos instructions :)  ...\n"
msg += "# AV -> Avancer , RC -> Reculer , TR -> Tourner à Droite , TL -> Tourner à Gauche  #\n"
msg += "Position de départ Rover (0,0) -> Orienté vers le Nord"
msg = msg.encode("utf-8")
socket.send(msg)


while True:

    requete_server = socket.recv(500)
    data_list = requete_server.decode('utf-8').split(" ", 1)
    cmd = data_list[0]

    if cmd == "TL":
        s: str = turnL()
        socket.send(s.encode("utf-8"))
    if cmd == "TR":
        s: str = turnR()
        socket.send(s.encode("utf-8"))
    if cmd == "AV":
        s: str = avance()
        socket.send(s.encode("utf-8"))
    if cmd == "RC":
        s: str = reculer()
        socket.send(s.encode("utf-8"))
    if cmd != "RC" and cmd != "TR" and cmd != "TL" and cmd != "AV":
        msg = " Invalid Command  ...\n"
        msg = msg.encode("utf-8")
        socket.send(msg)

    print(requete_server)

