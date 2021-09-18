
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
load_dotenv()

def check_if_table_exists(conn, table_name):
    table_name = table_name.replace("@gmail.com", "")
    cur = conn.cursor()
    cur.execute("select * from information_schema.tables where table_name=%s", (table_name,))
    result = bool(cur.rowcount)
    cur.close()

    return result

def create_client_table(conn, client_email, ):
    client_email = client_email.replace("@gmail.com", "")
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE {client_email} (id SERIAL PRIMARY KEY, date_string VARCHAR, weight VARCHAR);")
    cur.close()
    conn.commit()

if __name__ == '__main__':

    connection_string = os.environ["CONNECTION_STRING_TO_COCKROACHDB"]
    conn = psycopg2.connect(connection_string)
    print(check_if_table_exists(conn, "emrecenk9@gmail.com"))
    create_client_table(conn, "emrecenk9@gmail.com")
    print(check_if_table_exists(conn, "emrecenk9@gmail.com"))
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
