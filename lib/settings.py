from lib.io import IO

class Settings:
  def __init__(self, io):
    self.io = io

  def configure_settings_(self):
    settings = {}
    player_one_brain = raw_input(self.io.get_player_input("one", "brain: Human or AI"))
    settings['player_one_brain'] = player_one_brain
    player_two_brain = raw_input(self.io.get_player_input("two", "brain: Human or AI"))
    settings['player_two_brain'] = player_two_brain
    player_one_mark = raw_input(self.io.get_player_input("one", "game piece"))
    settings['player_one_mark'] = player_one_mark
    player_two_mark = raw_input(self.io.get_player_input("two", "game piece"))
    settings['player_two_mark'] = player_two_mark
    return settings
