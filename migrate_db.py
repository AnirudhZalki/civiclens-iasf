import sqlite3

DB_FILE = 'civic.db'

def migrate_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    try:
        # Add latitude column
        try:
            cursor.execute("ALTER TABLE issues ADD COLUMN latitude REAL")
            print("Added latitude column.")
        except sqlite3.OperationalError:
            print("latitude column already exists.")
            
        # Add longitude column
        try:
            cursor.execute("ALTER TABLE issues ADD COLUMN longitude REAL")
            print("Added longitude column.")
        except sqlite3.OperationalError:
            print("longitude column already exists.")
            
        conn.commit()
        print("Migration completed successfully.")
    except Exception as e:
        print(f"Migration failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_db()
