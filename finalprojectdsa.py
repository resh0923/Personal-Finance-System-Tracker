import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import tkinter.scrolledtext as st
import os


class SimpleSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance System Tracker")
        self.root.geometry("1400x600")

        # Initialize data
        self.usernames = []
        self.user_ids = []
        self.sources_of_income = {}  # Dictionary to store sources of income and their salaries
        self.finance_data = {'Fundamentals': [], 'Fun': [], 'Future You': []}

        # Create tab control
        self.tab_control = ttk.Notebook(root)

        # Create tabs
        self.file_tab = ttk.Frame(self.tab_control)
        self.finance_tab = ttk.Frame(self.tab_control)
        self.view_tab = ttk.Frame(self.tab_control)
        self.report_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.file_tab, text='File')
        self.tab_control.add(self.finance_tab, text='Finance')
        self.tab_control.add(self.view_tab, text='View')
        self.tab_control.add(self.report_tab, text='Report')
        self.tab_control.pack(expand=1, fill='both')

        # Initialize tabs
        self.create_file_tab()
        self.create_finance_tab()
        self.create_view_tab()
        self.create_report_tab()

    def create_file_tab(self):
        ttk.Label(self.file_tab, text="Username:").grid(column=0, row=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.file_tab)
        self.username_entry.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.file_tab, text="User ID:").grid(column=0, row=1, padx=10, pady=10)
        self.user_id_entry = ttk.Entry(self.file_tab)
        self.user_id_entry.grid(column=1, row=1, padx=10, pady=10)

        ttk.Button(self.file_tab, text="Add User", command=self.add_user).grid(column=0, row=2, padx=10, pady=10)
        ttk.Button(self.file_tab, text="Delete User", command=self.delete_user).grid(column=1, row=2, padx=10, pady=10)

        ttk.Button(self.file_tab, text="Continue", command=self.show_finance_tab).grid(column=1, row=4, padx=10, pady=10)

        self.user_listbox = tk.Listbox(self.file_tab)
        self.user_listbox.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky='ew')

    def add_user(self):
        username = self.username_entry.get().strip()
        user_id = self.user_id_entry.get().strip()
        if username and user_id:
            self.usernames.append(username)
            self.user_ids.append(user_id)
            self.user_listbox.insert(tk.END, f"{username} (ID: {user_id})")
            self.username_entry.delete(0, tk.END)
            self.user_id_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "User added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter both username and user ID.")

    def delete_user(self):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            self.user_listbox.delete(selected_index)
            del self.usernames[selected_index[0]]
            del self.user_ids[selected_index[0]]
            messagebox.showinfo("Success", "User deleted successfully!")
        else:
            messagebox.showwarning("Selection Error", "Please select a user to delete.")

    def create_finance_tab(self):
        main_frame = tk.Frame(self.finance_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        top_frame = tk.Frame(main_frame)
        top_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.total_button = tk.Button(top_frame, text="Show Totals", command=self.show_totals, width=15)
        self.total_button.pack(side=tk.LEFT, padx=10)

        self.continue_button = tk.Button(top_frame, text="Continue", command=self.show_view_tab, width=15)
        self.continue_button.pack(side=tk.LEFT, padx=10)

        categories_frame = tk.Frame(main_frame)
        categories_frame.pack(fill=tk.BOTH, expand=True)

        self.fundamentals_frame = self.create_category_frame(categories_frame, "Fundamentals", "#FFDDC1")
        self.fun_frame = self.create_category_frame(categories_frame, "Fun", "#C1E1FF")
        self.future_you_frame = self.create_category_frame(categories_frame, "Future You", "#D1FFC1")

        self.fundamentals_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.fun_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.future_you_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def create_category_frame(self, parent, category_name, bg_color):
        frame = tk.Frame(parent, bg=bg_color, padx=10, pady=10)
        label = tk.Label(frame, text=category_name, bg=bg_color, font=("Arial", 14))
        label.pack(pady=5)

        tree = ttk.Treeview(frame, columns=("Item", "Amount"), show="headings", height=8)
        tree.heading("Item", text="Item")
        tree.heading("Amount", text="Amount")
        tree.pack(pady=5, fill=tk.BOTH, expand=True)

        frame.tree = tree
        frame.data = []

        button_frame = tk.Frame(frame, bg=bg_color)
        button_frame.pack(pady=5)

        add_button = tk.Button(button_frame, text="Add Item", command=lambda: self.add_item(frame, category_name))
        add_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Item", command=lambda: self.delete_item(frame, category_name))
        delete_button.pack(side=tk.LEFT, padx=5)

        return frame

    def add_item(self, frame, category_name):
        item = simpledialog.askstring("Add Item", f"Enter item for {category_name}:")
        if not item:
            messagebox.showwarning("Input Error", "Item name cannot be empty.")
            return

        while True:
            amount_str = simpledialog.askstring("Add Amount", f"Enter amount for {item}:")
            if amount_str:
                try:
                    amount = float(amount_str)
                    break
                except ValueError:
                    messagebox.showerror("Input Error", "Please enter a valid numeric amount.")
            else:
                return

        frame.data.append({"item": item, "amount": amount})
        self.update_treeview(frame)
        messagebox.showinfo("Success", f"Item '{item}' with amount Php.{amount} added to {category_name}.")

    def delete_item(self, frame, category_name):
        selected_item = frame.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")
            return

        item_index = frame.tree.index(selected_item[0])
        deleted_item = frame.data.pop(item_index)
        self.update_treeview(frame)
        messagebox.showinfo("Success", f"Item '{deleted_item['item']}' removed from {category_name}.")

    def update_treeview(self, frame):
        for item in frame.tree.get_children():
            frame.tree.delete(item)

        for entry in frame.data:
            frame.tree.insert("", tk.END, values=(entry["item"], entry["amount"]))

    def create_view_tab(self):
        ttk.Label(self.view_tab, text="Source of Income Management", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Label(self.view_tab, text="Source of Income:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.source_entry = ttk.Entry(self.view_tab)
        self.source_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self.view_tab, text="Salary:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.salary_entry = ttk.Entry(self.view_tab)
        self.salary_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        ttk.Button(self.view_tab, text="Add", command=self.add_income_source).grid(row=1, column=2, padx=10, pady=5)
        ttk.Button(self.view_tab, text="Delete", command=self.delete_income_source).grid(row=2, column=2, padx=10, pady=5)

        ttk.Label(self.view_tab, text="Sources of Income").grid(row=3, column=0, columnspan=3, pady=10)

        self.income_tree = ttk.Treeview(self.view_tab, columns=("Source", "Salary"), show="headings")
        self.income_tree.heading("Source", text="Source")
        self.income_tree.heading("Salary", text="Salary")
        self.income_tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        ttk.Button(self.view_tab, text="Show Finance", command=self.refresh_summary_table).grid(row=5, column=0, columnspan=3, pady=10)

        ttk.Label(self.view_tab, text="Finance Summary").grid(row=6, column=0, columnspan=3, pady=10)

        self.summary_tree = ttk.Treeview(self.view_tab, columns=("Category", "Amount"), show="headings")
        self.summary_tree.heading("Category", text="Category")
        self.summary_tree.heading("Amount", text="Amount")
        self.summary_tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        ttk.Button(self.view_tab, text="Continue", command=self.show_report_tab).grid(row=8, column=0, columnspan=3, pady=10)

        self.view_tab.grid_rowconfigure(4, weight=1)
        self.view_tab.grid_rowconfigure(7, weight=1)
        self.view_tab.grid_columnconfigure(1, weight=1)

    def add_income_source(self):
        source = self.source_entry.get().strip()
        salary = self.salary_entry.get().strip()
        if not source or not salary:
            messagebox.showwarning("Input Error", "Please provide both source of income and salary.")
            return
        try:
            salary = float(salary)
            if source in self.sources_of_income:
                messagebox.showwarning("Duplicate Entry", "This source of income already exists.")
                return
            self.sources_of_income[source] = salary
            self.refresh_income_table()
            self.source_entry.delete(0, tk.END)
            self.salary_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid salary.")

    def delete_income_source(self):
        selected_item = self.income_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a source to delete.")
            return
        source = self.income_tree.item(selected_item, "values")[0]
        del self.sources_of_income[source]
        self.refresh_income_table()

    def refresh_income_table(self):
        for item in self.income_tree.get_children():
            self.income_tree.delete(item)
        for source, salary in self.sources_of_income.items():
            self.income_tree.insert("", tk.END, values=(source, f"Php.{salary:.2f}"))

    def refresh_summary_table(self):
        for item in self.summary_tree.get_children():
            self.summary_tree.delete(item)

        finance_totals = {}
        overall_total = 0
        for category in ["Fundamentals", "Fun", "Future You"]:
            frame = getattr(self, f"{category.lower().replace(' ', '_')}_frame")
            total = sum(item["amount"] for item in frame.data)
            finance_totals[category] = total
            overall_total += total

        total_income = sum(self.sources_of_income.values())

        for category, total in finance_totals.items():
            self.summary_tree.insert("", tk.END, values=(category, f"Php.{total:.2f}"))
        self.summary_tree.insert("", tk.END, values=("Total Income", f"Php.{total_income:.2f}"))
        self.summary_tree.insert("", tk.END, values=("Remaining Amount(less overall total in each category)", f"Php.{total_income - overall_total:.2f}"))

    def create_report_tab(self):
        ttk.Label(self.report_tab, text="Search for User", font=("Arial", 16)).grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        ttk.Label(self.report_tab, text="Search Username/User ID:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.search_entry = ttk.Entry(self.report_tab)
        self.search_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ttk.Button(self.report_tab, text="Search", command=self.search_user).grid(row=1, column=2, padx=10, pady=5)

        self.report_text = st.ScrolledText(self.report_tab, wrap=tk.WORD, height=20)
        self.report_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        ttk.Button(self.report_tab, text="Print", command=self.print_report).grid(row=3, column=0, pady=5)
        ttk.Button(self.report_tab, text="Search Again", command=self.clear_search).grid(row=3, column=1, pady=5)
        ttk.Button(self.report_tab, text="Exit", command=self.root.quit).grid(row=3, column=2, pady=5)

        self.report_tab.grid_rowconfigure(2, weight=1)
        self.report_tab.grid_columnconfigure(1, weight=1)

    def search_user(self):
        """
        Searches for a user by username or user ID and displays their data.
        """
        search_query = self.search_entry.get().strip()
        if not search_query:
            messagebox.showwarning("Input Error", "Please enter a username or user ID to search.")
            return

        user_found = False
        self.report_text.delete(1.0, tk.END)

        for username, user_id in zip(self.usernames, self.user_ids):
            if search_query == username or search_query == user_id:
                user_found = True
                self.report_text.insert(tk.END, f"Username: {username}\n")
                self.report_text.insert(tk.END, f"User ID: {user_id}\n\n")

                # Calculate totals
                finance_totals = {}
                overall_total = 0
                for category, frame in [("Fundamentals", self.fundamentals_frame), ("Fun", self.fun_frame), ("Future You", self.future_you_frame)]:
                    category_total = sum(item["amount"] for item in frame.data)
                    finance_totals[category] = category_total
                    overall_total += category_total

                total_income = sum(self.sources_of_income.values())
                remaining = total_income - overall_total

                # Display finance data
                self.report_text.insert(tk.END, "Finance Data:\n")
                for category, total in finance_totals.items():
                    self.report_text.insert(tk.END, f"  {category}: Php.{total:.2f}\n")

                # Display income summary
                self.report_text.insert(tk.END, f"\nTotal Income: Php.{total_income:.2f}\n")
                self.report_text.insert(tk.END, f"Overall Total (All Categories): Php.{overall_total:.2f}\n")
                self.report_text.insert(tk.END, f"Remaining Amount (after deducting the overall): Php{remaining:.2f}\n")

                # Display sources of income
                self.report_text.insert(tk.END, "\nSources of Income:\n")
                for source, salary in self.sources_of_income.items():
                    self.report_text.insert(tk.END, f"  {source}: Php.{salary:.2f}\n")
                break

        if not user_found:
            messagebox.showinfo("Not Found", "No user found with the provided username or user ID.")

    def print_report(self):
        """
        Prints the current report displayed in the Report Tab.
        """
        report_text = self.report_text.get(1.0, tk.END).strip()
        if not report_text:
            messagebox.showwarning("No Data", "No data available to print.")
            return

        try:
            with open("report.txt", "w") as file:
                file.write(report_text)
            os.startfile("report.txt", "print")
            messagebox.showinfo("Success", "Data sent to the printer successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while printing: {e}")

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.report_text.delete(1.0, tk.END)

    def show_totals(self):
        totals = {}
        overall_total = 0
        for category in ["Fundamentals", "Fun", "Future You"]:
            frame = getattr(self, f"{category.lower().replace(' ', '_')}_frame")
            total_amount = sum(item["amount"] for item in frame.data)
            totals[category] = total_amount
            overall_total += total_amount

        total_message = "\n".join([f"{category}: Php.{total:.2f}" for category, total in totals.items()])
        total_message += f"\n\nOverall Total: Php.{overall_total:.2f}"
        messagebox.showinfo("Total Amounts", total_message)

    def show_finance_tab(self):
        self.tab_control.select(self.finance_tab)

    def show_view_tab(self):
        self.tab_control.select(self.view_tab)

    def show_report_tab(self):
        self.tab_control.select(self.report_tab)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleSystem(root)
    root.mainloop()