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
    # def __init__(self):
    #     super(MyWindow, self).__init__()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self)
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()  # Экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)  # Инициализация GUI


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
# aa
# ga's
a = 121
sys.exit(app.exec())
