from PySide2.QtWidgets import QMessageBox

def popup(title, text, severity="warning"):

    if severity == "warning":
        severity = QMessageBox.Warning
    elif severity == "information":
        severity = QMessageBox.Information
    elif severity == "question":
        severity = QMessageBox.Question
    else:
        severity = QMessageBox.Critical

    msg = QMessageBox()
    msg.setIcon(severity)
    msg.setText(title)
    msg.setInformativeText(text)
    msg.setWindowTitle(title)
    msg.exec_()
