from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QCursor
import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5 import uic


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.handler)

    def handler(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        qp.setBrush(QColor("Yellow"))
        a = randint(1, 100)
        qp.drawEllipse(randint(0, 300), randint(0, 300), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
