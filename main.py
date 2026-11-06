
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import shutil
from datetime import datetime


# ==============================
# MAIN WINDOW
# ==============================

root = tk.Tk()
root.title("Expense Tracker | Personal Finance")
root.geometry("1100x720")
root.minsize(950, 650)

# ==============================
# DARK THEME COLORS
# ==============================

BG = "#0B1120"
SIDEBAR = "#111827"
CARD = "#172235"
BUTTON = "#1E293B"
TEXT = "#F1F5F9"
MUTED = "#94A3B8"
BLUE = "#38BDF8"
GREEN = "#34D399"
RED = "#FB7185"
PURPLE = "#A78BFA"
# ==============================
# LIGHT THEME COLORS
# ==============================

LIGHT_BG = "#F1F5F9"
LIGHT_SIDEBAR = "#FFFFFF"
LIGHT_CARD = "#FFFFFF"
LIGHT_BUTTON = "#E2E8F0"
LIGHT_TEXT = "#0F172A"
LIGHT_MUTED = "#64748B"
LIGHT_BLUE = "#0284C7"
LIGHT_GREEN = "#059669"
LIGHT_RED = "#E11D48"
LIGHT_PURPLE = "#7C3AED"

dark_mode = True

root.configure(bg=BG)

# ==============================
# MAIN LAYOUT
# ==============================

sidebar = tk.Frame(root, bg=SIDEBAR, width=220)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

main_area = tk.Frame(root, bg=BG)
main_area.pack(side="left", fill="both", expand=True)

# ==============================
# SIDEBAR HEADER
# ==============================

logo = tk.Label(
    sidebar,
    text="◈  EXPENSE PRO",
    font=("Segoe UI", 17, "bold"),
    bg=SIDEBAR,
    fg=BLUE
)
logo.pack(anchor="w", padx=20, pady=(30, 8))

logo_subtitle = tk.Label(
    sidebar,
    text="PERSONAL FINANCE",
    font=("Segoe UI", 8, "bold"),
    bg=SIDEBAR,
    fg=MUTED
)
logo_subtitle.pack(anchor="w", padx=22, pady=(0, 35))

# ==============================
# SIDEBAR NAVIGATION
# ==============================

nav_label = tk.Label(
    sidebar,
    text="MAIN MENU",
    font=("Segoe UI", 9, "bold"),
    bg=SIDEBAR,
    fg=MUTED
)
nav_label.pack(anchor="w", padx=22, pady=(0, 12))


def create_nav_button(text, color=TEXT):
    button = tk.Button(
        sidebar,
        text=text,
        font=("Segoe UI", 11),
        bg=SIDEBAR,
        fg=color,
        activebackground=BUTTON,
        activeforeground=BLUE,
        relief="flat",
        bd=0,
        anchor="w",
        padx=20,
        pady=12,
        cursor="hand2"
    )
    button.pack(fill="x", padx=10, pady=3)
    return button


dashboard_btn = create_nav_button("▦   Dashboard", BLUE)
dashboard_btn.config(
    command=lambda: show_page("Dashboard")
)
transactions_btn = create_nav_button("⇄   Transactions")
transactions_btn.config(
    command=lambda: show_page("Transactions")
)
income_btn = create_nav_button("+   Income", GREEN)
income_btn.config(command=lambda: show_page("Income"))
expenses_btn = create_nav_button("−   Expenses", RED)
expenses_btn.config(command=lambda: show_page("Expenses"))
analytics_btn = create_nav_button("▥   Analytics", PURPLE)
analytics_btn.config(command=lambda: show_page("Analytics"))

# ==============================
# SIDEBAR BOTTOM
# ==============================

sidebar_bottom = tk.Frame(sidebar, bg=SIDEBAR)
sidebar_bottom.pack(side="bottom", fill="x", padx=20, pady=25)

settings_label = tk.Button(
    sidebar_bottom,
    text="⚙  Settings",
    font=("Segoe UI", 11),
    bg=SIDEBAR,
    fg=TEXT,
    relief="flat",
    cursor="hand2"
)
settings_label.pack(anchor="w", pady=8)
settings_label.config(command=lambda: show_page("Settings"))


theme_label = tk.Button(
    sidebar_bottom,
    text="🌙  Dark Mode",
    font=("Segoe UI", 10),
    bg=SIDEBAR,
    fg=MUTED,
    relief="flat",
    cursor="hand2"
)
theme_label.pack(anchor="w", pady=8)

# ==============================
# DARK / LIGHT MODE
# ==============================

