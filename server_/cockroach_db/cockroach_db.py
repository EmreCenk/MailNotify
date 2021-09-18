
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
load_dotenv()

def check_if_table_exists(conn, table_name):
    sql_ = f"select * from information_schema.tables where table_name=%s"

    cur = conn.cursor()
    cur.execute(sql_, (table_name,))
    result = bool(cur.rowcount)
    cur.close()
    return result


connection_string = os.environ["CONNECTION_STRING_TO_COCKROACHDB"]
conn = psycopg2.connect(connection_string)
doesit = check_if_table_exists(conn, "student")
print(doesit)

conn.close()
#
# #creating a cursor
# cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
# # cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")
# # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Emre",) )
# cur.execute("SELECT * FROM student;")
#
# # cur.execute("SELECT * FROM student WHERE id = %s;", (1,))
# # print(cur.fetchone()["id"])
# print(cur.fetchall())
# conn.commit()
# cur.close()
#
