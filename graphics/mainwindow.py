from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore


class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
