from lib.command_line_runner import CommandLineRunner
from lib.io                  import IO
from lib.settings            import Settings

io = IO()
settings = Settings(io)
command_line_runner = CommandLineRunner(io, settings)
command_line_runner.start_game()
