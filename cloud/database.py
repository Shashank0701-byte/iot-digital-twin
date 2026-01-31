import sqlite3

DB_NAME = "telemetry.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            timestamp INTEGER,
            temperature REAL,
            humidity REAL,
            edge_alerts TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_telemetry(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO telemetry (device_id, timestamp, temperature, humidity, edge_alerts)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["device_id"],
        data["timestamp"],
        data.get("temperature"),
        data.get("humidity"),
        ",".join(data.get("edge_alerts", []))
    ))

    conn.commit()
    conn.close()
