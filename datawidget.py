import sqlite3
from tabulate import tabulate

def add_project(val):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO project (Client_name, Project_desc, Total_amount, Start_date, End_date) VALUES (?,?,?,?,?)", val)
    conn.commit()
    conn.close()
    
def add_transaction(val):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO transactions VALUES (?,?,?,?)", val)
    conn.commit()
    conn.close()

def view_all_projects():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * from project")
    project_list = c.fetchall()
    conn.commit()
    conn.close()
    return tabulate(project_list, headers = ['ProjectID', 'Client Name', 'Project Description', 'Total Amount', 'Start Date','End Date'], tablefmt='fancy_grid', stralign='left', numalign='center')

def view_all_transactions():
    conn = sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("SELECT * from transactions")
    transaction_list = c.fetchall()
    conn.commit()
    conn.close()
    return tabulate(transaction_list, headers = ['ProjectID','TransactionID','Amount(Rs.)','Transaction_Date'], tablefmt='fancy_grid', stralign='left', numalign='center')
    

def search_transaction(filter, value):
    conn = sqlite3.connect('database.db')
    c=conn.cursor()
    if filter == 'ProjectID':
        c.execute("SELECT * FROM transactions WHERE ProjectID = (?)", (str(value),))
    elif filter == 'TransactionID':
        c.execute("SELECT * FROM transactions WHERE TransactionID = (?)", (str(value),))
    else:
        if value[0] == 'Y':
            c.execute("SELECT * FROM transactions WHERE strftime('%Y', Transaction_Date) = ?",(str(value[1]),))
        else:
            c.execute("SELECT * FROM transactions WHERE strftime('%m',Transaction_Date) = ?", (str(value[1]),))
    transaction_list = c.fetchall()
    if len(transaction_list) == 0:
        conn.commit()
        conn.close()
        return 'No entries found!'
    conn.commit()
    conn.close()
    return tabulate(transaction_list, headers = ['ProjectID','TransactionID','Amount(Rs.)','Transaction_Date'], tablefmt='fancy_grid')


def search_project(filter, value):
    conn = sqlite3.connect('database.db')
    c=conn.cursor()
    if filter == 'ProjectID':
        c.execute("SELECT * FROM project WHERE ProjectID = (?)",(str(value),))
    elif filter == 'Start_Date':
        if value[0] == 'Y':
            c.execute("SELECT * FROM project WHERE strftime('%Y', Start_Date) = ?",(str(value[1]),))
        else:
            c.execute("SELECT * FROM project WHERE strftime('%m',Start_Date) = ?", (str(value[1]),))
    else:
        if value[0] == 'Y':
            c.execute("SELECT * FROM project WHERE strftime('%Y', End_Date) = ?",(str(value[1]),))
        else:
            c.execute("SELECT * FROM project WHERE strftime('%m',End_Date) = ?", (str(value[1]),))
    project_list = c.fetchall()
    if len(project_list) == 0:
        conn.commit()
        conn.close()
        return 'No entries found!'
    conn.commit()
    conn.close()
    return tabulate(project_list, headers = ['ProjectID', 'Client_name','Project_Description','Total_Amount','Start_Date', 'End_Date'], tablefmt='fancy_grid')
    

def id_in_projectlist(prj_id):
    conn = sqlite3.connect("database.db")
    c= conn.cursor()
    c.execute("SELECT * FROM project WHERE ProjectID = (?)",(str(prj_id),))
    project_list = c.fetchall()
    if len(project_list) == 0:
        conn.commit()
        conn.close()
        return False
    else:
        conn.commit()
        conn.close()
        return True
    

