#!/usr/bin/env python3

import random
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QLabel, QPushButton, QLineEdit, QPlainTextEdit
from PyQt5.QtGui import QIcon, QFont, QClipboard, QIntValidator

# Maximum length
maxchar = 1500

# Characters
char="abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.passlen = QLabel('Password Length', self)
        self.passlen.move(128,43)
        self.passlen.adjustSize()

        self.Title = QLabel('P-GEN GUI',self)
        self.Title.move(120,10)
        self.Title.setFont(QFont('Arial', 19))
        self.Title.adjustSize()

        generate = QPushButton("Generate", self)
        generate.move(128, 105)
        generate.setIcon(QIcon('gui/generate.png'))
        generate.clicked.connect(self.Generate)

        minusicon = QPushButton("-",self)
        minusicon.setGeometry(102,70,32,32)
        minusicon.clicked.connect(self.decrease)

        plusicon = QPushButton("+",self)
        plusicon.setGeometry(210,70,32,32)
        plusicon.clicked.connect(self.increase)

        copypass = QPushButton('Copy', self)
        copypass.move(128,250)
        copypass.setIcon(QIcon('gui/copy.png'))
        copypass.clicked.connect(self.copy)

        self.charlen = QLineEdit(self)
        self.charlen.setGeometry(137, 70, 70, 32)
        self.charlen.setText('12')

        self.onlyInt = QIntValidator()
        self.charlen.setValidator(self.onlyInt)

        self.passwordout = QPlainTextEdit(self)
        self.passwordout.setGeometry(60,140,240,100)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('P-GEN GUI')
        self.show()

    def increase(self):
    	if int(self.charlen.text()) < maxchar:
    		self.charlen.setText(str(int(self.charlen.text())+1))
    	else:
    		self.charlen.setText(str(maxchar))

    def decrease(self):
    	if int(self.charlen.text()) > 2:
    		self.charlen.setText(str(int(self.charlen.text())-1))
    	else:
    		self.charlen.setText('1')

    def Generate(self):
    	if int(self.charlen.text()) > maxchar:
    		self.charlen.setText(str(maxchar))

    	if int(self.charlen.text()) < 2:
    		self.charlen.setText('1')

    	password = ''

    	for i in range(int(self.charlen.text())):
    		password += random.choice(char)

    	self.passwordout.setPlainText(password)



    def copy(self):
    	cb = QApplication.clipboard()
    	cb.clear(mode=cb.Clipboard )
    	cb.setText(self.passwordout.PlainText(), mode=cb.Clipboard)
    	


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()