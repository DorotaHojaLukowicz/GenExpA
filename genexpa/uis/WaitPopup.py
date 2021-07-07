from PySide2.QtWidgets import QDialog

from genexpa.uis.uis.WaitPopupUI import Ui_Form


class WaitPopup(QDialog):
    def __init__(self, system):
        self.system = system
        super(WaitPopup, self).__init__(system.mainWindowApp)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.close_allowed = False

    def start(self):
        self.open()
        self.system.app.processEvents()

    def closeEvent(self, event):
        if self.close_allowed:
            super(WaitPopup, self).closeEvent(event)

        else:
            event.ignore()

    def calculation_finished(self):
        self.close_allowed = True
        self.close()
