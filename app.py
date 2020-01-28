import sys
import os
from PySide2.QtWidgets import QApplication
from windscribe_gui.ui import MainWindow


class App(MainWindow):
    pass


if __name__ == "__main__":
    app = QApplication()
    window = App()
    window.setFixedSize(400, 600)
    window.show()

    sys.exit(app.exec_())
    com = os.popen('windscribe account').read()
    print(com)