def toggle_theme():

    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:
        root.configure(bg=BG)
        sidebar.configure(bg=SIDEBAR)
        main_area.configure(bg=BG)

        theme_label.config(text="🌙  Dark Mode")

    else:
        root.configure(bg=LIGHT_BG)
        sidebar.configure(bg=LIGHT_SIDEBAR)
        main_area.configure(bg=LIGHT_BG)

        theme_label.config(text="☀  Light Mode")


theme_label.config(command=toggle_theme)


# ==============================
# TOP HEADER
# ==============================

header = tk.Frame(main_area, bg=BG)
header.pack(fill="x", padx=30, pady=(10, 5))

header_text = tk.Frame(header, bg=BG)
header_text.pack(side="left")

page_title = tk.Label(
    header_text,
    text="Dashboard Overview",
    font=("Segoe UI", 18, "bold"),
    bg=BG,
    fg=TEXT
)
page_title.pack(anchor="w")

page_subtitle = tk.Label(
    header_text,
    text="Track your money. Manage your future.",
    font=("Segoe UI", 10),
    bg=BG,
    fg=MUTED
)
page_subtitle.pack(anchor="w", pady=(5, 0))

date_label = tk.Label(
    header,
    text="MY FINANCE SPACE",
    font=("Segoe UI", 10, "bold"),
    bg=CARD,
    fg=BLUE,
    padx=15,
    pady=12
)
date_label.pack(side="right", anchor="center")

# ==============================
# PAGE NAVIGATION
# ==============================

def show_page(page_name):

    content.pack_forget()
    transactions_page.pack_forget()
    income_page.pack_forget()
    expenses_page.pack_forget()
    analytics_page.pack_forget()
    settings_page.pack_forget()

    if page_name == "Dashboard":

        page_title.config(text="Dashboard Overview")
        page_subtitle.config(
            text="Track your money. Manage your future."
        )

        content.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=5
        )

    elif page_name == "Transactions":

        page_title.config(text="Transactions")
        page_subtitle.config(
            text="View all your financial transactions."
        )

        transactions_page.pack(
            fill="both",
            expand=True
        )

        load_all_transactions()

    elif page_name == "Income":

        page_title.config(text="Income")
        page_subtitle.config(
            text="View all your income transactions."
        )

        income_page.pack(
            fill="both",
            expand=True
        )

        load_income_transactions()

    elif page_name == "Expenses":

        page_title.config(text="Expenses")
        page_subtitle.config(
            text="View all your expense transactions."
        )

        expenses_page.pack(
            fill="both",
            expand=True
        )

        load_expense_transactions()


    elif page_name == "Analytics":

        page_title.config(text="Analytics")
        page_subtitle.config( 
            text="Analyze your income and expenses."
        )

        analytics_page.pack(
            fill="both",
            expand=True
        )

        load_analytics()


    elif page_name == "Settings":

        page_title.config(text="Settings")
        page_subtitle.config(
            text="Manage your Expense Tracker settings."
        )

        settings_page.pack(
            fill="both",
            expand=True
        )
    
# ==============================
# DASHBOARD CONTENT AREA
# ==============================

content = tk.Frame(main_area, bg=BG)
content.pack(fill="both", expand=True, padx=30, pady=5)

welcome_card = tk.Frame(
    content,
    bg=CARD,
    highlightbackground="#263449",
    highlightthickness=1
)
welcome_card.pack(fill="x", pady=(0, 10))

welcome_title = tk.Label(
    welcome_card,
    text="Welcome to your Financial Dashboard!",
    font=("Segoe UI", 17, "bold"),
    bg=CARD,
    fg=TEXT
)
welcome_title.pack(anchor="w", padx=22, pady=(5, 2))

welcome_message = tk.Label(
    welcome_card,
    text="Your income, expenses and savings will appear here.",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=MUTED
)
welcome_message.pack(anchor="w", padx=22, pady=(0, 5))

# ==============================
# PLACEHOLDER FOR SUMMARY CARDS
# ==============================

section_title = tk.Label(
    content,
    text="FINANCIAL SUMMARY",
    font=("Segoe UI", 11, "bold"),
    bg=BG,
    fg=TEXT
)
section_title.pack(anchor="w", pady=(4, 5))

summary_area = tk.Frame(content, bg=BG)
summary_area.pack(fill="x")

for index in range(4):
    summary_area.columnconfigure(index, weight=1, uniform="cards")

    
# ==============================
# PROFESSIONAL SUMMARY CARDS
# ==============================

