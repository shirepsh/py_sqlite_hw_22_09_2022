"""
1. build a py contats prog
2. build a py prog who create the db (on sqlite3)
3. connect between the prog. real actions as insert, delete, selecte insted print
"""

from enum import Enum
from helper_sql_prog import *

class Actions (Enum):
    ADD_CONTCAT = 1
    SEARCH_CONTACT = 2
    DELETE_CONTACT = 3
    PRINT_ALL = 4
    EXIT = 5

def menu ():
    for opt in Actions:
        print (f"{opt.value} - {opt.name}")
    return int(input("select an option: "))
        
def main ():
    user_selection = menu()
    while user_selection != Actions.EXIT.value:
        if user_selection == Actions.ADD_CONTCAT.value: add_contact()
        if user_selection == Actions.SEARCH_CONTACT.value: search_a_contact()
        if user_selection == Actions.DELETE_CONTACT.value: delete_contact ()
        if user_selection == Actions.PRINT_ALL.value: print_all()
        user_selection = menu()

if __name__ == "__main__":
    main()

    
        






