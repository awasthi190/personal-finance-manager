# 💰 Personal Finance Manager Dashboard

A Python-based personal finance management dashboard that helps users track income and expenses, monitor transactions, and visualize their financial activity through interactive charts.

## 🚀 Features

- **Income Tracking** — Record and manage income transactions.
- **Expense Tracking** — Add and categorize daily expenses.
- **Interactive Dashboard** — View financial summaries and charts.
- **Data Visualization** — Explore financial activity using Plotly charts.
- **Transaction History** — Review previously recorded transactions.
- **SQLite Database** — Persist transaction records locally.
- **CSV Export** — Export transaction data for further analysis.
- **Simple User Interface** — Use a clean dashboard built with Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Dashboard interface |
| SQLite | Local transaction storage |
| Pandas | Data processing |
| Plotly | Interactive charts |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
personal-finance-manager/
│
├── app.py              # Main Streamlit application
├── database.py         # Database operations
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

The SQLite database (`finance.db`) is generated locally when the application initializes. It should not be committed to GitHub.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/awasthi190/personal-finance-manager.git
```

### 2. Open the project directory

```bash
cd personal-finance-manager
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

Your dashboard should open in your browser, usually at `http://localhost:8501`.

## 📊 How to Use

1. Launch the application.
2. Enter an income or expense transaction using the dashboard form.
3. Submit the transaction to save it.
4. Explore the financial summaries and interactive charts.
5. Review your transaction history.
6. Export the available transaction data as a CSV file.

## 🔒 Data and Privacy

- Transaction records are stored in a local SQLite database.
- The database file is excluded from version control.
- Avoid committing passwords, API keys, personal financial records, or other sensitive information.
- This project is intended for personal tracking and educational use; it is not a substitute for professional financial advice.

## 🎯 Project Goals

This project demonstrates practical skills in Python development, database integration, data analysis, interactive visualization, and building a web-based dashboard.

## 🔮 Future Improvements

- Monthly budgets and spending limits
- Monthly and yearly financial reports
- Savings goals and progress tracking
- Search, filtering, and date-range selection
- Expense category breakdowns
- Authentication and multi-user support
- Cloud database integration and online deployment

## 👨‍💻 Author

**Sarthak Awasthi**

B.Tech CSE — Artificial Intelligence

GitHub: [@awasthi190](https://github.com/awasthi190)

---

⭐ If you find this project useful, consider starring the repository.

*Built with Python and Streamlit.*