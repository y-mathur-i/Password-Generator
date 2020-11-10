from passGen import passwordGen
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passGenUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 448)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(32)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 0, 671, 131))
        self.title.setStyleSheet("border: 2px solid grey")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setFocusPolicy(QtCore.Qt.NoFocus)
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.sizeSelector = QtWidgets.QSpinBox(self.centralwidget)
        self.sizeSelector.setGeometry(QtCore.QRect(70, 210, 81, 22))
        self.sizeSelector.setMinimum(5)
        self.sizeSelector.setMaximum(50)
        self.sizeSelector.setObjectName("sizeSelector")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(280, 210, 111, 20))
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 280, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(480, 210, 150, 22))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setMinimumContentsLength(3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Weak")
        self.comboBox.addItem("Strong")
        self.comboBox.addItem("Very Strong")
        self.resLabel = QtWidgets.QTextBrowser(self.centralwidget)
        self.resLabel.setGeometry(QtCore.QRect(180, 380, 300, 131))
        self.resLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resLabel.setText("")
        self.resLabel.setObjectName("resLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.generate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Password generator"))
        self.radioButton.setText(_translate("MainWindow", "Numbers"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))

    def generate(self):
        result = self.generatePassword()
        # print(result)
        self.resLabel.setText(result)
        # self.resLabel.adjustSize()

    def generatePassword(self):
        num = True if self.radioButton.isChecked() else False
        length = self.sizeSelector.value()
        idx = self.comboBox.currentIndex()
        if idx == 0:
            strength = 'Weak'
        elif idx == 1:
            strength = 'Strong'
        elif idx == 2:
            strength = 'Very Strong'
        else:
            return "Choose the strength for your password"
        return passwordGen(length, num, strength)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())