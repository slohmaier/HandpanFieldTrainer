import sys

from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QApplication, QWidget

class HandpanTrainer(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        grid = QGridLayout(widget)
        self.setCentralWidget(widget)
        grid.addWidget(QLabel('Fields: '))

if __name__ == '__main__':
    app = QApplication()
    
    widget = HandpanTrainer()
    widget.show()

    sys.exit(app.exec())