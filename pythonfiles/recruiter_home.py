import sqlite3

# def get_all_jobs():
#     conn1 = sqlite3.connect('db/hireme.db')
#     cursor1 = conn1.cursor()
#     cursor1.execute('SELECT * FROM jobs')
#     jobs = cursor1.fetchall()
#     conn1.close()
#     return jobs

def get_all_jobs():
    conn = sqlite3.connect('db/hireme.db')
    conn.row_factory = sqlite3.Row  # Allows dict-style access
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM jobs')
    rows = cursor.fetchall()

    jobs = [dict(row) for row in rows]  # Convert each row to a dict

    conn.close()
    return jobs