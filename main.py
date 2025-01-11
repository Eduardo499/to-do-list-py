import json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import Qt
import sys

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To do list')
        self.setFixedSize(400, 500)

def main():
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()