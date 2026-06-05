import json

try:
    
    with open("expenses.json", "r") as file:
     expenses = json.load(file)

except:
    print("no existing expenses found:....")
    
    expenses = []

while True:
      
    category = input("plese enter a category: ")

    if category == "quit":
        break
                

    amount = float(input("plese enter the amount: "))

    expense = {
        "category": category,
        "amount": amount
    }
    expenses.append(expense) 



def calculate_total(expenses):
   
   total = 0

   for expense in expenses:
    total = total + expense["amount"]

   return total




def calculate_category_total(expenses):

    category_total = {}
 
    for expense in expenses:
    
     
     category = expense["category"]
    amount = expense["amount"]

    if category in category_total:
        category_total[category] = category_total[category] + amount

    else:
        category_total[category] = amount

    return category_total

    

print("category:", calculate_category_total(expenses))
print("\nexpenses")
print("total: ", calculate_total(expenses))

with open("expenses.json", "w") as file:
    json.dump(expenses,file)

    print("git test")
    