import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="Enter a todo", label_visibility="collapsed", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

