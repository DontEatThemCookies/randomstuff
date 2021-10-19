#!/usr/bin/env python3

# A very basic todo app
# Shelve module is used for object persistence

# 10/19/2021

import shelve
import datetime

def main():

    def w():
        print('')

    def todo():
        print('To-Do List:')
        w()
        if db == {}:
            print('Looks like the list is empty!')
            print('Why not start adding a few tasks todo?')
        else:
            print('ID | To-Do')
            w()
            for k, v in db.items():
                print(k+' | '+str(v))

    def split(text: str) -> (str, str):
        text = text.strip()
        space = text.find(' ')
        if space > 0:
            return text[:space], text[space + 1:]
        return text, "Error: No arguments."

    db = shelve.open('todo')
    idn = 0

    print('Type HELP for commands.')
    w()
    
    todo()
    print('===============================================')
    while True:
        query = input()
        query, args = split(query)

        if query.upper() == "NEW":
            a = args
            if args != "Error: No arguments.":
                idn = idn+1
                db[str(idn)] = a
                print('Successfully created a new task.')
                w()
            else:
                print('No description specified.')
                w()

        if query.upper() == "DONE":
            a = args
            try:
                int(a)
            except:
                print('Invalid ID number.')
            if db != {}:
                for key in db:
                    if key in a:
                        del db[str(a)]
                        print('Successfully marked task as done.')
                    else:
                        print('Did not find a todo with the provided ID.')
            else:
                print('The todo list seems to be empty.')
            w()

        if query.upper() == "TODO":
            todo()
            w()

        if query.upper() == "HELP":
            print('NEW [description] - Creates a new task')
            print('DONE [id] - Marks the specified task as done (deletes it)')
            print('TODO - Shows all tasks in a list.')
            print('EXIT - Exits the program.')
            w()
            
        if query.upper() == "EXIT":
            exit()


if __name__ == '__main__':
    main()
else:
    # Exit program if ToDo is imported as a module
    exit()

# Version 1
    
# To Do (ironic):
# Implement deadlines
