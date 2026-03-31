from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",          # change if different
    password="Ruchik@1809",
    database="energy_optimization"
)

cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return "Energy Optimization DB is running!"

# 🔹 API to fetch AC energy data
@app.route('/api/ac-data', methods=['GET'])
def get_ac_data():
    cursor.execute("SELECT * FROM ac_energy_data ORDER BY recorded_at DESC")
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
