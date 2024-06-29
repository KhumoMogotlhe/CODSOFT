# test_todo_gui.py

import unittest
from unittest.mock import MagicMock, patch
from ToDo_List.todo_gui import add_task, remove_task, complete_task, update_tasks

class TestToDoGUI(unittest.TestCase):

    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        self.assertTrue(add_task(self.tasks, "Task 1", "Description 1"))
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "Task 1")
        self.assertEqual(self.tasks[0]["description"], "Description 1")
        self.assertFalse(self.tasks[0]["completed"])

    def test_add_task_no_title(self):
        with patch('tkinter.messagebox.showwarning') as mock_showwarning:
            self.assertFalse(add_task(self.tasks, "", "Description 1"))
            mock_showwarning.assert_called_once_with("Input Error", "Task title is required.")
        self.assertEqual(len(self.tasks), 0)

    def test_remove_task(self):
        add_task(self.tasks, "Task 1", "Description 1")
        remove_task(self.tasks, 0)
        self.assertEqual(len(self.tasks), 0)

    def test_complete_task(self):
        add_task(self.tasks, "Task 1", "Description 1")
        complete_task(self.tasks, 0)
        self.assertTrue(self.tasks[0]["completed"])

    @patch('todo_gui.tk.Frame')
    def test_update_tasks(self, MockFrame):
        task_frame = MockFrame()
        add_task(self.tasks, "Task 1", "Description 1")
        update_tasks(self.tasks, task_frame)
        self.assertEqual(task_frame.winfo_children.call_count, 1)

if __name__ == '__main__':
    unittest.main()
