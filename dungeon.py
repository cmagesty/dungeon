import os
import random
import sys


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def double_space():
  print("")
  print("")

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
  return random.sample(CELLS, 3)


def move_player(player, move):
  #x and y coordinates of the cells
  x, y = player
  if move == "LEFT":
    x -= 1
  if move == "RIGHT":
    x += 1
  if move == "UP":
    y -= 1
  if move == "DOWN":
    y += 1
  return x, y


def get_moves(player):
  moves = ["LEFT", "RIGHT", "UP", "DOWN"]
  x, y = player
  if x == 0:
    moves.remove("LEFT")
  if x == 4:
    moves.remove("RIGHT")
  if y == 0:
    moves.remove("UP")
  if y == 4:
    moves.remove("DOWN")
  return moves


def draw_map(player):
  print(" _"*5)
  tile = "|{}"

  for cell in CELLS:
    x, y = cell
    if x < 4:
      line_end = ""
      if cell == player:
        output = tile.format("X")
      else:
        output = tile.format("_")
    else:
      line_end = "\n"
      if cell == player:
        output = tile.format("X|")
      else:
        output = tile.format("_|")
    print(output, end=line_end)

def retry():
  retry = True
  while retry:
    retryInput = input("Play again? [Y/n] ").lower()
    if retryInput == "y":
      game_loop()
    elif retryInput == "n":
      sys.exit()
    else:
      clear_screen()
      double_space()
      print("  ** invalid input **")
      double_space()

def game_loop():
  monster, door, player = get_locations()
  playing = True

  while playing:
    clear_screen()
    draw_map(player)
    valid_moves = get_moves(player)

    print("You're currently in room {}".format(player))
    print("You can move {}".format(", ".join(valid_moves)))
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
      print("\n See you next time! \n")
      break
    if move in valid_moves:
      player = move_player(player, move)

      if player == monster:
        double_space()
        print(" Oh no! The monster got you! Better luck next time!")
        double_space()
        playing = False
      if player == door:
        double_space()
        print(" You escaped! Congratulations! ")
        double_space()
        playing = False
    else:
      if move == "UP" or move == "DOWN" or move == "LEFT" or move == "RIGHT":
        double_space()
        input(" Walls are hard! Don't run into them!")
        double_space()
      else:
        double_space()
        input("Invalid Input")
        double_space()
  else:
    double_space()
    input("press enter to continue ")
    retry()


clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