def create_summary_card(parent, title, amount, color, icon, column):

    card = tk.Frame(
        parent,
        bg=CARD,
        highlightbackground="#334155",
        highlightthickness=1
    )

    card.grid(
        row=0,
        column=column,
        padx=8,
        sticky="nsew",
        ipady=5
    )

    tk.Label(
        card,
        text=icon,
        font=("Segoe UI", 13),
        bg=CARD,
        fg=color
    ).pack(anchor="w", padx=18, pady=(4, 1))

    tk.Label(
        card,
        text=title,
        font=("Segoe UI", 8, "bold"),
        bg=CARD,
        fg=MUTED
    ).pack(anchor="w", padx=10)

    amount_label = tk.Label(
        card,
        text=amount,
        font=("Segoe UI", 11, "bold"),
        bg=CARD,
        fg=color
)
    amount_label.pack(anchor="w", padx=18, pady=(3, 5))

    return amount_label

income_label = create_summary_card(
    summary_area, "TOTAL INCOME", "Rs. 0",
    GREEN, "↗", 0
)

expense_label = create_summary_card(
    summary_area, "TOTAL EXPENSES", "Rs. 0",
    RED, "↘", 1
)

balance_label = create_summary_card(
    summary_area, "NET BALANCE", "Rs. 0",
    BLUE, "◈", 2
)

# UPDATE DASHBOARD SUMMARY
def update_summary():

    total_income = 0
    total_expenses = 0
    category_expenses = {}

    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                amount = float(row[2])

                if row[3] == "Income":
                    total_income += amount

                elif row[3] == "Expense":
                    total_expenses += amount
                    category_expenses[row[1]] = category_expenses.get(row[1], 0) + amount

    except FileNotFoundError:
        pass

    net_balance = total_income - total_expenses
    for item in category_table.get_children():
        category_table.delete(item)

    for category, amount in category_expenses.items():
        category_table.insert(
            "",
            "end",
            values=(category, f"Rs. {amount:,.2f}")
        )
    print("CATEGORY-WISE EXPENSES:")

    for category, amount in category_expenses.items():
        print(f"{category}: Rs. {amount:,.2f}")

    income_label.config(text=f"Rs. {total_income:,.2f}")
    expense_label.config(text=f"Rs. {total_expenses:,.2f}")
    balance_label.config(text=f"Rs. {net_balance:,.2f}")

    # CATEGORY-WISE EXPENDITURES

category_title = tk.Label(
    content,
    text="CATEGORY-WISE EXPENDITURES",
    font=("Segoe UI", 11, "bold"),
    bg=BG,
    fg=TEXT
)

category_title.pack(anchor="w", pady=(8, 4))

# CATEGORY EXPENSES TABLE

category_card = tk.Frame(
    content,
    bg=CARD,
    highlightbackground="#334155",
    highlightthickness=1
)

category_card.pack(fill="x", pady=(0, 5))

category_table = ttk.Treeview(
    category_card,
    columns=("category", "amount"),
    show="headings",
    height=2,
    style="Expense.Treeview"
)

category_table.heading("category", text="CATEGORY")
category_table.heading("amount", text="TOTAL EXPENSE")

category_table.column("category", width=300, anchor="center")
category_table.column("amount", width=300, anchor="center")

category_table.pack(fill="x", padx=5, pady=4)
    


# TRANSACTION FORM
form_title = tk.Label(
    content,
    text="ADD NEW TRANSACTION",
    font=("Segoe UI", 12, "bold"),
    bg=BG,
    fg=TEXT
)
form_title.pack(anchor="w", pady=(7, 4))

form_card = tk.Frame(
    content,
    bg=CARD,
    highlightbackground="#334155",
    highlightthickness=1
)
form_card.pack(fill="x", pady=(0, 5))

# FORM FIELDS
fields_frame = tk.Frame(form_card, bg=CARD)
fields_frame.pack(fill="x", padx=8, pady=2)

for i in range(5):
    fields_frame.columnconfigure(i, weight=1)

# DATE
tk.Label(
    fields_frame, text="Date (YYYY-MM-DD)",
    bg=CARD, fg=MUTED, font=("Segoe UI", 9, "bold")
).grid(row=0, column=0, sticky="w", padx=6, pady=5)

date_entry = tk.Entry(
    fields_frame, bg="#0F172A", fg=TEXT,
    insertbackground=TEXT, relief="flat",
    highlightbackground="#334155",
    highlightthickness=1, font=("Segoe UI", 10)
)
date_entry.grid(row=1, column=0, sticky="ew", padx=6, ipady=3)

