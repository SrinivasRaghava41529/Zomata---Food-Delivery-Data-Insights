import streamlit as st
import pandas as pd
from src.db_connection import db


# Sidebar for insight category selection
category = st.sidebar.selectbox(
    "Select Insight Category",
    [
        "Peak Ordering Times",
        "Delayed Deliveries",
        "Top Customers by Orders",
        "Top Delivery Personnel",
        "Most Popular Restaurants"
    ]
)

# Helper function
def load_data(query):
    data = db.fetch_all(query)
    return pd.DataFrame(data) if data else pd.DataFrame()

# Show insights based on selection
if category == "Peak Ordering Times":
    st.subheader("Peak Ordering Times")
    df = load_data("""
        SELECT HOUR(order_date) AS order_hour, COUNT(*) AS total_orders 
        FROM Orders 
        GROUP BY order_hour 
        ORDER BY order_hour
    """)
    if not df.empty:
        st.bar_chart(df.set_index("order_hour"))
    else:
        st.info("No order data found.")

elif category == "Delayed Deliveries":
    st.subheader("Delayed Deliveries")
    df = load_data("""
        SELECT o.order_id, d.estimated_time, d.delivery_time, 
               TIMESTAMPDIFF(MINUTE, d.estimated_time, d.delivery_time) AS delay_minutes
        FROM Deliveries d
        JOIN Orders o ON d.order_id = o.order_id
        WHERE d.delivery_time > d.estimated_time
    """)
    if not df.empty:
        st.dataframe(df)
        st.metric("Average Delay (min)", round(df["delay_minutes"].mean(), 2))
    else:
        st.info("No delayed deliveries found.")

elif category == "Top Customers by Orders":
    st.subheader("Top Customers by Orders")
    df = load_data("""
        SELECT name, total_orders, average_rating 
        FROM Customers 
        ORDER BY total_orders DESC 
        LIMIT 10
    """)
    st.dataframe(df)

elif category == "Top Delivery Personnel":
    st.subheader("Top Delivery Personnel")
    df = load_data("""
        SELECT name, total_deliveries, average_rating 
        FROM DeliveryPersons 
        ORDER BY average_rating DESC 
        LIMIT 10
    """)
    st.dataframe(df)

elif category == "Most Popular Restaurants":
    st.subheader("Most Popular Restaurants")
    df = load_data("""
        SELECT name, cuisine_type, total_orders, rating 
        FROM Restaurants 
        ORDER BY total_orders DESC 
        LIMIT 10
    """)
    st.dataframe(df)
