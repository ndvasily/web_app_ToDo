import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# gi raspredeluva elementite kako sto se podredeni vo kodot.
st.title("My Todo App")  # naslovot go printa prv, podnaslov vtor i tn.
st.subheader("This is my todo app.")
st.write("This app is to help you complete more tasks daily.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key='new_todo')

st.session_state  # dopolnitelen prozor koj ni dava realtime input
# sekoj item mora da ima key za da bide prikazan vo sstate
