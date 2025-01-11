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

        self.tasks = self.loadTasks()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self._createInputField()
        self._createTodoList()
        self._createButtons()

        self.loadTasksToList()

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
            self.tasks.append(task_data)
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.todoList.addItem(item)
            self.inputField.clear()
            self.saveTasks()

    def removeSelectedTask(self):
        for item in self.todoList.selectedItems():
            task_text = item.text()
            self.todoList.takeItem(self.todoList.row(item))
            self.tasks = [task for task in self.tasks if task['text'] != task_text]
        self.saveTasks()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Delete:
            self.removeSelectedTask()
        super().keyPressEvent(event)

    def loadTasks(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
 
    def saveTasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def loadTasksToList(self):
        for task in self.tasks:
            item = QListWidgetItem(task["text"])
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Checked if task["completed"] else Qt.CheckState.Unchecked)
            self.todoList.addItem(item)

    def updateTaskStatus(self):
        for index in range(self.todoList.count()):
            item = self.todoList.item(index)
            task_text = item.text()
            task = next((task for task in self.tasks if task["text"] == task_text), None)
            if task:
                task["completed"] = item.checkState() == Qt.CheckState.Checked
        self.saveTasks() 

    def closeEvent(self, event):
        self.updateTaskStatus()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()