from db import get_db_connection

try:
    conn = get_db_connection()
    if conn.is_connected():
        print("✅ Connected to MySQL successfully!")
        conn.close()
except Exception as e:
    print("❌ Database connection failed:", e)