# CATEGORY
tk.Label(
    fields_frame, text="Category",
    bg=CARD, fg=MUTED, font=("Segoe UI", 9, "bold")
).grid(row=0, column=1, sticky="w", padx=6, pady=5)

category_box = ttk.Combobox(
    fields_frame,
    values=["Food", "Travel", "Bills", "Shopping", "Other"],
    state="readonly",
    font=("Segoe UI", 10)
)
category_box.grid(row=1, column=1, sticky="ew", padx=6, ipady=2)
category_box.set("Select Category")

# AMOUNT
tk.Label(
    fields_frame, text="Amount (Rs.)",
    bg=CARD, fg=MUTED, font=("Segoe UI", 9, "bold")
).grid(row=0, column=2, sticky="w", padx=6, pady=5)

amount_entry = tk.Entry(
    fields_frame, bg="#0F172A", fg=TEXT,
    insertbackground=TEXT, relief="flat",
    highlightbackground="#334155",
    highlightthickness=1, font=("Segoe UI", 10)
)
amount_entry.grid(row=1, column=2, sticky="ew", padx=6, ipady=9)

# TYPE
tk.Label(
    fields_frame, text="Transaction Type",
    bg=CARD, fg=MUTED, font=("Segoe UI", 9, "bold")
).grid(row=0, column=3, sticky="w", padx=6, pady=5)

type_box = ttk.Combobox(
    fields_frame,
    values=["Income", "Expense"],
    state="readonly",
    font=("Segoe UI", 10)
)
type_box.grid(row=1, column=3, sticky="ew", padx=6, ipady=5)
type_box.set("Select Type")

# ADD BUTTON
add_button = tk.Button(
    fields_frame,
    text="+  Add Transaction",
    font=("Segoe UI", 10, "bold"),
    bg=GREEN,
    fg="#0B1120",
    activebackground="#10B981",
    activeforeground="#0B1120",
    relief="flat",
    bd=0,
    padx=12,
    pady=5,
    cursor="hand2"
)
add_button.grid(row=1, column=4, sticky="ew", padx=6, pady=2)
print("Add Transaction button created successfully!")
# Fourth column remains available for layout flexibility.

# TRANSACTION HISTORY

history_title = tk.Label(
    content,
    text="TRANSACTION HISTORY",
    font=("Segoe UI", 13, "bold"),
    bg=BG,
    fg=TEXT
)
history_title.pack(anchor="w", pady=(3, 4))
print("TRANSACTION HISTORY SECTION CREATED")


history_card = tk.Frame(
    content,
    bg=CARD,
    highlightbackground="#263449",
    highlightthickness=1
)
history_card.pack(fill="x", expand=True, pady=(0, 0))

# TABLE STYLE
table_style = ttk.Style()
table_style.theme_use("clam")

table_style.configure(
    "Expense.Treeview",
    background="#0F172A",
    foreground=TEXT,
    fieldbackground="#0F172A",
    rowheight=18,
    font=("Segoe UI", 9),
    borderwidth=0
)

table_style.configure(
    "Expense.Treeview.Heading",
    background=BUTTON,
    foreground=TEXT,
    font=("Segoe UI", 9, "bold"),
    relief="flat"
)

table_style.map(
    "Expense.Treeview",
    background=[("selected", BLUE)],
    foreground=[("selected", BG)]
)


# TABLE FRAME
table_frame = tk.Frame(history_card, bg=CARD)
table_frame.pack(fill="both", expand=True, padx=4, pady=3)

table_frame.columnconfigure(0, weight=1)


# TRANSACTION TABLE
transaction_table = ttk.Treeview(
    table_frame,
    columns=("date", "category", "amount", "type"),
    show="headings",
    height=2,
    style="Expense.Treeview"
)

transaction_table.heading("date", text="DATE")
transaction_table.heading("category", text="CATEGORY")
transaction_table.heading("amount", text="AMOUNT")
transaction_table.heading("type", text="TYPE")

transaction_table.column("date", width=180, anchor="center")
transaction_table.column("category", width=200, anchor="center")
transaction_table.column("amount", width=180, anchor="center")
transaction_table.column("type", width=160, anchor="center")


# VERTICAL SCROLLBAR
table_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=transaction_table.yview
)

transaction_table.configure(
    yscrollcommand=table_scrollbar.set
)

transaction_table.grid(row=0, column=0, sticky="nsew")
table_scrollbar.grid(row=0, column=1, sticky="ns")


