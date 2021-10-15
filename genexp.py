import sys

from genexpa.uis.MainWindowApp import MainWindowApp
from PySide2.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    main_window = MainWindowApp(app)
    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
