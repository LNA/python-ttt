from lib.io import IO

class CommandLineRunner:
  def __init__(self, io):
    self.io = io

  def start_game(self):
    self.io.welcome()
    self._configure_settings_()

  def _configure_settings_(self):
    settings = {}
    player_one_brain = raw_input(self.io.get_player_input("one", "brain: Human or AI"))
    settings['player_one_brain'] = player_one_brain
    player_two_brain = raw_input(self.io.get_player_input("two", "brain: Human or AI"))
    settings['player_two_brain'] = player_two_brain
    player_one_mark = raw_input(self.io.get_player_input("one", "game piece"))
    settings['player_one_mark'] = player_one_mark
    player_two_mark = raw_input(self.io.get_player_input("two", "game piece"))
    settings['player_two_mark'] = player_two_mark
    print "Player one: " + player_one_brain + " " + player_one_mark
    print "Player two: " + player_two_brain + " " + player_two_mark
