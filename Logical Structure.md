Logical Structure:

Logical Structure of the Personal Finance System


1.	Main Application Class: SimpleSystem
•	Attributes:
•	usernames: List to store usernames.
•	user_ids: List to store user IDs.
•	sources_of_income: Dictionary to store sources of income and their corresponding salaries.
•	finance_data: Dictionary to store expenses categorized into "Fundamentals", "Fun", and "Future You".
•	tab_control: Notebook widget to manage different tabs in the application.
•	file_tab, finance_tab, view_tab, report_tab: Frames for each tab.

2.	Initialization (__init__ method)
•	Set up the main window and its properties.
•	Initialize data structures.
•	Create tabs and initialize each tab.

3.	Tab Creation Methods
•	create_file_tab
•	Input fields for username and user ID.
•	Buttons to add and delete users.
•	Listbox to display current users.
•	Button to continue to the finance tab.
•	create_finance_tab
•	Main frame for finance management.
•	Buttons to show totals and continue to the view tab.
•	Category frames for "Fundamentals", "Fun", and "Future You".
•	create_category_frame
•	Creates a frame for each category with a Treeview to display items and amounts.
•	Buttons to add and delete items in the category.
•	create_view_tab
•	Input fields for adding and deleting sources of income.
•	Treeview to display sources of income and their salaries.
•	Button to show finance summary.
•	create_report_tab
•	Input field for searching users by username or user ID.
•	Scrolled text area to display user reports.
•	Buttons for printing the report and searching again.

4.	User Management Methods
•	add_user
•	Adds a new user to the system and updates the listbox.
•	delete_user
•	Deletes the selected user from the listbox and the internal data structures.
5.	Finance Management Methods
•	add_item
•	Prompts the user to enter an item and amount for a specific category.
•	Updates the Treeview and internal data structure.
•	delete_item
•	Deletes the selected item from the category's Treeview and internal data structure.
•	update_treeview
•	Refreshes the Treeview to display current items and amounts.


6.	Income Management Methods
•	add_income_source
•	Adds a new source of income and its salary to the internal dictionary and updates the Treeview.
•	delete_income_source
•	Deletes the selected source of income from the Treeview and internal dictionary.
•	refresh_income_table
•	Updates the Treeview displaying sources of income.

7.	Summary and Report Methods
•	refresh_summary_table
•	Calculates and displays the total amounts for each category and overall income.
•	search_user
•	Searches for a user by username or user ID and displays their financial data.
•	print_report
•	Prints the current report displayed in the report tab.
•	clear_search
•	Clears the search input and report text area.


8.	Navigation Methods
•	show_totals
•	Displays total amounts for each category in a message box.
•	show_finance_tab
•	Switches to the finance tab.
•	show_view_tab
•	Switches to the view tab.
•	show_report_tab
•	Switches to the report tab.


Flow of Control
1.	The application starts and initializes the main window and data structures.
2.	The user can navigate through different tabs to manage users, finances, income sources, and reports.
3.	Users can add or delete entries in each category, and the application updates the corresponding Treeviews and internal data structures.
4.	The user can view summaries of their finances and generate reports based on their input.

