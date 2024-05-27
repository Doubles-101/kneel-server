import sqlite3
import json

def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        """)
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        orders=[]
        for row in query_results:
            orders.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_orders = json.dumps(orders)

    return serialized_orders


def get_single_order(pk, url_dict):

    with sqlite3.connect("./kneel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        if url_dict["query_params"] == {}:
            # Write the SQL query to get the information you want
            db_cursor.execute("""
            SELECT
                o.id,
                o.metal_id,
                o.size_id,
                o.style_id
            FROM Orders o
            WHERE o.id = ?
            """, (pk,))
            query_results = db_cursor.fetchone()

            # Serialize Python list to JSON encoded string
            dictionary_version_of_object = dict(query_results)
            serialized_order = json.dumps(dictionary_version_of_object)

    return serialized_order


def create_order(metal, size, style):
    with sqlite3.connect("./kneel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Orders (metal_id, size_id, style_id)
            VALUES (?,?,?)
            """,
            (metal, size, style)
        )

        conn.commit()

    return True

def delete_order(pk):
    with sqlite3.connect("./kneel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            DELETE FROM Orders WHERE id = ?
            """,
            (pk,)
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False
