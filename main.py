import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QButtonGroup,
                            QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")

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
        self.number_buttons = QButtonGroup(self)
        self.number_buttons.addButton(self.button0)
        self.number_buttons.addButton(self.button1)
        self.number_buttons.addButton(self.button2)
        self.number_buttons.addButton(self.button3)
        self.number_buttons.addButton(self.button4)
        self.number_buttons.addButton(self.button5)
        self.number_buttons.addButton(self.button6)
        self.number_buttons.addButton(self.button7)
        self.number_buttons.addButton(self.button8)
        self.number_buttons.addButton(self.button9)

        self.button_plus = QPushButton("+", self)
        self.button_minus = QPushButton("-", self)
        self.button_divide = QPushButton("/", self)
        self.button_multiply = QPushButton("*", self)
        self.operator_buttons = QButtonGroup(self)
        self.operator_buttons.addButton(self.button_plus)
        self.operator_buttons.addButton(self.button_minus)
        self.operator_buttons.addButton(self.button_divide)
        self.operator_buttons.addButton(self.button_multiply)

        self.button_equals = QPushButton("=", self)
        self.button_clear = QPushButton("C", self)

        self.calc_label = QLabel("", self)
        self.calc_label.setStyleSheet("font-size: 20px;")

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
        self.calc_label.setAlignment(Qt.AlignRight)
        vbox.addLayout(hbox_line1)
        vbox.addLayout(hbox_line2)
        vbox.addLayout(hbox_line3)
        vbox.addLayout(hbox_line4)

        self.setLayout(vbox)

        self.number_buttons.buttonClicked.connect(self.number_button_clicked)
        self.operator_buttons.buttonClicked.connect(self.operator_button_clicked)
        self.button_equals.clicked.connect(self.equal_button_clicked)
        self.button_clear.clicked.connect(self.clear_button_clicked)



    def number_button_clicked(self, button):  
        self.calc_label.setText(self.calc_label.text() + button.text())

    def operator_button_clicked(self, button):
        if self.calc_label.text() == "":
            return
        if self.calc_label.text()[-1].isdigit():
            self.calc_label.setText(self.calc_label.text() + button.text())
        else:
            self.calc_label.setText(self.calc_label.text()[:-1] + button.text())

    def clear_button_clicked(self):
        self.calc_label.setText("")

    def equal_button_clicked(self):
        if self.calc_label.text() == "":
            return
        if not self.calc_label.text()[-1].isdigit():
            print("not a numeric formular")
            return
        self.calc_label.setText(str(self.numeric_evaluation(self.calc_label.text())))



    def numeric_evaluation(self, string_to_eval):
        if "+" in string_to_eval:
            return self.numeric_evaluation(string_to_eval.split("+", 1)[0]) + self.numeric_evaluation(string_to_eval.split("+", 1)[1])
        if "-" in string_to_eval and not string_to_eval[0] == "-":  #check if first number negativ
            return self.numeric_evaluation(string_to_eval.split("-", 1)[0]) - self.numeric_evaluation(string_to_eval.split("-", 1)[1]) 
        if "*" in string_to_eval and "/" in string_to_eval:
            if string_to_eval.index("*") < string_to_eval.index("/"):
                return self.numeric_evaluation(string_to_eval.split("*", 1)[0]) * self.numeric_evaluation(string_to_eval.split("*", 1)[1]) 
            else:
                return self.numeric_evaluation(string_to_eval.split("/", 1)[0]) / self.numeric_evaluation(string_to_eval.split("/", 1)[1])
        if "*" in string_to_eval:
            return self.numeric_evaluation(string_to_eval.split("*", 1)[0]) * self.numeric_evaluation(string_to_eval.split("*", 1)[1])
        if "/" in string_to_eval:
            return self.numeric_evaluation(string_to_eval.split("/", 1)[0]) / self.numeric_evaluation(string_to_eval.split("/", 1)[1])

        return float(string_to_eval)
    

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()   


