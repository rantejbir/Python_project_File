import sqlite3
import csv


def insert_data():
    conn = sqlite3.connect("Presentation/cheese_database.db")
    c = conn.cursor()

    # Read data from the CSV file and insert into the table
    with open('canadianCheeseDirectory.csv', 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            c.execute(
                "INSERT INTO cheese_records (CheeseId, CheeseNameEn, ManufacturerNameEn, ManufacturerProvCode, "
                "ManufacturingTypeEn, WebSiteEn, FatContentPercent, MoisturePercent, ParticularitiesEn, FlavourEn, "
                "CharacteristicsEn, RipeningEn, Organic, CategoryTypeEn, MilkTypeEn, MilkTreatmentTypeEn, RindTypeEn, "
                "LastUpdateDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (row[0], row[1], row[3], row[5], row[6], row[8], row[10], row[11], row[12], row[14], row[16], row[18],
                 row[20], row[22], row[24], row[25], row[26], row[28]))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_data()
