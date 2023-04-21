import codecs

def get_todos():
    with codecs.open('todos.txt', 'r', 'utf-8') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_global):
    with codecs.open("todos.txt", "w", 'utf-8') as file:
        file.writelines(todos_global)