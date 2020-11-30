from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QCursor
import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class AddCoffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setLayout(self.main)


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.main = QVBoxLayout()
        uic.loadUi("main.ui", self)
        self.update_table()
        self.btn = QPushButton("Добавить")
        self.btn.clicked.connect(self.add_coffee)
        self.main.addWidget(self.Table)
        self.main.addWidget(self.btn)
        self.setLayout(self.main)

    def update_table(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.Table.setModel(model)

    def add_coffee(self):
        self.add = AddCoffee()
        self.add.show()
        self.add.pushButton.clicked.connect(self.coffee_to_db)

    def coffee_to_db(self):
        name_sort = self.add.lineEdit.text()
        degree = self.add.lineEdit_2.text()
        ground_grains = self.add.comboBox.currentText()
        taste = self.add.lineEdit_3.text()
        cost = self.add.lineEdit_4.text()
        volume = self.add.lineEdit_5.text()
        link = sqlite3.connect("coffee.sqlite")
        cursor = link.cursor()
        query = cursor.execute("""INSERT INTO `coffee`(`name_sort`, `degree of roasting`, `ground / in grains`,
         `the description of the taste`, `cost`, `volume`)
        VALUES (?, ?, ?, ?, ?, ?)""", (str(name_sort), str(degree), str(ground_grains), str(taste), int(cost), int(volume)))
        link.commit()
        self.add.lineEdit.clear()
        self.add.lineEdit_2.clear()
        self.add.lineEdit_3.clear()
        self.add.lineEdit_4.clear()
        self.add.lineEdit_5.clear()
        self.add.hide()
        self.update_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
