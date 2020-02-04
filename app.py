import sys
import logging
logging.basicConfig(filename="logs.log",
                    format='[%(levelname)s]: %(asctime)s [%(module)s > %(funcName)s > %(lineno)d]: %(message)s ',
                    datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)
from PySide2.QtWidgets import QApplication
from windscribe_gui.ui import MainWindow


logger = logging.getLogger(__name__)


class App(MainWindow):
    pass


if __name__ == "__main__":
    try:
        app = QApplication()
        window = App()
        window.setFixedSize(400, 450)
        window.show()
    except Exception as error:
        logger.error(error)

    sys.exit(app.exec_())
