import sqlite3
import json

def update_metal(id, metal_data):
    with sqlite3.connect("./kneel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Metals
                SET
                    metal = ?,
                    price = ?
            WHERE id = ?
            """,
            (metal_data['metal'], metal_data['price'], id)
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False
