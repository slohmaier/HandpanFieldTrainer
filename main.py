import random
import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QApplication, QWidget
from PySide6.QtWidgets import QSpinBox, QPushButton
import pyttsx3

class HandpanTrainer(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        grid = QGridLayout(widget)
        self.setCentralWidget(widget)
        grid.addWidget(QLabel('Fields: '), 0, 0)
        
        self._fields = QSpinBox()
        self._fields.setMinimum(1)
        self._fields.setMaximum(99)
        self._fields.setValue(8)
        grid.addWidget(self._fields, 0, 1)

        grid.addWidget(QLabel('Time[0.1s]: '), 1, 0)
        self._time = QSpinBox()
        self._time.setMinimum(1)
        self._time.setMaximum(9999)
        self._time.setValue(10)
        self._time.valueChanged.connect(self._timerProps)
        grid.addWidget(self._time, 1, 1)

        self._display = QLabel('0')
        font = self._display.font()
        font.setBold(True)
        font.setPointSize(72)
        self._display.setFont(font)
        self._display.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        grid.addWidget(self._display, 2, 0, 1, 2)

        self._button = QPushButton()
        self._button.setText('Start')
        self._button.clicked.connect(self._startStop)
        grid.addWidget(self._button, 3, 0, 1, 2)

        self._timer = QTimer(self)
        self._timer.stop()
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self._cycle)

        self._engine = pyttsx3.init()
        self._engine.setProperty('rate', 400)
    
    def _timerProps(self, dotOnesecs):
        mSecs = float(dotOnesecs) * 100.0
        self._timer.setInterval(mSecs)
    
    def _cycle(self):
        fields = self._fields.value()
        num = str(random.randint(1, fields))
        self._display.setText(num)
        self._engine.say(num)
        self._engine.runAndWait()
    
    def _startStop(self):
        if self._button.text() == 'Start':
            self._button.setText('Stop')
            self._timer.start()
        else:
            self._button.setText('Start')
            self._timer.stop()

if __name__ == '__main__':
    app = QApplication()
    
    widget = HandpanTrainer()
    widget.show()

    sys.exit(app.exec())