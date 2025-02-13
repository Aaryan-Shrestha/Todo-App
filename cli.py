# from functions import get_todos, write_todos
import functions
import time


print("Todo List App")

current_time = time.strftime("%d %b, %Y %H:%M:%S")
print("THe time is given below: ")
print(f"It is {current_time}")

while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):   # Bitwise OR Operator
        todos = functions.get_todos()

        # Trying to remove '\n' from the list
        # Method 1:
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # Method 2:
        # List Comprehension
        # new_todos = [item.strip("\n") for item in todos]

        # Method 3: Simplest Method
        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.capitalize()
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("What is the new todo? ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)


        except ValueError:
            print("You have entered a wrong sequence of command. Try again!")
            continue

    elif user_action.startswith("complete"):
        try:
            completed_todo = int(user_action[9:])

            todos = functions.get_todos()
            index = completed_todo - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo: '{todo_to_remove}' was removed from the list."
            print(message)

        except IndexError:
            print("There is no todo with that number in the todo-list.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")
print("Bye!")