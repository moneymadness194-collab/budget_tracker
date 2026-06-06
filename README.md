# budget_tracker
This is my first proper project i worked on while learmning backend and all fundamentals

Mainly the structure is:
|
|-----> connecting with postgresql at the top for recording expenses
|-----> using 5 functions for each action
   |
   |--> add_expense()--|For adding expenses with try and expect to avoide bugs when no value is added or string in the place of amount|
   |--> view_expenses()--|for retaining the table from postgre database and viewing in pannel|
   |--> calculate_total()--|Its for calculating the overall total of the table and retaining the value|
   |-->calculate_category_total()--|Its for calculating total per category and retaining that information|
   |
   Lastly there is the main function 
   -->main_menu()--->|I used loop and made a option screen inside the fucnction and assigned 1-5 integers to options and each option calls a function and it|                                                   \|continues until the choice is quit i have also used error handling in most part|/


