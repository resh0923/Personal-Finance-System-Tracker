PSEUDOCODE:

START

CLASS SimpleSystem

    METHOD __init__(root)
        SET root window title and size
        INITIALIZE lists for usernames, user_ids
        INITIALIZE dictionary sources_of_income (source: salary)
        INITIALIZE finance_data dictionary with categories: Fundamentals, Fun, Future You
        CREATE tab control with tabs: File, Finance, View, Report
        CALL create_file_tab()
        CALL create_finance_tab()
        CALL create_view_tab()
        CALL create_report_tab()

    METHOD create_file_tab()
        CREATE Username label and entry field
        CREATE User ID label and entry field
        CREATE Add User button -> calls add_user()
        CREATE Delete User button -> calls delete_user()
        CREATE Continue button -> calls show_finance_tab()
        CREATE Listbox to display current users

    METHOD add_user()
        GET username input
        GET user_id input
        IF both username and user_id are not empty THEN
            ADD username to usernames list
            ADD user_id to user_ids list
            INSERT username and user_id to user Listbox
            CLEAR username and user_id entry fields
            SHOW success message
        ELSE
            SHOW warning message to enter both fields

    METHOD delete_user()
        GET selected index from user Listbox
        IF an item is selected THEN
            DELETE selected item from Listbox
            REMOVE corresponding username and user_id from lists
            SHOW success message
        ELSE
            SHOW warning message to select a user

    METHOD create_finance_tab()
        CREATE main frame for finance
        CREATE buttons: Show Totals (calls show_totals()), Continue (calls show_view_tab())
        FOR each category (Fundamentals, Fun, Future You)
            CREATE category frame with background color
            CALL create_category_frame(frame, category)

    METHOD create_category_frame(frame, category)
        DISPLAY category name
        CREATE Treeview with columns for Item and Amount
        CREATE buttons: Add Item (calls add_item()), Delete Item (calls delete_item())
        INITIALIZE data list for category

    METHOD add_item(category)
        PROMPT user for item name
        PROMPT user for amount
        IF inputs are valid numbers THEN
            ADD item and amount to category's data list
            UPDATE corresponding Treeview
            SHOW success message
        ELSE
            SHOW warning/error message

    METHOD delete_item(category)
        GET selected item in category's Treeview
        IF an item is selected THEN
            REMOVE item from data list
            UPDATE Treeview
            SHOW success message
        ELSE
            SHOW warning message to select an item

    METHOD update_treeview(category)
        CLEAR current Treeview entries
        INSERT all items from category data list into Treeview

    METHOD create_view_tab()
        CREATE inputs for adding source of income and salary
        CREATE buttons: Add source (calls add_income_source()), Delete source (calls delete_income_source())
        CREATE Income sources Treeview
        CREATE button to show finance summary (calls refresh_summary_table())
        CREATE Finance summary Treeview
        CREATE Continue button (calls show_report_tab())

    METHOD add_income_source()
        GET source and salary input
        IF inputs are valid THEN
            ADD source and salary to sources_of_income dictionary
            UPDATE Income sources Treeview
            SHOW success message
        ELSE
            SHOW warning message

    METHOD delete_income_source()
        GET selected source in Income sources Treeview
        IF selected THEN
            REMOVE source from dictionary
            UPDATE Treeview
            SHOW success message
        ELSE
            SHOW warning message

    METHOD refresh_income_table()
        CLEAR Income sources Treeview
        INSERT all sources and salaries from dictionary into Treeview

    METHOD refresh_summary_table()
        CALCULATE totals for each category from finance_data
        CALCULATE total income from sources_of_income
        UPDATE Finance summary Treeview with totals and remaining balance

    METHOD create_report_tab()
        CREATE search input for username/user_id
        CREATE buttons: Search user, Print report, Search again, Exit
        CREATE scrollable text widget for report display

    METHOD search_user()
        GET search term input
        SEARCH in usernames and user_ids
        IF found THEN
            DISPLAY user info and finance summary in report text
        ELSE
            SHOW user not found message

    METHOD print_report()
        GET report text content
        SAVE report to a text file and send to printer
        SHOW success or error message accordingly

    METHOD clear_search()
        CLEAR search input
        CLEAR report display

    METHOD show_totals()
        CALCULATE and DISPLAY totals for each finance category in a popup

    METHOD show_finance_tab()
        SWITCH to Finance tab

    METHOD show_view_tab()
        SWITCH to View tab

    METHOD show_report_tab()
        SWITCH to Report tab

END CLASS

MAIN
    CREATE Tkinter root window
    CREATE instance of SimpleSystem with root window
    RUN main event loop

END






