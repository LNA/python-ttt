from lib.command_line_runner import CommandLineRunner
from lib.io                  import IO

io = IO()
command_line_runner = CommandLineRunner(io)
command_line_runner.start_game()
