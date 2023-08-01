import unittest
import sqlite3
import os
from Presentation.PresentationLayer import PresentationLayer

class TestPresentationLayer(unittest.TestCase):
    def setUp(self):
        # Create a temporary SQLite database file for testing
        self.database_file = 'test_database.db'
        self.connection = sqlite3.connect(self.database_file)
        self.presentation_layer = PresentationLayer(database_connection=self.connection)

    def tearDown(self):
        # Close the database connection and delete the temporary database file
        self.connection.close()
        if os.path.exists(self.database_file):
            os.remove(self.database_file)

    def test_add_record(self):
        # Test adding a new record
        initial_record_count = len(self.presentation_layer.record_list)

        new_record_data = {
            'cheese_id': '999',
            'cheese_name_en': 'Test Cheese',
            'manufacturer_name_en': 'Test Manufacturer',
            # Add other required attributes here
        }

        self.presentation_layer.create_record(**new_record_data)

        self.assertEqual(len(self.presentation_layer.record_list), initial_record_count + 1)

    def test_delete_record(self):
        # Test deleting an existing record
        # Assume there is an existing record with cheese_id = '228'
        initial_record_count = len(self.presentation_layer.record_list)

        self.presentation_layer.select_and_delete_record('228')

        self.assertEqual(len(self.presentation_layer.record_list), initial_record_count - 1)

if __name__ == '__main__':
    unittest.main()
