class IO:
  def welcome(self):
    return "Welcome to Tic Tac Toe!"

  def get_player_input(self, player_number, input):
   return "Select Player " + player_number + " " + input + " "

  def print_settings(self, settings, number, brain, mark):
    return "Player " + number +  " : " + settings[brain] + " " + settings[mark]

