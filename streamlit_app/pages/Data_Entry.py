import streamlit as st
from src.db_connection import db
import datetime



st.title("Data Entry")

operation = st.sidebar.selectbox(
    "Select Operator",
    ['Add Customer', 'Update Customer', 'Delete Customer']
)

# Add Customer

if operation == 'Add Customer':
    st.header('Add New customer')

    id = st.text_input("ID")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    location = st.text_input("Location")
    signup_date = st.date_input("Signup Date", value=datetime.date.today())
    is_premium = st.selectbox("Is Premium?", ["Yes", "No"])
    preferred_cuisine = st.text_input("Preferred Cuisine")
    total_orders = st.number_input("Total Orders", min_value=0, step=1)
    average_rating = st.slider("Average Rating", 0.0, 5.0, 0.0, step=0.1)

    if st.button('Add Customer'):
        query = """
            INSERT INTO Customers (customer_id,name, email, phone, location, signup_date, is_premium, preferred_cuisine, total_orders, average_rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """
        params = (
            name, email, phone, location, signup_date, 
            1 if is_premium == "Yes" else 0, preferred_cuisine, total_orders, average_rating
        )
        success = db.execute_query(query, params)

        if success:
            st.success(f"Customer '{name}' added successfully!")
        else:
            st.error("Failed to add customer.")

# Update Customer

elif operation == "Update Customer":
    st.header("Update Existing Customer")

    customer_id = st.number_input("Enter Customer ID to Update", min_value=1, step=1)

    field_to_update = st.selectbox("Select Field to Update", [
        "name", "email", "phone", "location", 
        "is_premium", "preferred_cuisine", 
        "total_orders", "average_rating"
    ])

    new_value = st.text_input("Enter New Value")

    if st.button("Update Customer"):
        # Special handling for numerical fields
        if field_to_update in ["total_orders", "average_rating"]:
            try:
                new_value = float(new_value) if field_to_update == "average_rating" else int(new_value)
            except ValueError:
                st.error("Invalid number format!")
                st.stop()

        if field_to_update == "is_premium":
            new_value = 1 if new_value.lower() in ["yes", "1", "true"] else 0

        query = f"""    
            UPDATE Customers
            SET {field_to_update} = %s
            WHERE customer_id = %s
        """
        params = (new_value, customer_id)
        success = db.execute_query(query, params)

        if success:
            st.success(f"Customer ID {customer_id} updated successfully!")
        else:
            st.error("Failed to update customer.")

# Delete customer

elif operation == "Delete Customer":
    st.header("🗑️ Delete Customer")

    customer_id = st.number_input("Enter Customer ID to Delete", min_value=1, step=1)

    if st.button("Delete Customer"):
        query = "DELETE FROM Customers WHERE customer_id = %s"
        params = (customer_id,)
        success = db.execute_query(query, params)

        if success:
            st.success(f"Customer ID {customer_id} deleted successfully!")
        else:
            st.error("Failed to delete customer.")