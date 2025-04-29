# streamlit_app/app.py

import streamlit as st
import sys, os

# 1) Page config must come first:
st.set_page_config(
    page_title="Zomato Food Delivery Management",
    page_icon="🍔",
    layout="wide"
)

# 2) Ensure your src folder is on the path:
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 3) Import your shared db and CSS
from src.db_connection import db
#from src.styling import apply_custom_css
#apply_custom_css()

# 4) Now all your UI code:
st.title("🍽️ Zomato Food Delivery Management System")
st.subheader("Welcome")

if db.connection:
    st.success("Connected to database successfully!")
else:
    st.error("Failed to connect to database.")

st.markdown("""
### 1. Data Entry
- Add, update, and delete records for:
    - Customers
    - Restaurants
    - Delivery Personnel
    - Orders
    - Deliveries
- Dynamically create or modify SQL tables (e.g., add columns).

### 2. Data Insights
Gain actionable business insights through five key categories:
- **Peak Ordering Times:** Find out when customers order the most.
- **Delayed Deliveries:** Identify delivery delays and performance issues.
- **Top Customers:** Track high-value or frequent users.
- **Best Delivery Personnel:** Monitor top-performing delivery agents.
- **Most Popular Restaurants:** See which places and cuisines are trending.

### 3. Dynamic Table Manager *(coming soon)*  
- Modify or view the database schema interactively.  
- Create new tables or inspect existing ones.
""")
