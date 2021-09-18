
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
load_dotenv()

class db:
    @staticmethod
    def check_if_table_exists(conn, table_name):
        table_name = table_name.replace("@gmail.com", "")
        cur = conn.cursor()
        cur.execute("select * from information_schema.tables where table_name=%s", (table_name,))
        result = bool(cur.rowcount)
        cur.close()

        return result

    @staticmethod
    def create_client_table(conn, client_email, ):
        client_email = client_email.replace("@gmail.com", "")
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE {client_email} (id SERIAL PRIMARY KEY, date_string VARCHAR, weight VARCHAR);")
        cur.close()
        conn.commit()

    @staticmethod
    def get_table(conn, email):
        email = email.replace("@gmail.com", "")

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {email};")
        results = cur.fetchall()
        cur.close()
        print(results)
        print(type(results))
        return results

    @staticmethod
    def insert_to_table(conn, email: str, date_string: str, weight: str):
        email = email.replace("@gmail.com", "")
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {email} (date_string, weight) VALUES(%s, %s)", (date_string, weight) )
        cur.close()

        # conn.commit()

if __name__ == '__main__':
    from datetime import datetime
    curmail = "emrecenk9@gmail.com"
    connection_string = os.environ["CONNECTION_STRING_TO_COCKROACHDB"]
    conn = psycopg2.connect(connection_string)

    # print(check_if_table_exists(conn, "emrecenk9@gmail.com"))
    # create_client_table(conn, "emrecenk9@gmail.com")
    # print(check_if_table_exists(conn, "emrecenk9@gmail.com"))

    db.insert_to_table(conn, curmail, str(datetime.now()), "12 kg")
    db.insert_to_table(conn, curmail, str(datetime.now()), "32 kg")
    db.insert_to_table(conn, curmail, str(datetime.now()), "15 kg")
    a = db.get_table(conn, curmail)
    print(a)
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
