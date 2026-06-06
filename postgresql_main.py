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

        
        category = input("please entre a category: ")
        if category.lower() == "quit":
            break
        elif category == "":
            print("category not found")
            continue
        
        amount = input("please entre a amount: ")
        
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
        print(row[0],"-",row[1],"-", row[2])



def calculate_total():

    cursor.execute("select sum(amount) from expenses")

    row = cursor.fetchone()
    
    print("total : ", float(row[0]))


def calculate_category_total():

    cursor.execute("select category,sum(amount) from expenses GROUP by category")

    rows = cursor.fetchall()

    for row in rows:
        print("category total: ", row[0], row[1])

def delete_expenses():

    while True:
        id = input("insert an id: ")
        if id == "":
            print("invalid id")
            continue
        elif id =="0":
            break
        try:
            id = int(id)
        except ValueError:
            print("please entre a valid number")
            continue
        
        cursor.execute("delete from expenses where id = %s",(id,))

        conn.commit()
        print("Expenses deleated!")

def update_expenses():
    while True:
        id = input("insert an id: ")
        if id == "":
            print("invalid id!")
            continue
        elif id == "0":
            break
        try:
            id = int(id)
        except:
            print("please entre a valid id!")
            continue

        amount = input("please entre the updated amount: ")

        if amount == "":
            print("invalid amount!")
            continue
        try:
            amount = float(amount)
        except ValueError:
            print("please entre a valid amount!")
            continue

        cursor.execute("update expenses set amount = amount + %s where id = %s",(amount,id))

        conn.commit()
        print ("amount updated!")

        
         
    
            

    




def main_menu():

    
    while True:
        print("1. Add expenses")
        print("2. View expenses")
        print("3. Calculate total")
        print("4. Calculate category total")
        print("5. Delete expenses")
        print("6.Update expenses")
        print("7. Quit")

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
            delete_expenses()
        elif choice == "6":
            update_expenses()
        elif choice == "7":
            break
        else:
            print("invalid choice")

            
        
        
main_menu()
conn.close()
    
