from lib.io import IO

class CommandLineRunner:
  def __init__(self, io):
    self.io = io

  def start_game(self):
    self.io.welcome()
    player_one_brain = raw_input(self.io.get_player_brain("one"))
    print (player_one_brain)




