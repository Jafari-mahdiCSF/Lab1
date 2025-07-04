import psycopg2
import csv
from config import config

def create_table():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        )
        """,
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        print("PhoneBook table created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_user_console():
    first_name = input("Enter user first name: ")
    phone = input("Enter user phone: ")
    sql = """INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (first_name, phone))
        conn.commit()
        cur.close()
        print("User added to phonebook.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_from_csv(filename):
    sql = """INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cur.execute(sql, (row[0], row[1]))
        conn.commit()
        cur.close()
        print("Data uploaded from CSV.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_user():
    choice = input("Update (1) Name or (2) Phone? ")
    if choice == "1":
        phone = input("Enter phone to find user: ")
        new_name = input("Enter new name: ")
        sql = """UPDATE phonebook SET first_name = %s WHERE phone = %s"""
        values = (new_name, phone)
    elif choice == "2":
        name = input("Enter user name: ")
        new_phone = input("Enter new phone: ")
        sql = """UPDATE phonebook SET phone = %s WHERE first_name = %s"""
        values = (new_phone, name)
    else:
        print("Invalid choice.")
        return

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Record updated.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def query_data():
    print("Query Options: 1) All, 2) By Name, 3) By Phone Prefix")
    choice = input("Choose: ")
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if choice == "1":
            cur.execute("SELECT * FROM phonebook")
        elif choice == "2":
            name = input("Enter name: ")
            cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
        elif choice == "3":
            prefix = input("Enter phone prefix: ")
            cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix + '%',))
        else:
            print("Invalid choice.")
            return
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def delete_user():
    print("Delete by: 1) Name or 2) Phone")
    choice = input("Choose: ")
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if choice == "1":
            name = input("Enter name: ")
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        elif choice == "2":
            phone = input("Enter phone: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        else:
            print("Invalid choice.")
            return
        conn.commit()
        print("Record deleted.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def main():
    while True:
        print("\nPhoneBook Menu")
        print("1. Create table")
        print("2. Insert user from console")
        print("3. Upload from CSV")
        print("4. Update user")
        print("5. Query data")
        print("6. Delete user")
        print("7. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            create_table()
        elif choice == "2":
            insert_user_console()
        elif choice == "3":
            filename = input("CSV filename: ")
            insert_from_csv(filename)
        elif choice == "4":
            update_user()
        elif choice == "5":
            query_data()
        elif choice == "6":
            delete_user()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
