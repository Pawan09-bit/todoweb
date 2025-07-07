def read_todo(filename="todo.txt"):
    with open(filename, "r") as file1:
        my_todos = file1.readlines()
        return my_todos


def write_todo(todo_list, filename="todo.txt"):
    with open(filename, "w") as file:
        file.writelines(todo_list)


# print(type(__name__))

if __name__ == "__main__":
    print("this is library")
    print(read_todo())

# print("code completed")