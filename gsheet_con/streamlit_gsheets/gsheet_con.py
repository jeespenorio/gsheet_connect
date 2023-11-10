import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json

# Load JSON key from keys.json
with open('keys.json') as f:
    service_account_key = json.load(f)

# Load credentials with additional scopes
credentials = Credentials.from_service_account_info(
    service_account_key,
    scopes=[
        'https://www.googleapis.com/auth/spreadsheets',  # for read and write access
        'https://www.googleapis.com/auth/drive',  # if you need access to Google Drive
    ]
)

# Authenticate with gspread
gc = gspread.authorize(credentials)

# Open the Google Sheets document by title
spreadsheet_title = 'GSheets_DataBase'  # Replace with your actual spreadsheet title
sh = gc.open(spreadsheet_title)

# Access a specific worksheet
worksheet_title = 'Product'
worksheet = sh.worksheet(worksheet_title)

# Get all values from the worksheet
values = worksheet.get_all_values()

# Perform Inventory Health Check
# Filter rows where "Current Inventory Level" is less than "Reorder Level"
threshold = 10
low_inventory_items = [row for row in values[1:] if int(row[3]) < int(row[4])]

# Display the values and health check result in Streamlit
st.table(values)
st.subheader("Inventory Health Check:")
if low_inventory_items:
    st.warning(f"The following items have low inventory (below reorder level):")
    st.table(low_inventory_items)
else:
    st.success("Inventory is healthy!")

# CRUD Operations
st.sidebar.subheader("CRUD Operations")

# Create Operation
st.sidebar.header("Create")
new_item = st.text_input("Enter a new item:")
if st.button("Add Item"):
    worksheet.append_row([new_item])

# Update Operation
st.sidebar.header("Update")
update_index = st.number_input("Enter the index to update:", min_value=2, max_value=len(values), step=1)
updated_value = st.text_input("Enter the updated value:")
if st.button("Update Item"):
    worksheet.update(f'A{update_index}', updated_value)

# Delete Operation
st.sidebar.header("Delete")
delete_index = st.number_input("Enter the index to delete:", min_value=2, max_value=len(values), step=1)
if st.button("Delete Item"):
    worksheet.delete_row(delete_index)

# Read Operation
st.sidebar.header("Read")
st.write("Current Data:")
st.table(values)
