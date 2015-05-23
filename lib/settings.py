from lib.io import IO

class Settings:
  def __init__(self, io):
    self.io = io

  def configure_settings_(self):
    settings =  self.__get_settings__()
    return settings

  def __get_settings__(self):
    player_one_brain = raw_input(self.io.get_player_input("one", "brain: Human or AI"))
    player_two_brain = raw_input(self.io.get_player_input("two", "brain: Human or AI"))
    player_one_mark = raw_input(self.io.get_player_input("one", "game piece"))
    player_two_mark = raw_input(self.io.get_player_input("two", "game piece"))
    return self.__save_settings__(player_one_brain, player_two_brain, player_one_mark, player_two_mark)

  def __save_settings__(self, player_one_brain, player_two_brain, player_one_mark, player_two_mark):
    settings = {}
    settings['player_one_brain'] = player_one_brain
    settings['player_two_brain'] = player_two_brain
    settings['player_one_mark'] = player_one_mark
    settings['player_two_mark'] = player_two_mark
    return settings

