## -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pyowm
import sys
import json
from PyQt5.QtWidgets import QInputDialog
exec(open("./config.py").read())
places = (place)
owms = (owms)
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 298)
        Form.setMinimumSize(QtCore.QSize(780, 298))
        Form.setMaximumSize(QtCore.QSize(780, 298))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 161, 71))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.temp)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 10, 161, 71))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.info)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 10, 161, 71))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.saves)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 90, 781, 211))
        self.frame.setMinimumSize(QtCore.QSize(781, 211))
        self.frame.setMaximumSize(QtCore.QSize(781, 211))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 731, 161))
        self.label.setObjectName("label")    

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def temp(self, Form):
        owm = pyowm.OWM(owms, language = "ru")
        text, ok = QtWidgets.QInputDialog.getText(None, 'Город', 'Ведите название города:')
        place = text
        observation = owm.weather_at_place(str(place))
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        if ok:
            self.label.setText(str("Погода в городе " + place + ": " + w.get_detailed_status() + ", " + str(temp) + "°C"))
    def saves(self, Form):
        owm = pyowm.OWM(owms, language = "ru")
        observation = owm.weather_at_place(places)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        self.label.setText(str("Погода в городе " + place + ": " + w.get_detailed_status() + ", " + str(temp) + "°C"))
        
    def info(self, Form):
        info = str("Программа находится в очень раннем развитии и пиздец какая корявая\nвсе баги которые вы найдете напишите в дискорд")
        self.label.setText(info)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Город"))
        self.pushButton_2.setText(_translate("Form", "Инфо"))
        self.pushButton_3.setText(_translate("Form",  "Узнать"))
        self.label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