# LOAD TRANSACTIONS INTO TABLE

def load_transactions():

    # Pehle table ko empty karo
    for item in transaction_table.get_children():
        transaction_table.delete(item)

    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row_number, row in enumerate(reader):
                if len(row) == 4:
                    transaction_table.insert(
                        "",
                        "end",
                        iid=str(row_number),
                        values=(
                            row[0],
                            row[1],
                            f"Rs. {float(row[2]):,.2f}",
                            row[3]
                        )
                    )

    except FileNotFoundError:
        pass


# DELETE SELECTED TRANSACTION

def delete_transaction():

    selected_item = transaction_table.selection()

    if not selected_item:
        messagebox.showwarning(
            "No Selection",
            "Please select a transaction to delete!"
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this transaction?"
    )

    if not confirm:
        return

    selected_id = int(selected_item[0])

    with open("transactions.csv", "r", newline="") as file:
        rows = list(csv.reader(file))

    del rows[selected_id]

    with open("transactions.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    load_transactions()
    update_summary()
    load_all_transactions()


    messagebox.showinfo(
        "Success",
        "Transaction deleted successfully!"
    )


# LOAD EXISTING TRANSACTIONS
load_transactions()

# DELETE BUTTON

delete_button = tk.Button(
    history_card,
    text="Delete Selected",
    font=("Segoe UI", 9, "bold"),
    bg=RED,
    fg=BG,
    activebackground="#F43F5E",
    activeforeground=BG,
    relief="flat",
    bd=0,
    padx=12,
    pady=5,
    cursor="hand2",
    command=delete_transaction
)

delete_button.pack(anchor="e", padx=10, pady=5)


# ADD TRANSACTION FUNCTION
def add_transaction():

    date = date_entry.get().strip()
    category = category_box.get()
    amount = amount_entry.get().strip()
    transaction_type = type_box.get()

    # CHECK EMPTY FIELDS
    if not date or not amount or category == "Select Category" or transaction_type == "Select Type":
        messagebox.showwarning("Missing Information", "Please fill all fields!")
        return

    # CHECK DATE FORMAT
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Invalid Date", "Enter date in YYYY-MM-DD format!")
        return

    # CHECK AMOUNT
    try:
        amount = float(amount)

        if amount <= 0:
            messagebox.showerror("Invalid Amount", "Amount must be greater than zero!")
            return

    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid number!")
        return

    # SAVE DATA IN CSV FILE
    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, transaction_type])

        # UPDATE DASHBOARD
        update_summary()
        load_transactions()

    messagebox.showinfo("Success", "Transaction saved successfully!")

    # CLEAR FIELDS
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_box.set("Select Category")
    type_box.set("Select Type")


# CONNECT BUTTON WITH FUNCTION
add_button.config(command=add_transaction)

# ==============================
# TRANSACTIONS PAGE
# ==============================

transactions_page = tk.Frame(main_area, bg=BG)

transactions_heading = tk.Label(
    transactions_page,
    text="All Transactions",
    font=("Segoe UI", 18, "bold"),
    bg=BG,
    fg=TEXT
)

transactions_heading.pack(anchor="w", padx=30, pady=20)

transactions_message = tk.Label(
    transactions_page,
    text="Your transaction records will appear here.",
    font=("Segoe UI", 11),
    bg=BG,
    fg=MUTED
)

transactions_message.pack(anchor="w", padx=30)

# DATE AND CATEGORY FILTERS

filter_frame = tk.Frame(transactions_page, bg=BG)
filter_frame.pack(anchor="w", padx=30, pady=15)

tk.Label(filter_frame, text="Start Date (YYYY-MM-DD)", bg=BG, fg=TEXT).pack(side="left", padx=5)

start_date_entry = tk.Entry(filter_frame, width=15)
start_date_entry.pack(side="left", padx=5)

tk.Label(filter_frame, text="End Date (YYYY-MM-DD)", bg=BG, fg=TEXT).pack(side="left", padx=5)

end_date_entry = tk.Entry(filter_frame, width=15)
end_date_entry.pack(side="left", padx=5)

tk.Label(filter_frame, text="Category", bg=BG, fg=TEXT).pack(side="left", padx=5)

category_filter = ttk.Combobox(
    filter_frame,
    values=["All", "Food", "Travel", "Bills", "Shopping", "Other"],
    width=12,
    state="readonly"
)
category_filter.pack(side="left", padx=5)
category_filter.set("All")

