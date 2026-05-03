import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QPushButton, QVBoxLayout, QHBoxLayout)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())


