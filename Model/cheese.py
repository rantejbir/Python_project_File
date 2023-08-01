# Super-class for CheeseRecord objects
class Cheese:
    def __init__(self, cheese_id, cheese_name):
        self.cheese_id = cheese_id
        self.cheese_name = cheese_name

    def display(self):
        print(f"Cheese ID: {self.cheese_id}")
        print(f"Cheese Name: {self.cheese_name}")


# Subclass to represent a specific type of cheese
class SpecificCheese(Cheese):
    def __init__(self, cheese_id, cheese_name, additional_info):
        super().__init__(cheese_id, cheese_name)
        self.additional_info = additional_info

    # Override the display method to include additional_info
    def display(self):
        super().display()
        print(f"Additional Info: {self.additional_info}")
