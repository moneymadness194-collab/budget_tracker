import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()

def add_expenses():

    while True:

        
        category = input("please entre a category")
        if category.lower() == "quit":
            break
        elif category == "":
            print("category not found")
            continue
        
        amount = input("please entre a amount")
        
        if amount == "":
            print("amount not found")
            continue
        
        try:
            amount = float(amount)
        except ValueError:
            print("please enter a valid amount")
            continue
        

        cursor.execute(
            """
            insert into expenses(category, amount)
            values(%s, %s)
            """,
            (category, amount)
        )
        conn.commit()

        print("expense added!")
    



def view_expenses():

    cursor.execute("select * from expenses")
    
    rows = cursor.fetchall()

    for row in rows:
        print(row[1], row[2])



def calculate_total():

    cursor.execute("select sum(amount) from expenses")

    row = cursor.fetchall()
    
    print("total : ", row[0])


def calculate_category_total():

    cursor.execute("select category,sum(amount) from expenses GROUP by category")

    rows = cursor.fetchall()

    for row in rows:
        print("category total: ", row[0], row[1])



def main_menu():

    
    while True:
        print("1. Add expenses")
        print("2. view expenses")
        print("3. calculate total")
        print("4.calculate category total")
        print("5. quit")

        choice = input("choice: ")

        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            calculate_category_total()
        elif choice == "5":
            break
        else:
            print("invalid choice")

            
        
        
main_menu()
conn.close()
    
