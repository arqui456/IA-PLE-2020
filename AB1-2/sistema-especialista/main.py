import sys

from GUI import GUI
from PyQt5.QtWidgets import QApplication

ui = QApplication(sys.argv)
ex = GUI()
sys.exit(ui.exec_())