filter_button = tk.Button(
    filter_frame,
    text="Apply Filter",
    bg=BLUE,
    fg=BG,
    font=("Segoe UI", 10, "bold"),
    padx=12,
    pady=7,
    cursor="hand2",
    command=lambda: filter_transactions()
)
filter_button.pack(side="left", padx=5)

reset_filter_button = tk.Button(
    filter_frame,
    text="Reset",
    bg=BUTTON,
    fg=TEXT,
    font=("Segoe UI", 10, "bold"),
    padx=12,
    pady=7,
    cursor="hand2",
    command=lambda: load_all_transactions()
)
reset_filter_button.pack(side="left", padx=5)

export_button = tk.Button(
    filter_frame,
    text="Export CSV",
    bg=GREEN,
    fg=BG,
    font=("Segoe UI", 10, "bold"),
    padx=12,
    pady=7,
    cursor="hand2",
    command=lambda: export_transactions()
)
export_button.pack(side="left", padx=5)

# ALL TRANSACTIONS TABLE

all_transactions_card = tk.Frame(
    transactions_page,
    bg=CARD,
    highlightbackground="#334155",
    highlightthickness=1
)

all_transactions_card.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=15
)

all_transactions_table = ttk.Treeview(
    all_transactions_card,
    columns=("date", "category", "amount", "type"),
    show="headings",
    style="Expense.Treeview"
)

all_transactions_table.heading("date", text="DATE")
all_transactions_table.heading("category", text="CATEGORY")
all_transactions_table.heading("amount", text="AMOUNT")
all_transactions_table.heading("type", text="TYPE")

all_transactions_table.column("date", width=180, anchor="center")
all_transactions_table.column("category", width=180, anchor="center")
all_transactions_table.column("amount", width=180, anchor="center")
all_transactions_table.column("type", width=180, anchor="center")

all_transactions_table.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# LOAD ALL TRANSACTIONS

def load_all_transactions():

    for item in all_transactions_table.get_children():
        all_transactions_table.delete(item)

    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4:
                    all_transactions_table.insert(
                        "",
                        "end",
                        values=(
                            row[0],
                            row[1],
                            f"Rs. {float(row[2]):,.2f}",
                            row[3]
                        )
                    )

    except FileNotFoundError:
        pass

    # EXPORT TRANSACTIONS TO CSV

def export_transactions():

    records = all_transactions_table.get_children()

    if not records:
        messagebox.showwarning(
            "No Records",
            "There are no transactions to export!"
        )
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")],
        title="Save Transactions"
    )

    if not file_path:
        return

    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Date", "Category", "Amount", "Type"])

            for item in records:
                writer.writerow(
                    all_transactions_table.item(item, "values")
                )

        messagebox.showinfo(
            "Export Successful",
            "Transactions exported successfully!"
        )

    except Exception as e:
        messagebox.showerror("Export Error", str(e))



def filter_transactions():

    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    selected_category = category_filter.get()

        # CHECK DATE FORMAT
    try:
        if start_date:
            datetime.strptime(start_date, "%Y-%m-%d")

        if end_date:
            datetime.strptime(end_date, "%Y-%m-%d")

    except ValueError:
        messagebox.showerror(
            "Invalid Date",
            "Enter dates in YYYY-MM-DD format!"
        )
        return

    if start_date and end_date and start_date > end_date:
        messagebox.showerror(
            "Invalid Date Range",
            "Start date cannot be after end date!"
        )
        return

    # CLEAR OLD RECORDS
    for item in all_transactions_table.get_children():
        all_transactions_table.delete(item)

    # LOAD FILTERED RECORDS
    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4:

                    if start_date and row[0] < start_date:
                        continue

                    if end_date and row[0] > end_date:
                        continue

                    if selected_category != "All" and row[1] != selected_category:
                        continue

                    all_transactions_table.insert(
                        "",
                        "end",
                        values=(
                            row[0],
                            row[1],
                            f"Rs. {float(row[2]):,.2f}",
                            row[3]
                        )
                    )

    except FileNotFoundError:
        pass

    # CHECK DATE FORMAT
    try:
        if start_date:
            datetime.strptime(start_date, "%Y-%m-%d")

        if end_date:
            datetime.strptime(end_date, "%Y-%m-%d")

    except ValueError:
        messagebox.showerror(
            "Invalid Date",
            "Enter dates in YYYY-MM-DD format!"
        )
        return

    if start_date and end_date and start_date > end_date:
        messagebox.showerror(
            "Invalid Date Range",
            "Start date cannot be after end date!"
        )
        return

    # CLEAR OLD RECORDS
    for item in all_transactions_table.get_children():
        all_transactions_table.delete(item)

    # LOAD FILTERED RECORDS
    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4:

                    if start_date and row[0] < start_date:
                        continue

                    if end_date and row[0] > end_date:
                        continue

                    if selected_category != "All" and row[1] != selected_category:
                        continue

                    all_transactions_table.insert(
                        "",
                        "end",
                        values=(
                            row[0],
                            row[1],
                            f"Rs. {float(row[2]):,.2f}",
                            row[3]
                        )
                    )

    except FileNotFoundError:
        pass

    # ==============================
