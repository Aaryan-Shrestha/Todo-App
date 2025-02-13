FILEPATH = "todo.txt"

def get_todos(file_path=FILEPATH):
    """Reads a text file and return the list of to-do items"""
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()  # It will create a list containing all the text inside the file in each line.
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """Writes the to-do items list in the text file"""
    with open(file_path, "w") as file:
        file.writelines(todos_arg)

# print(__name__) # In this file, its value is __main__, but when this file is import by any other .py file its value is file name (i.e functions in this case)
# Following code prevents the code at line 16 and 17 from being executed by other files when its imported.
if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())