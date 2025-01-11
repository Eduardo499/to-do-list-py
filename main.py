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
        self.file_path = 'tasks.json'
        #self.tasks = self.loadTasks()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self._createInputField()
        self._createTodoList()
        self._createButtons()

    def _createInputField(self):
        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText("Enter a new task...")
        self.inputField.returnPressed.connect(self.addTask)
        self.layout.addWidget(self.inputField)

    def _createTodoList(self):
        self.todoList = QListWidget()
        self.layout.addWidget(self.todoList)

    def _createButtons(self):
        buttonLayout = QHBoxLayout()
        self.addButton = QPushButton('Add')
        self.addButton.clicked.connect(self.addTask)
        buttonLayout.addWidget(self.addButton)

        self.removeButton = QPushButton('Remove Selected')
        self.removeButton.clicked.connect(self.removeSelectedTask)
        buttonLayout.addWidget(self.removeButton)

        self.layout.addLayout(buttonLayout)
    
    def addTask(self):
        task = self.inputField.text().strip()
        if task:
            task_data = {'text': task, 'completed': False}
            #self.tasks.append(task_data)
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.todoList.addItem(item)
            self.inputField.clear()
            #self.saveTasks()

    def removeSelectedTask(self):
        for item in self.todoList.selectedItems():
            task_text = item.text()
            self.todoList.takeItem(self.todoList.row(item))
            #self.tasks = [task for task in self.tasks if task['text'] != task_text]
        #self.saveTasks()

def main():
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()