import sys

from PyQt5.QtWidgets import QApplication

from graphics import mainwindow


def run():
	# Initialize the application:
	# - Import user's desktop settings
	# - Event handling from the underlying window system
	# - Parse command line options
	# - Define application's look and feel to match the equivalent native widgets
	# - Manage application's mouse cursor handling

	app = QApplication(sys.argv)

	# Initialize the config files
	# TODO

	# Initialize log files
	# TODO

	# Initialize the app window
	window = mainwindow.MainWindow()
	window.show()

	# App execution
	app.exec_()
