import streamlit as st
from src.db_connection import db

st.subheader("Create New Table")

with st.form("create_table_form"):
    new_table_name = st.text_input("Enter new table name")
    column_definitions = st.text_area("Enter column definitions\n (e.g. id INT PRIMARY KEY, name VARCHAR(100), date DATE)")
    create_btn = st.form_submit_button("Create Table")
    if create_btn and new_table_name and column_definitions:
        try:
            query = f"CREATE TABLE {new_table_name} ({column_definitions})"
            db.execute_query(query)
            st.success(f"Table `{new_table_name}` created successfully!")
        except Exception as e:
            st.error(f"Failed to create table: {e}")

st.divider()

st.subheader("Add Column to Existing Table")

tables = db.get_tables()

with st.form("add_column_form"):
    selected_table = st.selectbox("Select table", tables)
    new_column = st.text_input("Enter new column definition (e.g. age INT)")
    add_column_btn = st.form_submit_button("Add Column")

    if add_column_btn and selected_table and new_column:
        try:
            query = f"ALTER TABLE {selected_table} ADD COLUMN {new_column}"
            db.execute_query(query)
            st.success(f"Column `{new_column}` added to `{selected_table}` successfully!")
        except Exception as e:
            st.error(f"Failed to add column: {e}")
