
import streamlit as st
import pandas as pd
import plotly.express as px
import database
from datetime import date

st.set_page_config(
    page_title="Personal Finance Manager",
    page_icon="💰",
    layout="wide"
)

# Initialize permanent database
database.initialize_database()

st.title("💰 Personal Finance Manager")
st.caption("Track your money. Control your spending.")

# Add transaction form
st.header("➕ Add Income or Expense")

with st.form("transaction_form", clear_on_submit=True):

    transaction_type = st.selectbox(
        "Transaction Type",
        ["Income", "Expense"]
    )

    description = st.text_input(
        "Description",
        placeholder="e.g. Pocket money or Lunch"
    )

    if transaction_type == "Income":
        categories = [
            "Salary", "Pocket Money", "Freelance", "Business", "Other"
        ]
    else:
        categories = [
            "Food", "Travel", "Shopping", "Education",
            "Bills", "Health", "Entertainment", "Other"
        ]

    category = st.selectbox("Category", categories)

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=50.0
    )

    transaction_date = st.date_input(
        "Date",
        value=date.today()
    )

    # IMPORTANT: Define submitted inside the form
    submitted = st.form_submit_button(
        "Add Transaction",
        use_container_width=True
    )

# Process the submitted form OUTSIDE the form block
if submitted:
    if not description.strip():
        st.error("Please enter a description.")
    elif amount <= 0:
        st.error("Amount must be greater than zero.")
    else:
        database.add_transaction(
            transaction_date,
            description.strip(),
            category,
            transaction_type,
            amount
        )
        st.success("Transaction saved successfully!")
        st.rerun()

# Load saved transactions from SQLite
df = database.get_transactions()

# Calculate financial totals
income = df.loc[df["Type"] == "Income", "Amount"].sum()
expenses = df.loc[df["Type"] == "Expense", "Amount"].sum()
balance = income - expenses
savings_rate = balance / income * 100 if income > 0 else 0

st.divider()
st.header("📊 Financial Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Income", f"₹{income:,.2f}")
col2.metric("Total Expenses", f"₹{expenses:,.2f}")
col3.metric("Net Balance", f"₹{balance:,.2f}")
col4.metric("Savings Rate", f"{savings_rate:.1f}%")

# Charts
left, right = st.columns(2)

with left:
    st.subheader("Expenses by Category")

    expense_df = df[df["Type"] == "Expense"]

    if not expense_df.empty:
        category_totals = (
            expense_df.groupby("Category", as_index=False)["Amount"]
            .sum()
        )

        fig = px.pie(
            category_totals,
            names="Category",
            values="Amount",
            hole=0.5
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Add an expense to see your chart.")

with right:
    st.subheader("Income vs Expenses")

    comparison = pd.DataFrame({
        "Type": ["Income", "Expenses"],
        "Amount": [income, expenses]
    })

    fig = px.bar(
        comparison,
        x="Type",
        y="Amount",
        color="Type",
        text="Amount"
    )

    st.plotly_chart(fig, use_container_width=True)

# Transaction history
st.divider()
st.header("📋 Transaction History")

if not df.empty:
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Transactions as CSV",
        data=csv_data,
        file_name="my_transactions.csv",
        mime="text/csv"
    )
else:
    st.info("No transactions saved yet.")
