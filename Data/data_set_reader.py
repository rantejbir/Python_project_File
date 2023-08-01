import sqlite3

from Model.cheese_record import CheeseRecord


class DataSetReader:
    # Rest of the class remains unchanged

    def load_records(self, database_file):
        records = []
        try:
            with sqlite3.connect(database_file) as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM cheese_records")
                rows = c.fetchall()
                for row in rows:
                    # Modify the following line to pass the correct number of arguments to CheeseRecord
                    record = CheeseRecord(*row)
                    records.append(record)
            return records
        except sqlite3.Error as e:
            print(f"Error loading records from the database: {e}")
            return []