# INCOME PAGE
# ==============================

income_page = tk.Frame(main_area, bg=BG)

income_heading = tk.Label(
    income_page,
    text="Income Records",
    font=("Segoe UI", 18, "bold"),
    bg=BG,
    fg=TEXT
)
income_heading.pack(anchor="w", padx=30, pady=20)

income_message = tk.Label(
    income_page,
    text="View all your income transactions here.",
    font=("Segoe UI", 11),
    bg=BG,
    fg=MUTED
)
income_message.pack(anchor="w", padx=30)

# INCOME TABLE

income_table = ttk.Treeview(
    income_page,
    columns=("date", "category", "amount", "type"),
    show="headings",
    style="Expense.Treeview"
)

income_table.heading("date", text="DATE")
income_table.heading("category", text="CATEGORY")
income_table.heading("amount", text="AMOUNT")
income_table.heading("type", text="TRANSACTION TYPE")

income_table.column("date", width=200, anchor="center")
income_table.column("category", width=200, anchor="center")
income_table.column("amount", width=200, anchor="center")
income_table.column("type", width=200, anchor="center")

income_table.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=15
)


# LOAD INCOME TRANSACTIONS

def load_income_transactions():

    for item in income_table.get_children():
        income_table.delete(item)

    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4 and row[3].lower() == "income":

                    income_table.insert(
                        "",
                        "end",
                        values=(
                         row[0],
                         row[1],
                         f"Rs. {float(row[2]):,.2f}",
                         row[3]
                      )
                    )

    except FileNotFoundError:
        pass

# ==============================
# EXPENSES PAGE
# ==============================

expenses_page = tk.Frame(main_area, bg=BG)

expenses_heading = tk.Label(
    expenses_page,
    text="Expense Records",
    font=("Segoe UI", 18, "bold"),
    bg=BG,
    fg=TEXT
)
expenses_heading.pack(anchor="w", padx=30, pady=20)

expenses_message = tk.Label(
    expenses_page,
    text="View all your expense transactions here.",
    font=("Segoe UI", 11),
    bg=BG,
    fg=MUTED
)
expenses_message.pack(anchor="w", padx=30)

# EXPENSES TABLE

expenses_table = ttk.Treeview(
    expenses_page,
    columns=("date", "category", "amount", "type"),
    show="headings",
    style="Expense.Treeview"
)

expenses_table.heading("date", text="DATE")
expenses_table.heading("category", text="CATEGORY")
expenses_table.heading("amount", text="AMOUNT")
expenses_table.heading("type", text="TRANSACTION TYPE")

expenses_table.column("date", width=200, anchor="center")
expenses_table.column("category", width=200, anchor="center")
expenses_table.column("amount", width=200, anchor="center")
expenses_table.column("type", width=200, anchor="center")

expenses_table.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=15
)


# LOAD EXPENSE TRANSACTIONS

def load_expense_transactions():

    for item in expenses_table.get_children():
        expenses_table.delete(item)

    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4 and row[3].lower() == "expense":

                    expenses_table.insert(
                        "",
                        "end",
                        values=(
                            row[0],
                            row[1],
                            f"Rs. {float(row[2]):,.2f}",
                            row[3]
                        )
                    )

    except FileNotFoundError:
        pass

    # ==============================
# ANALYTICS PAGE
# ==============================

analytics_page = tk.Frame(main_area, bg=BG)

analytics_heading = tk.Label(
    analytics_page,
    text="Financial Analytics",
    font=("Segoe UI", 18, "bold"),
    bg=BG,
    fg=TEXT
)
analytics_heading.pack(anchor="w", padx=30, pady=20)

analytics_message = tk.Label(
    analytics_page,
    text="Analyze your income and expenses.",
    font=("Segoe UI", 11),
    bg=BG,
    fg=MUTED
)
analytics_message.pack(anchor="w", padx=30)

# ANALYTICS SUMMARY

