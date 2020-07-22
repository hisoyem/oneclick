# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

from gui import Ui_MainWindow  # импорт сгенерированного файла


# MainWindow.setFixedSize(1152, 566)
# self.tableWidget.setColumnWidth(0, 191)
# self.tableWidget.setColumnWidth(1, 191)
# self.tableWidget.setColumnWidth(2, 191)
# self.tableWidget.setColumnWidth(3, 191)
# self.tableWidget.setColumnWidth(4, 191)
# self.tableWidget.setColumnWidth(5, 191)

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()  # Экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)  # Инициализация GUI
        self.ui.pushButton_3.clicked.connect(self.add_5_mins)
        self.ui.pushButton_4.clicked.connect(self.add_15_mins)
        self.ui.pushButton_5.clicked.connect(self.add_60_mins)
        self.ui.pushButton_6.clicked.connect(self.set_0_mins)
        self.ui.checkBox_5.clicked.connect(self.checkbox_headless)
        self.ui.checkBox_6.clicked.connect(self.checkbox_chrome)

    def add_5_mins(self):
        """Add 5 minutes to interval spinBox"""

        self.ui.spinBox.setValue(self.ui.spinBox.value() + 5)

    def add_15_mins(self):
        """Add 15 minutes to interval spinBox"""

        self.ui.spinBox.setValue(self.ui.spinBox.value() + 15)

    def add_60_mins(self):
        """Add 60 minutes to interval spinBox"""

        self.ui.spinBox.setValue(self.ui.spinBox.value() + 60)

    def set_0_mins(self):
        """Add 60 minutes to interval spinBox"""

        self.ui.spinBox.setValue(0)

    def checkbox_headless(self):
        """If 1 of 2 checkboxes activated => deactivate previous"""

        if self.ui.checkBox_5.isChecked():
            print(True)
            self.ui.checkBox_6.setChecked(False)

    def checkbox_chrome(self):
        """If 1 of 2 checkboxes activated => deactivate previous"""

        if self.ui.checkBox_6.isChecked():
            self.ui.checkBox_5.setChecked(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
