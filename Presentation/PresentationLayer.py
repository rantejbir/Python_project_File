import csv
from Data.data_set_reader import DataSetReader
from Model.cheese_record import CheeseRecord  # Add this import statement

class PresentationLayer:
    def __init__(self, database_connection):
        self.record_list = []
        self.database_connection = database_connection

    def display_full_name(self):
        print("Rantejbir Singh")

    def load_data(self):
        database_file = "cheese_database.db"
        self.record_list = self.data_set_reader.load_records(database_file)


    def reload_data(self):
        self.load_data()

    def persist_data(self, record_list, filename):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for record in record_list:
                    writer.writerow(record.__dict__.values())

            print(f"Data has been successfully persisted to '{filename}'.")
        except Exception as ex:
            print(f"Error occurred while persisting data: {str(ex)}")

    def display_records(self):
        for cheese in self.record_list:
            cheese.display()
            print()

    def select_and_display_record(self):
        cheese_id = input("Enter the Cheese ID of the record to display: ")
        for record in self.record_list:
            if record.cheese_id == cheese_id:
                record.display()
                return
        print("Record not found.")

    def select_and_display_multiple_records(self):
        num_records = int(input("Enter the number of records to display: "))
        for i in range(num_records):
            if i >= len(self.record_list):
                break
            self.record_list[i].display()
            print()

    def create_record(self):
        print("Enter the details for the new record:")
        cheese_id = input("Cheese ID: ")
        cheese_name = input("Cheese Name: ")
        manufacturer_name = input("Manufacturer Name: ")
        manufacturer_prov_code = input("Manufacturer Prov Code: ")
        manufacturing_type = input("Manufacturing Type: ")
        website = input("Website: ")
        fat_content = input("Fat Content: ")
        moisture_content = input("Moisture Content: ")
        particularities = input("Particularities: ")
        flavour = input("Flavour: ")
        characteristics = input("Characteristics: ")
        ripening = input("Ripening: ")
        organic = input("Organic: ")
        category_type = input("Category Type: ")
        milk_type = input("Milk Type: ")
        milk_treatment_type = input("Milk Treatment Type: ")
        rind_type = input("Rind Type: ")
        last_update_date = input("Last Update Date: ")

        # Create a new CheeseRecord object with the entered values
        new_record = CheeseRecord(
            cheese_id,
            cheese_name,
            manufacturer_name,
            manufacturer_prov_code,
            manufacturing_type,
            website,
            fat_content,
            moisture_content,
            particularities,
            flavour,
            characteristics,
            ripening,
            organic,
            category_type,
            milk_type,
            milk_treatment_type,
            rind_type,
            last_update_date
        )

        # Add the new record to self.record_list
        self.record_list.append(new_record)

        print("New record created successfully.")

    def select_and_edit_record(self):
        record_id = input("Enter the ID of the record you want to select and edit: ")
        selected_record = None

        # Find the record with the matching ID
        for record in self.record_list:
            if record.cheese_id == record_id:
                selected_record = record
                break

        if selected_record is not None:
            print("Selected Record:")
            selected_record.display()

            # Prompt the user to enter new attribute values
            print("Enter the new values for the record attributes:")
            selected_record.cheese_name = input("Cheese Name: ")
            selected_record.manufacturer_name = input("Manufacturer Name: ")
            selected_record.manufacturer_prov_code = input("Manufacturer Prov Code: ")
            selected_record.manufacturing_type = input("Manufacturing Type: ")
            selected_record.website = input("Website: ")
            selected_record.fat_content = input("Fat Content: ")
            selected_record.moisture_content = input("Moisture Content: ")
            selected_record.particularities = input("Particularities: ")
            selected_record.flavour = input("Flavour: ")
            selected_record.characteristics = input("Characteristics: ")
            selected_record.ripening = input("Ripening: ")
            selected_record.organic = input("Organic: ")
            selected_record.category_type = input("Category Type: ")
            selected_record.milk_type = input("Milk Type: ")
            selected_record.milk_treatment_type = input("Milk Treatment Type: ")
            selected_record.rind_type = input("Rind Type: ")
            selected_record.last_update_date = input("Last Update Date: ")

            print("Record updated successfully.")
        else:
            print("Record not found.")

    def select_and_delete_record(self):
        cheese_id = input("Enter the Cheese ID of the record to delete: ")
        for record in self.record_list:
            if record.cheese_id == cheese_id:
                self.record_list.remove(record)
                print("Record deleted successfully.")
                return
        print("Record not found.")

    def run(self):
        self.display_full_name()
        self.load_data()
        self.display_records()
        while True:
            while True:
                print("Interactive Options:")
                print("1. Reload data from dataset")
                print("2. Persist data to disk")
                print("3. Select and display record(s)")
                print("4. Create a new record")
                print("5. Select and edit a record")
                print("6. Select and delete a record")
                print("0. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.load_data()
                    self.display_records()
                    print("Data reloaded from dataset.")

                elif choice == "2":
                    filename = input("Enter the filename for the new CSV file: ")
                    self.persist_data(self.record_list, filename)
                    print(f"Data persisted to {filename}.")

                elif choice == "3":
                    display_options = input("Enter '1' to display one record, '2' to display multiple records: ")
                    if display_options == "1":
                        self.select_and_display_record()
                    elif display_options == "2":
                        self.select_and_display_multiple_records()
                    else:
                        print("Invalid input.")

                elif choice == "4":
                    self.create_record()

                elif choice == "5":
                    self.select_and_edit_record()

                elif choice == "6":
                    self.select_and_delete_record()

                elif choice == "0":
                    print("Exiting the program.")
                    break

                else:
                    print("Invalid choice. Please try again.")


if __name__ == '__main__':
    presentation_layer = PresentationLayer()
    presentation_layer.run()
