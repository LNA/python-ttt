from lib.io import IO

class Setup:
  def __init__(self, io):
    self.io = io

  def get_game_options(self):
    settings = {player_one_brain: self.ui.gets_player_one_type  }
