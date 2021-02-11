import datawidget
from PyInquirer import prompt
from os import system
from colorama import init, Fore
if __name__ == '__main__':
    init()
    system('cls')
    while True:
        questions = [{
            'type':'list',
            'name':'outer_main',
            'message':'Enter your choice:',
            'choices': ['1. View all projects', '2. View all transactions', '3. Add new','4. Search','5. Exit']
        }]

        res = prompt(questions)['outer_main'][3:]
        system('cls')
        print("Enter your choice:", end  = ' ')
        print(Fore.YELLOW+res)
        print(Fore.WHITE)

        if res == 'View all projects':  ##View all projects
            all_prj = datawidget.view_all_projects().split("\n")
            print(Fore.WHITE+all_prj[0])
            print(Fore.CYAN+all_prj[1])
            if len(all_prj) > 2:
                for each_prj in all_prj[2:]:
                    print(Fore.WHITE+each_prj)
        elif res == 'View all transactions':    ##View all transactions
            all_trn = datawidget.view_all_transactions().split("\n")
            print(Fore.WHITE+all_trn[0])
            print(Fore.CYAN+all_trn[1])
            if len(all_trn) > 2:
                for each_trn in all_trn[2:]:
                    print(Fore.WHITE+each_trn)
        elif res == 'Add new':
            add_new_questions = [{
                'type':'list',
                'name':'inner_new',
                'message':'Add new: ',
                'choices':['Project', 'Transaction']
            }]
            ans = prompt(add_new_questions)['inner_new']
            system('cls')
            print("Add new:", end = ' ')
            print(Fore.YELLOW+ans)
            print(Fore.WHITE)
            if ans == "Project":
                cl_name = input("Client Name: ")
                prj_desc = input("Project Description: ")
                tot_amt = float(input("Total Amount: "))
                start_date = input("Enter Start date(YYYY-MM-DD): ")
                end_date = input("Enter End data(YYYY-MM-DD): ")
                datawidget.add_project((cl_name, prj_desc, tot_amt, start_date, end_date))
            else:
                prj_id = input("Enter ProjectID: ")
                id_bool = datawidget.id_in_projectlist(prj_id)
                if id_bool is True:
                    trn_id = input("Transaction ID: ")
                    amt = float(input("Amount: "))
                    trn_date = input("Enter Transaction date(YYYY-MM-DD): ")
                    datawidget.add_transaction((prj_id, trn_id, amt, trn_date))
                else:
                    print("ProjectID not found!")
        
        elif res == 'Exit':
            break