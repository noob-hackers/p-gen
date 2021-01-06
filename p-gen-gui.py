#!/usr/bin/env python3

import random
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QLabel, QPushButton, QLineEdit, QPlainTextEdit
from PyQt5.QtGui import QIcon, QFont, QClipboard, QIntValidator
from qt_material import apply_stylesheet

# Maximum length
maxchar: int = 1500

# Characters
char: str = 'abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^'


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.passlen = QLabel('Password Length', self)
        self.passlen.move(128, 43)
        self.passlen.adjustSize()

        self.Title = QLabel('P-GEN GUI', self)
        self.Title.move(120, 10)
        self.Title.setFont(QFont('Arial', 19))
        self.Title.adjustSize()

        generate = QPushButton("Generate", self)
        generate.setGeometry(113, 107, 130, 40)
        generate.setIcon(QIcon('gui/generate.png'))
        generate.clicked.connect(self.Generate)

        minusicon = QPushButton("-", self)
        minusicon.setGeometry(95, 70, 40, 40)
        minusicon.clicked.connect(self.decrease)

        plusicon = QPushButton("+", self)
        plusicon.setGeometry(209, 70, 40, 40)
        plusicon.clicked.connect(self.increase)

        copypass = QPushButton('Copy', self)
        copypass.move(128, 253)
        copypass.setIcon(QIcon('gui/copy.png'))
        copypass.clicked.connect(self.copy)

        self.charlen = QLineEdit(self)
        self.charlen.setGeometry(137, 70, 70, 36)
        self.charlen.setText('12')

        self.onlyInt = QIntValidator()
        self.charlen.setValidator(self.onlyInt)

        self.passwordout = QPlainTextEdit(self)
        self.passwordout.setGeometry(60, 149, 240, 100)
        self.passwordout.setReadOnly(True)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('P-GEN GUI')
        self.show()

    def increase(self) -> object:
        if int(self.charlen.text()) < maxchar:
            self.charlen.setText(str(int(self.charlen.text()) + 1))
        else:
            self.charlen.setText(str(maxchar))

    def decrease(self) -> object:
        if int(self.charlen.text()) > 2:
            self.charlen.setText(str(int(self.charlen.text()) - 1))
        else:
            self.charlen.setText('1')

    def Generate(self) -> object:
        if int(self.charlen.text()) > maxchar:
            self.charlen.setText(str(maxchar))

        if int(self.charlen.text()) < 2:
            self.charlen.setText('1')

        password = ''

        for i in range(int(self.charlen.text())):
            password += random.choice(char)

        self.passwordout.setPlainText(password)

    def copy(self) -> object:
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.passwordout.toPlainText(), mode=cb.Clipboard)


def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_pink.xml')
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
