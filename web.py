import streamlit as st
import functions as fc

todos = fc.get_todos()
st.set_page_config(layout="wide", page_title="ToDo-WebApp")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fc.write_todos(todos)

st.title("ToDo Web-App")
st.subheader("The ToDo App for Web view")
st.write("Use the To-Do App in your Webbrowser. <b>Simply cool!</b>",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fc.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new ToDO ...", 
              on_change=add_todo, key="new_todo")