analytics_summary = tk.Frame(
    analytics_page,
    bg=BG
)
analytics_summary.pack(
    fill="x",
    padx=30,
    pady=20
)

# TOTAL INCOME CARD

analytics_income_card = tk.Frame(
    analytics_summary,
    bg=CARD,
    padx=20,
    pady=20
)
analytics_income_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=8
)

tk.Label(
    analytics_income_card,
    text="TOTAL INCOME",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=MUTED
).pack(anchor="w")

analytics_income_label = tk.Label(
    analytics_income_card,
    text="Rs. 0.00",
    font=("Segoe UI", 20, "bold"),
    bg=CARD,
    fg=GREEN
)
analytics_income_label.pack(anchor="w", pady=10)

# TOTAL EXPENSES CARD

analytics_expense_card = tk.Frame(
    analytics_summary,
    bg=CARD,
    padx=20,
    pady=20
)
analytics_expense_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=8
)

tk.Label(
    analytics_expense_card,
    text="TOTAL EXPENSES",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=MUTED
).pack(anchor="w")

analytics_expense_label = tk.Label(
    analytics_expense_card,
    text="Rs. 0.00",
    font=("Segoe UI", 20, "bold"),
    bg=CARD,
    fg=RED
)
analytics_expense_label.pack(anchor="w", pady=10)

# NET BALANCE CARD

analytics_balance_card = tk.Frame(
    analytics_summary,
    bg=CARD,
    padx=20,
    pady=20
)
analytics_balance_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=8
)

tk.Label(
    analytics_balance_card,
    text="NET BALANCE",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=MUTED
).pack(anchor="w")

analytics_balance_label = tk.Label(
    analytics_balance_card,
    text="Rs. 0.00",
    font=("Segoe UI", 20, "bold"),
    bg=CARD,
    fg=BLUE
)
analytics_balance_label.pack(anchor="w", pady=10)


# LOAD ANALYTICS DATA

def load_analytics():

    total_income = 0
    total_expenses = 0

    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4:

                    amount = float(row[2])

                    if row[3].lower() == "income":
                        total_income += amount

                    elif row[3].lower() == "expense":
                        total_expenses += amount

    except FileNotFoundError:
        pass

    net_balance = total_income - total_expenses

    analytics_income_label.config(
        text=f"Rs. {total_income:,.2f}"
    )

    analytics_expense_label.config(
        text=f"Rs. {total_expenses:,.2f}"
    )

    analytics_balance_label.config(
        text=f"Rs. {net_balance:,.2f}"
    )

    # ==============================
# SETTINGS PAGE
# ==============================

settings_page = tk.Frame(main_area, bg=BG)

settings_heading = tk.Label(
    settings_page,
    text="Settings",
    font=("Segoe UI", 18, "bold"),
    bg=BG,
    fg=TEXT
)
settings_heading.pack(anchor="w", padx=30, pady=20)

settings_message = tk.Label(
    settings_page,
    text="Manage your Expense Tracker settings here.",
    font=("Segoe UI", 11),
    bg=BG,
    fg=MUTED
)
settings_message.pack(anchor="w", padx=30)

# REFRESH DATA BUTTON

refresh_btn = tk.Button(
    settings_page,
    text="⟳  Refresh Data",
    font=("Segoe UI", 11, "bold"),
    bg=BUTTON,
    fg=TEXT,
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)
refresh_btn.pack(anchor="w", padx=30, pady=20)


# BACKUP BUTTON

backup_btn = tk.Button(
    settings_page,
    text="▣  Backup Transactions", 
    font=("Segoe UI", 11, "bold"),
    bg=BUTTON,
    fg=TEXT,
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)
backup_btn.pack(anchor="w", padx=30, pady=5)

# REFRESH ALL DATA

def refresh_all_data():

    load_transactions()
    update_summary()
    load_all_transactions()
    load_income_transactions()
    load_expense_transactions()
    load_analytics()

    messagebox.showinfo(
        "Refresh",
        "All data refreshed successfully!"
    )

refresh_btn.config(command=refresh_all_data)

# BACKUP TRANSACTIONS

def backup_transactions():

    try:
        shutil.copy("transactions.csv", "transactions_backup.csv")

        messagebox.showinfo(
            "Backup",
            "Transactions backup created successfully!"
        )

    except FileNotFoundError:
        messagebox.showerror(
            "Backup Error",
            "No transactions file found!"
        )

backup_btn.config(command=backup_transactions)


# ==============================
# RUN APPLICATION
# ==============================

update_summary()

root.mainloop()



