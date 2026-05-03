import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.button0 = QPushButton("0", self)
        self.button1 = QPushButton("1", self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.button4 = QPushButton("4", self)
        self.button5 = QPushButton("5", self)
        self.button6 = QPushButton("6", self)
        self.button7 = QPushButton("7", self)
        self.button8 = QPushButton("8", self)
        self.button9 = QPushButton("9", self)
        self.button_plus = QPushButton("+", self)
        self.button_minus = QPushButton("-", self)
        self.button_divide = QPushButton("/", self)
        self.button_multiply = QPushButton("*", self)
        self.button_equals = QPushButton("=", self)
        self.button_clear = QPushButton("C", self)

        


        self.calc_label = QLabel("1+1+1+1+1+1+1+1+1+1", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        hbox_line1 = QHBoxLayout()
        hbox_line2 = QHBoxLayout()
        hbox_line3 = QHBoxLayout()
        hbox_line4 = QHBoxLayout()

        hbox_line1.addWidget(self.button1)
        hbox_line1.addWidget(self.button2)
        hbox_line1.addWidget(self.button3)
        hbox_line1.addWidget(self.button_plus)

        hbox_line2.addWidget(self.button4)
        hbox_line2.addWidget(self.button5)
        hbox_line2.addWidget(self.button6)
        hbox_line2.addWidget(self.button_minus)

        hbox_line3.addWidget(self.button7)
        hbox_line3.addWidget(self.button8)
        hbox_line3.addWidget(self.button9)
        hbox_line3.addWidget(self.button_multiply)

        hbox_line4.addWidget(self.button_clear)
        hbox_line4.addWidget(self.button0)
        hbox_line4.addWidget(self.button_divide)
        hbox_line4.addWidget(self.button_equals)

        vbox = QVBoxLayout()
        vbox.addWidget(self.calc_label)
        self.calc_label.setAlignment(Qt.AlignCenter)
        vbox.addLayout(hbox_line1)
        vbox.addLayout(hbox_line2)
        vbox.addLayout(hbox_line3)
        vbox.addLayout(hbox_line4)


        self.setLayout(vbox)



def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()   


