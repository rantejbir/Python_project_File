# Model/cheese_record.py

class CheeseRecord:
    def __init__(self, cheese_id, cheese_name_en, cheese_name_fr, manufacturer_name_en, manufacturer_name_fr,
                 manufacturer_prov_code, manufacturing_type_en, manufacturing_type_fr, website_en, website_fr,
                 fat_content_percent, moisture_percent, particularities_en, particularities_fr, flavour_en,
                 flavour_fr, characteristics_en, characteristics_fr, ripening_en, ripening_fr, organic,
                 category_type_en, category_type_fr, milk_type_en, milk_type_fr, milk_treatment_type_en,
                 milk_treatment_type_fr, rind_type_en, rind_type_fr, last_update_date):
        self.cheese_id = cheese_id
        self.cheese_name_en = cheese_name_en
        self.cheese_name_fr = cheese_name_fr
        self.manufacturer_name_en = manufacturer_name_en
        self.manufacturer_name_fr = manufacturer_name_fr
        self.manufacturer_prov_code = manufacturer_prov_code
        self.manufacturing_type_en = manufacturing_type_en
        self.manufacturing_type_fr = manufacturing_type_fr
        self.website_en = website_en
        self.website_fr = website_fr
        self.fat_content_percent = fat_content_percent
        self.moisture_percent = moisture_percent
        self.particularities_en = particularities_en
        self.particularities_fr = particularities_fr
        self.flavour_en = flavour_en
        self.flavour_fr = flavour_fr
        self.characteristics_en = characteristics_en
        self.characteristics_fr = characteristics_fr
        self.ripening_en = ripening_en
        self.ripening_fr = ripening_fr
        self.organic = organic
        self.category_type_en = category_type_en
        self.category_type_fr = category_type_fr
        self.milk_type_en = milk_type_en
        self.milk_type_fr = milk_type_fr
        self.milk_treatment_type_en = milk_treatment_type_en
        self.milk_treatment_type_fr = milk_treatment_type_fr
        self.rind_type_en = rind_type_en
        self.rind_type_fr = rind_type_fr
        self.last_update_date = last_update_date

    def display(self):
        print("Cheese ID:", self.cheese_id)
        print("Cheese Name (English):", self.cheese_name_en)
        print("Cheese Name (French):", self.cheese_name_fr)
        print("Manufacturer Name (English):", self.manufacturer_name_en)
        print("Manufacturer Name (French):", self.manufacturer_name_fr)
        print("Manufacturer Prov Code:", self.manufacturer_prov_code)
        print("Manufacturing Type (English):", self.manufacturing_type_en)
        print("Manufacturing Type (French):", self.manufacturing_type_fr)
        print("Website (English):", self.website_en)
        print("Website (French):", self.website_fr)
        print("Fat Content Percent:", self.fat_content_percent)
        print("Moisture Percent:", self.moisture_percent)
        print("Particularities (English):", self.particularities_en)
        print("Particularities (French):", self.particularities_fr)
        print("Flavour (English):", self.flavour_en)
        print("Flavour (French):", self.flavour_fr)
        print("Characteristics (English):", self.characteristics_en)
        print("Characteristics (French):", self.characteristics_fr)
        print("Ripening (English):", self.ripening_en)
        print("Ripening (French):", self.ripening_fr)
        print("Organic:", self.organic)
        print("Category Type (English):", self.category_type_en)
        print("Category Type (French):", self.category_type_fr)
        print("Milk Type (English):", self.milk_type_en)
        print("Milk Type (French):", self.milk_type_fr)
        print("Milk Treatment Type (English):", self.milk_treatment_type_en)
        print("Milk Treatment Type (French):", self.milk_treatment_type_fr)
        print("Rind Type (English):", self.rind_type_en)
        print("Rind Type (French):", self.rind_type_fr)
        print("Last Update Date:", self.last_update_date)
        print()
