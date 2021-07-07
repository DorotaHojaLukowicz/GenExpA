from PySide2.QtCore import QObject, Signal

class Actions(QObject):
    read_from_combined_input = Signal()
    load_quantified = Signal()
    open_licence_popup = Signal()

    lock_application = Signal()
    unlock_application = Signal()
