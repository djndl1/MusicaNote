#!/usr/bin/env python3

import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import QTimer

note_names = [
    'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
    'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
    'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
    'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
    'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6',
    'C7',
]

def initialize_generator():
    random.seed()

def generate_random_note() -> str:
    n = random.choice(note_names)
    return n

class NoteNotifier(QWidget):
    def __init__(self, interval=1000, parent=None):
        super().__init__(parent)

        initialize_generator()

        self.timer_interval = interval
        self.timer = QTimer()

        self.start_button = QPushButton('Start')
        self.stop_button = QPushButton('Stop')
        self.note_label = QLabel('C4')

        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.timer.timeout.connect(self.show_note)

        layout = QGridLayout()

        layout.addWidget(self.note_label, 0, 0, 1, 2)
        layout.addWidget(self.start_button, 1, 0)
        layout.addWidget(self.stop_button, 1, 1)

        self.setLayout(layout)

    def show_note(self):
        note = generate_random_note()
        self.note_label.setText(note)

    def start_timer(self):
        self.timer.start(self.timer_interval)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

if __name__ == '__main__':
    interval = 1
    if len(sys.argv) > 1:
        interval = int(sys.argv[1])

    initialize_generator()

    app = QApplication(sys.argv)
    window = NoteNotifier(interval * 1000)
    window.show()

    sys.exit(app.exec_())
