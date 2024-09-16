from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox, QLineEdit, QPushButton, QStackedWidget
from PyQt5 import uic
import sys


user = {"username": 'username',
        "password": 'password'}

currency_rate = {
    "EUR/USD": 1.06, "USD/EUR": 0.87,
    "EUR/GEL": 2.91, "GEL/EUR": 0.33,
    "USD/GEL": 2.64, "GEL/USD": 0.36,
    "GEL/GEL": 1, "USD/USD": 1,
    "EUR/EUR": 1
}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi("loadui1.ui", self)

        self.label = self.findChild(QLabel, 'not_authorized')
        self.login_btn = self.findChild(QPushButton, 'login_btn')
        self.username_inpt = self.findChild(QLineEdit, 'username_inpt')
        self.pass_inpt = self.findChild(QLineEdit, 'pass_inpt')
        self.change_pages = self.findChild(QStackedWidget, 'stackedWidget')
        self.from_combo = self.findChild(QComboBox, 'from_combo')
        self.to_combo = self.findChild(QComboBox,'to_combo')
        self.money_inpt = self.findChild(QLineEdit,'money_inpt')
        self.convert_btn = self.findChild(QPushButton,'convert_btn')
        self.reset_btn = self.findChild(QPushButton,'reset_btn')
        self.logout_btn = self.findChild(QPushButton,'logout_btn')
        self.converted_money = self.findChild(QLabel,'converted_money')

        self.login_btn.clicked.connect(self.check_validity)
        self.convert_btn.clicked.connect(self.convert)
        self.reset_btn.clicked.connect(self.reset)
        self.logout_btn.clicked.connect(self.logout)


        self.show()

    def check_validity(self):
        if user['username'] == self.username_inpt.text() and user['password'] == self.pass_inpt.text():
            self.username_inpt.setText("")
            self.pass_inpt.setText("")
            self.label.setText("")
            self.change_pages.setCurrentIndex(1)
        else:
            self.label.setText("Invalid Credentials!")

    def convert(self):
        try:
            amount = float(self.money_inpt.text())
            if amount < 0:
                raise ValueError
            final_result = amount * currency_rate[f"{self.from_combo.currentText()}/{self.to_combo.currentText()}"]
            self.converted_money.setText(f"Converted: {final_result:.2f} {self.to_combo.currentText()}")
        except ValueError:
            self.converted_money.setText("<font color='#a8a003'>Please enter a number.</font>")

    def reset(self):
        self.converted_money.setText("")
        self.money_inpt.setText("")

    def logout(self):
        self.change_pages.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    app.exec_()
