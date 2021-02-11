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
        elif res == 'Add new':  #Add new project or transaction
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
                prj_id = input("ProjectID: ")
                id_bool = datawidget.id_in_projectlist(prj_id)
                if id_bool is True:
                    trn_id = input("Transaction ID: ")
                    amt = float(input("Amount: "))
                    trn_date = input("Enter Transaction date(YYYY-MM-DD): ")
                    datawidget.add_transaction((prj_id, trn_id, amt, trn_date))
                else:
                    print("ProjectID not found!")
        elif res == 'Search':
            months = {
                'jan':'01',
                'feb':'02',
                'mar':'03',
                'apr':'04',
                'may':'05',
                'jun':'06',
                'jul':'07',
                'aug':'08',
                'sep':'09',
                'oct':'10',
                'nov':'11',
                'dec':'12'
            }
            search_questions = [{
                'type':'list',
                'name':'inner_search',
                'message':'Search: ',
                'choices':['Project', 'Transaction']
            }]
            ans = prompt(search_questions)['inner_search']
            system('cls')
            print("Search:", end = ' ')
            print(Fore.YELLOW+ans)
            print(Fore.WHITE)
            if ans == 'Project':
                search_questions = [{
                'type':'list',
                'name':'filter_search',
                'message':'Filter: ',
                'choices':['ProjectID', 'Start_Date', 'End_Date']
                }]
                ans2 = prompt(search_questions)['filter_search']
                system('cls')
                print("Search:", end = ' ')
                print(Fore.YELLOW+ans)
                print(Fore.WHITE)
                print("Filter:", end = ' ')
                print(Fore.YELLOW+ans2)
                print(Fore.WHITE)
                if ans2 == 'ProjectID':
                    prj_id = input("ProjectID: ")
                    prj_data = datawidget.search_project(ans2,prj_id).split("\n")
                    if len(prj_data) == 1:
                        print(Fore.RED+prj_data[0])
                        print(Fore.WHITE)
                    else:
                        print(Fore.WHITE+prj_data[0])
                        print(Fore.CYAN+prj_data[1])
                        for each_prj in prj_data[2:]:
                            print(Fore.WHITE+each_prj)
                elif ans2 == 'Start_Date':
                    yorm = input("Search by Year or Month(y or m):").lower()
                    if yorm == 'y':
                        year = input("Enter year(YYYY): ")
                        prj_data = datawidget.search_project(ans2,('Y', year)).split("\n")
                        if len(prj_data) == 1:
                            print(Fore.RED+prj_data[0])
                            print(Fore.WHITE)
                        else:
                            print(Fore.WHITE+prj_data[0])
                            print(Fore.CYAN+prj_data[1])
                            for each_prj in prj_data[2:]:
                                print(Fore.WHITE+each_prj)
                    elif yorm == 'm':
                        month = input("Enter month(mmm in text): ")
                        prj_data = datawidget.search_project(ans2,('m',months[month])).split("\n")
                        if len(prj_data) == 1:
                            print(Fore.RED+prj_data[0])
                            print(Fore.WHITE)
                        else:
                            print(Fore.WHITE+prj_data[0])
                            print(Fore.CYAN+prj_data[1])
                            for each_prj in prj_data[2:]:
                                print(Fore.WHITE+each_prj)  
                else:
                    yorm = input("Search by Year or Month(y or m):").lower()
                    if yorm == 'y':
                        year = input("Enter year(YYYY): ")
                        prj_data = datawidget.search_project(ans2,('Y', year)).split("\n")
                        if len(prj_data) == 1:
                            print(Fore.RED+prj_data[0])
                            print(Fore.WHITE)
                        else:
                            print(Fore.WHITE+prj_data[0])
                            print(Fore.CYAN+prj_data[1])
                            for each_prj in prj_data[2:]:
                                print(Fore.WHITE+each_prj)
                    elif yorm == 'm':
                        month = input("Enter month(mmm in text): ")
                        prj_data = datawidget.search_project(ans2,('m',months[month])).split("\n")
                        if len(prj_data) == 1:
                            print(Fore.RED+prj_data[0])
                            print(Fore.WHITE)
                        else:
                            print(Fore.WHITE+prj_data[0])
                            print(Fore.CYAN+prj_data[1])
                            for each_prj in prj_data[2:]:
                                print(Fore.WHITE+each_prj)   
            else:
                search_questions = [{
                'type':'list',
                'name':'filter_search',
                'message':'Filter: ',
                'choices':['ProjectID', 'TransactionID', 'Transaction_Date']
                }]
                ans2 = prompt(search_questions)['filter_search']
                system('cls')
                print("Search:", end = ' ')
                print(Fore.YELLOW+ans)
                print(Fore.WHITE)
                print("Filter:", end = ' ')
                print(Fore.YELLOW+ans2)
                print(Fore.WHITE)
                if ans2 == 'ProjectID':
                    prj_id = input("ProjectID: ")
                    prj_data = datawidget.search_transaction(ans2,prj_id).split("\n")
                    if len(prj_data) == 1:
                        print(Fore.RED+prj_data[0])
                        print(Fore.WHITE)
                    else:
                        print(Fore.WHITE+prj_data[0])
                        print(Fore.CYAN+prj_data[1])
                        for each_prj in prj_data[2:]:
                            print(Fore.WHITE+each_prj)
                elif ans2 == 'TransactionID':
                    trn_id = input("TransactionID: ")
                    prj_data = datawidget.search_transaction(ans2,trn_id).split("\n")
                    if len(prj_data) == 1:
                        print(Fore.RED+prj_data[0])
                        print(Fore.WHITE)
                    else:
                        print(Fore.WHITE+prj_data[0])
                        print(Fore.CYAN+prj_data[1])
                        for each_prj in prj_data[2:]:
                            print(Fore.WHITE+each_prj)
                else:
                    yorm = input("Search by Year or Month(y or m):").lower()
                    if yorm == 'y':
                        year = input("Enter year(YYYY): ")
                        prj_data = datawidget.search_transaction(ans2,('Y', year)).split("\n")
                        if len(prj_data) == 1:
                            print(Fore.RED+prj_data[0])
                            print(Fore.WHITE)
                        else:
                            print(Fore.WHITE+prj_data[0])
                            print(Fore.CYAN+prj_data[1])
                            for each_prj in prj_data[2:]:
                                print(Fore.WHITE+each_prj)
                    elif yorm == 'm':
                        month = input("Enter month(mmm in text): ")
                        prj_data = datawidget.search_transaction(ans2,('m',months[month])).split("\n")
                        if len(prj_data) == 1:
                            print(Fore.RED+prj_data[0])
                            print(Fore.WHITE)
                        else:
                            print(Fore.WHITE+prj_data[0])
                            print(Fore.CYAN+prj_data[1])
                            for each_prj in prj_data[2:]:
                                print(Fore.WHITE+each_prj)              
        elif res == 'Exit':
            break