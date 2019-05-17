#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pyowm
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):      
        self.btn = QPushButton('Город', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.temp)
        
        self.le = QLineEdit(self)
        self.le.move(130, 44)
        self.le.setGeometry(1, 50, 290, 49)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
    def temp(self):
        owm = pyowm.OWM('7d32e2a438de1683999132b81b27b79d', language = "ru")
        text, ok = QInputDialog.getText(self, 'Город', 'Ведите название города:')
        place = text
        observation = owm.weather_at_place(str(place))
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        if ok:
            self.le.setText(str("В городе " + place + " погода " + w.get_detailed_status() + str(temp)))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())