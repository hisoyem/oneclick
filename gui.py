# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1153, 563)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/quasar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1161, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setAccessibleDescription("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1151, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/restaurant-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("quasar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 150, 548, 259))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setMaximum(1000)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_7.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_7.addWidget(self.checkBox_6)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_7)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_5.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_5.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_5.addWidget(self.checkBox_4)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/access-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/add-link-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/settings-5-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(490, 80, 167, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 180, 1131, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 280, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setGeometry(QtCore.QRect(10, 460, 1131, 51))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(1080, 10, 41, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/quasar.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(890, 20, 161, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/clipboard-8-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setFixedSize(1152, 566)
        self.tableWidget.setColumnWidth(0, 191)
        self.tableWidget.setColumnWidth(1, 191)
        self.tableWidget.setColumnWidth(2, 191)
        self.tableWidget.setColumnWidth(3, 191)
        self.tableWidget.setColumnWidth(4, 191)
        self.tableWidget.setColumnWidth(5, 191)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quasar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Account"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Interval"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Progress"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Proxy"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Enabled"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Actions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tasks"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "Set interval"))
        self.checkBox_5.setText(_translate("MainWindow", "Headless browser"))
        self.checkBox_6.setText(_translate("MainWindow", "Google Chrome"))
        self.pushButton.setText(_translate("MainWindow", "Add to tasks"))
        self.checkBox.setText(_translate("MainWindow", "Youube"))
        self.checkBox_2.setText(_translate("MainWindow", "Search"))
        self.checkBox_3.setText(_translate("MainWindow", "News"))
        self.checkBox_4.setText(_translate("MainWindow", "Shopping"))
        self.pushButton_3.setText(_translate("MainWindow", "+5 mins"))
        self.pushButton_4.setText(_translate("MainWindow", "+10 mins"))
        self.pushButton_5.setText(_translate("MainWindow", "+1 hr"))
        self.pushButton_6.setText(_translate("MainWindow", "Back to 0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Add task"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Proxy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Settings"))
        self.label_3.setText(_translate("MainWindow", "License is invalid"))
        self.pushButton_2.setText(_translate("MainWindow", "Accept"))
        self.label_5.setText(_translate("MainWindow", "Quasar Cook AYCD v0.1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "License"))