from logg import logging
import controller as c




def menu():
    logging.info('Start info sistem')
    while True:
        menu_list = input("Enter\n"
                         "1 - Сотрудники\n"
                         "2 - Услуги\n"
                         "3 - Запись клиентов\n"
                         "0 - Выход\n")
        match menu_list:
            case "1":
                logging.info('menu staff')
                menu_staff()
            case "2":
                logging.info('menu service')
                menu_service()
            case "3":
                logging.info('menu customer record')
                menu_cust_rec()
            case "0":
                logging.info('exit programm')    
                quit() 
            case _:
                logging.error('incorrect values')
                print("Err")

def menu_staff():
    while True:
        staff_list()
def menu_service():
    while True:
        service_list()

def menu_cust_rec():
    while True:
        cust_rec_list()

def staff_list():
    while True:
        staff_list = input("Enter\n"
                                "1 - create\n"
                                "2 - edit\n"
                                "3 - del\n"
                                "4 - view\n"
                                "0 - previous menu\n")
        match staff_list:
            case "1":
                c.creat_staff(c.input_data('Введите ID: '),
                              c.input_data('Введите f_name: '),
                              c.input_data('Введите l_name: '),
                              c.input_data('Введите phone: '),
                              c.input_data('Введите service: '))
            case "2":
                c.edit_data('staff')
            case "3":
                c.delete_data('staff')
            case "4":
                c.view_data('staff')
            case "0":
                menu()
            case _:
                logging.error('incorrect values')
                print("Err")

def service_list():
    while True:
        service_list = input("Enter\n"
                                "1 - create\n"
                                "2 - edit\n"
                                "3 - del\n"
                                "4 - view\n"
                                "0 - previous menu\n")
        match service_list:
            case "1":
                c.service_lst(c.input_data('Введите ID: '),
                            c.input_data('Введите name: '),
                            c.input_data('Введите cost: '))
            case "2":
                c.edit_data('service')
            case "3":
                c.delete_data('service')
            case "4":
                c.view_data('service')
            case "0":
                menu()
            case _:
                print("Err")
       
def cust_rec_list():
    while True:
        cust_rec_list = input("Enter\n"
                                "1 - create\n"
                                "2 - edit\n"
                                "3 - del\n"
                                "4 - view\n"
                                "0 - previous menu\n")
        match cust_rec_list:
            case "1":
                c.cust_rec(c.input_data('Введите ID: '),
                            c.input_data('Введите f_name: '),
                            c.input_data('Введите l_name: '),
                            c.input_data('Введите phone: '),
                            c.input_data('Введите service: '),
                            c.input_data('Введите cost: '),
                            c.input_data('Введите date: '))
            case "2":
                c.edit_data('cust_rec')
            case "3":
                c.delete_data('cust_rec')
            case "4":
                c.view_data('cust_rec')
            case "0":
                menu()
            case _:
                print("Err")


