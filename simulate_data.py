import time
import random
import mysql.connector
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

print("🔁 Live AC Data Simulation Started...")

while True:
    voltage = round(random.uniform(220, 240), 2)
    current = round(random.uniform(4.5, 6.5), 2)
    power = round(voltage * current, 2)
    energy = round(power / 1000, 3)
    frequency = 50
    power_factor = round(random.uniform(0.90, 0.99), 2)

    sql = """
        INSERT INTO ac_energy_data
        (voltage, current, power, energy, frequency, power_factor)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (voltage, current, power, energy, frequency, power_factor)

    cursor.execute(sql, values)
    db.commit()

    print(f"Inserted → V:{voltage} I:{current} P:{power}")

    time.sleep(5)  # every 5 seconds
