import unittest
import os
import json
from guestbook import new_entry, delete_entry, list_entries, edit_entry, export_entries


class TestGuestBook(unittest.TestCase):
    def setUp(self):
        if os.path.exists("guestbook.txt"):
            os.remove("guestbook.txt")

    def test_new_entry(self):
        new_entry("This is a test note")
        with open("guestbook.txt", "r") as file:
            entries = file.readlines()
            self.assertEqual(entries[0].strip(), "This is a test note")

    def test_list_entries(self):
        new_entry("Note 1")
        new_entry("Note 2")
        self.assertEqual(list_entries(), ["Note 1", "Note 2"])

    def test_edit_entry(self):
        new_entry("Note 1")
        new_entry("Note 2")
        edit_entry(2, "Changed Note")
        self.assertEqual(list_entries(), ["Note 1", "Changed Note"])

    def test_export_entries(self):
        new_entry("Note 1")
        new_entry("Note 2")
        self.assertEqual(export_entries(), json.dumps(["Note 1", "Note 2"]))

    def test_delete_entry(self):
        new_entry("Note 1")
        new_entry("Note 2")
        delete_entry(1)
        self.assertEqual(list_entries(), ["Note 1"])


if __name__ == "__main__":
    unittest.main()
