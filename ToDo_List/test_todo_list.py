
import unittest
from ToDo_List.todo_list import add_task, remove_task, update_task, mark_task_complete, list_tasks

class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        add_task(self.tasks, "Task 1", "Description 1")
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "Task 1")
        self.assertEqual(self.tasks[0]["description"], "Description 1")
        self.assertFalse(self.tasks[0]["completed"])

    def test_remove_task(self):
        add_task(self.tasks, "Task 1", "Description 1")
        remove_task(self.tasks, 0)
        self.assertEqual(len(self.tasks), 0)

    def test_remove_task_invalid_index(self):
        add_task(self.tasks, "Task 1", "Description 1")
        result = remove_task(self.tasks, 1)
        self.assertEqual(result, "Invalid task number.")
        self.assertEqual(len(self.tasks), 1)

    def test_update_task(self):
        add_task(self.tasks, "Task 1", "Description 1")
        update_task(self.tasks, 0, "Updated Task 1", "Updated Description 1")
        self.assertEqual(self.tasks[0]["title"], "Updated Task 1")
        self.assertEqual(self.tasks[0]["description"], "Updated Description 1")

    def test_update_task_invalid_index(self):
        add_task(self.tasks, "Task 1", "Description 1")
        result = update_task(self.tasks, 1, "Updated Task 1", "Updated Description 1")
        self.assertEqual(result, "Invalid task number.")
        self.assertEqual(self.tasks[0]["title"], "Task 1")

    def test_mark_task_complete(self):
        add_task(self.tasks, "Task 1", "Description 1")
        mark_task_complete(self.tasks, 0)
        self.assertTrue(self.tasks[0]["completed"])

    def test_mark_task_complete_invalid_index(self):
        add_task(self.tasks, "Task 1", "Description 1")
        result = mark_task_complete(self.tasks, 1)
        self.assertEqual(result, "Invalid task number.")
        self.assertFalse(self.tasks[0]["completed"])

    def test_list_tasks(self):
        add_task(self.tasks, "Task 1", "Description 1")
        tasks_list = list_tasks(self.tasks)
        self.assertEqual(len(tasks_list), 1)
        self.assertIn("[✗] Task 1: Description 1", tasks_list[0])

if __name__ == '__main__':
    unittest.main()
