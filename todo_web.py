import streamlit as st
from streamlit import checkbox
import functions



st.title("My Todo App")
st.subheader("Application to manage Todo")
st.write("You can manage your daily Todo")
# st.checkbox("Read")
# st.checkbox("Write")
todos =functions.read_todo()
def add_todo():
    todo1=st.session_state['new_todo'] +"\n"
    # print(todo1)
    todos.append(todo1)
    functions.write_todo(todos)
    st.session_state['new_todo']=""


for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo,key =todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="Enter a todo",placeholder="Type a todo",key = "new_todo",on_change=add_todo)






