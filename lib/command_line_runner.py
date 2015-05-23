from lib.io import IO

class CommandLineRunner:
  def __init__(self, io, settings):
    self.io = io
    self.settings = settings

  def start_game(self):
    print self.io.welcome()
    settings = self.settings.configure_settings_()
    print self.io.print_settings(settings, 'one', 'player_one_brain', 'player_one_mark')
    print self.io.print_settings(settings, 'two', 'player_two_brain', 'player_two_mark')
