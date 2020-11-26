from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QCursor
import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QTableWidget
from PyQt5 import uic
import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.Table.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
