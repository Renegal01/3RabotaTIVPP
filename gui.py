import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from converter import Converter


class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.converter = Converter()

        self.input_label = QLabel('Value:', self)
        self.input_label.move(20, 20)

        self.input_text = QLineEdit(self)
        self.input_text.move(100, 20)

        self.from_label = QLabel('From:', self)
        self.from_label.move(20, 60)

        self.from_text = QLineEdit(self)
        self.from_text.move(100, 60)

        self.to_label = QLabel('To:', self)
        self.to_label.move(20, 100)

        self.to_text = QLineEdit(self)
        self.to_text.move(100, 100)

        self.result_label = QLabel('Result:', self)
        self.result_label.move(20, 140)

        self.result_text = QLabel(self)
        self.result_text.move(100, 140)

        self.convert_btn = QPushButton('Convert', self)
        self.convert_btn.move(20, 180)
        self.convert_btn.clicked.connect(self.convert)

        self.setGeometry(300, 300, 300, 230)
        self.setWindowTitle('Unit Converter')
        self.show()

    def convert(self):
        value = float(self.input_text.text())
        from_unit = self.from_text.text()
        to_unit = self.to_text.text()

        result = self.converter.convert(value, from_unit, to_unit)
        if result is not None:
            self.result_text.setText(str(result))
        else:
            self.result_text.setText('Invalid units')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterApp()
    sys.exit(app.exec_())













