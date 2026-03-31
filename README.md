STEP 1 — Start MySQL Server
Option A (Recommended)
Press Windows key
Search → Services
Find → MySQL80
Status must be Running
If not → Right click → Start

✅ MySQL is now running in background

STEP 2 — Open MySQL Workbench
Open MySQL Workbench
Click connection:
Local instance MySQL80
Enter password: (your password)

STEP 3 — Open VS Code
Open VS Code
File → Open Folder
Select:
energy-optimization_db

STEP 4 — Open Terminal in VS Code

STEP 5 — Activate Virtual Environment
.venv\Scripts\Activate

STEP 6 — Install Requirements
pip install flask mysql-connector-python python-dotenv

STEP 7 — Run Flask API
python app.py

STEP 8 — Open Browser
Test server
http://127.0.0.1:5000

STEP 9 — Start Live Data Simulation (NEW TERMINAL)
.venv\Scripts\Activate
python simulate_data.py

STEP 10 — Verify Live Insert in Workbench
SELECT * FROM ac_energy_data ORDER BY recorded_at DESC;

