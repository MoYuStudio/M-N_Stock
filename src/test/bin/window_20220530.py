import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import gui.gui as gui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    ui = gui.Ui_Window()
    ui.setupUi(window)
    window.show()

    sys.exit(app.exec_())