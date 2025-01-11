<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>To-Do List Application with PyQt6</h1>

<p>This is a simple To-Do List application built using PyQt6 and Python. It allows users to add, remove, and mark tasks as completed. The tasks are saved persistently in a JSON file, including their completion status.</p>

<h2>Features</h2>
<ul>
    <li><strong>Add Tasks</strong>: Users can add tasks by typing them in the input field and pressing Enter or clicking the "Add" button.</li>
    <li><strong>Remove Tasks</strong>: Users can remove selected tasks by clicking the "Remove Selected" button or using the Delete key.</li>
    <li><strong>Mark Tasks as Completed</strong>: Tasks can be marked as completed by checking the checkbox next to each task.</li>
    <li><strong>Persistent Storage</strong>: The tasks (including their completion status) are saved in a <code>tarefas.json</code> file and will be restored when the application is reopened.</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>PyQt6 (<code>pip install PyQt6</code>)</li>
</ul>

<h2>How to Run</h2>
<ol>
    <li>Clone the repository or download the script.</li>
    <li>Install the required dependencies by running:
        <pre><code>pip install PyQt6</code></pre>
    </li>
    <li>Run the application:
        <pre><code>python todo_app.py</code></pre>
    </li>
</ol>

<h2>File Structure</h2>
<pre>
/todo_app.py  - The main Python script for the To-Do List application
/tarefas.json - The file where tasks and their status are saved
</pre>

<h2>How to Use</h2>
<ul>
    <li><strong>Add a Task</strong>: Type the task in the input field and press Enter or click the "Add" button.</li>
    <li><strong>Remove a Task</strong>: Select a task from the list and click the "Remove Selected" button or press the Delete key.</li>
    <li><strong>Mark a Task as Completed</strong>: Click the checkbox next to a task to mark it as completed.</li>
    <li><strong>Save and Load Tasks</strong>: Tasks are automatically saved in <code>tarefas.json</code> and will be loaded when the application is opened again.</li>
</ul>
</body>
</html>
