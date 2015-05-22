from lib.command_line_runner import CommandLineRunner
from lib.ui                  import UI

ui = UI()
command_line_runner = CommandLineRunner(ui)
command_line_runner.start_game()
