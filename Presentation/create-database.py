import sqlite3

def create_table():
    conn = sqlite3.connect("cheese_database.db")
    c = conn.cursor()

    # Create the cheese_records table
    c.execute("""
        CREATE TABLE IF NOT EXISTS cheese_records (
            CheeseId INTEGER PRIMARY KEY,
            CheeseNameEn TEXT,
            CheeseNameFr TEXT,
            ManufacturerNameEn TEXT,
            ManufacturerNameFr TEXT,
            ManufacturerProvCode TEXT,
            ManufacturingTypeEn TEXT,
            ManufacturingTypeFr TEXT,
            WebSiteEn TEXT,
            WebSiteFr TEXT,
            FatContentPercent REAL,
            MoisturePercent REAL,
            ParticularitiesEn TEXT,
            ParticularitiesFr TEXT,
            FlavourEn TEXT,
            FlavourFr TEXT,
            CharacteristicsEn TEXT,
            CharacteristicsFr TEXT,
            RipeningEn TEXT,
            RipeningFr TEXT,
            Organic INTEGER,
            CategoryTypeEn TEXT,
            CategoryTypeFr TEXT,
            MilkTypeEn TEXT,
            MilkTypeFr TEXT,
            MilkTreatmentTypeEn TEXT,
            MilkTreatmentTypeFr TEXT,
            RindTypeEn TEXT,
            RindTypeFr TEXT,
            LastUpdateDate TEXT
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
